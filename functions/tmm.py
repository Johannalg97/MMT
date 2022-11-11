from math import radians, pi, sin, sqrt

import numpy as np
import mpmath

# Modulo para obtener la matriz de transferencia 

class TMM(object): 
    def __init__(self): 
        self.theta = 0
        self.l = 0
        self.n = []
        


    def get_propagation_vectors(self):
        """
        This method:
        *Calculates the initial propagation vector k_0 and 
        the propagation vector in the z-component of the system for each 
        angle and one  lamda, both of which are held constant 
        *Receives the angle (theta (float)), lamda (float), refractive index 
        of the first medium  (n0 (complex or float))
        *Returns k0 and kz (complex or floats )
        """
        if not (self.l > 0 and self.l <= 20):
            raise ValueError(f"{self.l} l is not valid")
        if not (self.theta >= 0 and self.theta < 90):
            raise ValueError(f"{self.theta} theta is not in range 0 to 89")
        
        i = (2 * pi)/self.l 
        setattr(self, 'propagation_vector_i', i)
        theta_radians = radians(self.theta)
        z = (self.n[0] * i) * sin(theta_radians)
        setattr(self, 'propagation_vector_z', z)
    
    def get_propagation_vectors_x(self):
        """
        This function:
        *Calculates the propagations vectors of the system in x- component
        *Recive the list  list_ni of the refractive index (complex or floats), 
        k0 and kz (calculated in the previous function (complex or floats))
        *Returns  a list of the propations vectors in the x-component (complex), 
        returns an element by per material
        """
        list_kx = []
        self.get_propagation_vectors() #llamada recursiva 
        


        for i in range(0, len(self.n)):
            a = (self.n[i] * self.propagation_vector_i)**2
            b = self.propagation_vector_z**2
            c = a - b
            kx = sqrt(c)
            list_kx.append(kx)
        
        return list_kx






def calculation_phi(list_ni, thicknesses, k0, theta):
    """
    This funtion:
    *Calculates the phi factor
    *Recive  the list  list_ni of the refractive index (complexex and/or floats), 
    a list with the thicknesses of all system layers 
    *Returns a list phi (complexes), returns an element by per layer
    """
    list_phi = []

    for i in range(0,len(thicknesses)):
        phi_i = (k0*list_ni[i+1]*thicknesses[i])*(mpmath.sqrt(1-((list_ni[0]/list_ni[i+1])*(np.sin(theta)))**2))
        list_phi.append (phi_i)
        
    return list_phi

def calculation_rij (polarizacion, kx, list_ni):
    """
    This funtion:
    *Calculates the reflection fresnel coefficients (rij)
    *Recive type of polarization (str), a list_kx (calculated in the one previous function (complex or floats)), 
    a list_ni (complexes)
    *Returns the list_rij (complex), returns an element by per interface
    """
    list_rij = []
    
    if polarizacion == "S":
        for i in range(0,len(list_ni)-1):
            rij = (kx[i]-kx[i+1])/(kx[i]+kx[i+1])
            list_rij.append(rij)
    elif polarizacion == "P":
        for i in range(0,len(list_ni)-1):
            rij = (list_ni[i]**2*kx[i+1]-list_ni[i+1]**2*kx[i])/(list_ni[i]**2*kx[i+1]+list_ni[i+1]**2*kx[i])
            list_rij.append(rij)
    else:
        print("La polarización no se reconoce" )

    return list_rij 
    
def calculation_tij (polarizacion, list_rij, ni):
    """
    This funtion:
    *Calculates the transmission fresnel coefficient (tij)
    *Recive type of polarization (str) and the lis of reflection fresnel coefficients (calculated in the previous function (complex or floats))
    *Returns the list_tij (complex), returns an element by per interface
    """
    list_tij = []

    if polarizacion == "S":

        for i in range(0, len(ni)-1):
            tij = 1 + list_rij[i]
            list_tij.append(tij)
    else:
        polarizacion == "P"
        for i in range(0,len (ni)-1):
            tij = (ni[i]/ni[i+1])*(1+list_rij[i])
            list_tij.append(tij)

    return list_tij 

def calculation_dm(list_rij , list_tij):
    """
    This funtion:
    *Calculates the dinamical matriz (complexes)
    *Recive two list the list_rij and list_tij (calculated in the previous functions )
    *Retur the list_mt (complex) returns an element by per element in the list_rij
    """
    list_mt = []
    for i,j in zip(list_rij , list_tij):
        mi = np.array([[1/j,i/j],[i/j,1/j]])
        list_mt.append(mi)

    return (list_mt)

def calculation_pm(lista_phi):
    """
    This funtion:
    *Calculates the propagation matriz (complexes)
    *Recive list phi (complexes)
    *Retur the a list of matriz (complexes) one for each layer of the system
    
    """
    list_mp = []
    for i in lista_phi:
        mp = np.array([[mpmath.exp(-1j*i),0],[0,mpmath.exp(1j*i)]])
        list_mp.append(mp)

    return list_mp
        
def multiplication(list_pm, list_dm):
    """
    This Funtion:
    *calculates the multiplication between the dynamic matrices and the propagation matrices
    *Recive two list list_pm and list_dm
    *Returns a 2*2 matrix with complex elements 

    """
    
    if len(list_pm) != 0:
        minde = np.identity(2)
        for i in range(0,len(list_pm)):
            minde = np.matmul(minde, list_dm[i])
            minde = np.matmul(minde,list_pm[i])
    else:
        minde = np.identity(2)
        for i in range(0,len(list_dm)-1):
            minde = np.matmul(minde, list_dm[i])
         

        
    return minde, list_dm 


    return TMT
    
#prueba
if __name__ == '__main__':
    list_ni = [1]
    espesores = []
   
    clc = TMM()
    clc.l = 0.0001
    clc.n = list_ni
    clc.theta = 45
    test = clc.get_propagation_vectors_x()
    print(test)
   

     
    """list_kx = calculation_kx(list_ni, k0_kz[0], k0_kz[1])
    list_phi = calculation_phi(list_ni, espesores, k0_kz[0],np.pi)
    list_rij = calculation_rij("S", list_kx, list_ni)
    list_tij = calculation_tij("P",list_rij, list_ni)
    list_dm = calculation_dm(list_rij,list_tij)
    list_pm = calculation_pm(list_phi)
    m = multiplication(list_pm, list_dm)
    print(k0_kz)
    print("lista de kx")
    print(list_kx)
    print("lista de phi")
    print(list_phi)
    print("lista de rij")
    print(list_rij)
    print("lista de tij")
    print(list_tij)
    print("dinamycal")
    print(list_dm)
    print("propagation")
    print(list_pm)
    print("multiplicaciòn")
    print(m)"""















   
    




