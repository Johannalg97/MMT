#Application of the transfer matrix method 
import numpy as np
import mpmath


def Fresnel_coefficients(polarizacion , theta , Ni):
    CoeFre_rij = []
    CoeFre_tij = []
    Theta_t = []
    theta_t = 0
    alpha = 0
    betha = 0
    
    for i in range(0, len (Ni)):
        theta_t = mpmath.sqrt(1 - ( Ni[i] / Ni[i+1] )**2 - ( mpmath.si(theta)**2))
        alpha = (mpmath.cos(theta_t)) / (theta)
        betha = Ni[i+1] / Ni[i]
        Theta_t.append(theta_t)
    
    if polarizacion == "P":
        for i in range(0,len (Ni)-1):
            rij = (alpha - betha) / (alpha + betha)
            tij = 2 / (1 + (alpha * betha))
            CoeFre_rij.append (rij)
            CoeFre_tij.append (tij)
    
    if  polarizacion == "S":
        for i in range(0,len (Ni)-1):
            rij = (1 - (alpha * betha))/(1 + (alpha * betha))
            tij = 2 / (alpha + betha)
            CoeFre_rij.append (rij)
            CoeFre_tij.append (tij)
    
    else:
        print("Enter a valid polarization (P or S) ")
    
    return [CoeFre_rij ,  CoeFre_tij, Theta_t]


def Dynamical_matrix(CoeFre_rij , CoeFre_tij):
    Dynamical_M = []

    for i,j in zip(CoeFre_rij , CoeFre_tij):
        Md = np.array([ [1 / j , i / j] , [i / j , 1 / j] ])
        Dynamical_M(Md)

    return Dynamical_M 

def Phi(Theta_t, Ni, lamda, Thickness):
    Phi = []
    phi = 0

    for i in range(0, len (Thickness)):
        phi =  ((2 * mpmath.pi) / lamda ) * Ni[i+1] * Thickness[i] * mpmath.cos(Theta_t[i])
        Phi.append (phi)
    
    return Phi
    

def Propagation_matrix(Phi):
    Propagation_M = []

    for i in Phi:
        Mp = np.array([[mpmath.exp(-1j*i),0],[0,mpmath.exp(1j*i)]])
        Propagation_M.append (Mp)
    
    return Propagation_M

def Multiplication( Dynamical_M, Propagation_M):
    Multiplication_M = np.identity(2)
    for i in range(0,len(Propagation_M)):
        Minde = np.matmul(Minde , Dynamical_M[i])
        Minde = np.matmul(Minde , Propagation_M[i])

    return Multiplication_M


def Transfer_matrix(polarizacion , theta , Ni, Thickness, lamda):
    rij_tij_theta_t = Fresnel_coefficients(polarizacion , theta , Ni)
    rij = rij_tij_theta_t[0]
    tij = rij_tij_theta_t[1]
    theta_t = rij_tij_theta_t[2]
    Dynamical_M = Dynamical_matrix(rij , tij)
    Phi = Phi(theta_t, Ni, lamda, Thickness)
    Propagation_M = Propagation_matrix(Phi)
    Multiplication_M = Multiplication( Dynamical_M, Propagation_M)

    return Multiplication_M
    










   
    




