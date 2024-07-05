# Ethereum Smart Contract Scanner (2021)

The Ethereum Smart Contract Scanner scans the Ethereum blockchain for the deployed smart contract and stores relevant contract information in a MySQL database.

## Features

- Scans the Ethereum blockchain for the deployed smart contract at least block 
- Retrieves contract addresses and associated token names
- Stores contract information in a MySQL database
- Supports automatic deletion of launched contracts from the database
- Provides real-time notifications using the system bell sound

## Prerequisites

- Python 3.6 or higher
- MySQL database
- Web3, requests, BeautifulSoup, and MySQL Connector libraries

## Usage

1. Clone the repository and install the required libraries.
2. Set up the MySQL database and configure the connection parameters in the script.
3. Replace `your RPC URL` with your own Ethereum API key in the `projectID` variable.
4. Run the script 

```
python scanner.py
```

5. Monitor the script as it scans the Ethereum blockchain and stores contract information in the database.

