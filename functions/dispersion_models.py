import sympy as smp 
from mpmath import sqrt

class DispersionModels(object): 
    """This class implements the main dispersion models
    """
    def __init__(self): 
        self.electron_charge = 1.602176634e-19        #in coulombs 
        self.electron_mass = 9.10938356e-31           #in kilograms
        self.permitivitty_vacuum = 8.8541878128e-12   #in  F/m
        self.list_parameters_lorenz = [1, 1, 1, 1]    # [electrons_per_unit, omega_0, omega, damping_coefficient]
        self.list_parameters_drude = [1, 1, 1, 1]     # [electrons_per_unit, epsilon_infinito, omega, damping_coefficient]
        self.list_parameters_sellmeier = [1, 1, 1, 1] # [A, B, wavelength, wavelength_0]
        self.list_parameters_cauchy = [1, 1, 1, 1]    # [A, B, C, wavelength]

    
    def get_lorenz_model(self):
        """
        This method:
        *Calculates the epsilon_1 and epsilon_2 values of the dielectric function using the lorenz model
        *Receives a list of all parameters entered by the user
        * Return epsilon_1 and epsilon_2
        """
        a = (self.electron_charge**2 * self.list_parameters_lorenz[0]) / (self.permitivitty_vacuum * self.electron_mass)
        b = self.list_parameters_lorenz[1]**2 - self.list_parameters_lorenz[2]**2
        c = self.list_parameters_lorenz[3] * self.list_parameters_lorenz[2]

        epsilon_1 = 1 + (a * ((b) / (b**2 + c**2)))
        epsilon_2 = a * ((c) / (b**2 + c**2))
        return epsilon_1, epsilon_2
    
    def get_drude_model(self):
        """
        This method:
        *Calculates the epsilon_1 and epsilon_2 values of the dielectric function using the drude model
        *Receives a list of all parameters entered by the user
        * Return epsilon_1 and epsilon_2
        """
        a = (self.electron_charge**2 * self.list_parameters_drude[0]) / (self.permitivitty_vacuum * self.electron_mass)
        b = a * self.list_parameters_drude[3]
        c = self.list_parameters_drude[2]**2 + self.list_parameters_drude[3]**2

        epsilon_1 = self.list_parameters_drude[1] - ((a) / (c))
        epsilon_2 = (b) / (self.list_parameters_drude[2] * c)
        return epsilon_1, epsilon_2
    
    def get_sellmeier_model(self):
        """
        This method:
        *Calculates the epsilon_1 and epsilon_2 values of the dielectric function using the Sellmeier model
        *Receives a list of all parameters entered by the user
        * Return epsilon_1 and epsilon_2
        """
        a = self.list_parameters_sellmeier[1] * self.list_parameters_sellmeier[2]**2
        b = self.list_parameters_sellmeier[2]**2 - self.list_parameters_sellmeier[3]**2

        epsilon_1 = self.list_parameters_sellmeier[0] + (a / b)
        epsilon_2 = 0
        return epsilon_1, epsilon_2
    
    def get_cauchy_model(self):
         """
        This method:
        *Calculates the epsilon_1 and epsilon_2 values of the dielectric function using the cauchy model
        *Receives a list of all parameters entered by the user
        * Return n and k
        """
        a = self.list_parameters_cauchy[1] / self.list_parameters_cauchy[3]**2
        b = self.list_parameters_cauchy[2] / self.list_parameters_cauchy[3]**4

        n = self.list_parameters_cauchy[0] + a + b
        k = 0
        return n, k 










    




        
        

        







