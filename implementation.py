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
		initialPopulation,
		maxFitness,
		fitnessFunction,
		parentsSelectionFunction,
		recombinationFunction,
		mutationFunction,
		nQueens=8,
		numberOfIndividuals=100,
		numberOfCouples=1,
		recombinationProbability=0.9,
		mutationProbability=0.4,
		maximumFitnessEvaluations=10000,
	):
	# Metrics.
	iteration = 0
	foundSolution = False
	firstSolutionAtIteration = 0
	fitnessEvaluationsCount = numberOfIndividuals
	averageFitnessPerIteration = []
	fitnessDeviationPerIteration = []
	# Generate the initial population.
	p = initialPopulation
	# Compute individuals fitnesses.
	f = [fitnessFunction(x) for x in p]
	# Run until the maximum number of fitness evaluations is reached.
	while (fitnessEvaluationsCount < maximumFitnessEvaluations):
		iteration += 1
		# Algorithm evaluation.
		if foundSolution == False:
			# Store the average fitness and standard deviation (first generation).
			aux = [float(x) for x in f]
			averageFitnessPerIteration.append(statistics.mean(aux))
			fitnessDeviationPerIteration.append(statistics.stddev(aux))
			# Check if a solution was found.
			if f[0] == maxFitness:
				foundSolution = True
				firstSolutionAtIteration = iteration
				break
		# Select couples to breed.
		c = parentsSelectionFunction(population=p, fitnesses=f, maxCouples=numberOfCouples)
		# Recombine couples (breed).
		n = recombinationFunction(nQueens=nQueens, couples=c, recombinationProbability=recombinationProbability)
		# Calculate childs fitnesses.
		k = [fitnessFunction(x) for x in n]
		fitnessEvaluationsCount += len(n)
		# Combine childs and their parents, also, combine their fitnesses.
		p = p + n
		f = f + k
		# Mutate.
		for i in range(len(p)):
			p[i], performed = mutationFunction(individual=p[i], genesCount=nQueens, mutationProbability=mutationProbability)
			if performed == True:
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
		'averageFitnesPerIteration': averageFitnessPerIteration,
		'fitnessDeviationPerIteration': fitnessDeviationPerIteration,
	}
	return metrics

def dumbImplementation(nQueens=8, maximumFitnessEvaluations=10000, numberOfCouples=1, population=[]):

	return implementation(
		initialPopulation=population,
		#maxFitness=fitness.fitnessNaiveMaxFitness(),
		#fitnessFunction=fitness.fitnessNaive,
		maxFitness=fitness.fitnessSumAllMaxFitness(),
		fitnessFunction=fitness.fitnessSumAll,
		parentsSelectionFunction=parents.selectParentsBestTwoOutOfFive,
		recombinationFunction=recombination.crossoverCutAndCrossFillSimplified,
		mutationFunction=mutation.mutationRandomGene,
		nQueens=8,
		numberOfIndividuals=100,
		numberOfCouples=numberOfCouples,
		recombinationProbability=0.9,
		mutationProbability=0.4,
		maximumFitnessEvaluations=maximumFitnessEvaluations,
	)

def naiveImplementation(nQueens=8, maximumFitnessEvaluations=10000, numberOfCouples=1, population=[]):

	return implementation(
		initialPopulation=population,
		maxFitness=fitness.fitnessSumAllMaxFitness(),
		fitnessFunction=fitness.fitnessSumAll,
		parentsSelectionFunction=parents.selectParentsBestTwoOutOfFive,
		recombinationFunction=recombination.crossoverCutAndCrossFill,
		mutationFunction=mutation.mutationSwapTwo,
		nQueens=8,
		numberOfIndividuals=100,
		numberOfCouples=numberOfCouples,
		recombinationProbability=0.9,
		mutationProbability=0.4,
		maximumFitnessEvaluations=maximumFitnessEvaluations,
	)

def smartImplementation(nQueens=8, maximumFitnessEvaluations=10000, numberOfCouples=1, population=[]):

	return implementation(
		initialPopulation=population,
		maxFitness=fitness.fitnessSumAllMaxFitness(),
		fitnessFunction=fitness.fitnessSumAll,
		parentsSelectionFunction=parents.selectParentsRoulette,
		recombinationFunction=recombination.crossoverOrderOne,
		mutationFunction=mutation.mutationDisturbance,
		nQueens=8,
		numberOfIndividuals=100,
		numberOfCouples=numberOfCouples,
		recombinationProbability=0.9,
		mutationProbability=0.4,
		maximumFitnessEvaluations=maximumFitnessEvaluations,
	)

