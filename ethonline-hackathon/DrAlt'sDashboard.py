#!/usr/bin/env python3
from tkinter import *
import requests
import sys
import time
import datetime
from urllib.request import urlopen
from collections import defaultdict
from json import loads
from etherscan.accounts import Account
import json

# this is where the display is being created
class ETHTicker:
	def __init__(self, master):
		self.master = master
		self.close_button = Button(image=ethlogo, command=self.close)
		self.close_button.grid(row=0, column=0)
		self.label = Label(master, text=("ETH Portfolio"), font=('mv boli',32, 'bold'), fg='black', bg = 'darkorchid4')
		self.label.grid(row=0, column=1)

	def labels():
		global errormessage
		hwg()
		internet_on()
		title = "Global data"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('ugotic', 28, 'bold'), bg='black', fg='gold')
		down_label.grid(row=1, column=1, sticky=W)

		if priceeth1hrchange *100 > price1hrchangediff:
				color = "lightgreen"
		elif priceeth1hrchange * 100 < price1hrchangediff * -1:
				color = "lightcoral"
		else:
				color = "white"
		percentage = "{:,.1%}".format(priceeth1hrchange)
		percentage2 = "{:,.1%}".format(priceeth24hrchange)
		currency = "{:,.2f}".format(priceeth)
		text1 = "ETH price: $" + str(currency) + "   (" + str(percentage) + " / " + str(percentage2) + ")"
		down_label = Label(text=(text1),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = color)
		down_label.grid(row=2, column=1, sticky=W)

		currency = "{:,.1f}".format(defi_market_cap)
		text4a = "DeFi marketcap: $" + str(currency) + " B  "
		down_label = Label(text=(text4a),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		down_label.grid(row=3, column=1, sticky=W)

		currency = "{:,.0f}".format(average_gasfee)
		text5 = "Average gas: " + str(currency) + " gwei  "
		date_time_obj = "{:,.1f}".format(average_wait_time)
		text5b = "Avg wait time: " + str(date_time_obj) + " min  "
		down_label = Label(text=(text5 + '\n' + text5b),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=4, column=1, sticky=W)

		title = "My DeFi wallet"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('ugotic UI', 28, 'bold'), bg='black', fg='gold')
		down_label.grid(row=5, column=1, sticky=W)

		currency = "${:,.1f}".format(defilockedusd)
		text10 = "Value locked: " + str(currency) + " B  "
		currency = "${:,.1f}".format(dominance_valueusd)
		text11 = str(dominance_name) + " locked: " + str(currency)  + " B  "
		down_label = Label(text=(text10 + '\n' + text11),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=6, column=1, sticky=W)

		currency = "{:,.0f}".format(TVLBTC)
		text12 = "BTC locked: " + str(currency) + u'\u20bf'
		currency = "{:,.0f}".format(LNDBTC)
		text12a = "Lightning volume: " + str(currency) + u'\u20bf'
		down_label = Label(text=(text12 + '\n' + text12a),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=7, column=1, sticky=W)
		
		title = "My ERCs"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('ugotic UI', 20, 'bold'), bg='black', fg='darkorchid4')
		down_label.grid(row=8, column=1, sticky=W)
		
		for token_name in eth_token_totals:
			if eth_token_totals[token_name] > -1.00001:
				text13 = token_name + "\n" + str(eth_token_totals[token_name])
				down_label = Label(text=(text13),justify=LEFT,font=('Helvetica',20, 'bold'), bg='black', fg='white')
				down_label.grid(row=9, column=1, sticky=W) 
		
		text98 = str(errormessage)
		down_label = Label(text=(text98),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='red')
		down_label.grid(row=27, column=1, sticky=W)
		errormessage = ""

		now = datetime.datetime.now()
		text99 = "Current time: " + str(now)
		down_label = Label(text=(text99),anchor=NW, justify=LEFT,font=('Helvetica',12), bg='black', fg='white')
		down_label.grid(row=28, column=1, sticky=W)
			
