import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from util.Individual import Individual
ind = Individual()
print('Test individual genotype methods')
print('Random Gentype',ind.genotype)
print('Get genes from genotype:')
for i in range(1, ind.getGeneNum()):
	print(i,ind.getGene(i))
print('------------')
print('Test Individual set genes')
ind.setGene(1,[0,0,0])
print(ind.getGene(1))
print(ind.genotype)
# TODO: make more unit test for test the function
