#
# parents.py
#

import random
import fitness

# ...
def selectParentsBestTwoOutOfFive(population=[], fitnesses=[]):
	# The default parents selection method is based on picking
	# five individuals randomically and then selecting the two
	# most qualified (higher fitness) to breed. This method will
	# return a list containing lists of two individuals.
	couples = []
	indvs = list(population)
	# Distribute individuals and place the top two together.
	while len(indvs) > 0:
		candidates = []
		for i in range(5):
			ind = random.choice(indvs)
			candidates.append(ind)
			indvs.remove(ind)
		candidates.sort(key=lambda x: fitnesses[population.index(x)], reverse=True)
		couples.append([candidates[0], candidates[1]])
	return couples

# ...
def roulette(population, fitnesses, sum):
    i = 0
    q = 0
    w = random.randint(1, sum)
    # Find the individual associated to the randomized range.
    while i < len(population):
        u = (fitnesses[i] + q + 1)
        if w > q and w <= u:
            w = i
            i = len(population)
        q = u
        i += 1
    return w

# ...
def selectParentsRoulette(population=[], fitnesses=[]):
    p = []
    sum = 0
    # We make a copy of the original population in order to
    # simplify the selection of unrepeated random individuals,
    # it is basically a implementation convenience.
    population = list(population)
    fitnesses = list(fitnesses)
    # The roulette wheel selection model gives each individual
    # a chance of being selected that is proportional to its
    # fitness. We randomize a number between 1 and the sum of
    # every individual fitness in order to grant proportional
    # changes. Then, select the individual associated to the
    # random fitness range.
    for fitness in fitnesses:
        sum += (fitness + 1)
    # Distribute individuals among families.
    while len(population) > 1:
        f = []
        for i in range(2):
            index = roulette(population, fitnesses, sum)
            sum -= (fitnesses[index] + 1)
            f.append(population[index])
            population.pop(index)
            fitnesses.pop(index)
        p.append(f)
    return p
