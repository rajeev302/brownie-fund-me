from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1] #last deployed contract for Fund Me. Brownie will help in that.
    account = get_account() #metamask account private key
    print(account)
    entrance_fee = fund_me.getEntranceFee() #amount to be funded
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee}) #call fund method of last deployed contract.


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    # withdraw()  