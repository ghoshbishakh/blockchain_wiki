from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import ipfsapi
from web3 import Web3
import json
from web3.auto import w3
import time
# from distance import Reputation

import argparse


api = ipfsapi.connect('127.0.0.1', 5001)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blockchain.db'
db = SQLAlchemy(app)


database = []


class Rec(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   Title = db.Column(db.String(200), nullable=False)
   Hash = db.Column(db.String(200), nullable=False)
    # date_created = db.Column(db.DateTime, default=datetime.utcnow)

   def __repr__(self):
      return '<Task %r>' % self.id






# infura_url = "https://ropsten.infura.io/v3/c40217a5035d4f458bdb66f72aa06c9c"
ganache_url = 'HTTP://127.0.0.1:8545'

# account1 = "0x25fc8f5B5Dc129FFDcA4E62F7b7e25112754110b"
# private_key1 = "4d53778e349bfd5f76eabeaeb5918a4be88672fa6d9faf6b7bfa99e5b67756e0"



# account1 = "0x19F1823B248C29cD15c73DbfEB097fD674c5b837"
# private_key1 = "83dfe9e0092db8c82129c97867a1ef4a5dbae5307c7ba51d72ef108e32ac9ca0"

# account1 = "0xa4A9a00D3908077c99BbaDdF0283ABfeE308e6E1"
# private_key1 = "6bf6ed8c82ab6befcf6f060e76fee6f83563adb94b09cc90d618158a67941afd"

# (0) 0xC459B74d6076dEf20ddd1Bf775d53f506dADd161 (100 ETH)
# (1) 0x3Ba6ab15D59F67261f07ec6CE24492D7B579A2dd (100 ETH)
# (2) 0xCF0d155F7831463A33C329D449cF474b051D4ae6 (100 ETH)
# (3) 0x88Ae20aE4a38a4ADc7e9EE1F519016dBD35Cf848 (100 ETH)
# (4) 0x6Ef06BA9D266240543Bba728BAC5eecc2379CABb (100 ETH)
# (5) 0x27f47f49AAC47eFbe73bCF716C150D15f3117Ec9 (100 ETH)
# (6) 0x1E2aB97A5aC66c413e75Fba8A466BB8E9f29C862 (100 ETH)
# (7) 0x6CB1D3CBf0b1041DDA43a3D4e2d8b48A77E6a967 (100 ETH)
# (8) 0x55FBE6De4359532821Bd6E6c74206Db3CE06454d (100 ETH)
# (9) 0x5C17Ad0070faeCf5B8C1Aa9752E1D7dA210C3B39 (100 ETH)

# Private Keys
# ==================
# (0) 0xaf1deaabcc421533a80f97cf2896fcc819e1ccf6c607bc63c9cc81a5749cb963
# (1) 0x674d3acbce99f2734bbbe2cc3c99aac814da31890aa2afe47c7c2dce6b09ac4f
# (2) 0x4ddba0da787546d133661cf787b23919e0702d3e783c130444471dea6378b292
# (3) 0xc1df84bf7c521aba149d3296d34f7755f5bd01a543e14648bff4a415d8a644a3
# (4) 0xeaa04f1c91d1ef8a3e5673b3f0d900baead9d5983eb27ec2c26b4a0f97ead340
# (5) 0xcd98a469b5897927983606c9d4f040cded630e496f20ae1f549b10b8154bff75
# (6) 0x4645d748f5974d136df24cdb2366c1d0c9defd42bbfcd763d069f38ad44a6529
# (7) 0x59fc3089e98645900363e6b0a1bd83ee8ba3a4eb1329a1e869074c5f32d2df79
# (8) 0xadebbfc49fdefbd962860a1683e757bb2a5171f917117406579ccdbce0ba74ce
# (9) 0x7f7fd37995f215ed7b677592ee68deaa54b2ed785dd319de4badab651adc43b2

# HD Wallet
# ==================
# Mnemonic:      retreat bird whale quiz hole favorite long pigeon source bone donate regret
# Base HD Path:  m/44'/60'/0'/0/{account_index}




account1 = "0x1e5f3899fa12ffab1c8f640262439d26c5266bb4"
private_key1 = "3f0081f54b9cf7c168548bb523c07fbf89d1ed96d7e72f38abffd461eb5c5614"

# account1 = "0x165d5bc83dffc82f73f7b5ba23ab11e68859a897"
# private_key1 = "25ed07cbc30887d3ef16e45597e593a2c3348f13194e63dc6922ad62c013a473"

# account1 = "0x165d5bc83dffc82f73f7b5ba23ab11e68859a897"
# private_key1 = "25ed07cbc30887d3ef16e45597e593a2c3348f13194e63dc6922ad62c013a473"


contract_address = "0x26c363c46ed12299ac49ef1d99a4432224c16e3a"

web3 = Web3(Web3.HTTPProvider(ganache_url))
address = Web3.toChecksumAddress(contract_address)
account1 = Web3.toChecksumAddress(account1)

# def init():

class wiki_contract:
   def __init__(self):
      
      abi = json.loads("""[
   {
      "constant": false,
      "inputs": [
         {
            "name": "author_address",
            "type": "address"
         },
         {
            "name": "author_reputation",
            "type": "uint256"
         }
      ],
      "name": "ReputationUpdate",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [],
      "name": "getTitles",
      "outputs": [
         {
            "name": "",
            "type": "string[]"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [],
      "name": "gasprice",
      "outputs": [
         {
            "name": "",
            "type": "uint256"
         }
      ],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [
         {
            "name": "_Title",
            "type": "string"
         }
      ],
      "name": "getTimestamps",
      "outputs": [
         {
            "name": "",
            "type": "uint256[]"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [
         {
            "name": "_author_address",
            "type": "address"
         },
         {
            "name": "value",
            "type": "uint256"
         }
      ],
      "name": "update_reputation",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [],
      "name": "send_eth",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [
         {
            "name": "_Title",
            "type": "string"
         },
         {
            "name": "_hash",
            "type": "string"
         }
      ],
      "name": "new_article",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [],
      "name": "contract_address",
      "outputs": [
         {
            "name": "",
            "type": "address"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [
         {
            "name": "_Title",
            "type": "string"
         }
      ],
      "name": "getHashes",
      "outputs": [
         {
            "name": "",
            "type": "string[]"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [],
      "name": "get_account_balance",
      "outputs": [
         {
            "name": "",
            "type": "uint256"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [
         {
            "name": "author_address",
            "type": "address"
         }
      ],
      "name": "getReputation",
      "outputs": [
         {
            "name": "",
            "type": "uint256"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [
         {
            "name": "_Title",
            "type": "string"
         }
      ],
      "name": "getAddress",
      "outputs": [
         {
            "name": "",
            "type": "address[]"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [],
      "name": "get_contract_balance",
      "outputs": [
         {
            "name": "",
            "type": "uint256"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "anonymous": false,
      "inputs": [
         {
            "indexed": false,
            "name": "ipfs_hash",
            "type": "string[]"
         },
         {
            "indexed": false,
            "name": "author_address",
            "type": "address[]"
         },
         {
            "indexed": false,
            "name": "timestamp",
            "type": "uint256[]"
         }
      ],
      "name": "article_dist_calc",
      "type": "event"
   }
]""")



      bytecode = "608060405230600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555034801561005157600080fd5b5061163d806100616000396000f3006080604052600436106100c5576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063333c8aef146100ca5780636be30e54146100f35780636ec232d31461011e57806379863ce91461013c5780637d07ef0b146101795780638ae6007a146101955780638edc091f1461019f578063966b3514146101c85780639694f9fb146101f35780639a4a8eff146102305780639c89a0e21461025b578063bf40fac114610298578063f0bc153a146102d5575b600080fd5b3480156100d657600080fd5b506100f160048036036100ec9190810190610f07565b610300565b005b3480156100ff57600080fd5b5061010861034b565b604051610115919061134e565b60405180910390f35b610126610434565b60405161013391906113de565b60405180910390f35b34801561014857600080fd5b50610163600480360361015e9190810190610f43565b610487565b60405161017091906113bc565b60405180910390f35b610193600480360361018e9190810190610f07565b61054d565b005b61019d6105dc565b005b3480156101ab57600080fd5b506101c660048036036101c19190810190610f84565b6105de565b005b3480156101d457600080fd5b506101dd610ab8565b6040516101ea9190611311565b60405180910390f35b3480156101ff57600080fd5b5061021a60048036036102159190810190610f43565b610ade565b604051610227919061134e565b60405180910390f35b34801561023c57600080fd5b50610245610c35565b60405161025291906113de565b60405180910390f35b34801561026757600080fd5b50610282600480360361027d9190810190610ede565b610c54565b60405161028f91906113de565b60405180910390f35b3480156102a457600080fd5b506102bf60048036036102ba9190810190610f43565b610ca0565b6040516102cc919061132c565b60405180910390f35b3480156102e157600080fd5b506102ea610d9c565b6040516102f791906113de565b60405180910390f35b80600260008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001819055505050565b60606000805480602002602001604051908101604052809291908181526020016000905b8282101561042b578382906000526020600020018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156104175780601f106103ec57610100808354040283529160200191610417565b820191906000526020600020905b8154815290600101906020018083116103fa57829003601f168201915b50505050508152602001906001019061036f565b50505050905090565b6000805a3a0290503373ffffffffffffffffffffffffffffffffffffffff166108fc829081150290604051600060405180830381858888f19350505050158015610482573d6000803e3d6000fd5b505090565b60606001826040518082805190602001908083835b6020831015156104c1578051825260208201915060208101905060208303925061049c565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060020180548060200260200160405190810160405280929190818152602001828054801561054157602002820191906000526020600020905b81548152602001906001019080831161052d575b50505050509050919050565b80600260008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000015401600260008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001819055505050565b565b600082908060018154018082558091505090600182039060005260206000200160009091929091909150908051906020019061061b929190610dbb565b50506001826040518082805190602001908083835b6020831015156106555780518252602082019150602081019050602083039250610630565b6001836020036101000a03801982511681845116808217855250505050505090500191505090815260200160405180910390206000018190806001815401808255809150509060018203906000526020600020016000909192909190915090805190602001906106c6929190610dbb565b50506001826040518082805190602001908083835b60208310151561070057805182526020820191506020810190506020830392506106db565b6001836020036101000a03801982511681845116808217855250505050505090500191505090815260200160405180910390206001013390806001815401808255809150509060018203906000526020600020016000909192909190916101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506001826040518082805190602001908083835b6020831015156107d257805182526020820191506020810190506020830392506107ad565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060020142908060018154018082558091505090600182039060005260206000200160009091929091909150555060001515600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060010160009054906101000a900460ff1615151415610932576000600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001819055506001600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060010160006101000a81548160ff0219169083151502179055505b7fa84b66a60e9ef2299f5cdc41e43e0f846db87e83d09231a7746cbb471b42c6aa6001836040518082805190602001908083835b60208310151561098b5780518252602082019150602081019050602083039250610966565b6001836020036101000a03801982511681845116808217855250505050505090500191505090815260200160405180910390206000016001846040518082805190602001908083835b6020831015156109f957805182526020820191506020810190506020830392506109d4565b6001836020036101000a03801982511681845116808217855250505050505090500191505090815260200160405180910390206001016001856040518082805190602001908083835b602083101515610a675780518252602082019150602081019050602083039250610a42565b6001836020036101000a0380198251168184511680821785525050505050509050019150509081526020016040518091039020600201604051610aac93929190611370565b60405180910390a15050565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60606001826040518082805190602001908083835b602083101515610b185780518252602082019150602081019050602083039250610af3565b6001836020036101000a0380198251168184511680821785525050505050509050019150509081526020016040518091039020600001805480602002602001604051908101604052809291908181526020016000905b82821015610c2a578382906000526020600020018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610c165780601f10610beb57610100808354040283529160200191610c16565b820191906000526020600020905b815481529060010190602001808311610bf957829003601f168201915b505050505081526020019060010190610b6e565b505050509050919050565b60003373ffffffffffffffffffffffffffffffffffffffff1631905090565b6000600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001549050919050565b60606001826040518082805190602001908083835b602083101515610cda5780518252602082019150602081019050602083039250610cb5565b6001836020036101000a0380198251168184511680821785525050505050509050019150509081526020016040518091039020600101805480602002602001604051908101604052809291908181526020018280548015610d9057602002820191906000526020600020905b8160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019060010190808311610d46575b50505050509050919050565b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610dfc57805160ff1916838001178555610e2a565b82800160010185558215610e2a579182015b82811115610e29578251825591602001919060010190610e0e565b5b509050610e379190610e3b565b5090565b610e5d91905b80821115610e59576000816000905550600101610e41565b5090565b90565b6000610e6c8235611586565b905092915050565b600082601f8301121515610e8757600080fd5b8135610e9a610e9582611426565b6113f9565b91508082526020830160208301858383011115610eb657600080fd5b610ec18382846115b0565b50505092915050565b6000610ed682356115a6565b905092915050565b600060208284031215610ef057600080fd5b6000610efe84828501610e60565b91505092915050565b60008060408385031215610f1a57600080fd5b6000610f2885828601610e60565b9250506020610f3985828601610eca565b9150509250929050565b600060208284031215610f5557600080fd5b600082013567ffffffffffffffff811115610f6f57600080fd5b610f7b84828501610e74565b91505092915050565b60008060408385031215610f9757600080fd5b600083013567ffffffffffffffff811115610fb157600080fd5b610fbd85828601610e74565b925050602083013567ffffffffffffffff811115610fda57600080fd5b610fe685828601610e74565b9150509250929050565b610ff98161155c565b82525050565b600061100a826114c1565b80845260208401935061101c83611452565b60005b8281101561104e57611032868351610ff0565b61103b8261150e565b915060208601955060018101905061101f565b50849250505092915050565b6000611065826114cc565b8084526020840193506110778361145f565b60005b828110156110a95761108d868354610ff0565b6110968261151b565b915060208601955060018101905061107a565b50849250505092915050565b60006110c0826114d7565b808452602084019350836020820285016110d985611471565b60005b848110156111125783830388526110f4838351611246565b92506110ff82611528565b91506020880197506001810190506110dc565b508196508694505050505092915050565b600061112e826114e2565b808452602084019350836020820285016111478561147e565b60005b8481101561117f578383038852611161838361127c565b925061116c82611535565b915060208801975060018101905061114a565b508196508694505050505092915050565b600061119b826114ed565b8084526020840193506111ad83611490565b60005b828110156111df576111c3868351611302565b6111cc82611542565b91506020860195506001810190506111b0565b50849250505092915050565b60006111f6826114f8565b8084526020840193506112088361149d565b60005b8281101561123a5761121e868354611302565b6112278261154f565b915060208601955060018101905061120b565b50849250505092915050565b600061125182611503565b8084526112658160208601602086016115bf565b61126e816115f2565b602085010191505092915050565b60008154600181166000811461129957600181146112b9576112fa565b607f600283041680865260ff1983166020870152604086019350506112fa565b600282048086526020860195506112cf856114af565b60005b828110156112f1578154818901526001820191506020810190506112d2565b80880195505050505b505092915050565b61130b8161157c565b82525050565b60006020820190506113266000830184610ff0565b92915050565b600060208201905081810360008301526113468184610fff565b905092915050565b6000602082019050818103600083015261136881846110b5565b905092915050565b6000606082019050818103600083015261138a8186611123565b9050818103602083015261139e818561105a565b905081810360408301526113b281846111eb565b9050949350505050565b600060208201905081810360008301526113d68184611190565b905092915050565b60006020820190506113f36000830184611302565b92915050565b6000604051905081810181811067ffffffffffffffff8211171561141c57600080fd5b8060405250919050565b600067ffffffffffffffff82111561143d57600080fd5b601f19601f8301169050602081019050919050565b6000602082019050919050565b60008160005260206000209050919050565b6000602082019050919050565b60008160005260206000209050919050565b6000602082019050919050565b60008160005260206000209050919050565b60008160005260206000209050919050565b600081519050919050565b600081549050919050565b600081519050919050565b600081549050919050565b600081519050919050565b600081549050919050565b600081519050919050565b6000602082019050919050565b6000600182019050919050565b6000602082019050919050565b6000600182019050919050565b6000602082019050919050565b6000600182019050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b82818337600083830152505050565b60005b838110156115dd5780820151818401526020810190506115c2565b838111156115ec576000848401525b50505050565b6000601f19601f83011690509190505600a265627a7a72305820e26bff828fd45a709d5c2ebad09953472b4342fd776229031574e1bd03015a7a6c6578706572696d656e74616cf50037"

      #Wiki = web3.eth.contract(abi = abi,bytecode = bytecode)
      #tx_receipt = web3.eth.waitForTransactionReceipt(0xbc7d32da528e93b984f91d2fe5a39eaf971f292ef0447ff2f74d88e708135cc1)

      contract = web3.eth.contract(
         address = address,
         abi = abi,
         bytecode =  bytecode
      )
      self.contract = contract
      #return contract


contract = wiki_contract().contract
# contract = contract.contract







    


class Data:
  def __init__(self,title,hash,content):   
    self.title = title
    self.hash = hash
    self.content = content

def sign_transaction(tx):
   signed_tx = web3.eth.account.signTransaction(tx, private_key=private_key1)
   
   print(web3.eth.sendRawTransaction(signed_tx.rawTransaction))


def transac(title,hash):
   print( web3.eth.getBalance(account1))
#    transaction = {
#         'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
#         'value': 1000000000,
#         'gas': 2000000,
#         'gasPrice': 234567897654321,
#         'nonce': web3.eth.getTransactionCount(account1),
#         'chainId': 1
#     }
#    key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
#    signed = w3.eth.account.signTransaction(transaction, key)

# w3.eth.sendRawTransaction(signed.rawTransaction)
   # tx = contract.functions.new_article(title,hash).buildTransaction({'nonce': web3.eth.getTransactionCount(account1), 'chainId': 10})
   tx = contract.functions.new_article(title,hash).buildTransaction({'gas': 700000,
    'gasPrice': web3.toWei('1', 'gwei'),
    'from': account1,
    'nonce': web3.eth.getTransactionCount(account1),
    'chainId' : 1})
   print(tx)
   sign_transaction(tx)

   # tx = contract.functions.getHashes().buildTransaction({'nonce': web3.eth.getTransactionCount(account1)+1})
   # signed_tx = web3.eth.account.signTransaction(tx, private_key=private_key1)
   # print(web3.eth.sendRawTransaction(signed_tx.rawTransaction))
# print(tx)
   

   print("list of titles :")
   print(contract.functions.getTitles().call())
   print("\n")
   print("versions with title name : " + str(title))

   hashes_versions = contract.functions.getHashes(title).call()

   print(hashes_versions)
   print("\n")

   print("authors addresses : ")

   authors_address = contract.functions.getAddress(title).call()
   
   print(authors_address)
   print("\n")
   





def file_to_ipfs(post,title_name):
   text_file = open(title_name + ".txt", "w")
   n = text_file.write(post)
   text_file.close()
   new_file = api.add(title_name + '.txt')
   print(new_file)
   return new_file['Hash']


# init()

@app.route("/")
def index():
   return render_template('index.html')
   # val2 = contract.functions.getTitles().call()
   # return (val2[-1])

@app.route('/new',methods = ['POST', 'GET'])
def new():
   if request.method == 'POST':
      title_name = request.form['title']
      post = request.form['post']
      hash_name = file_to_ipfs(post,title_name)
      transac(title_name,hash_name)
      new_rec = Rec(Title = title_name, Hash = hash_name)
      return redirect(url_for('success',title = title_name, hash = hash_name))   
      try :
         db.session.add(new_rec)
         db.session.commit()
         return redirect(url_for('success',title = title_name, hash = hash_name))
         
      except:
         return 'there was issue in adding task'

      # db.session.add(new_rec)
      # db.session.commit()
      return redirect(url_for('success',title = title_name, hash = hash_name))   

   else:
      return render_template('new.html')




@app.route('/success/<title>/<hash>')
def success(title,hash):
   val = 'Title is %s and hash is %s'  %(title,hash)
   return val


@app.route('/result/<title>/<hash>')
def result(title,hash):   
   content = api.cat(hash)
   content_ = content[3:-4]
   data = Data(title,hash,content_)
   return content_
   # return render_template('content.html', data = data)


@app.route('/search', methods =['POST','GET'])      
def search():
  
   if request.method == 'POST':
      title_name = request.form['title']
      record = Rec.query.filter_by(Title = title_name).first_or_404()
      content = api.cat(record.Hash)
      content_ = content[3:-4]
      
      data = Data(title_name,record.Hash,content_)
      # return redirect(url_for('result',title = title_name, hash = record.Hash))
      return render_template('search.html', data = data)
   else:
      return render_template('search.html', data = None)

@app.route('/edit/<title>/<hash>', methods =['POST','GET'])
def edit(title,hash):
   content = api.cat(hash)
   content_ = content[3:-4]
   # 
   data = Data(title,hash,content_)
   if request.method == 'POST':
      title_name = request.form['title']
      post = request.form['post']
      hash_name = file_to_ipfs(post,title_name)
      new_rec = Rec(Title = title_name, Hash = hash_name)

      # print(post)
      #return redirect(url_for('success',title = title_name, hash = hash_name))   
      try :
         db.session.add(new_rec)
         db.session.commit()
         return redirect(url_for('success',title = title_name, hash = hash_name))
      #return redirect('/login')
      except:
         return 'issue in adding task'

   else:
      
      return render_template('edit.html', data= data )
      



if __name__ == '__main__':


   
   app.run(debug = True)
   
   