from flask import Flask, request, jsonify
from web3 import Web3
import json
import os

app = Flask(__name__)

# Connect to the Base blockchain
w3 = Web3(Web3.HTTPProvider('https://base-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Load contract ABI and address
with open('contracts/Durak.json') as f:
    contract_data = json.load(f)

contract_address = w3.toChecksumAddress('YOUR_CONTRACT_ADDRESS')
contract = w3.eth.contract(address=contract_address, abi=contract_data['abi'])

@app.route('/draw_card', methods=['POST'])
def draw_card():
    player_address = request.json.get('player_address')
    txn = contract.functions.drawCard(player_address).buildTransaction({
        'from': player_address,
        'nonce': w3.eth.getTransactionCount(player_address),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei')
    })
    # Sign and send the transaction
    # Add code here to sign the transaction with the private key
    return jsonify({'status': 'Card drawn'})

if __name__ == '__main__':
    app.run(debug=True)
