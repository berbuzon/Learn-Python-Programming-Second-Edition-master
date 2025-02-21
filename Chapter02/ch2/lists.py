# lists.py


# creation
[]  # empty list
list()  # same as []
[1, 2, 3]  # as with tuples, items are comma separated
[x + 5 for x in [2, 3, 4]]  # Python is magic
list((1, 3, 5, 7, 9))  # list from a tuple
list('hello')  # list from a string


# main methods
a = [1, 2, 1, 3]
a.append(13)  # we can append anything at the end
a
[1, 2, 1, 3, 13]
a.count(1)  # how many `1` are there in the list?
2
a.extend([5, 7])  # extend the list by another (or sequence)
a
a.index(13)  # position of `13` in the list (0-based indexing)
a.insert(0, 17)  # insert `17` at position 0
a
a.pop()  # pop (remove and return) last element
a.pop(3)  # pop element at position 3
a
a.remove(17)  # remove `17` from the list
a
a.reverse()  # reverse the order of the elements in the list
a
a.sort()  # sort the list
a
a.clear()  # remove all elements from the list
a
a.append(100)  # append 100, heterogeneous type
a
['h', 'e', 'l', 'l', 'o', 100]
a.extend((1, 2, 3))  # extend using tuple
a
['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3]
a.extend('...')  # extend using string
a
['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']


# most common operations
a = [1, 3, 5, 7]
min(a)  # minimum value in the list
1
a = list('hello')  # makes a list from a string
a
a.append(100)  # append 100, heterogeneous type
a
a.extend((1, 2, 3))  # extend using tuple
a
a.extend('...')  # extend using string
a
a.extend([1 ,2, 3])

# cool sorting
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
sorted(a)
[(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
sorted(a, key=itemgetter(0))
a = [1, 3, 5, 7]
min(a)  # minimum value in the list
max(a)  # maximum value in the list
sum(a)  # sum of all values in the list
len(a)  # number of elements in the list
b = [6, 7, 8]
a + b  # `+` with list means concatenation
a * 3  # `*` has also a special meaning
from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
sorted(a)
sorted(a, key=itemgetter(0))
sorted(a, key=itemgetter(0, 1))
sorted(a, key=itemgetter(1))
sorted(a, key=itemgetter(1), reverse=True)
