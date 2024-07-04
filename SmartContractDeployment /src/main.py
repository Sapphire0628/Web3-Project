import os 
import json
from web3 import Web3
import time
import random


def initialContract():
    
    # Read File 
    _CA_file = open("../contract/TokenContract.sol", "r")       # TokenContract.sol is a template file
    _sol_file = _CA_file.read()
    _Tru_file = open("../migrations/2_Truffle_migration.txt", "r")  # 2_Truffle_migration.txt is a template file
    _js_file = _Tru_file.read()
    
    # Initial Contract variables
    _contractName = input("Contract Name : ")
    _tokenName = input("Token Name : ")
    _symbolName = input("Symbol : ")
    _totalSupply = input("Total Supply : ")
    _standardTax = input("Standard Tax : ")
    
    # Change and Write down
    _sol_file = _sol_file.replace("TestContract",_contractName).replace("tokenName", _tokenName).replace("symbolName", _symbolName).replace("_tTotal = 100000000", f"_tTotal = {_totalSupply}").replace("_standardTax=6",f"_standardTax={_standardTax}")
    _js_file = _js_file.replace("TestContract",_contractName)

    # New Contract File
    _CA_file = open(f"../contract/{_contractName}.sol", "w")
    _CA_file.write(_sol_file)
    _CA_file.close()
    
    _Tru_file = open("./ContractDeploy.js", "w")
    _Tru_file.write(_js_file)
    _Tru_file.close()
    
    time.sleep(2)
    
    return _contractName, _tokenName, _symbolName, _totalSupply, _standardTax



def deployContract(web3, _contractName, _tokenName, _symbolName, _totalSupply, _standardTax):
    file = open(f'/users/build/contracts/{_contractName}.json') # After truffle migrate, the contract json file is created in the build/contracts folder
    data = json.load(file)
    
    # input develop address
    address = input("Develop address : ")
    key = input("Private key : ")
    account_from = {"private_key": key,"address": address,}
    print(f'Attempting to deploy from account: { account_from["address"] }')
    
    # build contract
    Contract = web3.eth.contract(abi=data["abi"],bytecode=data["bytecode"])

    construct_txn = Contract.constructor().buildTransaction(
        {   'from': account_from['address'],
            'nonce': web3.eth.get_transaction_count(account_from['address']),
            'maxFeePerGas': web3.eth.gas_price + web3.toWei(f'{random.randint(2, 4)*3.14159}', 'gwei'),
            'maxPriorityFeePerGas': web3.toWei('1.5', 'gwei'),
        }
    )

    print("Contrac bytecode :")
    print()
    print(construct_txn)

    print("Confirm information : ")
    print(f"""
          
          Contract Name : {_contractName},
          Token Name : {_tokenName},
          Symbol : {_symbolName},
          Total Supply : {_totalSupply},
          Standard Tax : {_standardTax}
          """)
          
    # Deploy contract
    isDeploy = input("Decide to deploy? [y/n] :")
    if isDeploy ==  ("y" or "Y"):
        tx_create = web3.eth.account.sign_transaction(construct_txn, account_from['private_key'])
        tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Contract deployed at address: { tx_receipt.contractAddress }')

    return Contract, account_from, tx_receipt.contractAddress

    
    
def main():
    # Main Chain
    web3 = Web3(Web3.WebsocketProvider("your RPC URL"))

    # Test Chain
    #web3 = Web3(Web3.HTTPProvider('your RPC URL'))
    contractName, tokenName, symbolName, totalSupply, standardTax = initialContract()
    
    os.system("sudo truffle migrate")
    
    contract, account_from, contractAddress = deployContract(web3, contractName,tokenName,symbolName,totalSupply,standardTax)

    
        
         
    
    
if __name__ == '__main__':
    main()

