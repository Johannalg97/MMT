import numpy as np

def recibir_lista(lista_de_tuplas):
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
            w.append(i[0])
            n.append(i[1])
            k.append(0)

        elif len(i) == 3:
            w.append(i[0])
            n.append(i[1])
            k.append(i[2])
    
    return w, n, k 
    
def interpolacion(Lista, Rango):
    """Esta funcion me realiza la interpolaciòn  """
    X = np.linspace (Rango [0], Rango [1], 1)
    Y_n = np.interp (X, Lista [0], Lista [1])
    Y_k = Y = np.interp (X, Lista [0], Lista [2])
    return [X, Y_n, Y_k]
    



#prueba
if __name__ == '__main__':
    b = [(1, 2), (2, 4), (3, 6)]
    c = recibir_lista(b)
    print(c)
    print(type(c))
    #d = interpolacion(c, [1.5, 1.5])
    #print(d)


    








