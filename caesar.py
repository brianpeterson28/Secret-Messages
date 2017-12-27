from ciphers import Cipher
import string


class Caesar(Cipher):
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        alpha = string.ascii_uppercase
        self.offset = offset
        self.FORWARD = alpha + alpha[:self.offset+1]
        self.BACKWARD = alpha[:self.offset+1] + alpha

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)


if __name__ == '__main__':
    item = Caesar()
    print(str(item.FORWARD))
    print(str(item.BACKWARD))
