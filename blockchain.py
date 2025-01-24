import hashlib
import time

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.transactions) + self.previous_hash
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 50

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block):
        self.chain.append(block)

    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), time.time(), self.pending_transactions, self.get_latest_block().hash)
        self.add_block(block)
        print(f"Block successfully mined with hash: {block.hash}")

        # Reset pending transactions and add mining reward
        self.pending_transactions = [{"sender": "System", "receiver": miner_address, "product_details": {"product": "Mining Reward", "quantity": self.mining_reward}}]
    
    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)
