# sequences.py


# strings
# 4 ways to make a string
str1 = 'This is a string. We built it with single quotes.'
str2 = "This is also a string, but built with double quotes."
str3 = '''This is built using triple quotes,
so it can span multiple lines.'''
str4 = """This too
is a multiline one
built with triple double-quotes."""
str4  #A
'This too\nis a multiline one\nbuilt with triple double-quotes.'
print(str4)  #B
# This too
# is a multiline one
# built with triple double-quotes.


# encode / decode
s = "This is üŋíc0de"  # unicode string: code points
type(s)
# <class 'str'>
encoded_s = s.encode('utf-8')  # utf-8 encoded version of s
encoded_s
b'This is \xc3\xbc\xc5\x8b\xc3\xadc0de'  # result: bytes object
type(encoded_s)  # another way to verify it
# <class 'bytes'>
encoded_s.decode('utf-8')  # let's revert to the original
'This is üŋíc0de'
bytes_obj = b"A bytes object"  # a bytes object
type(bytes_obj)
# <class 'bytes'>


# length
print(len(str1))
# 49


# indexing and slicing
s = "The trouble is you think you have time."
print(s[0])  # indexing at position 0, which is the first char
# 'T'
print(s[5])  # indexing at position 5, which is the sixth char
# 'r'
print(s[:4])  # slicing, we specify only the stop position
# 'The '
print(s[4:])  # slicing, we specify only the start position
# 'trouble is you think you have time.'
print(s[2:14])  # slicing, both start and stop positions
# 'e trouble is'
print(s[2:14:3])  # slicing, start, stop and step (every 3 chars)
# 'erb '
print(s[:])  # quick way of making a copy
# 'The trouble is you think you have time.'


# formatting
greet_old = 'Hello %s!'
print(greet_old % 'Fabrizio')
# 'Hello Fabrizio!'
greet_positional = 'Hello {}!'
print(greet_positional.format('Fabrizio'))
# 'Hello Fabrizio!'
greet_positional = 'Hello {} {}!'
print(greet_positional.format('Fabrizio', 'Romano'))
# 'Hello Fabrizio Romano!'
greet_positional_idx = 'This is {0}! {1} loves {0}!'
print(greet_positional_idx.format('Python', 'Fabrizio'))
# 'This is Python! Fabrizio loves Python!'
print(greet_positional_idx.format('Coffee', 'Fab'))
# 'This is Coffee! Fab loves Coffee!'
keyword = 'Hello, my name is {name} {last_name}'
print(keyword.format(name='Fabrizio', last_name='Romano'))
# 'Hello, my name is Fabrizio Romano'


# formatted string literals
name = 'Fab'
age = 42
print(f"Hello! My name is {name} and I'm {age}")
# "Hello! My name is Fab and I'm 42"
from math import pi
print(f"No arguing with {pi}, it's irrational...")
# "No arguing with 3.141592653589793, it's irrational..."