def implementationWrapper(implementationFunction, nQueens=8, times=30, numberOfCouples=1, populations=[]):
	# Auxiliaries.
	success = 0
	convergencesIteration = []
	convergencesPerExecution = []
	averageFitnessPerExecution = []
	averageFitnesPerIterationPerExecution = []
	fitnessDeviationPerIterationPerExecution = []
	# Execute the naive algorithm multiple times and calculate averages.
	for i in range(times):
		# Run algorithm implementation.
		metrics = implementationFunction(
			nQueens=nQueens,
			maximumFitnessEvaluations=10000,
			numberOfCouples=numberOfCouples,
			population=populations[i]
			)
		foundSolution = metrics['foundSolution']
		firstSolutionFoundAtIteration = metrics['firstSolutionFoundAtIteration']
		numberOfConvergences = metrics['numberOfConvergences']
		averageFitness = metrics['averageFitness']
		averageFitnesPerIteration = metrics['averageFitnesPerIteration']
		fitnessDeviationPerIteration = metrics['fitnessDeviationPerIteration']
		# Update metrics if a solution was found.
		if foundSolution:
			# Count the number of executions that converged.
			success += 1
			# Store the iteration in which the algorithm converged, the number of
			# individuals that converged and the average fitness per execution. We
			# use this to calculate the mean and stardand deviation.
			convergencesIteration.append(float(firstSolutionFoundAtIteration))
			convergencesPerExecution.append(float(numberOfConvergences))
			averageFitnessPerExecution.append(float(averageFitness))
		# Store data relative to each iteration in each execution, we'll use it later
		# to plot the average fitness per iteration and fitness deviation per iteration
		# of the execution that was closer to the all time averages.
		averageFitnesPerIterationPerExecution.append(averageFitnesPerIteration)
		fitnessDeviationPerIterationPerExecution.append(fitnessDeviationPerIteration)

	# Find the execution whose average fitness was closer to the all time average.
	#averageFitness = statistics.mean(averageFitnessPerExecution)
	#averageFitness = 56
	#closestExecutionIndex = statistics.closestValueToAverage(averageFitnessPerExecution, averageFitness)

	# Find the execution whose average iteration of convergence was closer to the all time average.
	averageConvergenceIteration = statistics.mean(convergencesIteration)
	#averageConvergenceIteration = max(convergencesIteration)
	#averageConvergenceIteration = min(convergencesIteration)
	closestExecutionIndex = statistics.closestValueToAverage(convergencesIteration, averageConvergenceIteration)

	# Create a folder to place the graphs.
	#conveniences.createFolder('results')

	# Prepare data to generate the graph.
	#fileBaseName = "results/"+(implementationFunction.__name__).lower()
	e = fitnessDeviationPerIterationPerExecution[closestExecutionIndex]
	y = averageFitnesPerIterationPerExecution[closestExecutionIndex]
	x = [x for x in range(len(y))]

	#implementationFunction.__name__
	#plotAvr,fig = plotation.plotList(averageList,'fitness medio por iteracao')
	#plotation.saveImage(implementationFunction.__name__+'/average.png', plotAvr, fig)
	#plotDev, fig = plotation.plotList(deviationList,'desvio padrao do fitness por iteracao')
	#plotation.saveImage(implementationFunction.__name__+'/deviation.png', plotDev, fig)

	# ...
	print('1. Em quantas execucoes o algoritmo convergiu?')
	print('   ' + str(success) + '/' + str(times))

	# ...
	average = statistics.mean(convergencesIteration)
	deviation = statistics.stddev(convergencesIteration)
	print('2. Em que iteracao o algoritmo convergiu?')
	print('   Media:' + str(average))
	print('   Desvio Padrao:' + str(deviation))
	#conveniences.writeToFile('iterations.out', average)
	#conveniences.writeToFile('iterations.out', deviation)

	# ...
	average = statistics.mean(convergencesPerExecution)
	deviation = statistics.stddev(convergencesPerExecution)
	print('3. Quantos de individuos convergiram por execucao?')
	print('   Media:' + str(average))
	print('   Desvio Padrao:' + str(deviation))
	#conveniences.writeToFile('convergency.out', average)
	#conveniences.writeToFile('convergency.out', deviation)

	# ...
	average = statistics.mean(averageFitnessPerExecution)
	deviation = statistics.stddev(averageFitnessPerExecution)
	print('4. Fitness medio alcancado?')
	print('   Media: ' + str(average))
	print('   Desvio Padrao:' + str(deviation))
	#conveniences.writeToFile('fitness.out', average)
	#conveniences.writeToFile('fitness.out', deviation)

	return x, y, e
