# sets.py


small_primes = set()  # empty set
small_primes.add(2)  # adding one element at a time
small_primes.add(3)
small_primes.add(5)
print(small_primes)
small_primes.add(1)  # Look what I've done, 1 is not a prime!
print(small_primes)
small_primes.remove(1)  # so let's remove it
print(3 in small_primes)  # membership test
print(4 in small_primes)
print(4 not in small_primes)  # negated membership test
small_primes.add(3)  # trying to add 3 again
print(small_primes)  # no change, duplication is not allowed
bigger_primes = set([5, 7, 11, 13])  # faster creation
print(small_primes | bigger_primes)  # union operator `|`
print(small_primes & bigger_primes)  # intersection operator `&`
print(small_primes - bigger_primes)  # difference operator `-`

small_primes = {2, 3, 5, 5, 3}
print(small_primes)

# frozenset
small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])
try:
    small_primes.add(11)  # we cannot add to a frozenset
except AttributeError as e:
    print(e)
try:
    small_primes.remove(2)  # neither we can remove
except AttributeError as e:
    print(e)
print(small_primes & bigger_primes)  # intersect, union, etc. allowed
