#
# main.py
#

import copy
import population
import conveniences
import implementation

import matplotlib.pyplot as plot

n = 8
couples = 1
times = 100
populations = []

for i in range(times):
    p = population.generateRanomBinaryPopulationUniqueGenes(individualsCount=100, numberOfQueens=n)
    populations.append(p)

'''
print('')
print('##################################################')
print('############## IMPLEMENTACAO BURRA ###############')
print('##################################################')

implementation.implementationWrapper(
    implementationFunction=implementation.dumbImplementation,
    nQueens=n,
    times=times,
    numberOfCouples=couples,
    populations=copy.deepcopy(populations)
    )

print('##################################################')
print('')
'''

print('')
print('##################################################')
print('############## IMPLEMENTACAO BASICA ##############')
print('##################################################')

naive_x, naive_y, naive_e = implementation.implementationWrapper(
    implementationFunction=implementation.naiveImplementation,
    nQueens=n,
    times=times,
    numberOfCouples=couples,
    populations=copy.deepcopy(populations)
    )

print('##################################################')
print('')

print('')
print('##################################################')
print('############# IMPLEMENTACAO ESPERTA ##############')
print('##################################################')

smart_x, smart_y, smart_e = implementation.implementationWrapper(
    implementationFunction=implementation.smartImplementation,
    nQueens=n,
    times=times,
    numberOfCouples=couples,
    populations=copy.deepcopy(populations)
    )

print('##################################################')
print('')

# Create a folder to place the graphs.

conveniences.createFolder('results')

# Average fitness graph.

plot.figure()
plot.plot(naive_x, naive_y, "s-")
plot.plot(smart_x, smart_y, "o-")
plot.legend(["Parte I", "Parte II"], loc="lower right")
plot.title("Average fitness per iteration.")
plot.xlabel("Iteration")
plot.ylabel("Average Fitness")
plot.savefig("results/average-fitness.png", bbox_inches="tight")

# Standard deviation graph.

plot.figure()
plot.plot(naive_x, naive_e, "s-")
plot.plot(smart_x, smart_e, "o-")
plot.legend(["Parte I", "Parte II"], loc="upper right")
plot.title("Standard deviation per iteration.")
plot.xlabel("Iteration")
plot.ylabel("Fitness Standard Deviation")
plot.savefig("results/standard-deviation.png", bbox_inches="tight")

# Remove disposable files.

conveniences.removeOutFiles()
conveniences.deleteBytecodeFiles()
