#
# conveniences.py
#
import os
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

def decimalToBinary(l, expectedLength=3):
    s = listToStr(l)
    arr=[]
    while len(s) > 0:
        arrAux=[]
        tmp = int(s[0])
        s = s[1: ]
        while (tmp > 0):
            aux = 0 if (tmp % 2 == 0) else 1
            arrAux.insert(0,aux)
            tmp = (tmp // 2)
        while(len(arrAux) < expectedLength):
            arrAux.insert(0,0)
        arr = arr + arrAux
    return arr
# Write a data in the file especified
def writeToFile(file, data):
	with open(file,'a') as fd:
		fd.write(str(data))
		fd.write('\n')

def createFolder(name):
	try:
		os.mkdir(name)
	except:
		pass

# Remove files used to plot graphs
def removeOutFiles():
	files = [
			'iterations.out',
			'convergency.out',
			'fitness.out',
            'dumbImplementation/average.png',
            'dumbImplementation/deviation.png',
            'naiveImplementation/average.png',
            'naiveImplementation/deviation.png',
            'smartImplementation/average.png',
            'smartImplementation/deviation.png',
			]
	for file in files:
		try:
			os.remove(file)
		except:
			pass
