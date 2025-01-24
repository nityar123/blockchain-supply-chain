from blockchain import Blockchain
from supply_chain import SupplyChain

def main():
    supply_chain = SupplyChain()

    while True:
        print("\n--- Supply Chain System ---")
        print("1. Add a Transaction")
        print("2. Mine Transactions")
        print("3. View Blockchain")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            sender = input("Enter sender: ")
            receiver = input("Enter receiver: ")
            product = input("Enter product: ")
            quantity = int(input("Enter quantity: "))
            supply_chain.add_transaction(sender, receiver, {"product": product, "quantity": quantity})
            print("Transaction added!")
        elif choice == "2":
            miner = input("Enter miner's address: ")
            print("Mining pending transactions...")
            supply_chain.blockchain.mine_pending_transactions(miner)
            print("Block mined successfully!")
        elif choice == "3":
            print("\n--- Blockchain ---")
            for block in supply_chain.blockchain.chain:
                print(f"Index: {block.index}")
                print(f"Timestamp: {block.timestamp}")
                print(f"Transactions: {block.transactions}")
                print(f"Hash: {block.hash}")
                print(f"Previous Hash: {block.previous_hash}")
                print("-" * 30)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
