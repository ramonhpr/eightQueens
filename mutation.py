#
# mutation.py
#

import random
import conveniences

# Mutates a single gene (can lead to repetitive positions).
def mutationRandomGene(individual=[], genesCount=8, mutationProbability=0.4):
	# Check if the mutation should occur.
	mutationProbability *= 100
	mutationChance = random.randint(1, 100)
	if mutationChance > mutationProbability:
		return individual
	# Randomically select a gene index.
	geneIndex = random.randint(0, genesCount-1)
	geneIndex = geneIndex * (len(individual)/genesCount)
	# Randomically modify each bit in the selected gene.
	geneSize = (len(individual)/genesCount)
	for i in range(geneSize):
		individual[geneIndex+i] = random.randint(0, 1)
	return individual

# Swaps two genes.
def mutationSwapTwo(individual=[], genesCount=8, mutationProbability=0.4):
	geneSize = (len(individual)/genesCount)
	# Check if the mutation should occur.
	mutationProbability *= 100
	mutationChance = random.randint(1, 100)
	if mutationChance > mutationProbability:
		return individual
	# Randomically select a gene index.
	geneIndex1 = random.randint(0, genesCount-1)
	geneIndex1 = geneIndex1 * geneSize
	geneIndex2 = geneIndex1
	# Randomically select a different gene position.
	while geneIndex2 == geneIndex1:
		geneIndex2 = random.randint(0, genesCount-1)
		geneIndex2 = geneIndex2 * geneSize
	# Swap genes (we need to swap each bit).
	for i in range(geneSize):
		aux = individual[geneIndex1+i]
		individual[geneIndex1+i] = individual[geneIndex2+i]
		individual[geneIndex2+i] = aux
	return individual

def mutationDisturbance(individual=[], genesCount=8, mutationProbability=0.4):
	individualAux = []
	geneSize = (len(individual)/genesCount)

	# Check if the mutation should occur.
	mutationProbability *= 100
	mutationChance = random.randint(1, 100)
	if mutationChance > mutationProbability:
		return individual

	# Randomically select a gene index.
	geneIndex1 = random.randint(0, genesCount-1)
	geneIndex2 = geneIndex1
	# Randomically select a different gene position.
	while geneIndex2 == geneIndex1:
		geneIndex2 = random.randint(0, genesCount-1)

	geneIndex1 = geneIndex1 * geneSize
	geneIndex2 = geneIndex2 * geneSize

	rangeAux = abs(geneIndex1 - geneIndex2)

	lowerIndex = geneIndex2 if geneIndex1 > geneIndex2 else  geneIndex1

	individualAux = individual[lowerIndex:lowerIndex+rangeAux]
	individualAuxDecimals =  conveniences.binaryToDecimal(individualAux)
	random.shuffle(individualAuxDecimals)
	individualAux = conveniences.decimalToBinary(individualAuxDecimals)

	for i in range(rangeAux):
		individual[lowerIndex+i] = individualAux[i]

	return individual