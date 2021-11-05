# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:10:56 2021

@author: cpala
"""

def datos(nombre,apellido="Sin definir",edad=0):
    """Declarar el nombre y apellido como un string
    y la edad como un int"""
    print(f"Nombre:{nombre.title()}\nApellido: {apellido.title()}\nEdad::{edad}")
    return

datos("cristina")