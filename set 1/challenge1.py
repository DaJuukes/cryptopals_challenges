from binary_lib import hextobinary,binarytob64

def hextob64(hex):
    return binarytob64(hextobinary(hex))

print(hextob64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

