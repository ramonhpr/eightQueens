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

def implementationWrapper(implementationFunction, times=30):
	# Auxiliaries.
	success = 0
	convergencesIteration = []
	convergencesPerExecution = []
	averageFitnessPerExecution = []
	# Execute the naive algorithm multiple times and calculate averages.
	for i in range(times):
	    # Run algorithm implementation.
	    metrics = implementationFunction(maximumFitnessEvaluations=10000)
	    foundSolution = metrics['foundSolution']
	    firstSolutionFoundAtIteration = metrics['firstSolutionFoundAtIteration']
	    numberOfConvergences = metrics['numberOfConvergences']
	    averageFitness = metrics['averageFitness']
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
	# ...
	print('1. Em quantas execucoes o algoritmo convergiu?')
	print('   ' + str(success) + '/' + str(times))
	# ...
	average = statistics.mean(convergencesIteration)
	deviation = statistics.stddev(convergencesIteration)
	print('2. Em que iteracao o algoritmo convergiu?')
	print('   Media:' + str(average))
	print('   Desvio Padrao:' + str(deviation))
	# ...
	average = statistics.mean(convergencesPerExecution)
	deviation = statistics.stddev(convergencesPerExecution)
	print('3. Quantos de individuos convergiram por execucao?')
	print('   Media:' + str(average))
	print('   Desvio Padrao:' + str(deviation))
	# ...
	average = statistics.mean(averageFitnessPerExecution)
	deviation = statistics.stddev(averageFitnessPerExecution)
	print('4. Fitness medio alcancado?')
	print('   Media: ' + str(average))
	print('   Desvio Padrao:' + str(deviation))

def naiveImplementation(maximumFitnessEvaluations=10000):

	# Definitions.
	generatePopulationFunction = population.generateRanomBinaryPopulationUniqueGenes
	maxFitness = fitness.fitnessNaiveMaxFitness()
	fitnessFunction = fitness.fitnessNaive
	parentsSelectionFunction = parents.selectParentsBestTwoOutOfFive
	recombinationFunction = recombination.crossoverCutAndCrossFill
	mutationFunction = mutation.mutationSwapTwo

	# Metrics.
	iteration = 0
	foundSolution = False
	firstSolutionAtIteration = 0
	fitnessEvaluationsCount = 100

	# Generate the initial population.
	p = generatePopulationFunction(individualsCount=100)
	# Compute individuals fitnesses.
	f = [fitnessFunction(x) for x in p]

	while (fitnessEvaluationsCount < maximumFitnessEvaluations):
	#while (f[99] != maxFitness):

		# Algorithm evaluation.
		iteration += 1
		if foundSolution == False and f[0] == maxFitness:
			foundSolution = True
			firstSolutionAtIteration = iteration

		# Select couples to breed.
		c = parentsSelectionFunction(population=p, fitnesses=f)
		# Recombine couples (breed).
		n = recombinationFunction(c, genesCount=8, recombinationProbability=0.9)
		# Calculate childs fitnesses.
		k = [fitnessFunction(x) for x in n]
		fitnessEvaluationsCount += len(n)
		# Merge childs with their parents and, also, their fitnesses.
		p = p + n
		f = f + k
		# Mutate.
		for i in range(len(p)):

			mp = 0.4 #(0.4 * (1 - (f[i] / float(maxFitness))) ) + 0.1

			p[i] = mutationFunction(individual=p[i], genesCount=8, mutationProbability=mp)
			f[i] = fitnessFunction(p[i])
			fitnessEvaluationsCount += 1

		# Sort individuals by their fitnesses.
		z = zip(p, f)
		z.sort(key=lambda x: x[1], reverse=True)
		p, f = zip(*z)
		# Remove worst individuals from population.
		p = list(p[:100])
		f = list(f[:100])

		'''
		fucks = 0
		for fit in f:
			fucks += 1 if fit == maxFitness else 0
		print(fucks)
		#'''

	# Calculate metrics.
	aux = [float(x) for x in f]
	averageFitness = statistics.mean(aux)
	fitnessStardardDeviation = statistics.stddev(aux)
	convergencesCount = sum(x == maxFitness for x in f)

	metrics = {
		'foundSolution': foundSolution,
		'firstSolutionFoundAtIteration': firstSolutionAtIteration,
		'numberOfConvergences': convergencesCount,
		'averageFitness': averageFitness,
	}

	'''
	print("Iterations count: " + str(iteration))
	print("Fitness evaluations count: " + str(fitnessEvaluationsCount))
	print("Average fitness: " + str(averageFitness))
	print("Fitness standard deviation: " + str(fitnessStardardDeviation))
	print("Found solution: " + str(foundSolution))
	print("Number of convergences: " + str(convergencesCount))
	if foundSolution:
		print("First solution found at iteration: " + str(firstSolutionAtIteration))
	#'''

	'''
	print("")
	solutions = []
	aux = [conveniences.binaryToDecimal(x) for x in p]
	for item in aux:
		txt = ""
		for subitem in item:
			txt += (str(subitem) + " ")
		solutions.append(txt)
	solutions = list(set(solutions))
	for solution in solutions:
		print(solution)
	#'''

	return metrics
