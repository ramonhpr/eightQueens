#
# Population.py
#

from util.Individual import Individual
import util.config as config
import random
from operator import methodcaller

class Population:

	def __init__(self, num_individuals=100, numGenes=24, geneLen=3,
				parentsSelectionFunction=None, crossOverFunction=None, survivalSelectFunction=None):
		"""
		Initialize a population with num_individuals binary
		string individuals,the default genes number is 24
		and the default binary string (gene) length is 3
		"""
		self.individuals = []
		self.epoch = 0
		self.parentsSelectionFunction = self.__defaultParentsSelectionFunction if not parentsSelectionFunction else parentsSelectionFunction
		self.crossoverFunction = self.__defaultCrossoverFunction if not crossOverFunction else crossOverFunction
		self.survivalSelectFunction = self.__defaultSurvivalSelectFunction if not survivalSelectFunction else survivalSelectFunction

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

	def mutate(self):
		for ind in self.individuals:
			ind.mutation()

	def parentsSelection(self, *args, **kwargs):
		"""
		"""
		return self.parentsSelectionFunction(*args, **kwargs)

	def setSurvivalFunction(self, func):
		"""
		Set the survival slection function passed, for the user
		choice which crossover function use
		"""
		self.survivalSelectFunction = func

	def survivalSelect(self, *args, **kwargs):
		return self.survivalSelectFunction(*args, **kwargs)

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
		You will have to verify if the children is None
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

		newInd1 = ind1
		newInd2 = ind2
		if(random.randint(1, 10) < (config.RECOMBINATION_PROB * 10)):
			newInd1 = self.__recombine(ind1, firstSlice2, lastSlice2)
			newInd2 = self.__recombine(ind2, firstSlice1, lastSlice1)
			print('crossover - fitness indv1 ',newInd1.fitness(),newInd1.getGenotypeDecimal())
			print('crossover - fitness indv2 ',newInd2.fitness(),newInd2.getGenotypeDecimal())
			return (newInd1, newInd2)
		else:
			return (None, None)


	def basicCrossoverFunction(self, ind1, ind2):
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

		newInd1 = firstSlice1
		newInd1 = newInd1 + lastSlice2
		newInd2 = firstSlice2
		newInd2 = newInd2 + lastSlice1

		return (newInd1, newInd2)

	def __defaultParentsSelectionFunction(self):
		# The default parents selection method is based on picking
		# five individuals randomically and then selecting the two
		# most qualified (higher fitness) to breed. This method will
		# return a list containing lists of two individuals.
		couples = []
		indvs = list(self.individuals)
		# Distribute individuals and place the top two together.
		'''
		while len(indvs) > 0:
			candidates = []
			for i in range(5):
				ind = random.choice(indvs)
				candidates.append(ind)
				indvs.remove(ind)
			candidates.sort(key=lambda x: x.fitness(), reverse=True)
			couples.append([candidates[0], candidates[1]])
		'''
		indvs.sort(key=lambda x: x.fitness(), reverse=True)
		i=1

		while(indvs[0]==indvs[i]):
			i = i+1
			if(i==len(indvs)):
				i=1
				break

		couples.append([indvs[0], indvs[i]])
		
		return couples

	def __defaultSurvivalSelectFunction(self, numSurvivals=config.NUM_INDIVIDUALS):
		"""
		This function remove the individuals with small fitness from population
		"""
		# Sort individuals by fitness
		self.individuals.sort(key=methodcaller('fitness'), reverse=True)
		if len(self.individuals) >= numSurvivals:
			for i in range(len(self.individuals)-numSurvivals):
				print('survivalselect ',self.individuals.pop().getGenotypeDecimal())

		else:
			raise Exception('Your population is smaller than your settings. You probably do not run the crossover')
