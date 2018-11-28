from poloniex import Poloniex
#https://pypi.org/project/poloniex/#


#polo = Poloniex()
#help(polo)

polo = Poloniex()
ticker = polo.returnTicker()['BTC_ETH']
#print(ticker)


from poloniex import Poloniex
import os

# Шота нєрабочєє. Хз. Можливо ми зможемо без  цього обійтись. Бо тут пазоду для реальних ставок тільки таку апішку ннада.
api_key = os.environ.get("CAXFKPES-ZVEVH9S2-68O93JFD-LHA72YW5")
api_secret = os.environ.get("612fb1d36b098a4dfee559712115f9c0220c769b8a2a98b140d9f760885ee72d8e3d595a756c3b0b60ceeba60d59d18cc099a9dc6c4e5da51284104db9a5592e")
polo = Poloniex(api_key, api_secret)

ticker = polo.returnTicker()['BTC_ETH']
print(ticker)

balances = polo.returnBalances()
print(balances)
