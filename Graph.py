# -*- coding: utf-8 -*-
"""
PROYECTO O1
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio

Marzo 2022

CLASE GRAFO

"""

# Se importan las clases Nodo y Arista
from Node import node
from Edge import edge

class graph:
    
    #Atributos de la clase grafo
    def __init__(self):
        self.name = 'Graph'
        self.nodes = set(())
        self.edges = set(())
    
    # Se verifica la existencia del nodo con el parámetro nombre
    # Si existe regresa un 1
    def ExistingNode(self, name):
        for i in self.nodes:
            if i.id == name:
                return 1
    
    # Se verifica la existencia de la arista con el parámetro nombre
    # Si existe regresa un 1
    def ExistingEdge(self, name):
        for i in self.edges:
            if i.id == name:
                return 1
    
    # Aumenta el grado del nodo ingresado
    def n_degree(self, name):
        for i in self.nodes:
            n = int(i.id)
            if name == n:
                i.dg = i.dg + 1
                return 1
        
    # Agrega un nodo con el nombre ingresado como parámetro
    # Si el nodo existe regresa un 0 de lo contrario agrega el nodo y regresa un 1
    def AddNode(self, name):
        if self.ExistingNode(name) == 1:
            a = 0
        else:
            n_node = node(name)
            self.nodes.add(n_node)
            a = 1
            
        return a
            
    
    # Agrega una arista del nodo n0 al nodo n1
    # Si la arista existe regresa un 0 de lo contrario agrega la arista y regresa un 1
    # Cuando se agrega la arista aumenta el grado del nodo n0 y n1
    def AddEdge(self, n0, n1):
            
        name = str(n0) + ' -- ' + str(n1)
        
        if self.ExistingEdge(name) == 1:
            a = 0
        else:
            if self.ExistingNode(n0) == 0 or self.ExistingNode(n1) == 0:
                a = 0
            else: 
                n_edge = edge(name, str(n0), str(n1))
                self.edges.add(n_edge)
                a = 1
                
                self.n_degree(n0)
                self.n_degree(n1)
                
        return a
    
    # Obtiene el nodo indicado por su nombre
    def getNode(self, name):
        
        for i in self.nodes:
            if i.id == name:
                return i
    
    # Obtiene la arista indicada por su nombre
    def getEdge(self, name):
        e = 0
        for i in self.edges:
            if e == name:
                return i
            e = e + 1
    
    # Se muestra el grafo generado enlistando en primera instancia los nodos 
    # y posteriormente las aristas
    def showGraph(self):
        value = "Nodes: "
        
        for i in self.nodes:
             value = value + str(i.id) + ', '
        
        value = value + '\nEdges: '
        
        for j in self.edges:
            value = value + str(j.id) + ', '
        
        return print(value)

    # Se convierte el grafo al formato necesario para generar el archivo .gv
    def convertGraphViz(self):
        value = 'graph{\n'
        for i in self.edges:
            value = value + str(i.id) +';\n'
        value = value + '}\n'
        
        return value
    
    # Se genera el archivo .gv con el nombre ingresado y el número de nodos en el grafo
    def fileGraphViz(self, file_name):
        graph2save = self.convertGraphViz()
        f = open(file_name + str(len(self.nodes)) + '.gv', 'w+')
        f.write(graph2save)
            
            
            
        
        