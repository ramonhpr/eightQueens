#
# Population.py
#

from util.Individual import Individual
import random

class Population:

	def __init__(self, num_individuals=100, numGenes=24, geneLen=3, parentsSelectionFunction=None, crossOverFunction=None):
		"""
		Initialize a population with num_individuals binary
		string individuals,the default genes number is 24
		and the default binary string (gene) length is 3
		"""
		self.individuals = []
		self.epoch = 0
		self.parentsSelectionFunction = self.__defaultParentsSelectionFunction if not parentsSelectionFunction else parentsSelectionFunction
		self.crossoverFunction = self.__defaultCrossoverFunction if not crossOverFunction else crossOverFunction

		for i in range(0, num_individuals):
			individual = Individual(numGenes, geneLen)
			self.individuals.append(individual)

	def setFitnessFunc(self, fitnessFunc):
		"""
		Set for all individuals in the population the fitness function passed
		If the population is "running" it raise an exception
		"""
		if self.epoch > 0:
			raise Exception('You cannot pass a function when the population is running')
		else:
			for ind in self.individuals:
				ind.setFitnessFunc(fitnessFunc)

	def setCrossoverFunct(self, func):
		"""
		Set the crossover function passed, for the user
		choice which crossover function use
		"""
		self.crossoverFunction = func

	def crossover(self, *args, **kwargs):
		return self.crossoverFunction(*args, **kwargs)

	def setParentsSelectionFunct(self, func):
		"""
		Set the parents selection function passed, so the user
		can choose which function to use.
		"""
		self.parentsSelectionFunction = func

	def parentsSelection(self, *args, **kwargs):
		"""
		"""
		return self.parentsSelectionFunction(*args, **kwargs)

	def __recombine(self, ind, stackHead, stackTail):
		"""
		This is just an auxliar function to the default crossover function
		"""
		newInd = ind
		i = 4
		firstSlice = []
		for j in range(1,4):
			firstSlice.append(ind.getGene(j))
		# Pop from the 
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
	def __defaultCrossoverFunction(self, ind1, ind2):
		"""
		This function cut the 3 first genes and recombine the other ones
		with parents to generate new children
		"""
		firstSlice1 = []
		firstSlice2 = []
		lastSlice1 = []
		lastSlice2 = []
		for i in range(1,4):
			firstSlice1.append(ind1.getGene(i))
			firstSlice2.append(ind2.getGene(i))
		for i in range(4,int(ind1.getGeneNum())+1):
			lastSlice1.append(ind1.getGene(i))
			lastSlice2.append(ind2.getGene(i))
		newInd1 = self.__recombine(ind1,firstSlice2,lastSlice2)
		newInd2 = self.__recombine(ind2,firstSlice1,lastSlice1)
		return (newInd1,newInd2)

	def __defaultParentsSelectionFunction(self):
		# The default parents selection method is based on picking
		# five individuals randomically and then selecting the two
		# most qualified (higher fitness) to breed. This method will
		# return a list containing lists of two individuals.
		couples = []
		indvs = list(self.individuals)
		# Distribute individuals and place the top two together.
		while len(indvs) > 0:
			candidates = []
			for i in range(5):
				ind = random.choice(indvs)
				candidates.append(ind)
				indvs.remove(ind)
			candidates.sort(key=lambda x: x.fitness(), reverse=True)
			couples.append([candidates[0], candidates[1]])
		return couples

	def __survivalSelection(self):
		pass