# This is where you set the update time. 290000 is about 5 minutes	
		down_label.after(290000,ETHTicker.labels)

	def close(self):
		root.destroy()

def hwg():
	global priceeth
	global priceeth1hrchange
	global priceeth24hrchange
	global coin1price24hrchange
	global coin2price24hrchange
	global coin1symbol
	global coin2symbol
	global marketcapeth
	global marketcap24h
	global coin1price
	global coin2price
	global market_dominance_percentage
	global average_gasfee
	global defilockedusd
	global dominance_name
	global dominance_valueusd
	global TVLBTC
	global LNDBTC
	global status
	global errormessage
	global average_block_time
	global average_wait_time
	global coin1price1hrchange
	global coin2price1hrchange
	global defi_market_cap

	defi_market_cap = 0
	priceeth = 0
	priceeth1hrchange = 0
	priceeth24hrchange = 0
	marketcapeth = 0
	marketcap24h = 0
	market_dominance_percentage = 0
	average_gasfee = 0

	try:
#	get the defipulse Project data 
		defi_pulse_url = 'https://data-api.defipulse.com/api/v1/defipulse/api/GetProjects?api-key='+ defipulseApikey
		urltest = requests.get(defi_pulse_url)
		status = urltest.status_code
		if status == 429:
			print("Error DefiPulse. Wrong or expired API key")
			errormessage = "Error DefiPulse. Wrong or expired API key"
			raise
		elif status == 200:
			total_value_locked = requests.get(defi_pulse_url)
			json_obj = total_value_locked.json()

			for project in json_obj:
				name = project.get("name")
				if name == 'WBTC':
					WBTC = project['value']['tvl']['BTC'].get("value")
				elif name == 'RenVM':
					RENBTC = project['value']['tvl']['BTC'].get("value")
				elif name == 'Lightning Network':
					LNDBTC = project['value']['tvl']['BTC'].get("value")
			TVLBTC = WBTC + RENBTC + LNDBTC
		else:
			print("Error reading DeFiPulse. Error-code: " + str(status))
			errormessage = "Unknown error reading DeFiPulse Project"
	except:
		if status == 204:
			time.sleep(5)
			hwg()

	try:
#	get the defipulse Marketdata 
		defi_pulse_url = 'https://data-api.defipulse.com/api/v1/defipulse/api/MarketData?api-key='+ defipulseApikey
		urltest = requests.get(defi_pulse_url)
		status = urltest.status_code
		if status == 429:
			print("Error DefiPulse. Wrong or expired API key")
			errormessage = "Error DefiPulse. Wrong or expired API key"
			raise
		elif status == 200:
			marketdata=requests.get(defi_pulse_url).json()
			defilockedusd=marketdata['All']['total']
			dominance_valueusd = marketdata['All']['dominance_value']
			dominance_name = str(marketdata['All']['dominance_name'])
			dominance_valueusd = dominance_valueusd / 1000000000
			defilockedusd = defilockedusd / 1000000000
		else:
			print("Error reading DeFiPulse Market. Error-code: " + str(status))
			errormessage = "Unknown error reading DeFiPulse Market"
	except:
		if status == 204:
			time.sleep(5)
			hwg()

	try:
#	https://docs.ethgasstation.info/gas-price
		status = 1
		ethgas_url = 'https://ethgasstation.info/api/ethgasAPI.json?'
		urltest = requests.get(ethgas_url)
		status = urltest.status_code
		marketdata = requests.get(ethgas_url).json()
		average_gasfee = marketdata['average']
		average_block_time = marketdata['block_time']
		average_wait_time = marketdata['avgWait']

		average_gasfee = average_gasfee / 10

	except:
		errormessage = "Error reading EthGasStation " + str(status)
		print(errormessage)
		time.sleep(10)
		hwg()
		
	try:
