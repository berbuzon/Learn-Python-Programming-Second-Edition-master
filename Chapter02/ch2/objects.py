# objects.py

# code block # 1
age = 42
print(age)
age = 43  #A
print(age)


# code block # 2
age = 42
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
