from cryptography.fernet import Fernet

def encrypt(text):
	cipher_key = b'k23xVyzUySfHReKUoqBDBChiD8kLCpBjIjTVlhKIlIA='
	cipher = Fernet(cipher_key)
	encrypted =  cipher.encrypt(text)
	return str(encrypted)[2:-1]

def decypt(text):
	cipher_key = b'k23xVyzUySfHReKUoqBDBChiD8kLCpBjIjTVlhKIlIA='
	cipher = Fernet(cipher_key)
	decrypted_text = cipher.decrypt(text)
	return str(decrypted_text)[2:-1]


ins = []

with open('main.quizer', 'r') as file:
	ins = file.readlines()



with open('enc.quizer', 'w') as file:
	for item in ins:
		file.write(str(encrypt(item.encode('utf8')))+'\n')



'''enc = encrypt(b'ahoj')
print(decypt(enc))'''

cr = []

with open('enc.quizer', 'r') as file:
	cr = file.read().splitlines()

for item in cr:
	print(str(decypt(item.encode('utf8')))[:-2])