import math,re

hexdigit = "0123456789abcdef"
hex_bin = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
bin_b64 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
#bin_ascii = ["!", "\"", "#", "$", "%", "&", "\'","(",")","*","+","\'","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";",
#"<","=",">","?","@","A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[",
#"\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "{", "|", "}", "~"] 

def hextodec(hex):
    # Convert using base 16 system: FF = 16^1 * 15 + 16^0 * 15
    strlen = len(hex)
    dec = 0
    for x in range(strlen):
        dec += (16**(strlen - 1 - x) * (hexdigit.index(hex[x])))
    return dec

def dectohex(dec):
    r = dec % 16
    if (dec-r == 0):
        return hexdigit[int(r)]
    return dectohex((dec-r)/16) + hexdigit[int(r)]

def hextobinary(hex):
    strlen = len(hex)
    binar = ""
    for x in range(strlen):
        binar += hex_bin[hexdigit.index(hex[x])]
    return binar

def binarytoascii(binary_i):
    binary_int = int(binary_i, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = ""
    try:
        ascii_text = binary_array.decode()
    except: 
        return "err"
    r = re.sub("\\x00", "",ascii_text)
    return r

def dectoascii(dec):
    b = hextobinary(dectohex(dec))
    binary_int = int(b, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = ""
    try:
        ascii_text = binary_array.decode()
    except: 
        return "err"
    r = re.sub("\\x00", "",ascii_text)
    return r

def binarytohex(binary):
    arr = []
    hex = ""
    if (len(binary) % 4 > 0):
        binary = binary.rjust(len(binary) + ( 4- (len(binary) % 4)), '0')
    for x in range(math.floor(len(binary) / 4)):
        newstr = ""
        if x==0:
            newstr = binary[0:4]
        else: 
            newstr = binary[(x * 4): ((x+1) * 4)]
        arr.append(newstr)
    for x in range(len(arr)):
        hex+=hexdigit[hex_bin.index(arr[x])]
    return hex

def binarytob64(binary):
    # Convert using sextext system
    arr = []
    strd = ""
    for x in range(math.floor(len(binary) / 6)):
        newstr = ""
        if x==0:
            newstr = binary[0:6]
        else: 
            newstr = binary[(x * 6): ((x+1) * 6)]
        arr.append(newstr)
    if ((len(binary) % 6) > 0):
        # Leftover binary needs to padded with zeros
        prefill = binary[6  * math.floor(len(binary) / 6): len(binary)]
        filled = prefill.ljust(6, '0')
        arr.append(filled)
    if (len(arr) % 4) > 0:
        #need to fill to have blocks of 4
        if len(arr) < 4:
            for x in range(4 - len(arr)):
                arr.append('filler')
        else:
            mod = (len(arr) % 4)
            for x in range(4 - mod):
                arr.append('filler')
    for x in range(len(arr)):
        if (arr[x] == 'filler'):
            strd += '='
        else:
            strd += bin_b64[hextodec(binarytohex(arr[x]))]
    return strd
    