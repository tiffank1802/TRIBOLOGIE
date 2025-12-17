from math import pi
from materiau import Materiau  
P=100  # Charge en N
def deplacement(M1,r):
    E1 = M1.module_young
    v1 = M1.coefficient_poisson
    w=(1-v1**2)*P/(pi*E1*r)
    return w