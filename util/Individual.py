from random import randint
class Individual:
	def __init__(self, numBits=5):
		self.genotype = [randint(0,1) for _ in range(1,numBits+1)]
		self.fenotype = self.genotype
		self.error = 0 # FIXME: How to calculate me?
	def fitness(self):
		"""
		Calculate the fitness for the individual
		"""
		return 1.0/(1+self.error)