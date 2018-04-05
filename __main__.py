from util.Population import Population
import util.config as config

def cutAndCross():
	pass

pop = Population(config.NUM_INDIVIDUALS)
pop.setCrossoverFunct(cutAndCross)
# Show children created
for ind in pop.individuals:
	print(ind.genotype)

for i in range(0, config.ITERATIONS_LEN):
	# TODO: There should be a funtion like 'run'
	# 		to allow to select children and the survivors
	# 		and the crossover
	pass
# TODO: Plot a graph with the solution