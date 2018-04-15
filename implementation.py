#
# implementation.py
#

import fitness
import parents
import mutation
import population
import conveniences
import recombination

# ...
def naiveImplementation(maximumFitnessEvaluations=10000):

	# Generate the initial population.
	p = population.generateRanomBinaryPopulation(individualsCount=100, individualsLength=24)

	# Compute individuals fitnesses.
	f = [fitness.fitnessNaive(x) for x in p]

	while (f[0] != 8):

		# Select couples to breed.
		c = parents.selectParentsBestTwoOutOfFive(population=p, fitnesses=f)

		# Recombine couples (breed).
		n = recombination.crossoverCutAndCrossFill(c, genesCount=8, recombinationProbability=0.9)

		# Calculate childs fitnesses.
		k = [fitness.fitnessNaive(x) for x in n]

		# Merge childs with their parents and, also, their fitnesses.
		p = p + n
		f = f + k

		# Sort individuals by their fitnesses.
		z = zip(p, f)
		z.sort(key=lambda x: x[1], reverse=True)
		p, f = zip(*z)

		# Remove worst individuals from population.
		p = list(p[:100])
		f = list(f[:100])

		# Mutate.
		for i in range(len(p)):

			p[i] = mutation.mutationSimple(individual=p[i], genesCount=8, mutationProbability=0.4)
			f[i] = fitness.fitnessNaive(p[i])

	print("Found solution:")
	print("Individual: " + str(conveniences.binaryToDecimal(p[0])))
	print("Fitness: " + str(f[0]))
