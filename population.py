#
# population.py
#

import random
import conveniences

# Generate a set with binary strings.
def generateRanomBinaryPopulation(individualsCount=100, individualsLength=24):
	population = []
	for i in range(individualsCount):
		population.append([random.randint(0, 1) for _ in range(individualsLength)])
	return population

# Generate a set with binary strings (unique genes).
def generateRanomBinaryPopulationUniqueGenes(individualsCount=100):
	population = []
	for i in range(individualsCount):
		values = [0, 1, 2, 3, 4, 5, 6, 7]
		shuffled = random.shuffle(values)
		binaries = [conveniences.decimalToBinaryString(num=x, expectedLength=3) for x in values]
		flat_list = [item for sublist in binaries for item in sublist]
		nums_list = [int(x) for x in flat_list]
		population.append(nums_list)
	return population
