import numpy as np

def recibir_lista(Lista_de_tuplas):
    """Esta funcion recibe la lista de tuplas [(Lambda, n , k),...] de cada archivo 
    que eliga el usario, para separar, lambda, n y k por listas"""
    Lambda = []
    n = []
    k = []
    for tupla in Lista_de_tuplas:
        Lambda.append (tupla[0])
        n.append (tupla [1])
        k.append (tupla [2])
    return [Lambda, n, k]

def interpolacion(Lista, Rango):
    """Esta funcion me realiza la interpolaciòn  """
    X = np.linspace (Rango [0], Rango [1], 1)
    Y_n = np.interp (X, Lista [0], Lista [1])
    Y_k = Y = np.interp (X, Lista [0], Lista [2])
    return [X, Y_n, Y_k]
    



#prueba
if __name__ == '__main__':
    b = [(1, 2, 3), (2, 4, 6), (3, 6, 9)]
    c = recibir_lista(b)
    print(c)
    d = interpolacion(c, [1.5, 1.5])
    print(d)


    








