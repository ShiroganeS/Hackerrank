import numpy
line_1 = input()
n, m = numpy.array (line_1.split(), int)
arr = [ input (). split() for _ in range(n)]
AiR = numpy.array(arr, int)
produkt = numpy.prod(numpy.sum(AiR,axis=0), axis = 0)
print (produkt)
