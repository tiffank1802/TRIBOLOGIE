from math import pi
class Materiau:
    def __init__(self, nom="Acier", module_young=200e9, coefficient_poisson=.3, radius=0., raduis=None):
        # Accept both correct `radius` and legacy misspelling `raduis`.
        if raduis is not None:
            radius = raduis
        self.nom = nom
        self.module_young = module_young  # en Pascals
        self.coefficient_poisson = coefficient_poisson  # sans unité
        self.radius = radius  # en mètres
        self.raduis = self.radius  # compatibilité (ancienne orthographe)
        self.P=100  # Charge en N

    def __str__(self):
        return f"Matériau:\t {self.nom}, \nModule de Young: \t{self.module_young} Pa, \nCoefficient de Poisson: \t{self.coefficient_poisson}"
    def get_P_value(self):
        return self.P
    def set_P_value(self, value):
        self.P = value
    def contact(self, other):
        E1 = self.module_young
        E2 = other.module_young
        raduis1 = self.radius
        raduis2 = other.radius
        v1 = self.coefficient_poisson
        v2 = other.coefficient_poisson
        E_eq = 1 / ((1 - v1**2) / E1 + (1 - v2**2) / E2)
        if raduis1 == 0 and raduis2 == 0:
            raduis_eq = 0
        elif raduis1 == 0 or raduis2 == 0:
            raduis_eq = max(raduis1, raduis2)
        else:
            raduis_eq = 1 / (1 / raduis1 + 1 / raduis2) if raduis1 != 0 and raduis2 != 0 else max(raduis1, raduis2)
        
        return E_eq, raduis_eq
    def rayon_contact(self, other,P):
        E_eq, raduis_eq = self.contact(other)
        self.set_P_value(P)   # Met à jour la charge P de l'objet courant
        a = ((3 * P * raduis_eq) / (4 * E_eq))**(1 / 3)
        return a
    def enforcement(self,other):
        E_eq, raduis_eq = self.contact(other)
        a=self.rayon_contact(other,self.P)
    

        return a**2 / raduis_eq
    
    def pression_moyenne(self, other):
        a = self.rayon_contact(other,self.P)
        E_eq, raduis_eq = self.contact(other)
        return 0.42*(E_eq*a/raduis_eq)

    def pression_max(self, other):
        pression_moyenne = self.pression_moyenne(other)
        return (3/2) * pression_moyenne
    def raideur_contact(self, other):
        E_eq, _ = self.contact(other)
        a = self.rayon_contact(other,self.P)
        return 2 * E_eq * a
    def pression_contact(self, other, r):
        P = self.P
        a = self.rayon_contact(other,self.P)
        
        p = self.pression_max(other) * (1 - (r**2 / a**2))**0.5
        
        return p