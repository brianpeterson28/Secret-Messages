from affine import Affine
from atbash import Atbash
from caesar import Caesar
from Keyword import Keyword
import os
import string

AVAILABLE_CIPHERS = { "Caesar" : Caesar, 
	   				  "Affine" : Affine, 
					  "Atbash" : Atbash, 
					  "Keyword" : Keyword
					}

def main():
	show_welcome()
	show_available_ciphers(AVAILABLE_CIPHERS)
	cipher_name = get_cipher_name()
	action = get_action()

	if cipher_name.lower() == "keyword":
		if action == "encrypt":
			message = get_message()
			keyword = get_keyword()
			kwcipher = Keyword()
			encrypted_message = kwcipher.encrypt(message, keyword)
			print("The encrypted message is: " + encrypted_message) 
		else:
			message = get_message()
			keyword = get_keyword()
			kwcipher = Keyword()
			decrypted_message = kwcipher.decrypt(message, keyword)
			print("The decrytped message is: " + decrypted_message)
	else:
		if action == "encrypt":
			message = get_message()
			encrypted_message = encrypt_message(cipher_name.title(), message)
			print("The encrypted message is: " + encrypted_message)
		else:
			message = get_message()
			decrypted_message = decrypt_message(cipher_name.title(), message)
			print("The decrypted_message is: " + decrypted_message)

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
	cipher_name = cipher_name.title()
	try:
		test = AVAILABLE_CIPHERS[cipher_name]()
	except KeyError:
		print("Cipher Name Not Recognized. Please check your spelling.")
		cipher_name = get_cipher_name()
	return cipher_name

def get_action():
	action = input("To encrypt type \"encrypt\". To decrypt type \"decrypt\"." 
					+ " > ")
	action = action.lower()
	if action == "encrypt":
		return action
	elif action == "decrypt":
		return action
	else:
		print("Action Not Recognized. Please check your spelling.")
		action = get_action()

def get_message():
	message = input("Please enter the message. > ")
	return message

def get_keyword():
	keyword = input("Please enter the keyword. > ")
	keyword = keyword.upper()

	#Test 1
	if len(keyword) > 10:
		print("Length Error. A keyword cannot be longer than 10 characters.")
		keyword = get_keyword()

	#Test 2
	test_unique = ""
	test_keyword = keyword
	for item in test_keyword:
		if item == test_unique:
			print("Illegal Keyword Error. A keyword must have unique letters.")
			print("For example, the word \"Twist\" is illegal because " + 
				  "it contains two \"t\"\'s. But the word \"Axiom\"" 
				   + " is " + "valid because there are no repeated letters.")
			keyword = get_keyword()
		else:
			test_unique = item

	#Test 3
	alphabet = string.ascii_uppercase
	alphabet_dict = {}
	for char in alphabet:
		alphabet_dict[char] = char

	for item in keyword:
		try:
			alphabet_dict[item]
		except KeyError:
			print("Illegal Keyword Error. A keyword can only contain " + 
				"American alaphabet letters A - Z. \n" + "Spaces, " + 
				"punctuation, and special characters are not allowed.")
			keyword = get_keyword()

	return keyword

def encrypt_message(cipher_name, message):
	cipher = AVAILABLE_CIPHERS[cipher_name]()
	encrypted_message = cipher.encrypt(message)
	return encrypted_message

def decrypt_message(cipher_name, message):
	cipher = AVAILABLE_CIPHERS[cipher_name]()
	decrypted_message = cipher.decrypt(message)
	return decrypted_message

def end_program():
	end = input("Would you like to encrypt or decrypt another message, " + 
				"Yes or No? > ")
	if end.title() == "Yes":
		return False
	elif end.title() == "No":
		return True
	else:
		print("Quit Error. Please type \"Yes\" or \"No\".")
		end = end_program()
		
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear') 

if __name__ == '__main__':
	main()