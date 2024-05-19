
# Food4Less

Food4Less es una innovadora plataforma de reembolsos que utiliza tecnología para recompensar a los consumidores por la compra de productos alimenticios y medicamentos cercanos a su fecha de vencimiento. Con un enfoque en la sostenibilidad y el ahorro.  Esta idea nace con el fin de ayudar al medio ambiente ya que haciendo investigacion mas de 1 Billón de dólares se pierden en Suramérica cada año por desperdicio de alimentos. El 18% de los productos perecederos que llegan al anaquel se terminan desperdiciando. El 18% de los productos perecederos que llegan al anaquel se terminan desperdiciando. Entre un 9% y 16% anual se estima la pérdida del poder adquisitivo en LATAM.

Esta Idea se desarrollo durante la Hackaton de Avalanche los dias 18 y 19 de Mayo del 2024 en conjunto con Fernando Arenas, Brayan Urbina, Juan Felipe Jimenez, Sebastian Melo, Harold Espinoza

## Objetivo

- Incentivar la compra de productos cercanos a su vencimiento para reducir el desperdicio de alimentos y medicamentos.
- Proporcionar un ahorro significativo a los consumidores mediante reembolsos.
- Implementar un sistema de recompensas adicional utilizando un token propio que de beneficios adicionales a los que lo posean.

## Alcance

Lanzamiento inicial en Venezuela, seguido por Colombia y Panamá. Incorporación de sistemas de pago locales (Pago Móvil en Venezuela y Nequi en Colombia). Implementación de un sistema de reembolsos vía criptomonedas en la red Avalanche

## Análisis de Competencia:
Actualmente, existen pocas plataformas que ofrezcan un servicio similar en estos mercados. Las iniciativas de cashback suelen estar enfocadas en otros sectores, dejando una oportunidad abierta para que Food4Less se posicione como líder en la reducción de desperdicio de alimentos y medicamentos. Las barreras de entrada son manejables, ya que la plataforma puede aprovechar la infraestructura existente de pagos móviles y la adopción creciente de criptomonedas.


## Tecnología Utilizada:
Stack Tecnológico: Para el desarrollo de esta aplicación utilizamos las siguientes tecnologías:
- Back-end: Usamos NextJS como nuestro framework principal utilizando librerías como React 18 y Web3
- Fronted: Utilizamos tecnologías como NextJS y Tailwind
- Bases de Datos: Utilizamos MongoDB como Base de Datos No Relacional
- Web3: Utilizamos la plataforma de Avalanche que ofrece aplicaciones de herramientas y funcionalidades para aplicaciones descentralizadas. Para los Smart Contracts utilizamos el lenguaje de programación de Solidity


##  Plataforma Web 3: ERC-20 Nuez Token:
En este proyecto, se utilizó un contrato ERC-20 para crear un token personalizable con configuración básica, utilizando librerías estándar de ERC-20 para controlar el envío exclusivo por parte de los creadores. Tras verificar que el código estuviera libre de errores, se desplegó el contrato conectando nuestra cuenta para cubrir los costos de gas necesarios. Una vez desplegado, se habilitó un menú con funciones como approve (aprobar), transfer (transferir), transferFrom (transferir desde), allowance (prestación), balanceOf (saldo), decimals (decimales), name (nombre), symbol (símbolo) y totalSupply (oferta total). Para realizar una transferencia mediante la función transfer, se requiere la dirección del receptor y la cantidad a enviar, recordando que las transacciones se realizan en Gwei, por lo que para enviar una unidad del token, se debe ingresar 1 seguido de 18 ceros.

## Documentación

Para más detalles sobre el proyecto, consulta la [Documentación del Proyecto Food4Less](https://docs.google.com/document/d/1M9hyYd4AUZlmKgTo0yJE_2lYUFCl8HG1UMX4j4zFVgY/edit).

## Presentación

Para acceder a la presentación, visita este enlance [Presentacion del Proyecto Food4Less](https://docs.google.com/presentation/d/1Ek3LWuvrCOv_5oYuPVePp0VNNgnZ9v8gQn6dOH9AP8c/edit#slide=id.g85cf8b5f36_0_6059).

---------------------------------------------------

###  Uso e Instalacion de la Aplicacion

Usar  [pip](https://pip.pypa.io/en/stable/) para instalar los paquetes

```bash
pip install -r requirements.txt
```

### Usage

```bash
gunicorn main:app
```
