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