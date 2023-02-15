from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3 

FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork', 'mainnet-fork-dev']

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local","ganache-cli" ]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active networks is {network.show_active()}")
    print("Deploying Mocks ...")
    if len(MockV3Aggregator) <= 0: # only when we dont have an other mock deploed we should deploy a mock, MockV3Aggregator is also a list deployed 
        MockV3Aggregator.deploy(
            # 18, 200000000000000000, {"from": account}
            # DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account() ## toWei adds 18 zeros to 2000
            DECIMALS,STARTING_PRICE, {"from": get_account()} # changinged to have the same decimals that the function in the contract has 
        )  # feeding in the inputs in the contract of mocks (decimals and initials )
