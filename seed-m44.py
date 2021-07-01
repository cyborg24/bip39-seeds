from bitcoin import *
from cryptos import *

def check_history(addrx):
	if history(addrx):
		with open("seedm.txt", "a") as f:
			f.write(words)
			f.close()
			print("Transaction History Found")
			exit()
	else:
		print("No History")
i = 0
while 1:
	i = i+1
	print("###:", i)
	handle = open("english.txt", "r")
	linex = handle.read().splitlines()
	lines = random.sample(linex, len(linex))
	x1 = random.choice(lines)
	x2 = random.choice(lines)
	x3 = random.choice(lines)
	x4 = random.choice(lines)
	x5 = random.choice(lines)
	x6 = random.choice(lines)
	x7 = random.choice(lines)
	x8 = random.choice(lines)
	x9 = random.choice(lines)
	x10 = random.choice(lines)
	x11 = random.choice(lines)
	x12 = random.choice(lines)
	words = x1+ " "+ x2+" "+x3+" "+x4+" "+x5+" "+x6+" "+x7+" "+x8+" "+x9+" "+x10+" "+x11+" "+x12
	print(words)
	#words = "wheat potato emotion explain timber green gasp olive fence movie damage fancy"
	try:
		key = keystore.bip39_is_checksum_valid(words)
		coin = Bitcoin()
		wallet = coin.wallet(words)
		wx = wallet.keystore.root_derivation = "m/44'/0'/0'"
		print(wx)
		addr1 = wallet.new_receiving_address()
		print("Address1: ", addr1)
		#print("Prv1: ", wallet.privkey(addr1))
		check_history(addr1)
		
		for x in range(2):
			print("Addr: ",x)
			addr2 = wallet.new_change_address()
			print("Address: ", addr2)
			check_history(addr2)
		"""
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
		x = x+1
	except TabError:
		pass




