from flask import Flask, request, make_response
from web3 import Web3
from eth_account.messages import encode_defunct, _hash_eip191_message
from eth_account import Account
from hexbytes import HexBytes
from dotenv import load_dotenv
from bson import ObjectId
import pymongo
import os

load_dotenv()

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(os.getenv("HTTP_PROVIDER")))
mongo_client = pymongo.MongoClient(f"mongodb+srv://{os.getenv('USER_MONGO')}:{os.getenv('PWD_MONGO')}@{os.getenv('MONGO_URL')}/?retryWrites=true&w=majority&appName=Cluster0")

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
        "phonenumber": data["number"]
    })
    for message in messages:
        _message = encode_defunct(text=message["message"])
        signed_message = message["hash"]
        hb = HexBytes(signed_message)
        validated = w3.eth.account.recover_message(_message, signature=hb.hex())
        if not message.get("validated"):
            if validated == user["public_key"]:
                mycol.update_one({
                    "_id": message["_id"]
                },{
                    {"$set": {"validated": True}}
                })
            else:
                mycol.update_one({
                    "_id": message["_id"]
                },{
                    {"$set": {"malformated": True}}
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
