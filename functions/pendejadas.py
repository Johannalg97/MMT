 
from numpy import array, identity, matmul
from numpy import  matmul

list_1 = [[[4, -1, 2],[3, 0, 2], [0, -1, 4]], [[4, -1, 2], [3, 0, 2], [0, -1, 4]]]
list_2 = [[[6, -1, 2], [6, 0, 2], [0, -1, 4]]]
list_3 = [[[4, -1, 2],[3, 0, 2], [0, -1, 4]], [[4, -1, 2], [3, 0, 2], [0, -1, 4]], [[4, -1, 2], [3, 0, 2], [0, -1, 4]]]

def multiplicacio(list_1, list_2):

    Minde = identity(3)
    for i in range(0, len(list_2)):
        Minde = matmul(Minde, list_1[i])
        Minde = matmul(Minde, list_2[i])
    #largo = len(list_1) - 1
    #Minde = matmul(Minde, list_1[largo]) 
    return Minde

def multiplicacio_2(list):
    minde = identity(3)
    for i in range(0, len(list)):
            minde = matmul(minde, list[i])
    return minde

a = multiplicacio(list_1, list_2)
print(a)

b = multiplicacio_2(list_3)
print(b)