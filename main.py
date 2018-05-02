#
# main.py
#

import copy
import population
import conveniences
import implementation

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

implementation.implementationWrapper(
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

implementation.implementationWrapper(
    implementationFunction=implementation.smartImplementation,
    nQueens=n,
    times=times,
    numberOfCouples=couples,
    populations=copy.deepcopy(populations)
    )

print('##################################################')
print('')

# Remove disposable files.

conveniences.removeOutFiles()
conveniences.deleteBytecodeFiles()
