from challenge3 import crackOneChar

f = open('data.txt', 'r')
strings = f.read().split('\n')

vals = []

for x in strings:
    val = crackOneChar(x)
    val['original'] = x
    vals.append(val)

vals.sort(key=lambda x: x['val'])
print(vals[0]) # "Now that the party is jumping", key=5, original 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f