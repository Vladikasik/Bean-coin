import block
import json
import string
import random
import chain

class User:

    def __init__(self):
        self.adress = ''
        self.blocks = []
        self.sth_like_balance

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
                self.adress = a

    def find_blocks(self):
        curr_chain = chain.get_current()