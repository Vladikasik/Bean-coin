import block
import json
import string
import random
import chain
import rsa


class User:

    # do not create here because has <create> method
    def __init__(self, username='', address='', blocks=[],
                 sembalance_of_balance=0, public_key='', private_key=''):
        self.username = username
        self.address = address
        self.blocks = blocks
        self.semblance_of_balance = sembalance_of_balance
        self.public_key = public_key
        self.private_key = private_key

    # creating user with unique address
    def create(self, username):

        self.username = username

        with open('../consumable/users.json') as f:
            data = json.load(f)

        while 1:
            (pubkey, privkey) = rsa.newkeys(136)

            a = pubkey.save_pkcs1().splitlines()[1:-1]
            if a in data:
                pass
            else:
                self.address = a[0].decode('utf-8')
                break

        self.public_key = pubkey.save_pkcs1()
        self.private_key = privkey.save_pkcs1()

    def get_text_to_session(self):
        exit_list = f'["{str(self.username)}", "{str(self.address)}", "{str(self.blocks)}", "{str(self.semblance_of_balance)}", "{str(self.public_key)}", "{str(self.private_key)}"]'
        return exit_list

    # finding blocks where self address is sender or receiver
    def find_blocks(self):

        curr_chain = chain.get_current()

        for i in curr_chain:
            if i[user_from] == self.address or i[user_to] == self.address:
                self.blocks.append(i)
