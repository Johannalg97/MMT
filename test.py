#!/usr/bin/env python3
from tools.helpers import *
from functions.interpolacion import *
from functions.transfer_matrix_method import TransferMatrixMethod, TranferMatrixMethodHelper
from settings import DB_DIR






#Datos que ingresa el usuario 

w_i = 0.6    # longitud de onda inicial


#obtener ruta de archivos 

archivo = 'AMTIR-1.yml'
ruta_1 = '{}glass/ami/{}'.format(DB_DIR, archivo)
archivo_2 = 'Babar.yml'
ruta_2 = '{}main/Ag/{}'.format(DB_DIR, archivo_2)
archivo_3 = 'Rakic-BB.yml'
ruta_3 = '{}main/Be/{}'.format(DB_DIR, archivo_3)
archivo_4 = 'Hagemann.yml'
ruta_4 = '{}main/Bi/{}'.format(DB_DIR, archivo_4)
archivo_5 = 'Fang-2L.yml'
ruta_5 = '{}main/Bi2Se3/{}'.format(DB_DIR, archivo_5)


d_1 = get_schema_from_yaml(ruta=ruta_1)
d_2 = get_schema_from_yaml(ruta=ruta_2)
d_3 = get_schema_from_yaml(ruta=ruta_3)
d_4 = get_schema_from_yaml(ruta=ruta_4)
d_5 = get_schema_from_yaml(ruta=ruta_5)

# convierte a tuplas datos
c_1 = get_nk(d_1)   # array con n k en tupla 
c_2 = get_nk(d_2) 
c_3 = get_nk(d_3) 
c_4 = get_nk(d_4) 
c_5 = get_nk(d_5) 

list= get_list(c_5)
it = interpolation(list, w_i=w_i)


list_1= get_list(c_1)
list_2= get_list(c_2)
it_1 = interpolation(list_1, w_i=w_i)
it_2 = interpolation(list_2, w_i=w_i)


ref_idx_1 = complex(it_1[1],it_1[2])
ref_idx_2 = complex(it_2[1],it_2[2])

list_Ni = [ref_idx_1,ref_idx_2]

# Instancia de la clase TransferMatrixMethod

test = TransferMatrixMethod()
test.theta = 30
test.l = w_i
test.n = list_Ni
matrix = test.get_transfer_matrix()

# Reflectance and Transmittance

reflectance = TranferMatrixMethodHelper.reflectance(matrix)
transmittance = TranferMatrixMethodHelper.transmittance(matrix)
print(reflectance)
print(transmittance)

theta_inicial = 30
theta_final = 90
pasos = 100


a = get_list_theta(theta_inicial, theta_final, pasos)
print(len(a))






















