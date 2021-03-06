import hashlib
import time


class Block:

    def __init__(self, from_w, to_w, am, hash, mes='empty'):
        self.timestamp = time.time()
        self.wallet_sender = from_w
        self.wallet_receiver = to_w
        self.amount = am
        self.message = mes
        self.prev_hash = hash
        self.salt = 0
        self.confirmed = False
        self.signature = ''

    # some calculating to confirm the operation
    def confirm(self):
        self.confirmed = True

    # getting hash of block
    def get_hash(self):
        pass

        # return string as json obj to get hash for next block
    def get_text_without_signature(self):
        # Salt must be calculated and confirmation needn't change hash
        exit_str = json.dumps(self.get_dict())
        return exit_str

    # creating signature of block
    def create_signature(self):

        self.signature = rsa.sign(self.get_text_without_signature(), privkey, 'SHA-1')

    # returns dictionary with block info
    def get_dict(self):
        result_dict = {'TimeStamp': {self.timestamp}, 'SenderWallet': {self.wallet_sender},
                       'ReceiverWallet': {self.wallet_receiver}, 'Amount': {self.amount}, 'Message': {self.message},
                       'HashOfPreviousBlock' : {self.prev_hash}}

        return result_dict

    # simply returns the confirmation status
    def get_confirmation(self):
        return self.confirmed

    #  easier make it here
    # def make_genesis(self):
    #     genesis = Block("6vMkBZfwDPRjJ5D3vntC8ckeDku5opik", "MGvehibp2H7yEuyMXa4doWXP4NjPbfxP", 1, '')
    #
    #     return genesis
