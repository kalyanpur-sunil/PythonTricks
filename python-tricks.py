from __future__ import division
from pprint import pprint
import pdb
import collections
 
from collections import defaultdict
# enumerate
list_a = ['horse', 'cat', 'elephant']
for i, item in enumerate(list_a):
	print i, item

# pdb.set_trace()
# 0 horse
# 1 cat
# 2 elephant

# enumerate can also take another arguement
for i, item in enumerate(list_a, 101):
	print i, item

# 101 horse
# 102 cat
# 103 elephant

# dict/set comprehension
my_dict = {i: i*i for i in range(0,11)}
print my_dict

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

my_set = {i*i for i in range(0,11)}
print my_set
# set([0, 1, 4, 100, 81, 64, 9, 16, 49, 25, 36])

# forcing float division
result = 1.0/2
print 'using append .0: ', result


result = 1/2

print 'Using from __future__ import division (applicable only for python 2): ', result 

# (Python 2) want to easily share files in the directory 
# use python -m SimpleHTTPServer

# (Python 3)
# python -m http.server

expr = "[1,2,3]"
my_list = eval(expr)
print my_list

# profiling a script
# python -m cProfile my_script.py

# object introspection
my_obj = [1,2,3,4,5,6]
introspection = dir(my_obj)
print introspection

# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# debugging scripts 
# use pdb module.
# import pdb
# to set breakpoint pdb.set_trace()

# Simplify if consructs
n = 1
if n in [2,3,4,5,1]:
	print 'simplifed if consruct'

# reversing a list or string
a = [1,2,3,4]
reversed_list = a[::-1]
print reversed_list
# [4, 3, 2, 1]

# to reverse existing list
a.reverse()
print 'reversed existing list: ', a
# reversed existing list:  [4, 3, 2, 1]

# same can be applied to string
s = 'California'
print s[::-1]
# ainrofilaC

# pretty printing

my_dictionary = {i: i**i for i in range(0,11)}
pprint(my_dictionary)
#{0: 1,
 # 1: 1,
 # 2: 4,
 # 3: 27,
 # 4: 256,
 # 5: 3125,
 # 6: 46656,
 # 7: 823543,
 # 8: 16777216,
 # 9: 387420489,
 # 10: 10000000000}


# use of namedtuple
india = ('Delhi', 'India', 'Asia')
print india
print '%s is capital of %s and is in %s' % india
# it would be tough if there are large amount values.
# namedtuple from colletions comes to our rescue

Country = collections.namedtuple('Country', 'capital country continent')
print 'Country type: ', type(Country)

india = Country(capital='Delhi', country='India', continent='Asia')
print india.country

# How can I merge two Python dictionaries in a single expression?
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
a = {'f': 6}
# it is a two step process
# since we don't want to alter x, make a copy of x and assign to z.
# update x with y

z = x.copy()
z.update(y)

print 'Updated z: ', z

result = {}
def merge_dicts(*dicts):
	for dictionary in dicts:
		result.update(dictionary)

	return result

print 'calling merge_dicts() : ', merge_dicts(x,y,a)	

lst1 = [{"id": 1, "x": "one"}, {"id": 2, "x": "two"}]
lst2 = [{"id": 2, "x": "two"}, {"id": 3, "x": "three"}]

tmp_list = []
# for d in lst1:
# 	tmp_list.append(d)
# for d in lst2:
# 	tmp_list.append(d)
tmp_list.extend(lst1)
tmp_list.extend(lst2)

print 'temp list', tmp_list


# defaultdict
# a defaultdict is a dictonary with a default value for keys
key_list = ['ca','il','ia', 'il']
# not a good way of doing
f={}
for key in key_list:
	try:
		f[key] += 1
	except KeyError, e:
		f[key] = 1

print f


# good way of doing
frequency = defaultdict(int)

for key in key_list:
	frequency[key] += 1

print "frequency defaultdict: ", frequency

temp_dict = {'a':3, 'v':4}

# check if key exists in the dictionary
key='a'
if key in temp_dict:
	print 'key present'





