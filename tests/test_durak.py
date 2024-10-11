from web3 import Web3
import pytest
import json

@pytest.fixture
def w3():
    return Web3(Web3.EthereumTesterProvider())

@pytest.fixture
def contract(w3):
    with open('contracts/Durak.json') as f:
        contract_data = json.load(f)
    contract_address = '0xYourContractAddress'
    return w3.eth.contract(address=contract_address, abi=contract_data['abi'])

def test_initialization(contract):
    assert contract.functions.owner().call() == '0xYourOwnerAddress'

def test_draw_card(contract, w3):
    player = '0xPlayerAddress'
    initial_hand = contract.functions.playerHands(player).call()
    contract.functions.drawCard(player).transact({'from': player})
    new_hand = contract.functions.playerHands(player).call()
    assert len(new_hand) == len(initial_hand) + 1
