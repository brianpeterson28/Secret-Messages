from ciphers import Cipher
import string

class Affine(Cipher):

	def __init__(self):
		"""Initializes the Affine cipher class.

		The Affine cipher class initializes itself with a dictionary that 
		maps the uppercase ASCII alphabet to numerical values.
		"""

		self.alphabet = string.ascii_uppercase 
		self.alpha_2_num = {}
		self.num_2_alpha = {}
		self.mod = len(self.alphabet)
		index = 0
		for char in self.alphabet:
			self.alpha_2_num[char] = index
			self.num_2_alpha[index] = char
			index += 1 

	def encrypt(self, text):
		"""Encrypts messages using the Atbash algorithm.

		text is the message to be encrypted. 
		"""

		text = text.upper()
		affine_step_one = []
		affine_step_two = []
		affine_step_three = []
		encrypted_message = ""

		#Step 1: Loop through text and compare to alphabet to number 
		#transformation key. Translate each letter in text into an integer. 
		for item in text:
			for char in self.alpha_2_num.keys():
				if item == char:
						affine_step_one.append(self.alpha_2_num[char])
				else:
					try:
						self.alpha_2_num[item]
					except KeyError:
						affine_step_one.append(item)
						break

		#Step 2: Perform first step of numerical transformation.
		for item in affine_step_one:
			if isinstance(item, int):
				affine_step_two.append((item * 5) + 8)
			else:
				affine_step_two.append(item)

		#Step 3: Perform second step of numerical transformation. 
		for item in affine_step_two:
			if isinstance(item, int):
				affine_step_three.append(item % self.mod)
			else:
				affine_step_three.append(item)

		#Step 4: Convert integers back into letters using reverse key. 
		for item in affine_step_three:
			if isinstance(item, int):
				encrypted_message +=  self.num_2_alpha[item]
			else:
				encrypted_message += item

		return encrypted_message 


	def decrypt(self, text):
		"""Decrypts messages encrypted by the Affine algorithm.

		text is the message to be decrypted. 
		"""

		text = text.upper()
		affine_decrypt_1 = []
		affine_decrypt_2 = []
		affine_decrypt_3 = []
		decrypted_message = ""

		#Step 1: Loop through text and compare to alphabet to number 
		#transformation key. Translate each letter in text into an integer. 
		for item in text:
			for char in self.alpha_2_num.keys():
				if item == char:
					affine_decrypt_1.append(self.alpha_2_num[char])
				else:
					try:
						self.alpha_2_num[item]
					except KeyError:
						affine_decrypt_1.append(item)
						break

		#Step 2: Perform first step of numerical transformation.
		for item in affine_decrypt_1:
			if isinstance(item, int):
				affine_decrypt_2.append((item - 8) * 21) 
			else:
				affine_decrypt_2.append(item)

		#Step 3: Perform second step of numerical transformation. 
		for item in affine_decrypt_2:
			if isinstance(item, int):
				affine_decrypt_3.append(item % self.mod)
			else:
				affine_decrypt_3.append(item)

		#Step 4: Convert integers back into letters using reverse key. 
		for item in affine_decrypt_3:
			if isinstance(item, int):
				decrypted_message +=  self.num_2_alpha[item]
			else:
				decrypted_message += item

		return decrypted_message

		
if __name__ == '__main__':
	affine = Affine()
	print("\nThe Affine class's alphabet is: " + affine.alphabet + "\n")
	print("The letter to number encoding is: " + str(affine.alpha_2_num)+"\n")
	print("The number to letter encoding is: " + str(affine.num_2_alpha)+"\n")
	print("affinecipher = " + affine.encrypt("affinecipher") + "\n") 
	print(affine.decrypt("ihhwvcswfrcp"))
