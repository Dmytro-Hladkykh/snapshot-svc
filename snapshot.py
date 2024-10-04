import os
from web3 import Web3
import json
from dotenv import load_dotenv

load_dotenv()

def load_abi_from_file(filename):
    with open(os.path.join('contracts', filename)) as f:
        return json.load(f)

w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))
contract_address = os.getenv('NFT_COLLECTION_ADDRESS')
abi = load_abi_from_file('PhygitalCollection.json')

contract = w3.eth.contract(address=contract_address, abi=abi)

total_supply = contract.functions.totalSupply().call()
snapshot = {}

for i in range(total_supply):
    token_id = contract.functions.tokenByIndex(i).call()
    owner = contract.functions.ownerOf(token_id).call()
    
    if owner not in snapshot:
        snapshot[owner] = {'count': 0, 'tokens': []}
        balance = contract.functions.balanceOf(owner).call()
        
        for j in range(balance):
            owner_token_id = contract.functions.tokenOfOwnerByIndex(owner, j).call()
            snapshot[owner]['tokens'].append(owner_token_id)
        
        snapshot[owner]['count'] = balance

# Save results 
with open('snapshot.json', 'w') as f:
    json.dump(snapshot, f)
