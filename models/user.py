import block
import json
import string
import random
import chain


class User:

    def __init__(self):
        self.address = ''
        self.blocks = []
        self.semblance_of_balance = 0

    def create(self):

        with open('../consumable/users.json') as f:
            data = json.load(f)

        letters_and_digits = string.ascii_letters + string.digits
        a = ''.join((random.choice(letters_and_digits) for i in range(32)))
        if '0' in a or 'O' in a or 'I' in a or 'l' in a:
            pass
        else:
            if a in data:
                pass
            else:
                self.address = a

    def find_blocks(self):
        curr_chain = chain.get_current()
