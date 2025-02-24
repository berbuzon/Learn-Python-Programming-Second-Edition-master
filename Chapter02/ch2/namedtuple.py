# namedtuple.py


# the problem
<<<<<<< HEAD
>>> vision = (9.5, 8.8)
>>> vision
(9.5, 8.8)
>>> vision[0]  # left eye (implicit positional reference)
9.5
>>> vision[1]  # right eye (implicit positional reference)
8.8


# the solution
>>> from collections import namedtuple
>>> Vision = namedtuple('Vision', ['left', 'right'])
>>> vision = Vision(9.5, 8.8)
>>> vision[0]
9.5
>>> vision.left  # same as vision[0], but explicit
9.5
>>> vision.right  # same as vision[1], but explicit
8.8


# the change
>>> Vision = namedtuple('Vision', ['left', 'combined', 'right'])
>>> vision = Vision(9.5, 9.2, 8.8)
>>> vision.left  # still correct
9.5
>>> vision.right  # still correct (though now is vision[2])
8.8
>>> vision.combined  # the new vision[1]
=======
vision = (9.5, 8.8)
print(vision)
print(vision[0])  # left eye (implicit positional reference)
print(vision[1])  # right eye (implicit positional reference)


# the solution
from collections import namedtuple
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
print(vision[0])
print(vision.left)  # same as vision[0], but explicit
print(vision.right)  # same as vision[1], but explicit


# the change
Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)
print(vision.left)  # still correct
print(vision.right)  # still correct (though now is vision[2])
print(vision.combined)  # the new vision[1]
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4
9.2
