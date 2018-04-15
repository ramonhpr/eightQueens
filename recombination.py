#
# recombination.py
#

import random

# Default crossover, cut and crossfill method.
def crossoverCutAndCrossFill(couples=[], genesCount=8, recombinationProbability=0.9):
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
