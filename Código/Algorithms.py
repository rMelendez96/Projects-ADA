# -*- coding: utf-8 -*-
"""
PROYECTO 04
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio
Junio 2022
ALGORITMOS PARA GENERACIÓN DE GRAFOS
"""

from Graph import graph
import random
import numpy as np


def distance(n0, n1):
    # Se calcula la distancia entre dos nodos
    d = np.sqrt((n1.xpos - n0.xpos)**2 + (n1.ypos - n0.ypos)**2)
    return d
    

def grid_Graph(m, n=0, directed = False):
    
    """
    Genera grafo de malla
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
     
    """
    #Validación de parámetros
    # En caso de no ingresar n, n es igual a m
    if n == 0:
        n = m
    
    # Se saca el máximo entre los parámetros ingresados, puesto que m y n deben ser mayores a 1
    m=max(2,m)
    n=max(2,n)
    
    # Se crea el grafo    
    gph = graph()
    
    
    for i in range(m):
        for j in range(n):
            
            # Se agregan mxn nodos al grafo
            nnode = i * m + j
            gph.AddNode(nnode)
            
            # Se agregan las aristas para el nodo n(i,j) hacia n(i+1,j) y hacia el nodo n(i,j+1)
            if i < m-1:
                nnode_1 = (i + 1) * m + j
                a, name = gph.AddEdge(nnode, nnode_1)
                if a == 1:
                    edg = gph.getEdge(name)
                    edg.weight = random.randint(1,100)

            if j < n-1:
                nnode_2 = i*m + (j+1)
                a, name = gph.AddEdge(nnode, nnode_2)
                if a == 1:
                    edg = gph.getEdge(name)
                    edg.weight = random.randint(1,100)
     
    # Se regresa el grafo generado
    return gph


def ErdosRenyi_Graph(n, m, directed = False, auto = False):
    
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    
    """
    # Validación de parámetros
    if m < n-1:
        m = n-1
    
    if n <= 0:
        n = 1
    
    # Se crea el grafo
    gph = graph()
    
    # Se agregan los n nodos al grafo
    for i in range(n):
        gph.AddNode(i)
        
    # Se agregan las m aristas al grafo
    for i in range(m):
        
        # Se selecciona un par de nodos al azar
        n0 = random.randint(0,n-1)
        n1 = random.randint(0, n-1)
        
        # Si los nodos seleccionados son diferentes se agrega la arista
        if n0 != n1:
            a, name = gph.AddEdge(n0, n1)
            if a == 1:
                edg = gph.getEdge(name)
                edg.weight = random.randint(1,100)
    # Se regresa el grafo generado      
    return gph


def Gilbert_Graph(n, p, directed = False, auto = False):
    
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    
    """
    # Validación de parámetros
    if n <= 0:
        n = 1
    
    if p < 0:
        p = 0
    elif p > 1:
        p = 1
    
    # Se crea el grafo
    gph = graph()
    
    # Se agregan los n nodos al grafo
    for i in range(n):
        gph.AddNode(i)
    
    # Se agregan las aristas al grafo según el random generado y la probabilidad deseada
    for i in range(n):
        for j in range(n):
            
            if random.random() < p:
                if j != i:
                    a, name = gph.AddEdge(i, j)
                    if a == 1:
                        edg = gph.getEdge(name)
                        edg.weight = random.randint(1,100)

                    
    # Se regresa el grafo generado
    return gph


def geographic_Graph(n, r, directed = False, auto = False):
    
    """
    Genera grafo aleatorio con el modelo geográfico simple
    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear un nodo (0, 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
     
    """
    # Validación de parámetros
    if n <= 0:
        n = 1
    
    if r < 0:
        r = 0
    elif r > 1:
        r = 1
    
    # Se crea el grafo 
    gph = graph()
    
    # Se agregan los n nodos al grafo
    for i in range(n):
        # Si el nodo fue agregado se le asignan coordenadas aleatorias para x y y
        if gph.AddNode(i) == 1:
            node = gph.getNode(i)
            #print(str(node))
            node.xpos = random.random()
            node.ypos = random.random()
    
    # Se agrega la arista al grafo si la distancia entre estos es menor o igual a la ingresada como parámetro
    for i in range(n):
        for j in range(n):
            if i != j:
                d = distance(gph.getNode(i), gph.getNode(j))
                
                if d <= r:
                    a, name = gph.AddEdge(i, j)
                    if a == 1:
                        edg = gph.getEdge(name)
                        edg.weight = random.randint(1,100)
                    
    # Se regresa el grafo generado
    return gph


def BarabasiAlbert_Graph(n, d, directed = False, auto = False):
    
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    
    """
    
    # Validación de parámetros
    if n <= 0:
        n = 1
    
    if d <= 1:
        d = 2
    
    # Se crea el grafo
    gph = graph()
    
    # Se agrega el primer nodo
    gph.AddNode(0)
    
    # Se agregan los nodos de 1 hasta n
    for i in range(1,n):
        gph.AddNode(i)
        for j in range(i):
            #Se recupera cada nodo
            node = gph.getNode(j)
            # Se obtiene el grado de cada nodo
            degree = node.dg
            
            # Se calcula la probabilidad
            p = 1 - degree / d
            
            # Si el random generado es menor a la probabilidad calculada, se agrega la arista
            if random.random() < p:
                if j != i:  
                    a, name = gph.AddEdge(i, j)  
                    if a == 1:
                        edg = gph.getEdge(name)
                        edg.weight = random.randint(1,100)              
                
    # Se regresa el nodo generado
    return gph


def DorogovtsevMendes_Graph(n, directed = False):
    
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    
    """
    # Validación de parámetros
    if n < 3:
        n = 3
    
    # Se crea el grafo
    gph = graph()
    
    # Se agregan los primeros tres nodos al grafo
    for i in range(3):
        gph.AddNode(i)
    
    # Se agregan las aristas entre los primeros tres nodos formando un triángulo
    for i in range(3):
        if i < 2:
            a, name = gph.AddEdge(i, i+1)
            if a == 1:
                edg = gph.getEdge(name)
                edg.weight = random.randint(1,100)
        else:
            a, name = gph.AddEdge(i, i-i)
            if a == 1:
                edg = gph.getEdge(name)
                edg.weight = random.randint(1,100)
            
    # Se agregan los nodos desde 3 hasta n
    for i in range(3, n):
        gph.AddNode(i)
        
        # Se elige una arista existente al azar
        r_edge = random.randrange(0, i)
        
        # Se crean las aristas entre el nodo nuevo y los extremos de la arista seleccionada
        e = gph.getEdge_n(r_edge)
        n0 = int(e.source)
        n1 = int(e.target)
        a, name1 = gph.AddEdge(i, n0)
        b, name2 = gph.AddEdge(i, n1)
        
        edg1 = gph.getEdge(name1)
        edg1.weight = random.randint(1,100)
        edg2 = gph.getEdge(name2)
        edg2.weight = random.randint(1,100)


    # Se regresa el nodo generado
    return gph