from affine import Affine
from atbash import Atbash
from caesar import Caesar
from hill import Hill
import os
import string

AVAILABLE_CIPHERS = { "Caesar" : Caesar, 
	   				  "Affine" : Affine, 
					  "Atbash" : Atbash, 
					  "Hill" : Hill
					}

def main():
	show_welcome()
	show_available_ciphers(AVAILABLE_CIPHERS)
	cipher_name = get_cipher_name()
	message = get_message()
	encrypted_message = encrypt_message(cipher_name.title(), message)
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

def show_available_ciphers(available_ciphers):
	print("The following ciphers are available:\n")
	num = 1
	for name in available_ciphers.keys():
		print(str(num) + ". " + name)
		num += 1
	print("\n")

def get_cipher_name():
	cipher_name = input("Please enter the name of the cipher you would " +  
		           "like to use. > ")
	return cipher_name

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
	cipher = AVAILABLE_CIPHERS[cipher_name]()
	encrypted_message = cipher.encrypt(message)
	return encrypted_message

if __name__ == '__main__':
	main()