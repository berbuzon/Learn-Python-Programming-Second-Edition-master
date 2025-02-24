# objects.py

# code block # 1
age = 42
print(age)
<<<<<<< HEAD
# 42
age = 43  #A
print(age)
# 43
=======
age = 43  #A
print(age)
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4


# code block # 2
age = 42
<<<<<<< HEAD
print(id(age))
# 4377553168
age = 43
print(id(age))
# 4377553200


# code block # 3
class Person():
   def __init__(self, age):
       self.age = age
...
fab = Person(age=42)
print(fab.age)
# 42
print(id(fab))
# 2242671764752
print(id(fab.age))
# 140707790659288
fab.age = 25  # I wish!
print(id(fab))  # will be the same
# 2242671764752
print(id(fab.age))  # will be different
# 140707790658744
=======
id(age)
age = 42
print(id(age))
age = 43
print(id(age))
# code block # 3
class Person():
	def __init__(self, age):
		self.age = age

fab = Person(age=42)
print(fab.age)  # 42
print(id(fab))  # 4380878496
print(id(fab.age))  # 4377553168
fab.age = 25  # I wish!
print(id(fab))  # will be the same, 4380878496
print(id(fab.age))  # will be different, 4377552624
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4
