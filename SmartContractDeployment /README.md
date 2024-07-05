# Smart Contract Deployment Tool (2022)

The Smart Contract Deployment Tool facilitates the deployment of Ethereum smart contracts using Truffle and Web3. It allows users to generate and customize smart contract templates, deploy them to the Ethereum blockchain, and retrieve the contract address.


## Prerequisites

Before getting started, ensure that you have the following software installed on your machine:

- Python 3.6 or higher
- Truffle framework installed
- Web3 library installed
- Access to an Ethereum network (RPC URL)

## Usage

1. Run the script
```
python main.py
```

2. Provide the necessary contract details:
    - Contract Name
    - Token Name
    - Symbol
    - Total Supply
    - Standard Tax

3. Confirm the contract information displayed on the screen.

4. Decide whether to deploy the contract by entering 'y' or 'n'.

5. If you choose to deploy, provide the development address and private key.

6. The script will deploy the contract to the Ethereum network using Truffle and Web3. Once deployed, it will display the contract address.
