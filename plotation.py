import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.patches as mpatches

def plotGaussian(mean, sigma, label, mu=0):
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, mean)
    p, = plt.plot(x,mlab.normpdf(x, mu, sigma), label=label)
    return p

def plotList(lst, label):
    f = plt.figure()
    plt.ylabel(label)
    plt.xlabel('Numero de iteracoes')
    p, = plt.plot(lst, label=label)
    return p,f

def saveImage(name, p, f):
    leg = plt.legend(handles=[p],loc=4)
    ax = plt.gca().add_artist(leg)
    f.savefig(name)

# Function used to debug because it's blocking
def show():
    plt.show()

def plotByFile(fd):
    meanDumb = float(fd.readline())
    sigmaDumb = float(fd.readline())
    dumbplt = plotGaussian(meanDumb, sigmaDumb, 'dumb')
    leg = plt.legend(handles=[dumbplt],loc=1)
    ax = plt.gca().add_artist(leg)

    meanNaive = float(fd.readline())
    sigmaNaive = float(fd.readline())
    naiveplt = plotGaussian(meanNaive, sigmaNaive, 'naive')
    leg = plt.legend(handles=[naiveplt], loc=3)
    ax = plt.gca().add_artist(leg)

    meanSmart = float(fd.readline())
    sigmaSmart = float(fd.readline())
    smartplt = plotGaussian(meanSmart, sigmaSmart, 'smart')
    leg = plt.legend(handles=[smartplt], loc=4)
    ax = plt.gca().add_artist(leg)

if '__main__' == __name__:
    f = plt.figure()
    with open('iterations.out', 'r') as fd:
        plt.title('Iteracao de convergencia')
        plotByFile(fd)
    f.savefig('iterations.png')

    f = plt.figure()
    with open('convergency.out', 'r') as fd:
        plt.title('individuos que convergiram por execucao')
        plotByFile(fd)
    f.savefig('convergency.png')
    f = plt.figure()

    with open('fitness.out', 'r') as fd:
        plt.title('fitness alcancado')
        plotByFile(fd)
    f.savefig('fitness.png')

