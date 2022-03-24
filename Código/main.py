# -*- coding: utf-8 -*-
"""
PROYECTO 01
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio

Marzo 2022

GENERACIÓN DE GRAFOS

"""

import Algorithms

if __name__ == '__main__':
    
    # Para cada algoritmo de generación de grafos se muestran y generan 3 grafos
    # con 30, 100 y 500 nodos respectivamente y diferentes parámetros dependiendo
    # del algoritmo empleado
    
    #Grafos de Malla
    #30 nodos
    gph_m1 = Algorithms.grid_Graph(10, 3)
    gph_m1.showGraph()
    gph_m1.fileGraphViz('gridGraph')
    
    #100 nodos
    gph_m2 = Algorithms.grid_Graph(10, 10)
    gph_m2.showGraph()
    gph_m2.fileGraphViz('gridGraph')
    
    #500 nodos
    gph_m3 = Algorithms.grid_Graph(25, 20)
    gph_m3.showGraph()
    gph_m3.fileGraphViz('gridGraph')
    
    
    #Grafos Erdos-Renyi
    #30 nodos
    gph_er1 = Algorithms.ErdosRenyi_Graph(30, 50)
    gph_er1.showGraph()
    gph_er1.fileGraphViz('Erdos-Renyi_Graph')
    
    #100 nodos
    gph_er2 = Algorithms.ErdosRenyi_Graph(100, 120)
    gph_er2.showGraph()
    gph_er2.fileGraphViz('Erdos-Renyi_Graph')
    
    #500 nodos
    gph_er3 = Algorithms.ErdosRenyi_Graph(500, 650)
    gph_er3.showGraph()
    gph_er3.fileGraphViz('Erdos-Renyi_Graph')
    
    
    #Grafos Gilbert
    #30 nodos
    gph_g1 = Algorithms.Gilbert_Graph(30, 0.5)
    gph_g1.showGraph()
    gph_g1.fileGraphViz('Gilbert_Graph')
    
    #100 nodos
    gph_g2 = Algorithms.Gilbert_Graph(100, 0.3)
    gph_g2.showGraph()
    gph_g2.fileGraphViz('Gilbert_Graph')
    
    #500 nodos
    gph_g3 = Algorithms.Gilbert_Graph(500, 0.7)
    gph_g3.showGraph()
    gph_g3.fileGraphViz('Gilbert_Graph')
    
    
    #Grafos Geográfico Simple
    #30 nodos
    gph_gs1 = Algorithms.geographic_Graph(30, 0.4)
    gph_gs1.showGraph()
    gph_gs1.fileGraphViz('geographicGraph')
    
    #100 nodos
    gph_gs2 = Algorithms.geographic_Graph(100, 0.5)
    gph_gs2.showGraph()
    gph_gs2.fileGraphViz('geographicGraph')
    
    #500 nodos
    gph_gs3 = Algorithms.geographic_Graph(500, 0.4)
    gph_gs3.showGraph()
    gph_gs3.fileGraphViz('geographicGraph')
    
    
    #Grafos Barabasi-Albert
    #30 nodos
    gph_ba1 = Algorithms.BarabasiAlbert_Graph(30, 5)
    gph_ba1.showGraph()
    gph_ba1.fileGraphViz('Barabasi-Albert_Graph')
    
    #100 nodos
    gph_ba2 = Algorithms.BarabasiAlbert_Graph(100, 5)
    gph_ba2.showGraph()
    gph_ba2.fileGraphViz('Barabasi-Albert_Graph')
    
    #500 nodos
    gph_ba3 = Algorithms.BarabasiAlbert_Graph(500, 5)
    gph_ba3.showGraph()
    gph_ba3.fileGraphViz('Barabasi-Albert_Graph')
    
    
    #Grafos Dorogovtsev-Mendes
    #30 nodos
    gph_dm1 = Algorithms.DorogovtsevMendes_Graph(30)
    gph_dm1.showGraph()
    gph_dm1.fileGraphViz('Dorogovtsev-Mendes_Graph')
    
    #100 nodos
    gph_dm2 = Algorithms.DorogovtsevMendes_Graph(100)
    gph_dm2.showGraph()
    gph_dm2.fileGraphViz('Dorogovtsev-Mendes_Graph')
    
    #500 nodos
    gph_dm3 = Algorithms.DorogovtsevMendes_Graph(500)
    gph_dm3.showGraph()
    gph_dm3.fileGraphViz('Dorogovtsev-Mendes_Graph')
    