#
# Individual.py
#

import util.config as config
from random import randint
from math import factorial
from itertools import permutations

class Individual:

	fitnessFunc = None
	
	def __init__(self, genotypeLen=24, geneLen=3, fitnessFunc=None, mutationFunc=None):
		self.error = 0
		self.geneLen = geneLen
		self.genotype = Individual.generateGenotype(genotypeLen, geneLen)
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
		return self.fitnessFunc(self, *args, **kwargs)

	def setMutationFunc(self, mutationFunc):
		self.mutationFunc = mutationFunc

	def mutation(self, *args, **kwargs):
		"""
		Make mutation in the individual
		"""
		self.mutationFunc(*args, **kwargs)

	def __listToStr(self, l):
		"""
		This auxiliar function convert a list to a string
		"""
		return ''.join(str(i) for i in l)

	@staticmethod
	def generateGenotype(genotypeLen, geneLen):
		"""
		This auxiliar function return a list with genotypes permuutations
		"""
		index = randint(0, factorial(int(genotypeLen/geneLen)))
		genotypeDecimal = None
		for i,t in enumerate(permutations(range(int(genotypeLen/geneLen)))):
			if i == index:
				genotypeDecimal = list(t)
				break
		genotypeStr = []
		strFormat = '0'+str(geneLen)+'b'
		for i in genotypeDecimal:
			genotypeStr.append(format(i, strFormat))
		genotype = []
		for i in genotypeStr:
			genotype = genotype + [j for j in i]
		return genotype

	def __binaryToDecimal(self, l):
		"""
		This function receive a binary list and convert to a decimal list
		"""
		s = self.__listToStr(l)
		arr=[]
		while len(s) > 0:
			tmp = s[ :self.geneLen]
			s = s[self.geneLen: ]
			arr.append(int(tmp,2))
		return arr

	def getGenotypeDecimal(self):
		"""
		This function return the genotype conveted to decimal
		"""
		return self.__binaryToDecimal(self.genotype)

	def __defaultFitnessFunc(self, *args, **kwargs):
		f = 0
		# The fitness is equal to the number of queens in valid spots.
    	# Loop through each queen position (row assignment).
		for j in range(8):
			collisions = 0
			baseQueenRow = self.__binaryToDecimal(self.getGene(j+1))[0]
			# Look for queens on the same row or diagonal.
			for jx in range(8):
				endQueenRow = self.__binaryToDecimal(self.getGene(jx+1))[0]
				sameRow = (baseQueenRow == endQueenRow)
				onDiagonal = (abs(baseQueenRow-endQueenRow) == abs(j-jx))
				collisions += ((sameRow == 1 or onDiagonal == 1) and (jx != j))
			f += (collisions == 0)
		return f

	def __defaultMutationFunc(self, *args, **kwargs):
		"""
		Change two genes in a genotype according to the probability of mutation
		"""
		#positions to be found
		pos1, pos2 = 0, 0
		# compute chances of mutation
		if(randint(1,10) < (config.MUTATION_PROB * 10)):
			# pickup two different numbers to mutate in genotype
			while(pos1==pos2):
				pos1 = randint(0,7)
				pos2 = randint(0,7)
			# swap the first and second gene in genotype
			self.genotype[pos1],self.genotype[pos2]=self.genotype[pos2],self.genotype[pos1]
		