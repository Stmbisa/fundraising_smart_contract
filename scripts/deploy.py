from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS



def deploy_fund_me():
    account = get_account()
    # pass the price fee address to our fundMe contract through constructor
    # if we are a on a persistent network like rinkeby, use the associated address
    # otherwise  deploy mocks, SO WE CANT USE THE WALLET DIRECTLY BECAUSE WE HAVE TO DETERMINE
    # the most effecient method to would be to add it in the config file so that we fetch the address there if prove which network we are on

    # if network.show_active() != "development":
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS: # this is because we have more than one network we may have as many as we wish to add
        # whatever network we are on if its not in the list then we use config or we should use the else statment block
        # price_feed_address = "0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e"
        # we will get the price feed in the same location if we are using mainnet-fork
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed" 
        ]
    else:  # just in case are on development, we will use our mock kind of interface instead, here we are importing it were we builr from 
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address # we are doing this because this is a list of addresses of mocks
        # so here are using the most recent address 
        print("Mocks deployed successfully")

    # eth_usd_price_feed = 0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e
    # fund_me = FundMe.deploy('0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e', {"from": account}, publish_source = True) #this wouldnt work on scale
    # fund_me = FundMe.deploy(eth_usd_price_feed, {"from": account}, publish_source = True) # this wouldnt work well as well
    fund_me = FundMe.deploy(
        # price_feed_address, {"from": account}, publish_source=True # wwe would verify the contract depending on whether its on local or on a netwrok, 
        price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"), # .get verify isnt mandatory but it will help if we forget to add verify: True or false in the config file 
        # network.show_active() refer to a networ name we fetch from brownie either have specified
        #  config["networks"][network.show_active()].get("verify") refer to the cofig file and the default setting
    )
    # this is how you pass variables to constructors from brownie
    print(f"Contract deployed to ${fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
