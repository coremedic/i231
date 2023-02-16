## i231 Single DES in python ##
import binascii
from itertools import permutations

def permutation(data, table, bits):
    """
    permutation function
    takes in data to permute, permatation table
    and bits (should be 64, 56, 48, 28, or 24)
    returns permuted data 
    """
    p = ""
    for bit in range(0, bits):
        p = p + data[table[bit] - 1]
    
    return p

def shifts(data, shifts):
    """
    takes in data and amount of shifts
    shifts n number of times to the left
    """
    shifted_data = data << shifts
    return shifted_data

def xor(x, y):
    """
    takes in x and y
    xors x and y
    returns xored data
    """
    xored = x ^ y
    return xored


# Initial permutation 
initial_permutation_table = (
                [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
)

expansion_table = (
    []
)

def main():
    plaintext = input("Enter plaintext: ")
    plaintext_hex = plaintext.encode("utf-8").hex()
    print(f"Plaintext in base16: {plaintext_hex}")

    # appends 0's to make the text 64bit
    plaintext_bin = str(format(int(plaintext_hex, 16), "064b"))
    print(f"Plaintext in base2: {plaintext_bin}")
    plaintext_permuted = permutation(plaintext_bin, initial_permutation_table, 64)
    print(f"Plaintext after inital permutation: {plaintext_permuted}")

    # split step
    left_pt = plaintext_permuted[0:32]
    right_pt = plaintext_permuted[32:64]


if __name__ == "__main__":
    main()