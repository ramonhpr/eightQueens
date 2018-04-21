#
# fitness.py
#

import conveniences

# Returns the maximum fitness calculated by the fitnessNaive() method.
def fitnessNaiveMaxFitness():
	return 8

# The fitness is equal to the number of queens in valid spots.
# Loop through each queen position (row assignment).
def fitnessNaive(individualBinaryString):
	f = 0
	for j in range(8):
		collisions = 0
		baseQueenRow = conveniences.binaryStringToDecimal(individualBinaryString, (j*3), 3)
		# Look for queens on the same row or diagonal.
		for jx in range(8):
			endQueenRow = conveniences.binaryStringToDecimal(individualBinaryString, (jx*3), 3);
			sameRow = (baseQueenRow == endQueenRow);
			onDiagonal = (abs(baseQueenRow-endQueenRow) == abs(j-jx));
			collisions += ((sameRow == 1 or onDiagonal == 1) and (jx != j));
		f += (collisions == 0);
	return f

# Returns the maximum fitness calculated by the fitnessSumAll() method.
def fitnessSumAllMaxFitness():
	return 56

# The fitness is equal to the number of queens that don't
# interfere in anothers position (the base queen).
def fitnessSumAll(individualBinaryString):
    f = 0
    for j in range(8):
        baseQueenRow = conveniences.binaryStringToDecimal(individualBinaryString, (j*3), 3)
        # Look for queens on the same row or diagonal.
        for jx in range(8):
            endQueenRow = conveniences.binaryStringToDecimal(individualBinaryString, (jx*3), 3)
            sameRow = (baseQueenRow == endQueenRow)
            onDiagonal = (abs(baseQueenRow-endQueenRow) == abs(j-jx))
            f += int(sameRow == 0 and onDiagonal == 0 and (jx != j))
    return f
