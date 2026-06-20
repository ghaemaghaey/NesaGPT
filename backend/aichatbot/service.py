import requests
import json
import tiktoken


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def convertdollartotoman(amount):
    priceofdollar = requests.get(
        "http://www.tgju.org/?act=sanarateservice&client=tgju&noview&type=json"
    )
    dictfile = json.loads(priceofdollar.content)
    priceofdollar = int(dictfile["sana_buy_usd"]["price"].replace(",", "")[:-1])
    return amount * priceofdollar


def pricecheckforapi(text: str, pricefor1mtoken: int):
    """give text and price for 1 milion token for what you do and get the final cost of your prompt"""
    token_count = num_tokens_from_string(text, "gpt-4o")
    price = (token_count * pricefor1mtoken) / 1000000
    return convertdollartotoman(price)


def inandoutpricecheck(intext: str, outtext: str, inprice: int, outprice: int) -> float:
    outputprice = pricecheckforapi(outtext, outprice)
    inputprice = pricecheckforapi(intext, inprice)
    return inputprice + outputprice
