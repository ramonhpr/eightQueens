#
# recombination.py
#
# Can be used for any board size (any number of queens).
# Possible exception is the function crossoverOrderOne().
#

import math
import random
import conveniences

# Default crossover, cut and crossfill method.
def crossoverCutAndCrossFill(nQueens=8, couples=[], recombinationProbability=0.9):
	childs = []
	recombinationProbability *= 100
	# Calculate the number of genes in an individual based on the number of queens.
	geneLength = int(math.ceil(math.log(nQueens, 2)))
	genesCount = nQueens
	# Loop through the couples and breed the luck ones (inside the recombination margin).
	for couple in couples:
		breedChance = random.randint(1, 100)
		if breedChance < recombinationProbability:
			# This couple was selected, apply the Cut and Crossfill recombination.
			parent1 = []
			parent2 = []
			# Transform the binary genes to decimals (easier to compare).
			for i in range(genesCount):
				parent1.append(conveniences.binaryStringToDecimal(couple[0], (i*geneLength), geneLength))
				parent2.append(conveniences.binaryStringToDecimal(couple[1], (i*geneLength), geneLength))
			# Randomically select a gene.
			cutIndex = random.randint(1, genesCount-2)
			# Childs (cut parents).
			child1 = parent1[:cutIndex]
			child2 = parent2[:cutIndex]
			# Crossfill.
			index1 = 0
			index2 = 0
			while(index1 < genesCount and index2 < genesCount):
				if parent1[index1] not in child2:
					child2.append(parent1[index1])
				if parent2[index2] not in child1:
					child1.append(parent2[index2])
				index1 += 1
				index2 += 1
			# Transform childs genes to their binary representation.
			child1 = [conveniences.decimalToBinaryString(num=x, expectedLength=geneLength) for x in child1]
			child1 = [item for sublist in child1 for item in sublist]
			child1 = [int(x) for x in child1]
			child2 = [conveniences.decimalToBinaryString(num=x, expectedLength=geneLength) for x in child2]
			child2 = [item for sublist in child2 for item in sublist]
			child2 = [int(x) for x in child2]
			# Append childs.
			childs.append(child1)
			childs.append(child2)
	return childs

# Cut and crossfill method simplified (doesn't check for duplicates).
def crossoverCutAndCrossFillSimplified(nQueens=8, couples=[], recombinationProbability=0.9):
	childs = []
	recombinationProbability *= 100
	# Calculate the number of genes in an individual based on the number of queens.
	geneLength = int(math.ceil(math.log(nQueens, 2)))
	genesCount = nQueens
	# Loop through the couples and breed the luck ones (inside the recombination margin).
	for couple in couples:
		breedChance = random.randint(1, 100)
		if breedChance < recombinationProbability:
			# Randomically select a gene and calculate its index.
			cutIndex = random.randint(1, genesCount-2)
			cutIndex = cutIndex * (len(couple[0])/genesCount)
			# Slices.
			aFirstSlice = couple[0][:cutIndex]
			aSecondSlice = couple[0][cutIndex:]
			bFirstSlice = couple[1][:cutIndex]
			bSecondSlice = couple[1][cutIndex:]
			# Compose childs
			childA = aFirstSlice + bSecondSlice
			childB = bFirstSlice + aSecondSlice
			# Append childs.
			childs.append(childA)
			childs.append(childB)
	return childs

# ... (NOT SURE IF THIS METHOD CAN BE USED FOR ANY BOARD SIZE, AS IT IS)
def crossoverOrderOne(nQueens=8, couples=[], recombinationProbability=0.9):
	childs = []
	recombinationProbability *= 100
	# Calculate the number of genes in an individual based on the number of queens.
	geneLength = int(math.ceil(math.log(nQueens, 2)))
	genesCount = nQueens
	# Loop through the couples and breed the luck ones (inside the recombination margin).
	for couple in couples:
		breedChance = random.randint(1, 100)
		if breedChance < recombinationProbability:
			# This couple was selected, apply the Order One Crossover recombination.
			j = 0
			k = 0
			parent1 = []
			parent2 = []
			subListLength = random.randint(3, 4)
			# ...
			if subListLength == 3:
				n = random.randint(0, 4)
			else:
				n = random.randint(0, 3)
			# Transform the binary genes to decimals (easier to compare).
			for i in range(genesCount):
				parent1.append(conveniences.binaryStringToDecimal(couple[0], (i*geneLength), geneLength))
				parent2.append(conveniences.binaryStringToDecimal(couple[1], (i*geneLength), geneLength))
			# Childs (cut parents).
			child1 = parent1[n:n+subListLength]
			child2 = parent2[n:n+subListLength]
			# ...
			for i in range(genesCount):
				indexAux = (n + subListLength + i) % 8
				index1 = (n + subListLength + j) % 8
				index2 = (n + subListLength + k) % 8
				if parent2[indexAux] not in child1:
					child1.insert(index1, parent2[indexAux])
					j += 1
				if parent1[indexAux] not in child2:
					child2.insert(index2, parent1[indexAux])
					k += 1
			# Transform childs genes to their binary representation.
			child1 = [conveniences.decimalToBinaryString(num=x, expectedLength=geneLength) for x in child1]
			child1 = [item for sublist in child1 for item in sublist]
			child1 = [int(x) for x in child1]
			child2 = [conveniences.decimalToBinaryString(num=x, expectedLength=geneLength) for x in child2]
			child2 = [item for sublist in child2 for item in sublist]
			child2 = [int(x) for x in child2]
			# Append childs.
			childs.append(child1)
			childs.append(child2)
	return childs
