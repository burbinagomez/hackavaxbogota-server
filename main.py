from flask import Flask, request, make_response
from web3 import Web3
from eth_account.messages import encode_defunct, _hash_eip191_message
from eth_account import Account
from hexbytes import HexBytes
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
import pymongo
import json
import os

load_dotenv()
f = open('abi.json')
abi = json.load(f)
app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(os.getenv("HTTP_PROVIDER")))
mongo_client = pymongo.MongoClient(f"mongodb+srv://{os.getenv('USER_MONGO')}:{os.getenv('PWD_MONGO')}@{os.getenv('MONGO_URL')}/?retryWrites=true&w=majority&appName=Cluster0")
nuez_contract = w3.eth.contract(os.getenv("CONTRACT_ADDRESS"), abi=abi)
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

@app.route("/create/wallet", methods=["POST"])
def create_wallet():
    data = request.json
    acc = w3.eth.account.create()
    private_key = w3.to_hex(acc.key)
    mydb = mongo_client["nuez"]
    mycol = mydb["user"]
    wallet_address = acc.address
    mycol.insert_one({
        "private_key": private_key,
        "public_key": wallet_address,
        "phonenumber": data["number"]
    })
    return make_response({
        "message": "Transaccion correcta",
        "data": wallet_address
    },200)

@app.route("/sign", methods=["POST"])
def sign_message():
    data = request.json
    mydb = mongo_client["nuez"]
    col_user = mydb["user"]
    mycol = mydb["messages"]
    user = col_user.find_one({
        "phonenumber": data["number"]
    })
    account = Account.from_key(user["private_key"])
    message = encode_defunct(text=data["hash_image"])
    signed_message = account.sign_message(message)
    mycol.insert_one({
        "phonenumber":data["number"],
        "message": data["hash_image"],
        "hash": signed_message.signature.hex()
    })
    return make_response({
        "message": "Transaccion correcta"
    },200)

@app.route("/verify", methods=["POST"])
def verify_message():
    data = request.json
    mydb = mongo_client["nuez"]
    col_user = mydb["user"]
    user = col_user.find_one({
        "phonenumber": data["number"]
    })
    mycol = mydb["messages"]
    messages = mycol.find({
        "phonenumber": data["number"],
        "validated":  {"$exists": False} 
    })
    response = []
    for message in messages:
        response.append(message)
    amount = len(response)
    if amount != 0:
        transaction = nuez_contract.functions.transfer(user["public_key"], amount+1000000000000000000).build_transaction({
            'chainId': 43113,  # ID de la cadena Avalanche (C-Chain)
            'gas': 8000000,  # Gas límite para la transacción (ajusta según tus necesidades)
            'gasPrice': w3.to_wei('50', 'gwei'),  # Precio del gas (en gwei)
            'nonce': w3.eth.get_transaction_count(os.getenv("OWNER_ADDRESS")),
        })
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=os.getenv("PRIVATE_KEY"))
        # Enviar la transacción firmada
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Esperar a que se confirme la transacción
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        print("Transferencia exitosa. Hash de la transacción:", tx_receipt.transactionHash.hex())
    if len(response) > 0:
        mycol.update_many({
                "phonenumber": data["number"],
                "validated": {"$exists": False} 
            },{
                "$set": {"validated": True}
            })
    return make_response({
        "message": "Transaccion correcta"
    },200)


@app.route("/items", methods=["GET"])
def get_items():
    mydb = mongo_client["nuez"]
    mycol = mydb["products"]
    response = []
    for data in mycol.find():
        data.pop("_id")
        response.append(data)
    return make_response({
        "message": "Transaccion correcta",
        "data": response
    },200)
    
app.run("0.0.0.0",debug = True)
