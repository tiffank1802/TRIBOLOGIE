class Materiau:
    def __init__(self, nom="Acier", module_young=200e9, coefficient_poisson=.3):
        self.nom = nom
        self.module_young = module_young  # en Pascals
        self.coefficient_poisson = coefficient_poisson  # sans unité

    def __str__(self):
        return f"Matériau: {self.nom}, Module de Young: {self.module_young} Pa, Coefficient de Poisson: {self.coefficient_poisson}"