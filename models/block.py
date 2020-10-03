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

    # some calculating to confirm the operation
    def confirm(self):
        self.confirmed = True

    # return string as json obj to get hash for next block
    def get_text(self):
        # Salt must be calculated and confirmation needn't change hash

        exit_str = "{TimeStamp:{%s},SenderWallet:{%s},ReceiverWallet:{%s},Amount:{%s},Message:{%s}HashOfPreviousBlock:{%s}}" % (str(self.timestamp), self.wallet_sender, self.wallet_receiver, str(self.amount), self.message, self.prev_hash)

        return exit_str

    # simply returns the confirmation status
    def get_confirmation(self):
        return self.confirmed

    # easier make it here
    def make_genesis(self):

        genesis = Block("6vMkBZfwDPRjJ5D3vntC8ckeDku5opik", "MGvehibp2H7yEuyMXa4doWXP4NjPbfxP", 1, '')

        return genesis
