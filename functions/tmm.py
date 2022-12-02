from math import radians, pi, sin


from mpmath import sqrt, exp #allows you to handle complex numbers
from numpy import array, identity, matmul


# Modulo para obtener la matriz de transferencia 

class Transfer_Matrix_method(object): 
    """
    This class implements the transfer matrix method
    """
    def __init__(self): 
        self.theta = 0          #angulo
        self.l = 0              #longitud de onda
        self.n = []             # indices de refracciòn
        self.thicknesses = []   # espesores
        self.polaritation = "P" #tipo de polarizaciòn 
        


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
        This method:
        *Calculates the propagations vectors of the system in x- component
        *Recive the list  list_ni of the refractive index (complex or floats), 
        k0 and kz (calculated in the previous function (complex or floats))
        *Returns  a list of the propations vectors in the x-component (complex), 
        returns an element by per material
        """
        list = []
        self.get_propagation_vectors() #llamada recursiva 

        for i in range(0, len(self.n)):
            a = (self.n[i] * self.propagation_vector_i)**2
            b = self.propagation_vector_z**2
            c = a - b
            kx = sqrt(c)
            list.append(kx)
        setattr(self, 'list_kx', list)

    def get_phi(self):
        """
        This method:
        *Calculates the phi factor
        *Recive  the list  list_ni of the refractive index (complexex and/or floats), 
        a list with the thicknesses of all system layers 
        *Returns a list phi (complexes), returns an element by per layer
        """
        list = []
        self.get_propagation_vectors()

        if len(self.thicknesses) > 0:
            for i in range(0, len(self.thicknesses)):
                a = self.propagation_vector_i * self.n[i+1] * self.thicknesses[i]
                b = self.n[0] / self.n[i+1]
                c = sin(self.theta)
                d = a * sqrt(1-(b*c)**2)
                list.append (d)
        setattr(self, 'list_phi', list)

    def get_reflection_fresnel_coefficients(self):
        """
        This method:
        *Calculates the reflection fresnel coefficients (rij)
        *Recive type of polarization (str), a list_kx (calculated in the one 
        previous function (complex or floats)), 
        a list_ni (complexes)
        *Returns the list_rij (complex), returns an element by per interface 
        """
        list = []
        self.get_propagation_vectors_x()

        if not (self.polaritation in ["P", "S"]):
            raise ValueError(f"{self.polaritation} Polaritation is not valid ")

        if not (self.polaritation == "P"):
            for i in range(0,len(self.list_n)-1):
                a = self.list_kx[i] - self.list_kx[i+1]
                b = self.list_kx[i] + self.list_kx[i+1]
                r = a / b
                list.append(r)
        
        for i in range(0,len(self.n)-1):
            a = self.n[i]**2 * self.list_kx[i+1] 
            b = self.n[i+1]**2 * self.list_kx[i]
            r = a -b / a + b 
            list.append(r) 
        setattr(self, 'reflection_coefficients', list)
        
    def get_trasmission_fresnel_coefficients(self):
        """
        This method:
        *Calculates the transmission fresnel coefficient (tij)
        *Recive type of polarization (str) and the lis of reflection fresnel 
        coefficients (calculated in the previous function (complex or floats))
        *Returns the list_tij (complex), returns an element by per interface
        """
        list = []
        self.get_reflection_fresnel_coefficients()

        if not (self.polaritation == "P"):
            for i in range(0, len(self.reflection_coefficients)):
                tij = 1 + self.reflection_coefficients[i]
                list.append(tij)
        
        for i in range(0, len(self.reflection_coefficients)):
            a = self.n[i] / self.n[i+1]
            b = 1 * self.reflection_coefficients[i]
            tij = a *  b
            list.append(tij)
        setattr(self, 'trasmission_coefficients', list)

    def get_dinamical_matriz(self):
        """
        This method:
        *Calculates the dinamical matriz (complexes)
        *Recive two list the list_rij and list_tij (calculated in the previous functions )
        *Retur one list of matrix (complex or float) returns an element by per element in the list_rij
        """
        list = []
        self.get_reflection_fresnel_coefficients()
        self.get_trasmission_fresnel_coefficients()
        
        for i,j in zip(self.reflection_coefficients , self.trasmission_coefficients):
            a = array([[1/j,i/j],[i/j,1/j]])
            list.append(a)
        setattr(self, 'dinamical_matrices', list)

    def get_propagation_matriz(self):
        """
        This method:
        *Calculates the propagation matriz (complexes)
        *Recive list phi (complexes)
        *Retur the a list of matriz (complexes) one for each layer of the system
        
        """
        list = []
        self.get_phi()

        if len(self.thicknesses) > 0:
            for i in self.list_phi:
                a = array([[exp(-1j*i),0],[0, exp(1j*i)]])
                list.append(a)
        setattr(self, 'propagation_matriz', list)
        
    def get_transfer_matrix(self):
        """
        This Funtion:
        *calculates the multiplication between the dynamic matrices and the propagation matrices
        *Recive two list list_pm and list_dm
        *Returns a 2*2 matrix with complex elements 

        """
        self.get_dinamical_matriz()
        self.get_propagation_matriz()
        a = len(self.dinamical_matrices) - 1
        m = identity(2)

        if not (len(self.propagation_matriz) == 0):
            for i in range(0, len(self.propagation_matriz)):
                m = matmul(m, self.dinamical_matrices[i])
                m = matmul(m, self.propagation_matriz[i])
            m = matmul(m, self.dinamical_matrices[a])
            
        for i in range(0, len(self.dinamical_matrices)):
            m = matmul(m, self.dinamical_matrices[i])
        setattr(self, 'trasfer matrix', m)
            

  

           
    
#prueba
if __name__ == '__main__':
    list_ni = [1, 2+4j, 3+6j, 4]
    list_t = [5,6]
    
   
    clc = Transfer_Matrix_method()
    clc.l = 0.0001
    clc.n = list_ni
    clc.theta = 45
    clc.thicknesses = list_t

    test_1 = clc.get_propagation_vectors()
    test_2 = clc.get_reflection_fresnel_coefficients()
    test_3 = clc.get_trasmission_fresnel_coefficients()
    test_4 = clc.get_phi()
    test_5 = clc.get_dinamical_matriz()
    test_6 = clc.get_propagation_matriz()
    test_7 = clc.get_transfer_matrix()
    print(vars(clc))

    

"""    print(test_1)
    test_2 = clc.get_propagation_vectors_x()
    print(test_2)
    test_3 = clc.get_phi()
    print(test_3)
    test_4 = clc.get_rij()
    print(test_4)
    test_5 = clc.get_tij()
    print(test_5)
    test_6 = clc.get_dm()
    print(test_6)
    test_7 = clc.get_pm()
    print(test_7) 
    list_kx = calculation_kx(list_ni, k0_kz[0], k0_kz[1])
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















   
    




