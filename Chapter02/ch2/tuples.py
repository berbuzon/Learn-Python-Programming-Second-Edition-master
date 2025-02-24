# tuples.py


<<<<<<< HEAD
>>> t = ()  # empty tuple
>>> type(t)
<class 'tuple'>
>>> one_element_tuple = (42, )  # you need the comma!
>>> three_elements_tuple = (1, 3, 5)  # braces are optional here
>>> a, b, c = 1, 2, 3  # tuple for multiple assignment
>>> a, b, c  # implicit tuple to print with one instruction
(1, 2, 3)
>>> 3 in three_elements_tuple  # membership test
True


# swap
>>> a, b = 1, 2
>>> c = a  # we need three lines and a temporary var c
>>> a = b
>>> b = c
>>> a, b  # a and b have been swapped
(2, 1)

# swap pythonic
>>> a, b = 0, 1
>>> a, b = b, a  # this is the Pythonic way to do it
>>> a, b
(1, 0)
=======
t = ()  # empty tuple
print(type(t))

one_element_tuple = (42, )  # you need the comma!
print (type (one_element_tuple))
three_elements_tuple = (1, 3, 5)  # braces are optional here
print(three_elements_tuple)
a, b, c = 1, 2, 3  # tuple for multiple assignment
print(a, b, c)  # implicit tuple to print with one instruction

print(3 in three_elements_tuple)  # membership test

# swap
a, b = 1, 2
c = a  # we need three lines and a temporary var c
a = b
b = c
print(a, b)  # a and b have been swapped

# swap pythonic
a, b = 0, 1
a, b = b, a  # this is the Pythonic way to do it
print(a, b)
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4
