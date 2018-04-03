#
# conveniences.py
#

def binaryToDecimal(string, i, length):
    num = 0
    maximum = (i+length)
    while i < maximum:
        num = num << 1
        num += int(string[i])
        i = i + 1
    return num