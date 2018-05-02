#
# main.py
#

import implementation
import conveniences

times = 30
# Remove the files generated to plot
conveniences.removeOutFiles()

print('')
print('##################################################')
print('############## IMPLEMENTACAO SMART ###############')
print('##################################################')

implementation.implementationWrapper(implementationFunction=implementation.smartImplementation, nQueens=8, times=times)

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
print('############## IMPLEMENTACAO BURRA ###############')
print('##################################################')

implementation.implementationWrapper(implementationFunction=implementation.dumbImplementation, nQueens=8, times=times)

print('##################################################')
print('')
