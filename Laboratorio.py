import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import numpy as np

A = [1,2,3]
B = ["a","b","c"]
D = [1,2,3,"a","b","c"]
C = [A, B]
U = [1,2,3,4,5,6,7,8,9,10,"a","b","c"]

def union(conjuntos): 
    resultado = []
    for conjunto in conjuntos:
        for elemento in conjunto:
            if elemento not in resultado:
                resultado.append(elemento)
    return resultado

def interseccion(conjuntos): 
    resultado = []
    for elemento in conjuntos[0]:
        for conjunto in conjuntos[1:]:
            if elemento not in conjunto:
                break
        else:
            resultado.append(elemento)
    return resultado

def diferencia(A,B):
    resultado = []
    for elemento in A:
        if elemento not in B:
            resultado.append(elemento)
    return resultado

def complemento(universo,conjunto):
    return diferencia(universo,conjunto)

def cardinalidad(conjunto):
    return "El conjunto tiene una carnidalidad de: "+len(conjunto)

def isSubconjunto(A,B):
    for elemento in A:
        if elemento not in B:
            return "El primer conjunto no es subconjunto del segundo"
    return "El primer conjunto es subconjunto del segundo"

def disjuntos(A,B):
    for elemento in A:
        if elemento in B:
            return "Los conjuntos no son disjuntos"
    return "Los conjuntos son disjuntos"
    
def graficar_venn_con_elementos(listas):
    # Convertir listas a conjuntos
    conjuntos = [set(lista) for lista in listas]
    
    # Crear el diagrama de Venn adecuado
    if len(conjuntos) == 2:
        diagram = venn2(conjuntos, set_labels=('Conjunto 1', 'Conjunto 2'))
    elif len(conjuntos) == 3:
        diagram = venn3(conjuntos, set_labels=('Conjunto 1', 'Conjunto 2', 'Conjunto 3'))
    else:
        print("Máximo 3 conjuntos permitidos.")
        return
    
    plt.show()
    
graficar_venn_con_elementos([A,B])

