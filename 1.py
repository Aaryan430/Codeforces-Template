# Importing the libraries.
from sympy.matrices.expressions.transpose import Transpose
import numpy as np
from sympy import Matrix
import time

# Alphabet set
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


# Function to encrypt the text.
def encrypt(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]
    

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]
      
        numbers = np.dot(K, P) % 26
        n = numbers.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted

# Function to decrypt the text.
def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]


    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % 26
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted


# Function for doing the Plain Text attack
def PlainTextAttack(message,cipher,m):

    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [
        message_in_numbers[i : i + m]
        for i in range(0, len(message_in_numbers), int(m))
    ]
        
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + m]
        for i in range(0, len(cipher_in_numbers), m)
    ]
    Pmat=Matrix(split_P)
    Cmat=Matrix(split_C)

    Pinv= Pmat.inv_mod(26)
    Key=(Pinv*Cmat)%26
    Key=Key.T
    return Key


# Driver code starts from here.
def main():
    # Initailising the start time.
    start_time = time.time()

    # Message to encrypt
    message = "ATTACKIST"

    # key matrix
    K=Matrix([[3,10,20],[20,9,17],[9,4,17]])

    # printing the key
    print(K)


    # finding the inverse of the key matrix
    Kinv=K.inv_mod(26)

    # st
    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)


    print("Original message: " + message)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + decrypted_message)
    print(PlainTextAttack(message,encrypted_message,3))
    print("--- %s seconds ---" % (time.time() - start_time))


main() 