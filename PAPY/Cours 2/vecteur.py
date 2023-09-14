from array import array # On évite ainsi de recourrir à numpy en utilisant un built-in
import math # bien utile pour tout un tas d'opérations

class Vecteur:
    def __init__(self, x, y):
        pass

    def __repr__(self):
        """Représentation textuelle de l'objet"""
        pass
    
    def __iter__(self):
        """Iterateur sur les élements du vecteur, utilise yield"""
    
    def __str__(self):
        """Appelé par print()"""
        pass
    
    def __eq__(self, other):
        """Surcharge de l'opérateur =="""
        pass

    def __abs__(self):
        """surcharge du built-in abs()"""
        pass

if __name__ == '__main__':
    print('main')