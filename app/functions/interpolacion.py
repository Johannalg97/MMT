import numpy as np

def get_list(lista_de_tuplas):
    """
    Esta funcion recibe la lista de tuplas [(Lambda, n , k),...] de cada archivo 
    que eliga el usario, para separar, lambda, n y k por listas

    lista_de_tuplas - list []

    return:
    """
    w = []
    n = []
    k = []
    
    for i in lista_de_tuplas:
        if len(i) == 2:
            w.append(float(i[0]))
            n.append(float(i[1]))
            k.append(0)

        elif len(i) == 3:
            w.append(float(i[0]))
            n.append(float(i[1]))
            k.append(float(i[2]))
    
        return w, n, k 
    
def interpolation(lista, w_i=0.0, w_f=0.0, respuesta="angular"): 
    """Esta funcion me realiza la interpolaciòn  """
    
    if respuesta == "angular":
        w_f = w_i
        pasos = 1
    
    elif respuesta == "espectral":
        pasos = 200
        if not (w_i < w_f):
            raise ValueError("La Longitud de onada inicial debe ser menor que longitud de onda final ")
    
    x = np.linspace(w_i, w_f, pasos)
    y_n = np.interp(x, lista[0], lista[1])
    y_k = Y = np.interp(x, lista [0], lista [2])

    return float(x), float(y_n), float(y_k)
    








    








