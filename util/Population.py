from util.Individual import Individual
class Population:
	def __init__(self, num_individuals, numGenes=24, geneLen=3):
		"""
		Initialize a population with num_individuals binary
		string individuals,the default genes number is 24
		and the default binary string (gene) length is 3
		"""
		self.individuals = []
		self.epoch = 0
		for i in range(0, num_individuals):
			self.individuals.append(Individual(numGenes, geneLen))

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

	# Private functions
	def __parentsSelection(self):
		pass
	def __survivalSelection(self):
		pass
