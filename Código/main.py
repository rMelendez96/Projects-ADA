# -*- coding: utf-8 -*-
"""
PROYECTO 03
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio
Mayo 2022
GENERACIÓN DE GRAFOS
IMPLEMENTACIÓN DE ALGORITMO DIJKSTRA
"""

import Algorithms

if __name__ == '__main__':
    
    # Para cada algoritmo de generación de grafos se muestran y generan 2 grafos
    # con 70 y 500 nodos respectivamente y diferentes parámetros dependiendo
    # del algoritmo empleado
    
    # Para cada grafo generado se generan los grafos correspondientes con el algoritmo de Dijkstra
    
    #Grafos de Malla
    #Pocos nodos
    print("Grafo de Malla 70 Nodos")
    gph_m1 = Algorithms.grid_Graph(10, 7)
    gph_m1.showGraph()
    gph_m1.fileGraphViz('gridGraph')
    print("Dijkstra")
    dk_gph_m1, d = gph_m1.Dijkstra(0)
    dk_gph_m1.showGraph()
    dk_gph_m1.fileGraphViz_Dijkstra("gridGraph_Dijkstra", d)

    #Muchos Nodos
    print("Grafo de Malla 500 Nodos")
    gph_m2 = Algorithms.grid_Graph(25, 20)
    gph_m2.showGraph()
    gph_m2.fileGraphViz('gridGraph')
    print("Dijkstra")
    dk_gph_m2, d = gph_m2.Dijkstra(0)
    dk_gph_m2.showGraph()
    dk_gph_m2.fileGraphViz_Dijkstra("gridGraph_Dijkstra", d)

    
    #Grafos Erdos-Renyi
    #Pocos nodos
    print("Grafo Erdos-Renyi 70 Nodos")
    gph_er1 = Algorithms.ErdosRenyi_Graph(70, 90)
    gph_er1.showGraph()
    gph_er1.fileGraphViz('Erdos-Renyi_Graph')
    print("Dijkstra")
    dk_gph_er1, d = gph_er1.Dijkstra(0)
    dk_gph_er1.showGraph()
    dk_gph_er1.fileGraphViz_Dijkstra("Erdos-Renyi_Graph_Dijkstra", d) 

    #Muchos nodos
    print("Grafo Erdos-Renyi 500 Nodos")
    gph_er2 = Algorithms.ErdosRenyi_Graph(500, 650)
    gph_er2.showGraph()
    gph_er2.fileGraphViz('Erdos-Renyi_Graph')
    print("Dijkstra")
    dk_gph_er2, d = gph_er2.Dijkstra(0)
    dk_gph_er2.showGraph()
    dk_gph_er2.fileGraphViz_Dijkstra("Erdos-Renyi_Graph_Dijkstra", d) 
    
    
    #Grafos Gilbert
    # Pocos nodos
    print("Grafo Gilbert 70 Nodos")
    gph_g1 = Algorithms.Gilbert_Graph(70, 0.5)
    gph_g1.showGraph()
    gph_g1.fileGraphViz('Gilbert_Graph')
    print("Dijkstra")
    dk_gph_g1, d = gph_g1.Dijkstra(0)
    dk_gph_g1.showGraph()
    dk_gph_g1.fileGraphViz_Dijkstra("Gilbert_Graph_Dijkstra", d) 
    
    
    # Muchos nodos
    print("Grafo Gilbert 500 Nodos")
    gph_g2 = Algorithms.Gilbert_Graph(500, 0.7)
    gph_g2.showGraph()
    gph_g2.fileGraphViz('Gilbert_Graph')
    print("Dijkstra")
    dk_gph_g2, d = gph_g2.Dijkstra(0)
    dk_gph_g2.showGraph()
    dk_gph_g2.fileGraphViz_Dijkstra("Gilbert_Graph_Dijkstra", d) 
    
    #Grafos Geográfico Simple
    #Pocos nodos
    print("Grafo Geográfico 30 Nodos")
    gph_gs1 = Algorithms.geographic_Graph(70, 0.4)
    gph_gs1.showGraph()
    gph_gs1.fileGraphViz('geographicGraph')
    print("Dijkstra")
    dk_gph_gs1, d = gph_gs1.Dijkstra(0)
    dk_gph_gs1.showGraph()
    dk_gph_gs1.fileGraphViz_Dijkstra("geographicGraph_Dijkstra", d) 
    
    # Muchos nodos
    print("Grafo Geográfico 500 Nodos")
    gph_gs2 = Algorithms.geographic_Graph(500, 0.4)
    gph_gs2.showGraph()
    gph_gs2.fileGraphViz('geographicGraph')
    print("Dijkstra")
    dk_gph_gs2, d = gph_gs2.Dijkstra(0)
    dk_gph_gs2.showGraph()
    dk_gph_gs2.fileGraphViz_Dijkstra("geographicGraph_Dijkstra", d) 
    
    #Grafos Barabasi-Albert
    #Pocos nodos
    print("Grafo Barabasi-Albert 30 Nodos")
    gph_ba1 = Algorithms.BarabasiAlbert_Graph(70, 5)
    gph_ba1.showGraph()
    gph_ba1.fileGraphViz('Barabasi-Albert_Graph')
    print("Dijkstra")
    dk_gph_ba1, d = gph_ba1.Dijkstra(0)
    dk_gph_ba1.showGraph()
    dk_gph_ba1.fileGraphViz_Dijkstra("Barabasi-Albert_Graph_Dijkstra", d) 

    # Muchos nodos
    print("Grafo Barabasi-Albert 500 Nodos")
    gph_ba2 = Algorithms.BarabasiAlbert_Graph(500, 5)
    gph_ba2.showGraph()
    gph_ba2.fileGraphViz('Barabasi-Albert_Graph')
    print("Dijkstra")
    dk_gph_ba2, d = gph_ba2.Dijkstra(0)
    dk_gph_ba2.showGraph()
    dk_gph_ba2.fileGraphViz_Dijkstra("Barabasi-Albert_Graph_Dijkstra", d) 
    
    
    #Grafos Dorogovtsev-Mendes
    #Pocos nodos
    print("Grafo Dorogovtsev-Mendes 30 Nodos")
    gph_dm1 = Algorithms.DorogovtsevMendes_Graph(70)
    gph_dm1.showGraph()
    gph_dm1.fileGraphViz('Dorogovtsev-Mendes_Graph')
    print("Dijkstra")
    dk_gph_dm1, d = gph_dm1.Dijkstra(0)
    dk_gph_dm1.showGraph()
    dk_gph_dm1.fileGraphViz_Dijkstra("Dorogovtsev-Mendes_Graph_Dijkstra", d) 

    # Muchos nodos
    print("Grafo Dorogovtsev-Mendes 500 Nodos")
    gph_dm2 = Algorithms.DorogovtsevMendes_Graph(500)
    gph_dm2.showGraph()
    gph_dm2.fileGraphViz('Dorogovtsev-Mendes_Graph')
    print("Dijkstra")
    dk_gph_dm2, d = gph_dm2.Dijkstra(0)
    dk_gph_dm2.showGraph()
    dk_gph_dm2.fileGraphViz_Dijkstra("Dorogovtsev-Mendes_Graph_Dijkstra", d) 
   