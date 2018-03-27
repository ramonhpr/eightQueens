from random import randint
class Individual:
	fitnessFunc = None
	def __init__(self, numBits=5, fitnessFunc=None):
		self.genotype = [randint(0,1) for _ in range(1,numBits+1)]
		self.fenotype = self.genotype
		self.error = 0 # FIXME: How to calculate me?
		if not fitnessFunc:
			self.fitnessFunc = self.__defaultFitnessFunc
		else:
			self.fitnessFunc = fitnessFunc
	def setFitnessFunc(self, fitnessFunc):
		self.fitnessFunc = fitnessFunc
	def fitness(self, *args, **kwargs):
		"""
		Calculate the fitness for the individual
		"""
		return self.fitnessFunc(*args,**kwargs)

	def __defaultFitnessFunc(self, *args, **kwargs):
		return 1.0/(1+self.error)
