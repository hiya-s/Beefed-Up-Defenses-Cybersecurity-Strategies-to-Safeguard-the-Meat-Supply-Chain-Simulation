from web3 import Web3
import json

# Connect to local Ganache or Infura (if on testnet)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))  # Ganache RPC

# Replace with your deployed contract address and ABI
contract_address = "0xYourContractAddressHere"
with open("BeefTrace_abi.json") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=abi)
account = w3.eth.accounts[0]

def log_event(description, actor):
    tx_hash = contract.functions.addEvent(description, actor).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Logged event: {description} by {actor}")

# Example usage
log_event("Cattle tagged", "RFID Livestock System")
log_event("Meat processed", "Processing ERP")
