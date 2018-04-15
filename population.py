#
# population.py
#

import random

# Generate a set with binary strings.
def generateRanomBinaryPopulation(individualsCount=100, individualsLength=24):
	population = []
	for i in range(individualsCount):
		population.append([random.randint(0, 1) for _ in range(individualsLength)])
	return population
