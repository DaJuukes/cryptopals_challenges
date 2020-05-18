import math
from binary_lib import asciitobinary,binarytohex,binarytoascii
from challenge3 import bin_xor

def padKey(str_in, key):
    newstr = ""
    left = math.floor(len(str_in) / len(key))
    for x in range(left):
        newstr+=key
    for x in range(len(str_in) % len(key)):
        newstr+=key[x]
    return newstr

def repeatXorEncrypt(plaintext, key):
    newkey = padKey(plaintext, key)
    binary_key = asciitobinary(newkey)
    binary_text = asciitobinary(plaintext)
    xored = bin_xor(binary_text, binary_key)
    return binarytohex(xored)



print(repeatXorEncrypt("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal", "ICE")) #0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20690a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
