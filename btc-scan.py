import hashlib
from bitcoin import *
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
from web3.auto import w3
from web3 import Web3,HTTPProvider
import web3

from bitcoin import *
from cryptos import *
import os
#word = input("Enter word: ")

def check_history(addrx):
	if history(addrx):
		with open("zzmm.txt", "a") as f:
			f.write(words)
			f.close()
			print("Transaction History Found")
	else:
		print("No History")
i = 0
while 1:
    i = i+1
    print("###:", i)
    MNEMONIC: str = generate_mnemonic(language="english", strength=128)

    # Secret passphrase/password for mnemonic
    PASSPHRASE: Optional[str] = None  # "meherett"

    # Initialize Ethereum mainnet BIP44HDWallet
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
    # Get Ethereum BIP44HDWallet from mnemonic
    bip44_hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE
    )
    # Clean default BIP44 derivation indexes/paths
    bip44_hdwallet.clean_derivation()
    words = bip44_hdwallet.mnemonic()
    print(words)
	#words = "wheat potato emotion explain timber green gasp olive fence movie damage fancy"
	#try:
    key = keystore.bip39_is_checksum_valid(words)
    coin = Bitcoin()
    wallet = coin.p2wpkh_wallet(words) #84
    #wallet = coin.wallet(words) #44
    print(wallet.keystore.root_derivation)
    addr1 = wallet.new_receiving_address()
    print("Address1: ", addr1)
    #print("Prv1: ", wallet.privkey(addr1))
    check_history(addr1)
    for x in range(2):
        print("Addr: ", x)
        addr2 = wallet.new_change_address()
        print("Address: ", addr2)
        check_history(addr2)
        x=x+1

    """
    addr2 = wallet.new_change_address()
    print("Address2: ", addr2)
    check_history(addr2)
    addr3 = wallet.new_change_address()
    print("Address3: ", addr3)
    check_history(addr3)
    addr4 = wallet.new_change_address()
    print("Address4: ", addr4)
    check_history(addr4)
    addr5 = wallet.new_change_address()
    print("Address5: ", addr5)
    check_history(addr5)
    """
		
	#except:
		#pass

