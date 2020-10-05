import block

class Chain:

    def __init__(self):

        self.main_chain = []

        pass

    def get_current(self):

        pass

    def validate_chain(self):

        pass

    def write_to_file(self, chain_to_write):

        with open('current_chain.json', 'w') as f:

            json.dump(chain_to_write, f)





