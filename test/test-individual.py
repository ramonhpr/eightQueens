import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from util.Individual import Individual
from random import randint
ind = Individual()
print('Test Individual genotype methods')
print('Random Gentype',ind.genotype)
print('Get genes from genotype:')
for i in range(0, ind.getGeneNum()):
	print(i+1,ind.getGene(i+1))

print('------------')
print('Test Individual set genes')
ind.setGene(1,[0,1,0])
print(ind.getGene(1))
print(ind.genotype)

print('------------')
print('Test Individual set fitness function')
def simpleTest(error):
	return error/100
def testNarguments(error1, error2, error3):
	return max(error1,error2,error3)/(error1+error2+error3)
ind.setFitnessFunc(simpleTest)
print('Fitness with one argument',ind.fitness(randint(0,10)))
ind.setFitnessFunc(testNarguments)
print('Fitness with more arguments',ind.fitness(randint(0,10),randint(0,10),randint(0,10)))

print('------------')
print('Test Individual set mutation function')
ind.mutation()
print(ind.genotype)