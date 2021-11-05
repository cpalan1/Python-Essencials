# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 22:33:15 2021

@author: cpala
"""

compras=input("Ingresar los productos del carro separado por comas: ")
compras_p=compras.replace(",","\n")
print(compras_p)
z=compras.split(",")
print ("\nArticulo1:{}\nArticulo2:{}\nArticulo3:{}".format(z[0],z[1],z[2]))

