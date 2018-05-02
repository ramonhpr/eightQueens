#
# main.py
#

import implementation
import conveniences

n = 8
times = 100

'''
print('')
print('##################################################')
print('############## IMPLEMENTACAO BURRA ###############')
print('##################################################')

implementation.implementationWrapper(implementationFunction=implementation.dumbImplementation, nQueens=n, times=times)

print('##################################################')
print('')
'''

print('')
print('##################################################')
print('############## IMPLEMENTACAO BASICA ##############')
print('##################################################')

implementation.implementationWrapper(implementationFunction=implementation.naiveImplementation, nQueens=n, times=times)

print('##################################################')
print('')

print('')
print('##################################################')
print('############# IMPLEMENTACAO ESPERTA ##############')
print('##################################################')

implementation.implementationWrapper(implementationFunction=implementation.smartImplementation, nQueens=n, times=times)

print('##################################################')
print('')

# Remove disposable files.

conveniences.removeOutFiles()
conveniences.deleteBytecodeFiles()
