# bytearray.py


<<<<<<< HEAD
>>> bytearray()  # empty bytearray object
bytearray(b'')
>>> bytearray(10)  # zero-filled instance with given length
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> bytearray(range(5))  # bytearray from iterable of integers
bytearray(b'\x00\x01\x02\x03\x04')
>>> name = bytearray(b'Lina')  #A - bytearray from bytes
>>> name.replace(b'L', b'l')
bytearray(b'lina')
>>> name.endswith(b'na')
True
>>> name.upper()
bytearray(b'LINA')
>>> name.count(b'L')
=======
bytearray()  # empty bytearray object
bytearray(b'')
bytearray(10)  # zero-filled instance with given length
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
bytearray(range(5))  # bytearray from iterable of integers
bytearray(b'\x00\x01\x02\x03\x04')
name = bytearray(b'Lina')  #A - bytearray from bytes
name.replace(b'L', b'l')
bytearray(b'lina')
name.endswith(b'na')
True
name.upper()
bytearray(b'LINA')
name.count(b'L')
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4
1
