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
    
def interpolacion(Lista, w_i=0.0, w_f=0.0, respuesta="angular"): 
    """Esta funcion me realiza la interpolaciòn  """
    
    if respuesta == "angular":
        w_f = w_i
        pasos = 1
    
    elif respuesta == "espectral":
        pasos = 200
        if not (w_i < w_f):
            raise ValueError("La Longitud de onada inicial debe ser menor que longitud de onda final ")
    
    x = np.linspace(w_i, w_f, pasos)
    y_n = np.interp(x, Lista[0], Lista[1])
    y_k = Y = np.interp(x, Lista [0], Lista [2])

    return x, y_n, y_k 
    




#prueba
if __name__ == '__main__':
    b = [(1, 2), (2, 4), (3, 6)]
    c = recibir_lista(b)
    print(c)
    print(type(c))
    #d = interpolacion(c, [1.5, 1.5])
    #print(d)


    








