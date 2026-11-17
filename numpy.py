# Basic Python Errors

# SyntaxError: invalid code structure
# IndentationError: wrong indentation
# NameError: undefined variable or function
# TypeError: operation on the wrong data type
# ValueError: right type, inappropriate value
# ZeroDivisionError: division by zero
# IndexError: list index out of range
# KeyError: dictionary key not found
# AttributeError: object has no such attribute or method
# ImportError / ModuleNotFoundError: module can’t be imported or found
# FileNotFoundError: file doesn’t exist
# RecursionError: maximum recursion depth exceeded
# StopIteration: no more items in an iterator
# OverflowError: number too large to represent
# MemoryError: out of memory
# KeyboardInterrupt: program stopped by Ctrl + C

import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
b = a.reshape(2, 4)
print(b)

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.concatenate((a,b), axis = 1)
print(c)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.stack((a,b), axis = 1)
print(c)

a = np.array([1,2,3,4,5,6,7,8])
b = np.hstack(a)
c = np.vstack(a)
print(b)
print(c)

a = np.array([1,2,3,4])
b = a.copy()
a[0] = 10
print(a)
print(b)

a = np.array([1, 2, 3, 4])
b = a.view()
a[0] = 10
print(a)
print(b)

a = np.array([1,2,3,4])
print(a.dtype)

data = np.array([4, 8, 15, 16, 23, 42])

print(np.sum(data))      
print(np.mean(data))     
print(np.median(data))   
print(np.min(data))      
print(np.max(data))      
print(np.std(data))      
print(np.var(data))      
print(np.prod(a))        
print(np.cumsum(a))    