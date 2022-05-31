import numpy
first_value = input()
n, m = numpy.array (first_value.split(), int)
arr = [ input (). split() for _ in range(n)]
AiR = numpy.array(arr, int)
mean = numpy.mean(AiR, axis = 1)
var = numpy.var(AiR, axis = 0)
std = numpy.std(AiR)
rnd = numpy.around(std, 11)
print (mean,var,rnd,sep="\n",end="")