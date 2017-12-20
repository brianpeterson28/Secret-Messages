"""Treehouse Tech Degree - Project 2 - Secret Messages

This is an interactive program that allows the user to encrypt and decrypt 
messages using various cipher methods. 
"""

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
    """Main Program Logic

    1. Display welcome message
    2. Determine which cipher to use
    3. Determine which action to perform (i.e. encrypt or decrypt)
    4. If Keyword cipher chosen then do special calculations
    5. If any other cipher was selected then perform general calculations
    6. Determine whether to terminate program or repeat it.
    """

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
    """Prints the welcome message to the command line."""

    print("\nThis is the Secret Messages Project for the Treehouse" 
        + " Techdegree.")


def show_available_ciphers(available_ciphers):
    """Prints the available ciphers the command line."""

    print("The following ciphers are available:\n")
    num = 1
    for name in available_ciphers.keys():
        print(str(num) + ". " + name)
        num += 1
    print("\n")


def get_cipher_name():
    """Gets the cipher name from the user. 

    It tests to make sure the user has entered a valid cipher name and then 
    it returns a valid string cipher name. 
    """

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
    """Gets the desired action from the user.

    It tests to make sure the user has entered a valid action and the it then 
    returns a valid string action. The only valid actions are encrypt and 
    decrypt. 
    """

    action = input("To encrypt type \"encrypt\". To decrypt type \"decrypt\"." 
                    + " > ").lower()
    
    if action == "encrypt":
        return action
    elif action == "decrypt":
        return action
    else:
        print("Action Not Recognized. Please check your spelling.")
        action = get_action()
        return action


def get_message():
    """Gets the message to be encrypted or decrypted from the user.

    It takes input from the use and returns a string message.
    """
    message = input("Please enter the message. > ")
    return message


def get_keyword():
    """Gets the keyword if Keyword Cipher selected by user.

    It tests to make sure the keyword meets certain requirements. If the user's
    input does not satisfy the criteria then it explains the problem and 
    prompts the user to re-enter a keyword. 

    Once all the relevant criteria are met, it returns the keyword to be used
    by the Keyword Cipher object. 
    """

    keyword = input("Please enter the keyword. > ")
    keyword = keyword.upper()

    #Does not allow keywords longer than 10 letters. 
    if len(keyword) > 10:
        print("Length Error. A keyword cannot be longer than 10 characters.")
        keyword = get_keyword()

    #Does not allow keywords with non-unique letters. 
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

    #Does not allow keywords with spaces or punctuation. 
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
    """Encrypts the message based upon the selected cipher. 

    Dynamically encrypts the message based on the user's input. It returns the
    encrypted message as a string. 
    """

    cipher = AVAILABLE_CIPHERS[cipher_name]()
    encrypted_message = cipher.encrypt(message)
    return encrypted_message


def decrypt_message(cipher_name, message):
    """Decrypts the message based upon the selected cipher. 

    Dynamically decrypts the message based on the user's input. It returns the
    decrypted message as a string. 
    """

    cipher = AVAILABLE_CIPHERS[cipher_name]()
    decrypted_message = cipher.decrypt(message)
    return decrypted_message


def end_program():
    """Terminates the program. 

    Dynamically termintaes the program based on the user's input. 
    """

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
    """Clears the screen of all prior input and output."""

    os.system('cls' if os.name == 'nt' else 'clear') 


if __name__ == '__main__':
    main()
