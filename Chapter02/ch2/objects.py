# objects.py

# code block # 1
age = 42
print(age)
# 42
age = 43  #A
print(age)
# 43


# code block # 2
age = 42
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