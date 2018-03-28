from random import randint
class Individual:
	fitnessFunc = None
	def __init__(self, genotypeLen=24, geneLen=3, fitnessFunc=None, mutationFunc=None):
		self.geneLen = geneLen
		self.genotype = [randint(0,1) for _ in range(0,genotypeLen)]
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
	def getGeneNum(self):
		"""
		Get the number of genes in the genotype
		"""
		return len(self.genotype)/self.geneLen
	def getGene(self, i):
		"""
		Get ith gene in the genotype
		"""
		if i <= 0:
			raise Exception('You can only get a gene starting to 1 to ' + str(self.geneLen))
		i=i-1
		return self.genotype[i*self.geneLen:i*self.geneLen+self.geneLen]
	def setGene(self, i, gene):
		if i <= 0 :
			raise Exception('You can only set a gene starting to 1 to ' + str(self.geneLen))
                i=i-1
		if not isinstance(gene, list):
			raise TypeError('The gene should be a list')
		if len(gene) > self.geneLen:
			raise Exception('The gene is bigger than '+ str(self.geneLen))
		# TODO: Verify if the string is binary
		self.genotype[i*self.geneLen:i*self.geneLen+self.geneLen] = gene
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
