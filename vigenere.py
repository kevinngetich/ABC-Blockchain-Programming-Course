# Author: Kevin Ng'etich
# Title: Vigenere Cipher implementation for ABC blockchain programming course task

alphabet = "abcdefghijklmnopqrstuvwxyz"

# get the key and message to encrypt from the user
key = input("Enter the key you wish to use to encrypt your message: ")
message = input("Enter the message you wish to encrypt: ")

cipher = ""
counter = 0

# generete ciphertext using vigenere cipher
for index in range(len(message)):
    if not message[index].isalpha():
        cipher += message[index]
        continue
    
    replace = alphabet[(alphabet.index(message[index]) + alphabet.index(key[counter % len(key)])) % len(alphabet)]
    cipher += replace
    counter += 1

# print output to screen
print("The encrypted message is: ", cipher)
