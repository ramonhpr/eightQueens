#
# fitness.py
#

def binaryToDecimal(string, i, length):
    num = 0
    maximum = (i+length)
    while i < maximum:
        num = num << 1
        num += int(string[i])
        i = i + 1
    return num 

def sumall(individual):
    f = 0
    # The fitness is equal to the number of queens that don't 
    # interfere in anothers position (base queen).
    for j in range(8):
        baseQueenRow = binaryToDecimal(individual.genotype, (j*3), 3)
        # Look for queens on the same row or diagonal.
        for jx in range(8):
            endQueenRow = binaryToDecimal(individual.genotype, (jx*3), 3)
            sameRow = (baseQueenRow == endQueenRow)
            onDiagonal = (abs(baseQueenRow-endQueenRow) == abs(j-jx))
            f += int(sameRow == 0 and onDiagonal == 0 and (jx != j))
    return f