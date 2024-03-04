
import sys

class Solution:
    def __init__(self):
        pass

    def evaluate(self):
        # TODO Ajouter le code pour calculer la valeur de la fonction objectif
        # dans les classes dérivées
        # Nous supposons que la valeur de l'objectif doit être minimisée.
        # Par défaut, nous retournons donc la plus grande valeur possible pour
        # un nombre à virgule flottante.
        return sys.float_info.max
    def validate(self):
        locations_list = list(range(0, self.problem.count_locations()))
        if sorted(self.visit_sequence) == locations_list:
            return True
        
        return False
