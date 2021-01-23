from etherscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0xE85a4A5483139Ea4bf30728AE6Efe7a8cA7f447f'

api = Account(address=address, api_key=key)
balance = api.get_balance()
print(balance)
