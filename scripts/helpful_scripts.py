from brownie import network, config, accounts,  MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000 # Web3.toWei(200, "ether")

def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or 
        network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        print(f"The active network is {network.show_active()}")
        return accounts[0]
    else:
        print(f"The active network is {network.show_active()}")
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        mock_aggregator_address = MockV3Aggregator.deploy(
            DECIMALS,  
            STARTING_PRICE, 
            {"from": get_account()}
        )
    price_feed_address = MockV3Aggregator[-1].address
    