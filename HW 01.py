'''
Created on Sep 2, 2018
@author:  Erik Lim
Pledge:   "I pledge my honor that I have abided by the Stevens Honor System." - EL

Homework 01: Testing triangle classification
'''

import unittest
import TriangleClassify

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(TriangleClassify.classify_triangle(3,4,5),"This triangle is right","This triangle is also scalene")
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(TriangleClassify.classify_triangle(1,1,1),"This triangle is equilateral")
    def testMyTestSet3 (self):
        self.assertEqual(TriangleClassify.classify_triangle(10,10,10),"This triangle is isosceles")
    def testMyTestSet4 (self):
        self.assertEqual(TriangleClassify.classify_triangle(10,15,30),"This triangle is scalene")                

if __name__ == '__main__':                                                
    unittest.main()