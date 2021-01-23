from etherscan.accounts import Account
   
api_key = 'Y5FVVVUJQSB8H1HBI8TGRKZKFBW9TPNB45'
address = '0xE85a4A5483139Ea4bf30728AE6Efe7a8cA7f447f'

api = Account(address,api_key)
balance = api.get_balance()
print(balance)
