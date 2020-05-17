from binary_lib import hextobinary,binarytohex

def xor(one, two):
    if one==two:
        return '0'
    else:
        return '1'

# precondition : orig, target have the same length, are in hexadecimal form
def hex_xor(orig, target):
    orig_b = hextobinary(orig)
    target_b = hextobinary(target)
    final_b = ""
    for x in range(len(orig_b)):
        final_b += xor(orig_b[x], target_b[x])
    return binarytohex(final_b)

print(hex_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")) # 746865206b696420646f6e277420706c6179