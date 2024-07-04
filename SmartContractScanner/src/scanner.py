"""-------------------------------Packages importing-------------------------------"""

# Web3 & HTTP connection packages
import requests 
from web3 import Web3
from bs4 import BeautifulSoup

# Time packages 
import datetime 
import time

# Pandas packages
import pandas as pd


# Mysql packages
import mysql
import mysql.connector



import os

"""-------------------------------------Setting-------------------------------------"""

# Mysql connection

connection = mysql.connector.MySQLConnection(user='user', password='password',
                                             host='127.0.0.1',database='database')



cursor = connection.cursor()

print("SQL Connected")
print()

projectID= 'your RPC URL'
web3 = Web3(Web3.HTTPProvider(projectID))

headers = header


    
    
def blockScannerForContract(duration):
    """
    Scans the Ethereum blockchain for smart contract transactions within the specified duration.
    
    Parameters:
    - duration (int): Number of blocks to scan.
    
    Returns: None
    """
    
    # Get the latest block number and calculate the starting block number
    _newBlock = web3.eth.blockNumber
    _startBlock = _newBlock - duration 
    
    print("Looking for Smart Contract: ")
    print()
    
    decision = input("Del table YES or NO :")
    if decision == "y":
        # Delete all rows from the ContractScans table
        del_stmt = "DELETE FROM ContractScans;"
        cursor.execute(del_stmt)
        connection.commit()
    
    while(_newBlock>_startBlock):
        
        # Retrieve the block data
        _block = web3.eth.get_block(_startBlock, True)
        _blockTranscation = _block["transactions"]
        _time = datetime.datetime.utcfromtimestamp(web3.eth.get_block(_startBlock)["timestamp"])


        
        
        for i in range(0,len(_blockTranscation)):
            _transaction = _blockTranscation[i]
            
            if (len(_transaction["input"])>7000 ):
                _transactionReceipt = web3.eth.get_transaction_receipt(_transaction["hash"].hex())
                
                if (_transactionReceipt["contractAddress"] != (None and [])):
                     

                    ContractAddress = _transactionReceipt["contractAddress"]
                    
                    
                    _url = f"https://etherscan.io/token/{ContractAddress}"
                    
                    # Send a request to retrieve the webpage content
                    response = requests.get(_url,headers=headers) 
                    _body = BeautifulSoup(response.content, "lxml")
                    _token = _body.find(class_="media-body")
                    
                    _tableList = _body.find(id="nav_tabs")
                    if _tableList != None:
                        _tableList.find_all("li")
                        
                    _isDex = True
                    for item in _tableList :
                        if item.text == "NFT Trades":
                            _isDex = False
                            
                    if _token != None and _isDex == True:
                        if _token.find("span") != None:
                            _tokenName = _token.find("span").text

                            # Insert/update the contract information in the ContractScans table
                            _insertStatement= """INSERT INTO ContractScans (contractAddress,tokenName, isLaunch, Chain, timeStamp) 
                                            VALUES (%s,%s, %s, %s, %s)
                                            ON DUPLICATE KEY UPDATE
                                            contractAddress = %s,
                                            tokenName = %s,
                                            isLaunch = %s,
                                            Chain = %s, 
                                            timeStamp = %s;"""
                                            
                            cursor.execute(_insertStatement, (ContractAddress,_tokenName,0,"ETH",_time,ContractAddress,_tokenName,0,"ETH",_time))
                            connection.commit()
                            os.system("tput bel")

        _startBlock = _startBlock +1
        
        # Delete rows from the ContractScans table where isLaunch=1
        _autoDelStatement = """DELETE FROM ContractScans WHERE isLaunch=1;"""
        cursor.execute(_autoDelStatement)
        connection.commit()

        while(_newBlock == _startBlock):
            time.sleep(8) 
            _newBlock = web3.eth.blockNumber
            
            
    cursor.close()
        
    
blockScannerForContract(50)
