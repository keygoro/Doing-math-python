# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:44:54 2019

@author: tamagawa
"""

#7.4.1 微分電卓

from sympy import Symbol, Derivative, sympify, pprint #sympify:sympyオブジェクトに変換
from sympy.core.sympify import SympifyError

def derivative (f,var):
    var = Symbol(var)
    d = Derivative(f,var).doit()
    pprint(d)
    
if __name__=='__main__':
     
    f = input('Enter　a function')
    var = input('Enter the variable to differentiate  with respect to:')
    
try: 
        f = sympify(f)
    
except SympifyError:
        print('Invalid input')

else:
        derivative(f, var)
