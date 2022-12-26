import sympy as smp 

"""class DispersionModels(object): 
    
    This class implements the main dispersion models
    
    def __init__(self): 
        self.electron_charge = 1.602176634e-19      #in coulombs 
        self.electron_mass = 9.10938356e-31         #in kilograms
        self.permitivitty_vacuum = 8.8541878128e-12 #in  F/m
        self.n = []             # indices de refracciòn
        self.thicknesses = []   # espesores
        self.polaritation = "P" #tipo de polarizaciòn """
        

x, y, z = smp.symbols('x y z')

f = x**2 + y * smp.sin(z)
a  = f.subs([(x,1),(y,3),(z,smp.pi/2)])
print(a)






