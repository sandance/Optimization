#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import os
import sys
import collections
import functools

Item = namedtuple("Item", ['index', 'value', 'weight'])

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




#Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
#    item_count = int(firstLine[0])
 #   capacity = int(firstLine[1])
    n=int(firstLine[0])
    k=int(firstLine[1])
    maxweight=k

    items = []

    for i in range(1,n+1):
        line = lines[i]
        parts = line.split()
#        print "%d %d\n"% (int(parts[0]), int(parts[1]))
	items.append([int(parts[0]),int(parts[1])])
#	print items

	# put your solution here
    bestvalue, reconstruction = knapsack(items, maxweight)
#   print bestvalue,reconstruction	
    x_list=[0]*n
    for value, weight in reconstruction:
                for i,val  in enumerate(items):
                        if val[0] == value:
                                        x_list[i]=1    

    	# prepare the solution in the specified output format
    flag=1
    output_data = str(bestvalue) + ' ' + str(flag) + '\n'
#  output_data += ' '.join(map(str, taken)
#    print " ".join(str(v) for v in x_list)
    output_data += ' '.join(str(v) for v in x_list)
    return output_data
'''
    # now try to solve it with greedy and compare with DP
    crics = []

    for i in range(1, n+1):
        line = lines[i]
        parts = line.split()
        crics.append(Item(i-1, int(parts[0]), int(parts[1])))
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in crics:
        if weight + item.weight <= k:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    if bestvalue > value:
	flag=1
    else:
	flag=0'''
    #output_data = str(bestvalue) + ' ' + str(flag) + '\n'
    #output_data += ' '.join(str(v) for v in x_list)	
#    return output_data
  


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

