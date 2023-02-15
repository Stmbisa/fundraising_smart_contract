from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f'The current entry fee is ${entrance_fee}')
    print("Funding")
    fund_me.fund({"from": account, 'value': entrance_fee})
    # fund is a function that requires a value so it has to be fed in here 

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    # withdraw is a function that already determined that all the funds should be withdrawn thats why we dont need a value keyword here


def main():
    fund()
    withdraw()