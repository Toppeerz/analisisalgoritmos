import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

def format_set_for_venn(conjunto):
    return ", ".join(map(str, conjunto))

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

def diferencia(A, B):
    resultado = []
  
    for elemento in A:
        if elemento not in B:
            resultado.append(elemento)
      
    return resultado

def complemento(universo, conjunto):
    return diferencia(universo, conjunto)

root = tk.Tk()

union_label = tk.Label(root) 
inter_label = tk.Label(root)
diff_label = tk.Label(root)
comp_label = tk.Label(root)

def on_button_click():
    # Obtener elementos de A, B y C desde las entradas de la interfaz gráfica
    A = entry_A.get().strip().split(',')
    B = entry_B.get().strip().split(',')
    C = entry_C.get().strip().split(',')
    
    # Crear copias de las listas originales para evitar modificaciones inesperadas
    A_list = A.copy()
    B_list = B.copy()
    C_list = C.copy()

    # Imprimir los resultados de las operaciones en la consola
    print("Unión:")
    union_result = union([A, B, C])
    print(union_result)

    print("\nIntersección:")
    interseccion_result = interseccion([A, B, C])
    print(interseccion_result) 

    print("\nDiferencia:")  
    diferencia_result = diferencia(A, B)
    print(diferencia_result)

    print("\nComplemento:")
    total = union([A, B, C])
    complemento_result = complemento(total, A) 
    print(complemento_result)

    # Configurar las etiquetas con los resultados en la interfaz gráfica
    union_label.config(text="Unión: " + str(union_result))
    inter_label.config(text="Intersección: " + str(interseccion_result))
    diff_label.config(text="Diferencia: " + str(diferencia_result))
    comp_label.config(text="Complemento: " + str(complemento_result))

    union_label.pack()
    inter_label.pack()
    diff_label.pack()
    comp_label.pack()

    # Realizar operaciones y configurar el diagrama de Venn
    AB = list(set(A_list) & set(B_list))
    BC = list(set(B_list) & set(C_list))
    AC = list(set(A_list) & set(C_list))
    ABC = list(set(A_list) & set(B_list) & set(C_list))
    primero = list(set(diferencia(A_list, AB)) - set(AC))
    segundo = list(set(diferencia(B_list, AB)) - set(BC))
    tercero = list(set(diferencia(C_list, AC)) - set(BC))
    cuarto = list(set(AB) - set(ABC))
    quinto = list(set(BC) - set(ABC))
    sexto = list(set(AC) - set(ABC))

    # Crear el diagrama de Venn
    v = venn3(subsets=(len(A_list) - len(AB) - len(AC), len(B_list) - len(AB) - len(BC), len(BC), 
                      len(A_list) - len(AC) - len(AB), len(C_list) - len(AC) - len(BC),
                      len(AC), len(ABC)),
              set_labels=('A', 'B', 'C'))

    # Configurar las etiquetas en el diagrama de Venn
    v.get_label_by_id('100').set_text('\n'.join(map(str, primero)) if primero else "Conjunto vacío")
    v.get_label_by_id('010').set_text('\n'.join(map(str, segundo)) if segundo else "Conjunto vacío")
    v.get_label_by_id('001').set_text('\n'.join(map(str, tercero)) if tercero else "Conjunto vacío")
    v.get_label_by_id('110').set_text('\n'.join(map(str, cuarto)) if cuarto else "Conjunto vacío")
    v.get_label_by_id('011').set_text('\n'.join(map(str, quinto)) if quinto else "Conjunto vacío")
    v.get_label_by_id('101').set_text('\n'.join(map(str, sexto)) if sexto else "Conjunto vacío")
    v.get_label_by_id('111').set_text('\n'.join(map(str, ABC)) if ABC else "Conjunto vacío")

    # Guardar el diagrama de Venn como una imagen
    plt.savefig('diagrama_venn_ABC.png')
    plt.clf()

    print("Diagrama de Venn de 3 conjuntos generado")

# Crear la ventana principal
root = tk.Tk()

# Crear campos de entrada y botón en la interfaz gráfica
entry_A_label = tk.Label(root, text="Ingrese elementos de A (separado por comas):")
entry_A_label.pack()
entry_A_var = tk.StringVar()
entry_A = tk.Entry(root, textvariable=entry_A_var)
entry_A.pack()

entry_B_label = tk.Label(root, text="Ingrese elementos de B (separado por comas):")
entry_B_label.pack()
entry_B_var = tk.StringVar() 
entry_B = tk.Entry(root, textvariable=entry_B_var)
entry_B.pack()

entry_C_label = tk.Label(root, text="Ingrese elementos de C (separado por comas):")
entry_C_label.pack()
entry_C_var = tk.StringVar()
entry_C = tk.Entry(root, textvariable=entry_C_var)
entry_C.pack()

button = tk.Button(root, text="Calcular", command=on_button_click)
button.pack()

# Iniciar el bucle principal
root.mainloop()
