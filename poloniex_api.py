from poloniex import Poloniex
import os


api_key = os.environ.get("QY44P4MS-OP962F3U-Q4GG8019-9BGU678M")
api_secret = os.environ.get("451e6efe08c36b97f49d38b2057845389576dfd96ad5f2ef0da3db05fb9facab65819a8e27fc3e137a0bbf6bb139d86646df0b5f59ab8ccaa5439eb6d6402787")

polo = Poloniex(api_key, api_secret)

ticker = polo.returnTicker()['BTC_ETH']
print(ticker)

balances = polo.returnBalances()
print(balances)
