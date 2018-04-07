#
# test-population.py
#

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import util.roulette
from util.Population import Population
from util.Individual import Individual

def recombine(ind, stackHead, stackTail):
    newInd = ind
    i = 3
    firstSlice = []
    for j in range(1,3):
        firstSlice.append(ind.getGene(j))
    # The head from the another individual is like a stack
    while len(stackTail) > 0:
        tmp = stackTail.pop(0)
        if not tmp in firstSlice:
            newInd.setGene(i, tmp)
            i+=1
    while len(stackHead) > 0:
        tmp = stackHead.pop(0)
        if not tmp in firstSlice:
            newInd.setGene(i, tmp)
            i+=1
    return newInd

def cutAndCross(ind1, ind2):
    # fix the first 2 genes
    firstSlice1 = []
    firstSlice2 = []
    lastSlice1 = []
    lastSlice2 = []
    for i in range(1,3):
        firstSlice1.append(ind1.getGene(i))
        firstSlice2.append(ind2.getGene(i))
    for i in range(3,int(ind1.getGeneNum())+1):
        lastSlice1.append(ind1.getGene(i))
        lastSlice2.append(ind2.getGene(i))
    newInd1 = recombine(ind1,firstSlice2,lastSlice2)
    newInd2 = recombine(ind2,firstSlice1,lastSlice1)
    return (newInd1,newInd2)

pop = Population(15)
print('- Test crossover function')
for ind1,ind2 in pop.parentsSelectionFunction():
    print('Parents selected')
    print(ind1.getGenotypeDecimal())
    print(ind2.getGenotypeDecimal())
    print('New Individuals')
    i,j = pop.crossover(ind1, ind2)
    print(i.getGenotypeDecimal())
    print(j.getGenotypeDecimal())
    print('------')


print('- Test local crossover function')
pop.setCrossoverFunct(cutAndCross)
for ind1,ind2 in pop.parentsSelectionFunction():
    print('Parents selected')
    print(ind1.getGenotypeDecimal())
    print(ind2.getGenotypeDecimal())
    print('New Individuals')
    i,j = pop.crossover(ind1, ind2)
    print(i.getGenotypeDecimal())
    print(j.getGenotypeDecimal())
    print('------')

# Test roulette wheel selection.
print("\n- Test Roulette Wheel Selection \n")
parents = util.roulette.parents(pop.individuals)
# Breed individuals selected through the roulette wheel.
for ind1, ind2 in parents:
    print("Parents selected:")
    print(ind1.getGenotypeDecimal())
    print(ind2.getGenotypeDecimal())
    print("New Individuals:")
    i, j = pop.crossover(ind1, ind2)
    print(i.getGenotypeDecimal())
    print(j.getGenotypeDecimal())
    print("")


