#
# mutation.py
#

import random

# Mutates a single gene (can lead to repetitive positions).
def mutationRandomizeGene(individual=[], genesCount=8, mutationProbability=0.4):
	# Check if the mutation should occur.
	mutationProbability *= 100
	mutationChance = random.randint(1, 100)
	if mutationChance < mutationProbability:
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
	# Check if the mutation should occur.
	mutationProbability *= 100
	mutationChance = random.randint(1, 100)
	if mutationChance < mutationProbability:
		return individual
	# Randomically select a gene index.
	geneIndex1 = random.randint(0, genesCount-1)
	geneIndex1 = geneIndex1 * (len(individual)/genesCount)
	geneIndex2 = geneIndex1
	# Randomically select a different gene position.
	while geneIndex2 == geneIndex1:
		geneIndex2 = random.randint(0, genesCount-1)
		geneIndex2 = geneIndex2 * (len(individual)/genesCount)
	# Swap genes (we need to swap each bit).
	geneSize = (len(individual)/genesCount)
	for i in range(geneSize):
		aux = individual[geneIndex1+i]
		individual[geneIndex1+i] = individual[geneIndex2+i]
		individual[geneIndex2+i] = aux
	return individual
