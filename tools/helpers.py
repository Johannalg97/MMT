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
    for i, v in enumerate(data):
        if v.get('type').startswith('tabulate'):
            for j in v['data'].split('\n'):
                tupla = tuple(j.split())
                aux.append(tupla)
    return aux
