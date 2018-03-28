from random import randint
class Individual:
	fitnessFunc = None
	def __init__(self, numBits=5, fitnessFunc=None, mutationFunc=None):
		self.genotype = [randint(0,1) for _ in range(1,numBits+1)]
		self.fenotype = self.genotype
		self.error = 0 # FIXME: How to calculate me?
		if not fitnessFunc:
			self.fitnessFunc = self.__defaultFitnessFunc
		else:
			self.fitnessFunc = fitnessFunc
		if not mutationFunc:
			self.mutationFunc = self.__defaultMutationFunc
		else:
			self.mutationFunc = mutationFunc
	def setFitnessFunc(self, fitnessFunc):
		self.fitnessFunc = fitnessFunc
	def fitness(self, *args, **kwargs):
		"""
		Calculate the fitness for the individual
		"""
		return self.fitnessFunc(*args,**kwargs)
	def setMutationFunc(self, mutationFunc):
		self.mutationFunc = mutationFunc
	def mutation(self, *args, **kwargs):
		"""
		Make mutation in the individual
		"""
		self.mutationFunc(*args,**kwargs)

	def __defaultFitnessFunc(self, *args, **kwargs):
		return 1.0/(1+self.error)
	def __defaultMutationFunc(self, *args, **kwargs):
		# swap the first and second gene in genotype
		self.genotype[0],self.genotype[1]=self.genotype[1],self.genotype[0]