#	get blockchain data https://blockchair.com/api/docs#link_M03
		status = 0
		blockchair_url = 'https://api.blockchair.com/ethereum/stats'
		urltest = requests.get(blockchair_url)
		status = urltest.status_code

		blockchair_api_request = requests.get(blockchair_url).json()
		market_dominance_percentage = blockchair_api_request['data']['market_dominance_percentage']

		market_dominance_percentage = market_dominance_percentage / 100

	except:
		errormessage = "Error reading Blockchair: " + str(status)
		print(errormessage)
		time.sleep(10)
		hwg()
	
	try:
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/coins/ethereum').read()	
		marketcap24h = float(loads(coingecko_api_request)['market_data']['market_cap_change_percentage_24h'])
		priceeth1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		priceeth24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])
		marketcapeth = float(loads(coingecko_api_request)['market_data']['market_cap']['usd'])
		priceeth = float(loads(coingecko_api_request)['market_data']['current_price']['usd'])
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/coins/'+ ETHspecialcoin1).read()	
		coin1price = float(loads(coingecko_api_request)['market_data']['current_price']['usd'])
		coin1symbol= str(loads(coingecko_api_request)['symbol'])
		coin1price24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])
		coin1price1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/coins/' + ETHspecialcoin2).read()	
		coin2price = float(loads(coingecko_api_request)['market_data']['current_price']['usd'])
		coin2symbol= str(loads(coingecko_api_request)['symbol'])
		coin2price1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		coin2price24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])

		priceeth24hrchange = priceeth24hrchange / 100
		coin2price24hrchange = coin2price24hrchange / 100
		coin1price24hrchange = coin1price24hrchange / 100
		priceeth1hrchange = priceeth1hrchange / 100
		coin2price1hrchange = coin2price1hrchange / 100
		coin1price1hrchange = coin1price1hrchange / 100
		marketcapeth = marketcapeth / 1000000000
		print(priceeth)

	except:
		errormessage = "Error reading Coingecko "
		print(errormessage)
		time.sleep(10)
		hwg()
	
	try:
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/global/decentralized_finance_defi').read()	
		defi_market_cap = float(loads(coingecko_api_request)['data']['defi_market_cap'])
		defi_market_cap = defi_market_cap / 1000000000

	except:
		errormessage = "Error reading Coingecko Defi" 
		print(errormessage)
		time.sleep(10)
		hwg()

def internet_on(url='http://www.google.com/', timeout=5):
	try:
		_ = requests.get(url, timeout=timeout)
		return True
	except requests.ConnectionError:
		errormessage = "No internet connection available."
	return False

eth_token_totals = defaultdict(lambda : 0)
address ='0xE85a4A5483139Ea4bf30728AE6Efe7a8cA7f447f'
url = 'https://api.etherscan.io/api?module=account&action=tokentx&address='+address+'&startblock=0&endblock=999999999&sort=asc&apikey=YourApiKeyToken'
response = requests.get(url)
address_content = response.json()
result = address_content.get("result")
for transaction in result:
	tx_from = transaction.get("from")
	tx_to = transaction.get("to")
	value = int(transaction.get("value"))
	decimals = int(transaction.get("tokenDecimal"))
	token_name = transaction.get("tokenName")
	gasprice = transaction.get("gasPrice")
	token_symbol = transaction.get("tokenSymbol")
	real_value = value * 10 ** (decimals * -1)
	if tx_to == address.lower():
		eth_token_totals[token_name] += real_value
	else:
		eth_token_totals[token_name] += (real_value * -1)

exec(open(r"variables").read())
errormessage=""
LNDBTC=0
TVLBTC=0
defilockedusd=0
dominance_valueusd=0
dominance_name=0
total_value_locked=0
defilockedusd=0
root = Tk()
root.configure(cursor='none', bg='black')
root.attributes('-fullscreen', True)
logo = PhotoImage(file=r"ethlogo.png")
ethlogo = logo.subsample(26,26)
my_gui = ETHTicker(root)
ETHTicker.labels()
root.mainloop()
