# -*- coding: utf-8 -*-
"""
PROYECTO 01
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio

Marzo 2022

CLASE NODO

"""

class node:
    
    # Parámetros ingresados: nombre del nodo, grado, posición x y y
    def __init__(self, name, degree = 0, x = 0.0, y = 0.0):
        
        # Atributos de la clase Nodo
        self.id = name
        self.dg = degree
        self.xpos = x
        self.ypos = y
        
    def __str__(self):
        
        # Regresa la representación en string del identificador del nodo
        return self.id
        