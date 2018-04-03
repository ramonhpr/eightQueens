import random

def defaultMutation():
	#positions to be found
	pos1, pos2 = 0, 0
	
	# compute chances of mutation
	if(random.randint(1,10) < (MUTATION_PROB * 10)):
		# pickup two different numbers to mutate
		while(pos1==pos2):
			pos1 = random.randint(0,7)
			pos2 = random.randint(0,7) 
		# swap the first and second gene in genotype
		self.genotype[pos1],self.genotype[pos2]=self.genotype[pos2],self.genotype[pos1]
	



defaultMutation()