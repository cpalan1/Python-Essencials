# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:30:04 2021

@author: cpala
"""

frase_larga=input("Ingrese una frase: ")
letra_bsq=input("letra a contar: ")
j=0
for cntrl in frase_larga :
    if cntrl == letra_bsq:
      j+=1
print (j)