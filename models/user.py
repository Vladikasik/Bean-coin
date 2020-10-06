import block
import json
import string
import random
import chain
import rsa


class User:

    # do not create here because has <create> method
    def __init__(self):
        self.username = ''
        self.address = ''
        self.blocks = []
        self.semblance_of_balance = 0
        self.public_key = 0
        self.private_key = 0

    # creating user with unique address
    def create(self, username):

        self.username = username

        with open('../consumable/users.json') as f:
            data = json.load(f)

        while 1:
            (a, privkey) = rsa.newkeys(50)

            a = str(a)

            if a in data:
                pass
            else:
                self.address = a
                break


    # finding blocks where self address is sender or receiver
    def find_blocks(self):

        curr_chain = chain.get_current()

        for i in curr_chain:
            if i[user_from] == self.address or i[user_to] == self.address:
                self.blocks.append(i)

