import os
import sys 
import collections 
import functools

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)







def knapsack(items,maxweight):
	''' Items are a sequence of pairs (value,weight) where value is a number and weight is a non negative number'''
	
	# Return the value of the most valuable subsequence of the first i elements 
	# in items whose weights sum to no than j

	@memoized
	def bestvalue(i,j):
		if i==0: return 0
		value, weight = items[i-1] # items is dictionary (value , weight) pair
		if weight > j:
			return bestvalue(i-1,j)
		else:
			return max(bestvalue(i-1,j),bestvalue(i-1,j - weight) + value)
		

	j = maxweight
    	result = []
    	for i in xrange(len(items), 0, -1):
        	if bestvalue(i, j) != bestvalue(i - 1, j):
            		result.append(items[i - 1])
            		j -= items[i - 1][1]
    	result.reverse()
    	return bestvalue(len(items), maxweight), result


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('usage: knapsack.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    firstLine = lines[0].split()
    n=int(firstLine[0])
    k=int(firstLine[1])
    


    maxweight = k
#    items = [map(int, line.split()) for line in lines[1:]]
    items = []

    for i in range(1,n+1):
        line = lines[i]
        parts = line.split()
        print "%d %d\n"% (int(parts[0]), int(parts[1]))
        items.append([int(parts[0]),int(parts[1])])

    bestvalue, reconstruction = knapsack(items, maxweight)

    print('Best possible value: {0}'.format(bestvalue))
    print('Items:')
    for value, weight in reconstruction:
        print('V: {0}, W: {1}'.format(value, weight))
'''

def getints():
        return map(int,raw_input().split())


if __name__ == '__main__':
	n,k=getints()
	maxweight = k
	items = [ getints() for i in xrange(n)]
	opt=1
	bestvalue, reconstruction = knapsack(items, maxweight)
	print("%d %d" % (bestvalue,opt))  
#	print('Items:')
	x_list=[0]*n
    	for value, weight in reconstruction:
        	for i,val  in enumerate(items):
			if val[0] == value:
					x_list[i]=1
		
	print " ".join(str(v) for v in x_list)
'''
