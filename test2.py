from tools.helpers import *
from functions.interpolacion import *
from functions.transfer_matrix_method import TransferMatrixMethod
from settings import DB_DIR


test = TransferMatrixMethod()
test.theta = 40
test.l = 0.633
test.n = [(1.51), (1)]
test.polaritation = 'P'

a = test.get_propagation_vectors()
print('vectores de onda iniciales')
print(a)


b = test.get_propagation_vectors_x()
print('vectorres de propagacion en x')
print(b)

c = test.get_phi()
print('phi')
print(c)

d = test.get_reflection_fresnel_coefficients()
print('coeficiet r')
print(d)

c = test.get_trasmission_fresnel_coefficients()
print('coeficient t')
print(c)

d = test.get_dinamical_matriz()
print('dinamical matriz')
print(d)


e = test.get_propagation_matriz()
print('propagetion matriz')
print(e)


f = test.get_transfer_matrix()
print('tranfer matriz')
print(f)

g = test.get_reflectance()
print('reflectance')
print(g)

h = test.get_transmittance()
print('transmitance')
print(h)

i = test.get_absortance()
print('absortancia')
print(i)

suma = g + h + i
print(suma)