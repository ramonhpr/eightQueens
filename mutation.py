#
# mutation.py
#

import random

# ...
def mutationSimple(individual=[], genesCount=8, mutationProbability=0.4):

	mutationProbability *= 100
	mutationChance = random.randint(1, 100)
	if mutationChance < mutationProbability:
		return individual

	geneIndex = random.randint(0, genesCount-1)
	geneIndex = geneIndex * (len(individual)/genesCount)

	geneSize = (len(individual)/genesCount)

	for i in range(geneSize):

		individual[geneIndex+i] = random.randint(0, 1)

	return individual
