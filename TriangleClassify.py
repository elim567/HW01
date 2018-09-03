'''
Created on Sep 2, 2018
@author:  Erik Lim
Pledge:   "I pledge my honor that I have abided by the Stevens Honor System." - EL

Homework 01: Testing triangle classification
'''

def classify_triangle(a, b, c):    
    if a**2 + b**2 == c**2:
        return ("This triangle is right")
        if a!=b and b!=c and c!=a:
            return ("This triangle is also scalene")
        elif a == b or b == c or a == c:
            if a!=b or b!=c or c!=a:
                return ("This triangle is also isoceles")
    elif a!=b and b!=c and c!=a:
        return ("This triangle is scalene")
    elif a == b == c:
        return ("This triangle is equilateral")
    elif a == b or b == c or a == c:
        if a!=b or b!=c or c!=a:
            return ("This triangle is isosceles")
    
            
