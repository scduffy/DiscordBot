import time
import _tkinter

"""
super_commando_encryption: Encrypts and Decrypts private communications between Super Commandos and Thot Patrol Agents.
"""

__author__ = "Chase Duffy"
__copyright__ = "Copyright 2018, Govt. of Uganda"

# Global alphabet list that both encryption and decryption use as a reference.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", " ", ",", "\"", "'", ".", "/", "!", "@", "#", "$", "%", "^", "&", "(",
            ")", "-", "_", "+", "=", "{", "[", "]", "}", ":", ";", "?", "\\", "|", "<", ">", "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "0", "’", "“", "”", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# Getter for user input of original phrase.
def get_to_encryption():
    user_input = input("Enter phrase to be encrypted: ")
    return user_input


# Getter for user input of key.
def get_key():
    key = input("Enter the key: ")
    return key


# Getter for user input of encrypted text.
def get_from_encryption():
    encrypted = input("Enter encrypted phrase: ")
    return encrypted


# Takes a phrase given by user and a key and encrypts it.
# Note only this software can accurately decrypt the already encrypted messages.
def encrypt(phrase, key):
    encrypted_phrase = ""
    encrypted_chars = []
    char_indexes = []
    key_indexes = []

    # Iterating through each character in given message.
    for char in phrase:
        # Catching error in case of unexpected/unrecognized unicode characters.
        # Assigns unrecognized characters as '^' by default to make them recognizable in output.
        try:
            char_index = alphabet.index(char)
        except ValueError:
            flair()
            print()
            print("Error: Character not recognized. Replacing with '^'.")
            print()
            flair()
            char_index = 37
        # Adds index of recognized character in alphabet list to a list of indexes
        char_indexes.append(char_index)
        # Iterates through all chars in key and assigns their char indexes within the alphabet to a list of indexes.
    for char in key:
        # Tries to add indexes of recognized characters to list. If not recognized, program exits so that the message
        # will not be encrypted with a broken key. (In future may change this to try and fix key).
        try:
            key_index = alphabet.index(char)
        except ValueError:
            flair()
            print()
            print("Error: Character not recognized in key. Exiting to prevent message from becoming indecipherable.")
            print()
            flair()
            raise SystemExit
        key_indexes.append(key_index)

    key_counter = 0
    # Applies the actual encryption by adding the index of char key_counter key in the alphabet to the index of char x
    # in the phrase.
    # If message is longer than the key, the key_counter resets to 0 so that it adds the index of the char in pos 1 of
    # the key again.
    for x in range(len(phrase)):
        if key_counter >= len(key_indexes):
            key_counter = 0
        # Encryption application
        #encrypted_chars.append((char_indexes[x] + key_indexes[key_counter]) % (len(alphabet) - 1))
        encrypted_chars.append((char_indexes[x] + key_indexes[key_counter]) % 96)
        key_counter += 1

    # Convert numerical representation of chars into real chars
    for number in encrypted_chars:
        encrypted_phrase += alphabet[number]

    return encrypted_phrase


# Takes encrypted phrase and a key and decrypts message to make it human readable.
# Note that the decryption only works on encrypted messages generated from THIS program.
def decrypt(phrase, key):
    decrypted_phrase = ""
    decrypted_chars = []
    char_indexes = []
    key_indexes = []

    # Catching error in case of unexpected/unrecognized unicode characters.
    # Assigns unrecognized characters as '^' by default to make them recognizable in output.
    for char in phrase:
        try:
            char_index = alphabet.index(char)
        except ValueError:
            flair()
            print()
            print("Error: Character not recognized. Replacing with '^'.")
            print()
            flair()
            char_index = 37
        # Adds index of recognized character in alphabet list to a list of indexes
        char_indexes.append(char_index)

    # Tries to add indexes of recognized characters to list of key indexes. If not recognized, program exits so that the
    # original message will not be scrambled due to a key with an invalid character set.
    for char in key:
        try:
            key_index = alphabet.index(char)
        except ValueError:
            flair()
            print()
            print("Error: Character not recognized in key. Exiting due to invalid character in key.")
            print()
            flair()
            raise SystemExit
        key_indexes.append(key_index)

    # Decrypts by subtracting the index of the char in the alphabet at key_indexes[key_counter] from the index of the
    # char in the alphabet at char_indexes[x]. This undoes what the encryption did originally so long as the keys are
    # the same phrase.
    key_counter = 0
    for x in range(len(phrase)):
        if key_counter >= len(key_indexes):
            key_counter = 0
        # Decryption application
        #decrypted_chars.append((char_indexes[x] - key_indexes[key_counter]) % (len(alphabet) - 1))
        decrypted_chars.append((char_indexes[x] - key_indexes[key_counter]) % 96)
        key_counter += 1

    # Convert numerical representation of chars into real chars
    for number in decrypted_chars:
        decrypted_phrase += alphabet[number]

    return decrypted_phrase


