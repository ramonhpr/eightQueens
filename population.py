#
# population.py
#
# Can be used for any board size (any number of queens).
#

import math
import random
import conveniences

# Generate a set with binary strings.
def generateRanomBinaryPopulation(individualsCount=100, numberOfQueens=8):
	population = []
	geneSize = int(math.ceil(math.log(numberOfQueens, 2)))
	for i in range(individualsCount):
		values = [random.randint(0, numberOfQueens-1) for _ in range(numberOfQueens)]
		shuffled = random.shuffle(values)
		binaries = [conveniences.decimalToBinaryString(num=x, expectedLength=geneSize) for x in values]
		flat_list = [item for sublist in binaries for item in sublist]
		nums_list = [int(x) for x in flat_list]
		population.append(nums_list)
	return population

# Generate a set with binary strings (unique genes).
def generateRanomBinaryPopulationUniqueGenes(individualsCount=100, numberOfQueens=8):
	population = []
	geneSize = int(math.ceil(math.log(numberOfQueens, 2)))
	for i in range(individualsCount):
		values = [x for x in range(0, numberOfQueens)]
		shuffled = random.shuffle(values)
		binaries = [conveniences.decimalToBinaryString(num=x, expectedLength=geneSize) for x in values]
		flat_list = [item for sublist in binaries for item in sublist]
		nums_list = [int(x) for x in flat_list]
		population.append(nums_list)
	return population
