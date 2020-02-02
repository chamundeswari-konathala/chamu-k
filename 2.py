Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/Users/ACER/Desktop/chamu/python prg/1.py ============
0
2
4
6
8
10
12
14
16
18
20
>>> 
============ RESTART: C:/Users/ACER/Desktop/chamu/python prg/1.py ============
Traceback (most recent call last):
  File "C:/Users/ACER/Desktop/chamu/python prg/1.py", line 2, in <module>
    print(sum(i))
TypeError: 'int' object is not iterable
>>> 
============ RESTART: C:/Users/ACER/Desktop/chamu/python prg/1.py ============
110
>>> 
=============================== RESTART: Shell ===============================
>>> i=list(range(0,22,2))
>>> print(i)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> print(sum(i))
