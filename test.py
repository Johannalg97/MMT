#!/usr/bin/env python3
from tools.helpers import *
from functions.interpolacion import *
from settings import DB_DIR


archivo = 'AMTIR-1.yml'
ruta = '{}glass/ami/{}'.format(DB_DIR, archivo)
longitud_onda = 1.2    # dato ingresado por el usurio
# leer archivo .yaml
d = get_schema_from_yaml(ruta=ruta)
# convierte a tuplas datos
c = get_nk(d)           # array con n k en tupla 
print(c)


