from blockchain import Blockchain

class SupplyChain:
    def __init__(self):
        self.blockchain = Blockchain()

    def add_transaction(self, sender, receiver, product_details):
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "product_details": product_details,
        }
        self.blockchain.add_transaction(transaction)

    def mine_pending_transactions(self, miner_address):
        self.blockchain.mine_pending_transactions(miner_address)
