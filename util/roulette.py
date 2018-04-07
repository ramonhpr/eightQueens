#
# roulette.py
#

import random

def roulette(population, sum):
    i = 0
    q = 0
    w = random.randint(1, sum)
    # Find the individual associated to the randomized range.
    while i < len(population):
        u = (population[i].fitness() + q + 1)
        if w > q and w <= u:
            w = i
            i = len(population)
        q = u
        i += 1
    return population[w]

def parents(population, parentsPerFamily=2, repeatParents=0):
    p = []
    sum = 0
    # We make a copy of the original population in order to 
    # simplify the selection of unrepeated random individuals,
    # it is basically a implementation convenience.
    population = list(population)
    # The roulette wheel selection model gives each individual
    # a chance of being selected that is proportional to its
    # fitness. We randomize a number between 1 and the sum of
    # every individual fitness in order to grant proportional
    # changes. Then, select the individual associated to the
    # random fitness range.
    for individual in population:
        sum += (individual.fitness() + 1)
    # Distribute individuals among families.
    while len(population) > 1:
        f = []
        for i in range(parentsPerFamily):
            k = roulette(population, sum)
            sum -= (k.fitness() + 1)
            f.append(k)
            if repeatParents == 0:
                population.remove(k)
        p.append(f)
    return p