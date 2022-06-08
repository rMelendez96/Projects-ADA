# -*- coding: utf-8 -*-
"""
PROYECTO 04
Unidad: Diseño y Análisis de Algoritmos
Alumno: Raquel Eugenia Meléndez Zamudio
Junio 2022
GENERACIÓN DE GRAFOS
IMPLEMENTACIÓN DE ALGORITMOS KRUSKAL (DIRECTO E INVERSO) y PRIM
"""

import Algorithms

if __name__ == '__main__':
    
    # Para cada algoritmo de generación de grafos se muestran y generan 2 grafos
    # con 70 y 500 nodos respectivamente y diferentes parámetros dependiendo
    # del algoritmo empleado
    
    # Para cada grafo generado se generan los árboles de expansión mínima correspondientes 
    # con los algoritmos Kurskal (Directo e Inverso) y Prim
    
    #Grafos de Malla
    #Pocos nodos
    print("Grafo de Malla 70 Nodos")
    gph_m1 = Algorithms.grid_Graph(10, 7)
    gph_m1.fileGraphViz('gridGraph')
    mst_kd = gph_m1.KruskalD()
    mst_kd.fileGraphViz('gridGraph_KruskalD')
    mst_ki = gph_m1.KruskalI()
    mst_ki.fileGraphViz('gridGraph_KruskalI')
    mst_p = gph_m1.Prim()
    mst_p.fileGraphViz('gridGraph_Prim')

    #Muchos Nodos
    print("Grafo de Malla 500 Nodos")
    gph_m2 = Algorithms.grid_Graph(25, 20)
    gph_m2.fileGraphViz('gridGraph')
    mst_kd = gph_m2.KruskalD()
    mst_kd.fileGraphViz('gridGraph_KruskalD')
    mst_ki = gph_m2.KruskalI()
    mst_ki.fileGraphViz('gridGraph_KruskalI')
    mst_p = gph_m2.Prim()
    mst_p.fileGraphViz('gridGraph_Prim')

    
    #Grafos Erdos-Renyi
    #Pocos nodos
    print("Grafo Erdos-Renyi 70 Nodos")
    gph_er1 = Algorithms.ErdosRenyi_Graph(70, 90)
    gph_er1.fileGraphViz('Erdos-Renyi_Graph')
    mst_kd = gph_er1.KruskalD()
    mst_kd.fileGraphViz('Erdos-Renyi_Graph_KruskalD')
    mst_ki = gph_er1.KruskalI()
    mst_ki.fileGraphViz('Erdos-Renyi_Graph_KruskalI')
    mst_p = gph_er1.Prim()
    mst_p.fileGraphViz('Erdos-Renyi_Graph_Prim')

    #Muchos nodos
    print("Grafo Erdos-Renyi 500 Nodos")
    gph_er2 = Algorithms.ErdosRenyi_Graph(500, 650)
    gph_er2.fileGraphViz('Erdos-Renyi_Graph')
    mst_kd = gph_er2.KruskalD()
    mst_kd.fileGraphViz('Erdos-Renyi_Graph_KruskalD')
    mst_ki = gph_er2.KruskalI()
    mst_ki.fileGraphViz('Erdos-Renyi_Graph_KruskalI')
    mst_p = gph_er2.Prim()
    mst_p.fileGraphViz('Erdos-Renyi_Graph_Prim')
    
    
    #Grafos Gilbert
    # Pocos nodos
    print("Grafo Gilbert 70 Nodos")
    gph_g1 = Algorithms.Gilbert_Graph(70, 0.5)
    gph_g1.fileGraphViz('Gilbert_Graph')
    mst_kd = gph_g1.KruskalD()
    mst_kd.fileGraphViz('Gilbert_Graph_KruskalD')
    mst_ki = gph_g1.KruskalI()
    mst_ki.fileGraphViz('Gilbert_Graph_KruskalI')
    mst_p = gph_g1.Prim()
    mst_p.fileGraphViz('Gilbert_Graph_Prim')
    
    
    # # Muchos nodos
    print("Grafo Gilbert 200 Nodos")
    gph_g2 = Algorithms.Gilbert_Graph(200, 0.7)
    gph_g2.fileGraphViz('Gilbert_Graph')
    mst_kd = gph_g2.KruskalD()
    mst_kd.fileGraphViz('Gilbert_Graph_KruskalD')
    mst_ki = gph_g2.KruskalI()
    mst_ki.fileGraphViz('Gilbert_Graph_KruskalI')
    mst_p = gph_g2.Prim()
    mst_p.fileGraphViz('Gilbert_Graph_Prim')
    
    #Grafos Geográfico Simple
    #Pocos nodos
    print("Grafo Geográfico 70 Nodos")
    gph_gs1 = Algorithms.geographic_Graph(70, 0.4)
    gph_gs1.fileGraphViz('geographicGraph')
    mst_kd = gph_gs1.KruskalD()
    mst_kd.fileGraphViz('geographicGraph_KruskalD')
    mst_ki = gph_gs1.KruskalI()
    mst_ki.fileGraphViz('geographicGraph_KruskalI')
    mst_p = gph_gs1.Prim()
    mst_p.fileGraphViz('geographicGraph_Prim')
    
    # Muchos nodos
    print("Grafo Geográfico 200 Nodos")
    gph_gs2 = Algorithms.geographic_Graph(200, 0.4)
    gph_gs2.fileGraphViz('geographicGraph')
    mst_kd = gph_gs2.KruskalD()
    mst_kd.fileGraphViz('geographicGraph_KruskalD')
    mst_ki = gph_gs2.KruskalI()
    mst_ki.fileGraphViz('geographicGraph_KruskalI')
    mst_p = gph_gs2.Prim()
    mst_p.fileGraphViz('geographicGraph_Prim')
    
    #Grafos Barabasi-Albert
    #Pocos nodos
    print("Grafo Barabasi-Albert 70 Nodos")
    gph_ba1 = Algorithms.BarabasiAlbert_Graph(70, 5)
    gph_ba1.fileGraphViz('Barabasi-Albert_Graph')
    mst_kd = gph_ba1.KruskalD()
    mst_kd.fileGraphViz('Barabasi-Albert_Graph_KruskalD')
    mst_ki = gph_ba1.KruskalI()
    mst_ki.fileGraphViz('Barabasi-Albert_Graph_KruskalI')
    mst_p = gph_ba1.Prim()
    mst_p.fileGraphViz('Barabasi-Albert_Graph_Prim')

    # Muchos nodos
    print("Grafo Barabasi-Albert 500 Nodos")
    gph_ba2 = Algorithms.BarabasiAlbert_Graph(500, 5)
    gph_ba2.fileGraphViz('Barabasi-Albert_Graph')
    mst_kd = gph_ba2.KruskalD()
    mst_kd.fileGraphViz('Barabasi-Albert_Graph_KruskalD')
    mst_ki = gph_ba2.KruskalI()
    mst_ki.fileGraphViz('Barabasi-Albert_Graph_KruskalI')
    mst_p = gph_ba2.Prim()
    mst_p.fileGraphViz('Barabasi-Albert_Graph_Prim')
    
    
    #Grafos Dorogovtsev-Mendes
    #Pocos nodos
    print("Grafo Dorogovtsev-Mendes 70 Nodos")
    gph_dm1 = Algorithms.DorogovtsevMendes_Graph(70)
    gph_dm1.fileGraphViz('Dorogovtsev-Mendes_Graph')
    mst_kd = gph_dm1.KruskalD()
    mst_kd.fileGraphViz('Dorogovtsev-Mendes_Graph_KruskalD')
    mst_ki = gph_dm1.KruskalI()
    mst_ki.fileGraphViz('Dorogovtsev-Mendes_Graph_KruskalI')
    mst_p = gph_dm1.Prim()
    mst_p.fileGraphViz('Dorogovtsev-Mendes_Graph_Prim')

    #Muchos nodos
    print("Grafo Dorogovtsev-Mendes 500 Nodos")
    gph_dm2 = Algorithms.DorogovtsevMendes_Graph(500)
    gph_dm2.fileGraphViz('Dorogovtsev-Mendes_Graph')
    mst_kd = gph_dm2.KruskalD()
    mst_kd.fileGraphViz('Dorogovtsev-Mendes_Graph_KruskalD')
    mst_ki = gph_dm2.KruskalI()
    mst_ki.fileGraphViz('Dorogovtsev-Mendes_Graph_KruskalI')
    mst_p = gph_dm2.Prim()
    mst_p.fileGraphViz('Dorogovtsev-Mendes_Graph_Prim')
   