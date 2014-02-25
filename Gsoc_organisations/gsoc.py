__author__ = 'Akshay'
from numpy import*

gsoc_14 = loadtxt('organisations.txt', dtype = 'string')  # Get all the organisations of 2014
gsoc_13 = loadtxt('organisations1.txt', dtype= 'string')  # Get all the organisations of 2013
c = [i.split(',')[1] for i in gsoc_14]
d = [i.split(',')[1] for i in gsoc_13]
e = [i for i in c if i not in d]
print e  # Array containing new organisations when compared to 2013