# final_considerations.py


<<<<<<< HEAD
>>> a = 1000000
>>> b = 1000000
>>> id(a) == id(b)
False


>>> a = 5
>>> b = 5
>>> id(a) == id(b)
True
=======
a = 1000000
b = 1000000
print(id(a) == id(b))  # False

a = 5
b = 5
print(id(a) == id(b))  # True
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4


# how to choose data structures
# example customer objects
customer1 = {'id': 'abc123', 'full_name': 'Master Yoda'}
customer2 = {'id': 'def456', 'full_name': 'Obi-Wan Kenobi'}
customer3 = {'id': 'ghi789', 'full_name': 'Anakin Skywalker'}
# collect them in a tuple
customers = (customer1, customer2, customer3)
# or collect them in a list
customers = [customer1, customer2, customer3]
# or maybe within a dictionary, they have a unique id after all
customers = {
    'abc123': customer1,
    'def456': customer2,
    'ghi789': customer3,
}


# negative indexing
<<<<<<< HEAD
>>> a = list(range(10))  # `a` has 10 elements. Last one is 9.
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(a)  # its length is 10 elements
10
>>> a[len(a) - 1]  # position of last one is len(a) - 1
9
>>> a[-1]  # but we don't need len(a)! Python rocks!
9
>>> a[-2]  # equivalent to len(a) - 2
8
>>> a[-3]  # equivalent to len(a) - 3
7
=======
a = list(range(10))  # `a` has 10 elements. Last one is 9.
print(a)
a = list(range(10))  # `a` has 10 elements. Last one is 9.
print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(a))  # its length is 10 elements
print(a[len(a) - 1])  # position of last one is len(a) - 1
print(a[-1])  # but we don't need len(a)! Python rocks!
print(a[-2])  # equivalent to len(a) - 2
print(a[-3])  # equivalent to len(a) - 3
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4
