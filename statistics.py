#
# statistics.py
#
# Taken from https://stackoverflow.com/questions/15389768/standard-deviation-of-a-list
#

def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        return 0
    return sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        return 0
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5

def closestValueToAverage(values, average):
    index = 0
    average = float(average)
    for i in range(len(values)):
        if abs(values[i]-average) < abs(values[index]-average):
            index = i
    return index
