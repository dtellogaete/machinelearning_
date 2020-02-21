# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:21:44 2020

@author: Daniel
"""

def price(product):
    cont_a = 0
    cont_b = 0
    cont_c = 0
    cont_d = 0    
    for i in product:
        if 'A' in i:
            cont_a = cont_a+1            
        if 'B' in i:
            cont_b = cont_b+1            
        if 'C' in i:
            cont_c = cont_c+1
        if 'D' in i:
            cont_d = cont_d+1            
    promo_a = (cont_a//3)
    cont_a = cont_a-promo_a*3
    promo_b = (cont_b//2)
    cont_b = cont_b-promo_b*2
    
        
    price = cont_a*50+cont_b*30+cont_c*20+cont_d*15+promo_a*130+promo_b*45
    print( price)
    
    
print(price('BBB'))

def price(purchase):
    cont = [0,0,0,0] 
    products = ['A','B','C','D']
    promo_quantity = [3, 2, 1, 1]
    price_unit = [50, 30, 20, 15]
    promo_price = [130, 45, 20, 15 ]
    promo = [0,0,0,0]
    for i in purchase:
        for j  in range(len(products)):
            if products[j] in i:
                cont[j]=cont[j]+1   
    value = 0
    for i in range(len(products)):
        promo[i] = cont[i]//promo_quantity[i]
        cont[i] = cont[i]-promo[i]*promo_quantity[i]              
        value = value +cont[i]*price_unit[i]+promo[i]*promo_price[i]    
    print( value)
    return value

import unittest

class MyTest(unittest.TestCase):
    
      
        
    def test(self):
        self.assertEqual(price('AAABBD'), 190)
        
        
t = MyTest()
print(t.test())







    
    
    
