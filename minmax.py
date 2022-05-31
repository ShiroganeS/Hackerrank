import numpy
first_value = input()
n, m = numpy.array (first_value.split(), int)
arr = [ input (). split() for _ in range(n)]
AiR = numpy.array(arr, int)
produkt = numpy.max(numpy.min(AiR,axis=1))
print (produkt)