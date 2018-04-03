#
# Population.py
#

from util.Individual import Individual
import random

class Population:

	def __init__(self, num_individuals=100, numGenes=24, geneLen=3, parentsSelectionFunction=None):
		"""
		Initialize a population with num_individuals binary
		string individuals,the default genes number is 24
		and the default binary string (gene) length is 3
		"""
		self.individuals = []
		self.epoch = 0
		self.parentsSelectionFunction = self.__defaultParentsSelectionFunction if not parentsSelectionFunction else parentsSelectionFunction

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
		self.crossover = func

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
