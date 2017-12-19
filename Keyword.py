from ciphers import Cipher
import copy
import string

class Keyword(Cipher):
	def __init__(self):
		"""Initializes the Keyword cipher class.

		The Keyword cipher class initializes itself with the uppercase ASCII 
		alphabet as the alphabet to be used when encrypting and decrypting 
		messages.
		"""

		self.normal_alphabet = []
		for item in string.ascii_uppercase:
			self.normal_alphabet.append(item)


	def encrypt(self, text, keyword):
		"""Encrypts messages using the Keyword algorithm.

		text is the message to be encrypted. 
		keyword is the keyword used to shift the alphabet. 
		"""

		text = text.upper()
		encrypted_message = ""
		self.create_kw_list(keyword)
		self.keyword_alphabet = self.create_kw_alphabet()
		self.encrypt_key = dict(zip(self.normal_alphabet, 
									self.keyword_alphabet))
		for letter in text:
			try:
				encrypted_message += self.encrypt_key[letter]
			except KeyError:
				encrypted_message += letter
		return encrypted_message


	def decrypt(self, text, keyword):
		"""Decrypts messages encrypted by the Keyword algorithm. 

		text is the message to be decrypted.
		keyword is the keyword that was originally used to encrypt the message. 
		"""

		text = text.upper()
		decrypted_message = ""
		self.create_kw_list(keyword)
		self.keyword_alphabet = self.create_kw_alphabet()
		self.decrypt_key = dict(zip(self.keyword_alphabet, 
									self.normal_alphabet))
		for letter in text:
			try:
				decrypted_message += self.decrypt_key[letter]
			except KeyError:
				decrypted_message += letter
		return decrypted_message


	def create_kw_list(self, keyword):
		"""Prepares keyword string for processing by encrypt() and decrypt().

		This is a helper function  that converts keyword from a string to a 
		list so that keyword can be utilized more readily by the encrypt and 
		decrypt methods.
		"""

		keyword = keyword.upper()
		self.keyword_list = []
		for item in keyword:
			self.keyword_list.append(item)


	def create_kw_alphabet(self):
		"""Creates translation key for encrypting and decrypting messages.

		This is a helper function that creates the alphabet used to translate 
		messages using the Keyword algorithm.
		"""

		kw_alphabet = copy.deepcopy(self.normal_alphabet)
		for item in self.keyword_list:
			for letter in kw_alphabet:
				if item == letter:
					kw_alphabet.remove(letter)
		kw_alphabet = self.keyword_list + kw_alphabet
		return kw_alphabet


if __name__ == '__main__':
	lobo = Keyword()
	print(lobo.encrypt("knowledge is power", "kryptos"))
	print(lobo.decrypt("dghvetpst bm ihvtl", "kryptos"))
	print(lobo.normal_alphabet)
	print(lobo.keyword_alphabet)
