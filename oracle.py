from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import ipfsapi
from web3 import Web3
import json
from web3.auto import w3
import time

from distance import Reputation
from app import wiki_contract



class event_listener:

	def __init__(self, contract, account,private_key):
		self.contract = contract
		# self.contract_address = contract_address
		self.account = account
		self.private_key = private_key
		

	

	    #print(event)
	
	   
	      

	def log_loop(self,event_filter, poll_interval,web3,m,T):
		while True:
			for event in event_filter.get_new_entries():
				# event = event_filter.get_new_entries()
				print("event detected")
				# print(web3.eth.getFilterLogs(event_filter.filter_id))
				#print(event["args"]["ipfs_hash"])

				hashes = event["args"]["ipfs_hash"]
				total_versions = len(hashes)
				hashes = hashes[total_versions-m:]

				author_address = event["args"]["author_address"]
				author_address = author_address[total_versions-m:]

				timestamp = event["args"]["timestamp"]
				timestamp = timestamp[total_versions-m:]

				

				print(hashes)
				print("\n\n")

				print(author_address)
				print("\n\n")


				author_reputation = []

				for i in range(len(author_address)):
					val = self.contract.functions.getReputation(author_address[i]).call()
					author_reputation.append(val)
				print(author_reputation)
				print("\n\n")
				X = Reputation(author_address,author_reputation,hashes,timestamp,m,T)
				updated_reputations = X.final_updation()
				print(updated_reputations)

				for i in range(len(author_address)):
					tx = self.contract.functions.ReputationUpdate(author_address[i],updated_reputations[i]).buildTransaction({'nonce': web3.eth.getTransactionCount(self.account)})
					signed_tx = web3.eth.account.signTransaction(tx, private_key = self.private_key)
				print(web3.eth.sendRawTransaction(signed_tx.rawTransaction)) 

				time.sleep(poll_interval) 

				

	        # receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
	        # result = contract.events.article_dist_calc.processReceipt(receipt)
	        # print(result[0]['args'])
	        #print(event[0]["args"]["article_ipfs_hashes"])
	        # print(web3.eth.abi.decodeLog(inputs, hexString, topics))
	        #handle_event(event)
	        

def main():
	

	ganache_url = 'HTTP://127.0.0.1:8545'
	web3 = Web3(Web3.HTTPProvider(ganache_url))


	#     Available Accounts

	# (0) 0x8C9194Ab5426af038fc32471d92d76098682F271 (100 ETH)
	# (1) 0x9929A2434AFC8599992FDb75BB58f0E5D015c097 (100 ETH)
	# (2) 0xB3A3f27166e5717C8888745D9d7031b0E6a4F447 (100 ETH)
	# (3) 0x1dA55B36de127dd7E1d7e1DA9D24EF704d04A3b2 (100 ETH)
	# (4) 0x3f31E8FB9ffCDC446c4130664084Cf0649e59D22 (100 ETH)
	# (5) 0x17b00BD55861d1b7bFd01959Bb9EcdeFAbFf77e7 (100 ETH)
	# (6) 0x0CE322E209FEce91AeE6d06A3f66Cd548380718E (100 ETH)
	# (7) 0xe0cAE87A455Cb9863622Bd51bddB3D28B754406e (100 ETH)
	# (8) 0xAAd4e25f5Ef010fF1E157B3C58b82ea6309885A2 (100 ETH)
	# (9) 0x90fD8D3d1C91fBa6dC5F6F63D691E98dC3741145 (100 ETH)

	# Private Keys

	# (0) 0x414844e149c5567d0ad35927352bf9d162748cb3e991449e07d17fba478e1386
	# (1) 0x77afed77b6b008cbca3f9d8019c36334f662f16bbfe0fcda356da290b6a56f4e
	# (2) 0x0ddf60e5e7e6f1e3661747b86cca02c3390b3fe0448b4fd34a50055a3a158671
	# (3) 0x157d26b4aa30f0461c38efa6508f40ca82ec84dfab488775b280b71bfa096178
	# (4) 0xc4cc5ba7dfb85ce41fac4782c87b086ffc3aaafa75fdd7a879ba135dadeb9161
	# (5) 0xaa71958b34a708ebc519402ffa381dab6e65c788313679690d591cb6789060b9
	# (6) 0xadc0d262a8a1063526369e08b30c91051bc8fa83f9fc436d03b721be46c80ba8
	# (7) 0x97fde9f75ce82b6d38babb640ab7c2d17e040d5aecea62012d419425f7271633
	# (8) 0x54d93b4c888e0ba9ced3bf7dac6b1f0eae6ad9acfc970b47cf43f89de7692f93
	# (9) 0xe3a02c3136e8c66e99dde9dd11046cbd7b64863d9877d8873407f25bdf4f1d67

	account1 = "0x8C9194Ab5426af038fc32471d92d76098682F271"
	private_key1 = "0x414844e149c5567d0ad35927352bf9d162748cb3e991449e07d17fba478e1386"

	contract = wiki_contract().contract
	m = 10
	T = 2000



	
	block_filter = contract.events.article_dist_calc.createFilter(fromBlock="latest")

	# block_filter = web3.eth.filter({'fromBlock' : 'latest', 'address' : contract_address, 'from' : account1})

	
	event_listener(contract, account1,private_key1).log_loop(block_filter,0,web3,m,T)
	# log_loop(block_filter,0,web3,m,T)


if __name__ == '__main__':
    main()



    