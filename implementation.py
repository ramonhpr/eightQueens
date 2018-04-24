#
# implementation.py
#

import fitness
import parents
import mutation
import statistics
import population
import conveniences
import recombination
import plotation

def implementation(
		generatePopulationFunction,
		maxFitness,
		fitnessFunction,
		parentsSelectionFunction,
		recombinationFunction,
		mutationFunction,
		nQueens=8,
		numberOfIndividuals=100,
		recombinationProbability=0.9,
		mutationProbability=0.4,
		maximumFitnessEvaluations=10000,
	):
	# Metrics.
	iteration = 0
	foundSolution = False
	firstSolutionAtIteration = 0
	fitnessEvaluationsCount = numberOfIndividuals
	# Generate the initial population.
	p = generatePopulationFunction(individualsCount=numberOfIndividuals)
	# Compute individuals fitnesses.
	f = [fitnessFunction(x) for x in p]
	while (fitnessEvaluationsCount < maximumFitnessEvaluations):
		# Algorithm evaluation.
		iteration += 1
		if foundSolution == False and f[0] == maxFitness:
			foundSolution = True
			firstSolutionAtIteration = iteration
		# Select couples to breed.
		c = parentsSelectionFunction(population=p, fitnesses=f)
		# Recombine couples (breed).
		n = recombinationFunction(c, genesCount=nQueens, recombinationProbability=recombinationProbability)
		# Calculate childs fitnesses.
		k = [fitnessFunction(x) for x in n]
		fitnessEvaluationsCount += len(n)
		# Merge childs with their parents and, also, their fitnesses.
		p = p + n
		f = f + k
		# Mutate.
		for i in range(len(p)):
			p[i] = mutationFunction(individual=p[i], genesCount=nQueens, mutationProbability=mutationProbability)
			f[i] = fitnessFunction(p[i])
			fitnessEvaluationsCount += 1
		# Sort individuals by their fitnesses.
		z = zip(p, f)
		z.sort(key=lambda x: x[1], reverse=True)
		p, f = zip(*z)
		# Remove worst individuals from population.
		p = list(p[:numberOfIndividuals])
		f = list(f[:numberOfIndividuals])
	# Calculate metrics.
	aux = [float(x) for x in f]
	averageFitness = statistics.mean(aux)
	fitnessStardardDeviation = statistics.stddev(aux)
	convergencesCount = sum(x == maxFitness for x in f)
	# Return metrics packed in a dictionary.
	metrics = {
		'foundSolution': foundSolution,
		'firstSolutionFoundAtIteration': firstSolutionAtIteration,
		'numberOfConvergences': convergencesCount,
		'averageFitness': averageFitness,
	}
	return metrics

def dumbImplementation(nQueens=8, maximumFitnessEvaluations=10000):

	return implementation(
		generatePopulationFunction=population.generateRanomBinaryPopulation,
		maxFitness=fitness.fitnessNaiveMaxFitness(),
		fitnessFunction=fitness.fitnessNaive,
		parentsSelectionFunction=parents.selectParentsBestTwoOutOfFive,
		recombinationFunction=recombination.crossoverCutAndCrossFillSimplified,
		mutationFunction=mutation.mutationRandomGene,
		nQueens=8,
		numberOfIndividuals=100,
		recombinationProbability=0.9,
		mutationProbability=0.4,
		maximumFitnessEvaluations=maximumFitnessEvaluations,
	)

def naiveImplementation(nQueens=8, maximumFitnessEvaluations=10000):

	return implementation(
		generatePopulationFunction=population.generateRanomBinaryPopulationUniqueGenes,
		maxFitness=fitness.fitnessSumAllMaxFitness(),
		fitnessFunction=fitness.fitnessSumAll,
		parentsSelectionFunction=parents.selectParentsBestTwoOutOfFive,
		recombinationFunction=recombination.crossoverCutAndCrossFill,
		mutationFunction=mutation.mutationSwapTwo,
		nQueens=8,
		numberOfIndividuals=100,
		recombinationProbability=0.9,
		mutationProbability=0.4,
		maximumFitnessEvaluations=maximumFitnessEvaluations,
	)

def smartImplementation(nQueens=8, maximumFitnessEvaluations=10000):

	return implementation(
		generatePopulationFunction=population.generateRanomBinaryPopulationUniqueGenes,
		maxFitness=fitness.fitnessSumAllMaxFitness(),
		fitnessFunction=fitness.fitnessSumAll,
		parentsSelectionFunction=parents.selectParentsRoulette,
		recombinationFunction=recombination.crossoverCutAndCrossFill,
		mutationFunction=mutation.mutationSwapTwo,
		nQueens=8,
		numberOfIndividuals=100,
		recombinationProbability=0.9,
		mutationProbability=0.4,
		maximumFitnessEvaluations=maximumFitnessEvaluations,
	)

def implementationWrapper(implementationFunction, nQueens=8, times=30):
	# Auxiliaries.
	success = 0
	convergencesIteration = []
	convergencesPerExecution = []
	averageFitnessPerExecution = []
	# Execute the naive algorithm multiple times and calculate averages.
	for i in range(times):
		# Run algorithm implementation.
		metrics = implementationFunction(nQueens=nQueens, maximumFitnessEvaluations=10000)
		foundSolution = metrics['foundSolution']
		firstSolutionFoundAtIteration = metrics['firstSolutionFoundAtIteration']
		numberOfConvergences = metrics['numberOfConvergences']
		averageFitness = metrics['averageFitness']
		# Update metrics if a solution was found.
		if foundSolution:
			# Count the number of executions that converged.
			success += 1
			print(metrics)
			# Store the iteration in which the algorithm converged, the number of
			# individuals that converged and the average fitness per execution. We
			# use this to calculate the mean and stardand deviation.
			convergencesIteration.append(float(firstSolutionFoundAtIteration))
			convergencesPerExecution.append(float(numberOfConvergences))
			averageFitnessPerExecution.append(float(averageFitness))
	# plotation.plotList(averageFitnessPerExecution, 'Fitness medio')
	# plotation.show()
	# ...
	print('1. Em quantas execucoes o algoritmo convergiu?')
	print('   ' + str(success) + '/' + str(times))
	# ...
	average = statistics.mean(convergencesIteration)
	deviation = statistics.stddev(convergencesIteration)
	print('2. Em que iteracao o algoritmo convergiu?')
	print('   Media:' + str(average))
	print('   Desvio Padrao:' + str(deviation))
	conveniences.writeToFile('iterations.out', average)
	conveniences.writeToFile('iterations.out', deviation)
	# plotation.plotGaussian(average, deviation, 'iterations')
	# ...
	average = statistics.mean(convergencesPerExecution)
	deviation = statistics.stddev(convergencesPerExecution)
	print('3. Quantos de individuos convergiram por execucao?')
	print('   Media:' + str(average))
	print('   Desvio Padrao:' + str(deviation))
	conveniences.writeToFile('convergency.out', average)
	conveniences.writeToFile('convergency.out', deviation)
	# plotation.plotGaussian(average, deviation, 'convergency')
	# ...
	average = statistics.mean(averageFitnessPerExecution)
	deviation = statistics.stddev(averageFitnessPerExecution)
	print('4. Fitness medio alcancado?')
	print('   Media: ' + str(average))
	print('   Desvio Padrao:' + str(deviation))
	conveniences.writeToFile('fitness.out', average)
	conveniences.writeToFile('fitness.out', deviation)
