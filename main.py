#
# main.py
#

import implementation

times = 30

print('')
print('##################################################')
print('############## IMPLEMENTACAO BURRA ###############')
print('##################################################')

implementation.implementationWrapper(implementationFunction=implementation.dumbImplementation, nQueens=8, times=times)

print('##################################################')
print('')

print('')
print('##################################################')
print('############## IMPLEMENTACAO BASICA ##############')
print('##################################################')

implementation.implementationWrapper(implementationFunction=implementation.naiveImplementation, nQueens=8, times=times)

print('##################################################')
print('')

print('')
print('##################################################')
print('############## IMPLEMENTACAO BASICA ##############')
print('##################################################')

implementation.implementationWrapper(implementationFunction=implementation.smartImplementation, nQueens=8, times=times)

print('##################################################')
print('')
