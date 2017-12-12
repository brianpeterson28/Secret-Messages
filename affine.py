from ciphers import Cipher
import string

class Affine(Cipher):

	def __init__(self):
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
		text = text.upper()
		affine_step_one = []
		affine_step_two = []
		affine_step_three = []
		encrypted_message = ""

		for item in text:
			for char in self.alpha_2_num.keys():
				if  item == char:
					affine_step_one.append(self.alpha_2_num[char])

		for item in affine_step_one:
			affine_step_two.append((item * 5) + 8)	

		for item in affine_step_two:
			affine_step_three.append(item % self.mod)

		for item in affine_step_three:
			for num in self.num_2_alpha.keys():
				if item == num:
					encrypted_message += self.num_2_alpha[item]

		return encrypted_message 

	def decrypt(self, text):
		pass


if __name__ == '__main__':
	affine = Affine()
	print("\nThe Affine class's alphabet is: " + affine.alphabet + "\n")
	print("The letter to number encoding is: " + str(affine.alpha_2_num)+"\n")
	print("The number to letter encoding is: " + str(affine.num_2_alpha)+"\n")
	print("affinecipher = " + affine.encrypt("affinecipher") + "\n") 
								  #expected = IHHWVCSWFRCP
