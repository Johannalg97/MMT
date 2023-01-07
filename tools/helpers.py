import yaml
from mpmath import sqrt



# funtion tools
def get_schema_from_yaml(ruta=''):
    """ This funtion read the file yaml """
    data_yaml = {}
    try:
        with open(ruta) as file:
            data_yaml = yaml.load(file, Loader=yaml.FullLoader)
    except Exception:
        data_yaml = None
    return data_yaml

def get_nk(d):
    """  
        This funtion return a list of tuplas: [(lambda, n, k )]
    """
    aux = []
    data = d['DATA']
    for j, v in enumerate(data):
        if v.get('type').startswith('tabulate'):
            for j in v['data'].split('\n'):
                tupla = tuple(j.split())
                aux.append(tupla)
    return aux

def get_list_theta(initial_value, final_value, pasos): 
    """
    function that returns a list with the list of angles 
    or wavelengths that the program will traverse. 

    """
    a = initial_value
    incremento = (final_value - initial_value) / pasos
    list = []
    while len(list) < pasos:
        a = a + incremento
        list.append(a) 
    return list

def get_nk_from_dielectric_fuction(dielectric_function):
    """
    This funtion:
    *Calculate los valores de n y k from the dielectic funtion
    *Receives the valuos of the dielectic funtion (epsilon_1 and epsilon_2)
    * Retur a list with two values n and k
    """

    a = sqrt(dielectric_function[0]**2 + dielectric_function[1]**2)
    n = sqrt((dielectric_function[0] + a )/2 )
    k = sqrt((-dielectric_function[0] + a )/2 ) 
    return float(n), float(k)




    



    