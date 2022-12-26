import yaml



# funtion tools
def get_schema_from_yaml(ruta=''):
    """ funcion lee archivo yaml """
    data_yaml = {}
    try:
        with open(ruta) as file:
            data_yaml = yaml.load(file, Loader=yaml.FullLoader)
    except Exception:
        data_yaml = None
    return data_yaml

def get_nk(d):
    """ convierte data 
        return - lista con tuplas [(lambda, n, k )]
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
    a = initial_value
    incremento = (final_value - initial_value) / pasos
    list_theta = []
    while len(list_theta) < pasos:
        a = a + incremento
        list_theta.append(a) 
    return list_theta
