# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:17:00 2021

@author: cpala
"""

num=int(input("Escriba un numero positivo: "))
while num<=0:
    print ("Numero negativo, vuelva a ingresar")
    num=int(input("Escriba un numero positivo: "))
print ("El numero es correcto")