# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:35:32 2021

@author: User
"""

import unittest
from .WhiteDwarf import get_Nh, aprox
class TestFunc(unittest.TestCase):

    def test_get_Nh(self):
        self.assertEqual(get_Nh(0), 0) 
        print('test_get_Nh2 OK')
    
    def test_get_Nh2(self):
        self.assertEqual(get_Nh(100), 10.0) 
        print('test_get_Nh2 OK')
    
    def test_aprox(self):        
        self.assertEqual(aprox([17769.0,16865.743295019158],[54552,64552.0],0,60000),17276.90574712644)  
        print('test_aprox OK')
       


if __name__ == '__main__':
     unittest.main()