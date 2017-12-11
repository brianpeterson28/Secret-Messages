import os
from caesar import Caesar

AVAILABLE_CIPHERS = ["Caesar", "Affine", "Atbash", "Key Word"]

def main():
	show_welcome()
	show_available_ciphers(AVAILABLE_CIPHERS)
	cipher_name = get_cipher_name()
	message = get_message()
	encrypted_message = encrypt_message(cipher_name, message)
	print("The user selected the follwoing cipher: " + cipher_name)
	print("The user entered the follwoing message: " + "\"" + message + "\"")
	print("The encrypted message is: " + encrypted_message)
	if end_program():
		pass
	else:
		clear_screen()
		main() 

def show_welcome():
	print("\nThis is the Secret Messages Project for the Treehouse" 
		+ " Techdegree.")

def show_available_ciphers(list_of_ciphers):
	print("The following ciphers are available:\n")
	num = 1
	for item in list_of_ciphers:
		print(str(num) + ". " + item)
		num += 1
	print("\n")

def get_cipher_name():
	cipher = input("Please enter the name of the cipher you would " +  
		           "like to use. > ")
	return cipher

def get_message():
	message = input("Please enter the message. > ")
	return message

def end_program():
	end = input("Would you like to encrypt or decrypt another message? > ")
	if end == "Yes":
		return False
	else:
		return True

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear') 

def encrypt_message(cipher_name, message):
	cipher = create_cipher(cipher_name)
	encrypted_message = cipher.encrypt(message)
	return encrypted_message

def create_cipher(cipher_name):
	cipher = None 
	if cipher_name == "Caesar":
		cipher = Caesar()
		return cipher
	else:
		pass

if __name__ == '__main__':
	main()