# -*- coding: utf-8 -*-
"""
PROYECTO 03
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio
Mayo 2022
CLASE ARISTA
"""


class edge:
    
    # Parámetros ingresados: nombre de la arista, inicio y fin de la arista, peso de la arista
    def __init__(self, name, begin, end, weight = 0):
        
        # Atributos de la clase Arista
        self.source = begin
        self.target = end
        self.id = name
        self.weight = weight
        
    def __str__(self):
        
        # Regresa la representación en string del identificador de la arista
        return str(self.id)