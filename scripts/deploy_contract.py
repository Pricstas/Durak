from web3 import Web3
import json

# Connect to the Base blockchain
w3 = Web3(Web3.HTTPProvider('https://base-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Credentials
private_key = 'YOUR_PRIVATE_KEY'
account = w3.eth.account.from_key(private_key)

# Read and compile the smart contract
with open('contracts/Durak.sol', 'r') as file:
    contract_source = file.read()

from solcx import compile_source

compiled_sol = compile_source(contract_source)
contract_interface = compiled_sol['<stdin>:Durak']

# Deploy the contract
Durak = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
txn = Durak.constructor().buildTransaction({
    'from': account.address,
    'nonce': w3.eth.getTransactionCount(account.address),
    'gas': 3000000,
    'gasPrice': w3.toWei('50', 'gwei')
})

signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(f'Transaction hash: {tx_hash.hex()}')

# Wait for the transaction to be mined
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(f'Contract deployed at address: {tx_receipt.contractAddress}')
