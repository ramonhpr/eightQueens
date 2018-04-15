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
