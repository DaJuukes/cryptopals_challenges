import string, math
from binary_lib import dectohex,hextobinary,binarytoascii,dectoascii
from challenge2 import xor, bin_xor

freq = {"E": 12.02, "T": 9.10, "A": 8.12, "O": 7.68, "I": 7.31, "N": 6.95, "S": 6.28, "R": 6.02, "H": 5.92, "D": 4.32, "L": 3.98, "U": 2.88, "C": 2.71,
 "M": 2.61, "F": 2.30, "Y": 2.11, "W": 2.09, "G": 2.03, "P": 1.82, "B": 1.49, "V": 1.11, "K": 0.69, "X": 0.17, "Q": 0.11, "J": 0.10, "Z": 0.07, " ": 10.0, "\\": 0.0}
alphabet = list(string.ascii_uppercase + " " + "\\")


list(string.ascii_lowercase)
def aggregateDiff(strIn): #Precondition: string with only alphabet letters, no punctuation
   # whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
 #   clean_pre = ''.join(filter(whitelist.__contains__, strIn))
    clean = strIn.upper()
    totalDiff = 0.0
    for x in range(len(alphabet)):
        if (clean.count(alphabet[x]) > 0):
            totalDiff += abs((clean.count(alphabet[x]) / len(clean) * 100) - freq[alphabet[x]])
        else:
            totalDiff += freq[alphabet[x]]
    if (totalDiff == 0.0):
        return 1000
    return totalDiff

def crackOneChar(inputStr):
    # check every ASCII char up to 126 starting from 33
    print("Cracking " + inputStr)
    xored = []
    strs = []
    for x in range(127):
        char = dectohex(x)
        charn = hextobinary(char)
        inputstrn = hextobinary(inputStr)
        fullcharn = fullPad(charn, len(inputstrn))
        done = binarytoascii(bin_xor(inputstrn, fullcharn))
        if (done=='err'):
            xored.append({"char": binarytoascii(charn), "val": 1000, "done": done})
        else: 
            xored.append({"char": binarytoascii(charn), "val": aggregateDiff(done), "done": done})
        strs.append(done)
    
    xored.sort(key=lambda x: x['val'])
    return xored[0]
    
    

def fullPad(str_in, length):
    left = math.floor(length / len(str_in))
    newstr = ""
    for x in range(left):
        newstr+=str_in
    for x in range(length % len(str_in)):
        newstr+=str_in[x]
    return newstr

print(crackOneChar("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")) # Cooking MC's like a pound of bacon, key X
#print(binarytoascii("11000010110001001100011"))