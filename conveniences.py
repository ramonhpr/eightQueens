#
# conveniences.py
#

# Converts a portion of a binary string to a decimal.
def binaryStringToDecimal(string, i, length):
    num = 0
    maximum = (i+length)
    while i < maximum:
        num = num << 1
        num += int(string[i])
        i = i + 1
    return num

# Converts a decimal number to its binary correspondent.
def decimalToBinaryString(num=0, expectedLength=3):
    bin = ""
    while (num > 0):
        aux = "0" if (num % 2 == 0) else "1"
        bin = (aux + bin)
        num = (num // 2)
    while(len(bin) < expectedLength):
        bin = ("0" + bin)
    return bin

# This auxiliar function convert a list to a string.
def listToStr(l):
    return ''.join(str(i) for i in l)

# Converts a list of binary strings to decimals.
def binaryToDecimal(l):
	s = listToStr(l)
	arr=[]
	while len(s) > 0:
		tmp = s[ :3]
		s = s[3: ]
		arr.append(int(tmp,2))
	return arr
