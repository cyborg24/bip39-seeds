from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
from web3.auto import w3
from web3 import Web3,HTTPProvider
import web3

i = 0
while(1):
    i = i+1
    print("###:", i)
    w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/7b5ccbd2feee4832a43cc9f5aaabf0be'))
    #print(w3.isConnected())

    # Generate english mnemonic words
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

    print("Mnemonic:", bip44_hdwallet.mnemonic())
    print("Base HD Path:  m/44'/60'/0'/0/{address_index}", "\n")

    # Get Ethereum BIP44HDWallet information's from address index
    for address_index in range(1):
        # Derivation from Ethereum BIP44 derivation path
        bip44_derivation: BIP44Derivation = BIP44Derivation(
            cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
        )
        # Drive Ethereum BIP44HDWallet
        bip44_hdwallet.from_path(path=bip44_derivation)
        #Get balance for address
        eth_balance = w3.eth.getBalance(bip44_hdwallet.address())
        eth_balance = int(eth_balance) / (10**18)
        if eth_balance > 0.0001:
            with open("zzzethfound.txt", "a") as f:
                f.write(f"{bip44_hdwallet.mnemonic()} ==> {eth_balance} \n")
                f.close()
                print("Transaction History Found")
        #print("BALANCE: ", eth_balance)
        # Print address_index, path, address and private_key
        print(f"({address_index}) {bip44_hdwallet.path()} {bip44_hdwallet.address()} 0x{bip44_hdwallet.private_key()} BAL:{eth_balance}")
        # Clean derivation indexes/paths
        bip44_hdwallet.clean_derivation()
