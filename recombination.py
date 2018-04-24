#
# recombination.py
#

import random
import conveniences

# Default crossover, cut and crossfill method.
def crossoverCutAndCrossFill(couples=[], genesCount=8, recombinationProbability=0.9):
	childs = []
	recombinationProbability *= 100
	for couple in couples:
		breedChance = random.randint(1, 100)
		if breedChance < recombinationProbability:
			parent1 = []
			parent2 = []
			geneSize = (len(couple[0]) // genesCount)
			# Transform binaries (genes) to decimals.
			for i in range(genesCount):
				parent1.append(conveniences.binaryStringToDecimal(couple[0], (i*geneSize), geneSize))
				parent2.append(conveniences.binaryStringToDecimal(couple[1], (i*geneSize), geneSize))
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
			child1 = [conveniences.decimalToBinaryString(num=x, expectedLength=3) for x in child1]
			child1 = [item for sublist in child1 for item in sublist]
			child1 = [int(x) for x in child1]
			child2 = [conveniences.decimalToBinaryString(num=x, expectedLength=3) for x in child2]
			child2 = [item for sublist in child2 for item in sublist]
			child2 = [int(x) for x in child2]
			# Append childs.
			childs.append(child1)
			childs.append(child2)
	return childs

# Cut and crossfill method simplified (doesn't check for duplicates).
def crossoverCutAndCrossFillSimplified(couples=[], genesCount=8, recombinationProbability=0.9):
	childs = []
	recombinationProbability *= 100
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

def crossoverOrderOne(couples=[], genesCount=8, recombinationProbability=0.9):
	childs = []
	recombinationProbability *= 100
	for couple in couples:
		breedChance = random.randint(1, 100)
		if breedChance < recombinationProbability:
			parent1 = []
			parent2 = []
			j = 0
			k = 0
			geneSize = (len(couple[0]) // genesCount)
			subListLength = random.randint(3,4)
			if subListLength == 3:
				n = random.randint(0,4)
			else:
				n = random.randint(0,3)

			for i in range(genesCount):
				parent1.append(conveniences.binaryStringToDecimal(couple[0], (i*geneSize), geneSize))
				parent2.append(conveniences.binaryStringToDecimal(couple[1], (i*geneSize), geneSize))

			child1 = parent1[n:n+subListLength]
			child2 = parent2[n:n+subListLength]

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

			child1 = [conveniences.decimalToBinaryString(num=x, expectedLength=3) for x in child1]
			child1 = [item for sublist in child1 for item in sublist]
			child1 = [int(x) for x in child1]
			child2 = [conveniences.decimalToBinaryString(num=x, expectedLength=3) for x in child2]
			child2 = [item for sublist in child2 for item in sublist]
			child2 = [int(x) for x in child2]

			childs.append(child1)
			childs.append(child2)

	return childs