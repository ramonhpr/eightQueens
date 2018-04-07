from util.Population import Population
import util.config as config
pop = Population(config.NUM_INDIVIDUALS)

# Show children created
for ind in pop.individuals:
	print(ind.getGenotypeDecimal(), '->',ind.fitness())

print('running..')
for i in range(config.ITERATIONS_LEN):
	newInds=[]
	# FIXME: The parent select function is choicing same parents,
	# that shouldn't happen because the crossover function will generate
	# and fill the population with the same individual
	for ind1,ind2 in pop.parentsSelectionFunction():
		i,j = pop.crossover(ind1, ind2)
		if i:
			newInds.append(i)
		if j:
			newInds.append(j)
	pop.individuals= pop.individuals + newInds

	pop.mutate()
	# TODO: surrond the bellow function by try-except
	pop.survivalSelect(config.NUM_INDIVIDUALS)

	print('new population')
	for ind in pop.individuals:
		print(ind.getGenotypeDecimal(), '->',ind.fitness())
# TODO: Plot a graph with the solution
