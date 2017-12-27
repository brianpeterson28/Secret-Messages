from ciphers import Cipher
import string


class Atbash(Cipher):

    def __init__(self):
        """Initializes the Atbash cipher class.

        The Atbash cipher class initializes itself with the a forward and
        backward uppercase ASCII alphabet as the alphabet to be used when
        encrypting and decrypting messages.
        """

        self.alphabet = string.ascii_uppercase
        self.forward_list = self.create_forward_alpha_list(self.alphabet)
        self.backward_list = self.create_backward_alpha_list(self.alphabet)
        self.encrypt_key = dict(zip(self.forward_list, self.backward_list))
        self.decrypt_key = dict(zip(self.forward_list, self.backward_list))

    def encrypt(self, text):
        """Encrypts messages using the Atbash algorithm.

        text is the message to be encrypted.
        """

        text = text.upper()
        encrypted_message = ""
        for item in text:
            try:
                encrypted_message += self.encrypt_key[item]
            except KeyError:
                encrypted_message += item
        return encrypted_message

    def decrypt(self, text):
        """Decrypts messages encrypted by the Atbash algorithm.

        text is the message to be decrypted.
        """

        text = text.upper()
        decrypted_message = ""
        for item in text:
            try:
                decrypted_message += self.decrypt_key[item]
            except KeyError:
                decrypted_message += item
        return decrypted_message

    def create_backward_alpha_list(self, alphabet):
        """Creates alphabet to be used in __init__ method

        This is a helper function that creates an element of the key to be used
        to encrypt and decrypt messages.
        """

        backward_list = []
        for item in alphabet[::-1]:
            backward_list.append(item)
        return backward_list

    def create_forward_alpha_list(self, alphabet):
        """Creates alphabet to be used in __init__ method

        This is a helper function that creates an element of the key to be used
        to encrypt and decrypt messages.
        """

        forward_list = []
        for item in alphabet:
            forward_list.append(item)
        return forward_list


if __name__ == '__main__':
    atbash = Atbash()
    print(atbash.forward_list)
    print(atbash.backward_list)
    print(atbash.ecrypt_key)
    print(atbash.decrypt_key)
    message = "ab  cd!"
    print(atbash.encrypt(message))
    secret = atbash.encrypt(message)
    print(atbash.decrypt(secret))
