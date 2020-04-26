from time import time
from numpy.random import random_sample
from numpy import max, abs, zeros
from numpy.linalg import eigvals
from multiprocessing import Pool, cpu_count



def max_eigval(i):
	a = random_sample((100,100))
	print('process id:', os.getpid())
	return max(abs(eigvals(A)))

if __name__ == "__main__":

	num_of_cpu = cpu_count()

	n = 10000
	A = zeros(n)
	
	with Pool(num_of_cpu) as p:
		start = time()

		A = p.map(max_eigval,range(n))

		finish = time()

		print('Finished in ', finish-start, 's')