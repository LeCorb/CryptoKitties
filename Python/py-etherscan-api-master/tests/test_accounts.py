import unittest

from etherscan.accounts import Account

SINGLE_BALANCE = '40807178566070000000000'
SINGLE_ACCOUNT = '0xE85a4A5483139Ea4bf30728AE6Efe7a8cA7f447f'
MULTI_ACCOUNT = [
    '0xE85a4A5483139Ea4bf30728AE6Efe7a8cA7f447f',
    '0xE85a4A5483139Ea4bf30728AE6Efe7a8cA7f447f',
]
MULTI_BALANCE = [
    {'account': '0xE85a4A5483139Ea4bf30728AE6Efe7a8cA7f447f',
     'balance': '40807178566070000000000'},
    {'account': '0xE85a4A5483139Ea4bf30728AE6Efe7a8cA7f447f',
     'balance': '40807178566070000000000'}
]
API_KEY = 'Y5FVVVUJQSB8H1HBI8TGRKZKFBW9TPNB45'


class AccountsTestCase(unittest.TestCase):

    def test_get_balance(self):
        api = Account(address=SINGLE_ACCOUNT, api_key=API_KEY)
        self.assertEqual(api.get_balance(), SINGLE_BALANCE)

    def test_get_balance_multi(self):
        api = Account(address=MULTI_ACCOUNT, api_key=API_KEY)
        self.assertEqual(api.get_balance_multiple(), MULTI_BALANCE)
