#
# Individual.py
#

from random import randint

class Individual:

	fitnessFunc = None
	
	def __init__(self, genotypeLen=24, geneLen=3, fitnessFunc=None, mutationFunc=None):
		self.error = 0
		self.geneLen = geneLen
		self.genotype = [randint(0, 1) for _ in range(0, genotypeLen)]
		self.fenotype = self.genotype
		self.fitnessFunc = self.__defaultFitnessFunc if not fitnessFunc else fitnessFunc
		self.mutationFunc = self.__defaultMutationFunc if not mutationFunc else mutationFunc

	def getGeneNum(self):
		"""
		Get the number of genes in the genotype
		"""
		return int(len(self.genotype)/self.geneLen)

	def getGene(self, i):
		"""
		Get ith gene in the genotype
		"""
		if i <= 0:
			raise Exception('You can only get a gene starting to 1 to ' + str(self.geneLen))
		i = i-1
		return self.genotype[i*self.geneLen:i*self.geneLen+self.geneLen]

	def setGene(self, i, gene):
		"""
		Set the ith gene in genotype
		If the argument passed is not a binary list it raise an exception
		"""
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
		self.mutationFunc(*args, **kwargs)

	def binaryToDecimal(self, string, i, length):
		num = 0
		maximum = (i+length)
		while i < maximum:
			num = num << 1
			num += int(string[i])
			i = i + 1
		return num

	def __defaultFitnessFunc(self, *args, **kwargs):
		f = 0
		# The fitness is equal to the number of queens in valid spots.
    	# Loop through each queen position (row assignment).
		for j in range(8):
			collisions = 0
			baseQueenRow = self.binaryToDecimal(self.genotype, (j*3), 3)
			# Look for queens on the same row or diagonal.
			for jx in range(8):
				endQueenRow = self.binaryToDecimal(self.genotype, (jx*3), 3);
				sameRow = (baseQueenRow == endQueenRow);
				onDiagonal = (abs(baseQueenRow-endQueenRow) == abs(j-jx));
				collisions += ((sameRow == 1 or onDiagonal == 1) and (jx != j));
			f += (collisions == 0);
		return f

	def __defaultMutationFunc(self, *args, **kwargs):
		"""
		Change two genes in a genotype according to the probability of mutation
		"""
		#positions to be found
		pos1, pos2 = 0, 0
		# compute chances of mutation
		if(random.randint(1,10) < (MUTATION_PROB * 10)):
			# pickup two different numbers to mutate in genotype
			while(pos1==pos2):
				pos1 = random.randint(0,7)
				pos2 = random.randint(0,7) 
			# swap the first and second gene in genotype
			self.genotype[pos1],self.genotype[pos2]=self.genotype[pos2],self.genotype[pos1]
		