def startup():
    flair()

    # Prints out SUPER COMMANDO SOFTWARE in ASCII art for aesthetic and as a watermark for being made specifically for
    # the super commandos under the command of Captain Alex(RIP).
    print(" ____  _     ____  _____ ____    ____  ____  _      _      ____  _      ____  ____    ____  ____  _____ ____"
          "_  _      ____  ____  _____")
    print("/ ___\/ \ /\/  __\/  __//  __\  /   _\/  _ \/ \__/|/ \__/|/  _ \/ \  /|/  _ \/  _ \  / ___\/  _ \/    //__ _"
          "_\/ \  /|/  _ \/  __\/  __/")
    print("|    \| | |||  \/||  \  |  \/|  |  /  | / \|| |\/||| |\/||| / \|| |\ ||| | \|| / \|  |    \| / \||  __\  / "
          "\\| |  ||| / \||  \/||  \  ")
    print("\___ || \_/||  __/|  /_ |    /  |  \__| \_/|| |  ||| |  ||| |-||| | \||| |_/|| \_/|  \___ || \_/|| |     | |"
          "  | |/\||| |-|||    /|  /_ ")
    print("\____/\____/\_/   \____\\\\_/\_\  \____/\____/\_/  \|\_/  \|\_/ \|\_/  \|\____/\____/  \____/\____/\_/     "
          "\_/  \_/  \|\_/ \|\_/\_\\\\____\\")
    print()

    flair()
    print()

    print("Loading...")
    # Sleeps the program to give illusion that it is "Loading".
    time.sleep(5)


# A piece of flair to help with the look of the program output.
def flair():
    print("============================================================================================================"
          "===========================")


# Main method. All functions are called here.
def main():
    startup()
    print("Welcome to Super Commando Encryption Software\n")
    flair()
    print()

    # Check if agent is registered and had valid ID. High quality security measures.
    agent_id = input("Enter Agent ID: ")
    if agent_id == "november papa golf alpha yankee" or agent_id == "sierra delta charlie hotel alpha delta"\
            or agent_id == "test":
        print("\nAuthorized\n")
        print("Welcome Agent.\n")

        flair()
        print()

        # Asks user for decision about weather they want to encrypt or decrypt text.
        choice = input("Encrypt or Decrypt: ")

        while True:
            # Encryption choice
            if choice.upper() == "ENCRYPT" or choice.upper() == "E":
                print()
                phrase = get_to_encryption()
                key = get_key()
                output = encrypt(phrase, key)
                print("\nEncrypted Text: ", output, "\n")
                flair()
                print()
            # Decryption choice
            elif choice.upper() == "DECRYPT" or choice.upper() == "D":
                print()
                phrase = get_from_encryption()
                key = get_key()
                output = decrypt(phrase, key)
                print("\nDecrypted Text: ", output, "\n")
                flair()
                print()
            # If neither encryption or decryption is chosen, defaults to non-valid input and asks again.
            else:
                print()
                print("Not a valid input.")
                print()

            # Asks if user wants to run the program again.
            flair()
            print()
            run = input("Run again (y/n): ")
            print()
            flair()

            if run.lower() == "n":
                print("Signing out...")
                raise SystemExit
            else:
                print()
                choice = input("Encrypt or Decrypt: ")

    # If the Agent ID is not valid, immediately exit program. (In future i also want it to delete the program from the
    # host computer.
    else:
        print("Unauthorized ID. Exiting.")
        raise SystemExit


main()
