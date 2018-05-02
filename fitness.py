#
# fitness.py
#
# Can be used for any board size (any number of queens).
#

import math
import conveniences

# Returns the maximum fitness calculated by the fitnessNaive() method.
def fitnessNaiveMaxFitness(nQueens=8):
	return nQueens

# The fitness is equal to the number of queens in valid spots.
# Loop through each queen position (row assignment).
def fitnessNaive(individualBinaryString, nQueens=8):
	f = 0
	geneLength = int(math.ceil(math.log(nQueens, 2)))
	for j in range(nQueens):
		collisions = 0
		baseQueenRow = conveniences.binaryStringToDecimal(individualBinaryString, (j*geneLength), geneLength)
		# Look for queens on the same row or diagonal.
		for jx in range(nQueens):
			endQueenRow = conveniences.binaryStringToDecimal(individualBinaryString, (jx*geneLength), geneLength);
			sameRow = (baseQueenRow == endQueenRow);
			onDiagonal = (abs(baseQueenRow-endQueenRow) == abs(j-jx));
			collisions += ((sameRow == 1 or onDiagonal == 1) and (jx != j));
		f += (collisions == 0);
	return f

# Returns the maximum fitness calculated by the fitnessSumAll() method.
def fitnessSumAllMaxFitness(nQueens=8):
	return nQueens*(nQueens-1)

# The fitness is equal to the number of queens that don't
# interfere in anothers position (the base queen).
def fitnessSumAll(individualBinaryString, nQueens=8):
	f = 0
	geneLength = int(math.ceil(math.log(nQueens, 2)))
	for j in range(nQueens):
		baseQueenRow = conveniences.binaryStringToDecimal(individualBinaryString, (j*geneLength), geneLength)
		# Look for queens on the same row or diagonal.
		for jx in range(nQueens):
			endQueenRow = conveniences.binaryStringToDecimal(individualBinaryString, (jx*geneLength), geneLength)
			sameRow = (baseQueenRow == endQueenRow)
			onDiagonal = (abs(baseQueenRow-endQueenRow) == abs(j-jx))
			f += int(sameRow == 0 and onDiagonal == 0 and (jx != j))
	return f
