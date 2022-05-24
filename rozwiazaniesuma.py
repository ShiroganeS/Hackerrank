import numpy
N, M = map(int, input().split())
lines=[input().split() for _ in range(N)]
A = numpy.array(lines,int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))