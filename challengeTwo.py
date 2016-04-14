import string


__author__ = 'root'

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
input = input.lower()

key = 'abcdefghijklmnopqrstuvwxyz'

output = ''

for c in input:
    if c.isalpha():
        charValue = (key.index(c) + 2) % 26
        output += key[charValue]
    else:
        output += c

print(output)



url = "http://www.pythonchallenge.com/pc/def/map.html"

translateAlphabet = "cdefghijklmnopqrstuvwxyzab"

translateTab = str.maketrans(key, translateAlphabet)
print(url.translate(translateTab))


