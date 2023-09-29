from array import array # On évite ainsi de recourrir à numpy en utilisant un built-in
import math # bien utile pour tout un tas d'opérations
from numbers import Real


class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        if isinstance(new_x, Real):
            self._x = new_x
        else: 
            raise ValueError(f'x needs to be a real numbers, the input {new_x} is of type {type(new_x)}')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        if isinstance(new_y, Real):
            self._y = new_y
        else: 
            raise ValueError(f'x needs to be a real numbers, the input {new_y} is of type {type(new_y)}')
    @property
    def norme(self):
        return self.__abs__()
    
    @classmethod
    def angle(cls, v1, v2):
        if isinstance(v1, cls) and isinstance(v2, cls):
            return math.acos((v1*v2)/(v1.norme*v2.norme))
        else: raise ValueError(f'wrong type, mate')

    def __repr__(self):
        return f'Vecteur({self.x},{self.y})'        
    
    def __iter__(self):
        yield self.x
        yield self.y
    
    def __str__(self):
        return f'x = {self.x}, y = {self.y}'  
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.x == other.x and self.y == other.y: 
                return True
        else: return False

    def __abs__(self):
        return (self.x**2+self.y**2)**0.5
    
    @classmethod
    def from_iterable(cls, it):
        return cls(it[0], it[1]) 
    
    @classmethod
    def from_polar(cls, r: float,theta: float):
        return cls(r*math.cos(theta), r*math.sin(theta)) 

    def __add__(self, k):
        if isinstance(k, type(self)):
            return Vecteur(self.x + k.x, self.y + k.y)  
        else:
            new_k = Vecteur.from_iterable(k)
            self.__add__(new_k)

    def __sub__(self, k):
        if isinstance(k, type(self)):
            return Vecteur(self.x - k.x, self.y - k.y)  
        else:
            new_k = Vecteur.from_iterable(k)
            self.__sub__(new_k)     

    def __neg__(self):
        # Define the behavior of the unary - operator for Vecteur objects
        return Vecteur(-self.x, -self.y)

    def __mul__(self, k):
        if isinstance(k, Real):
            return Vecteur(k*self.x, k*self.y)
        elif isinstance(k, type(self)):
            return self.x * k.x + self.y * k.y  
        else:
            new_k = Vecteur.from_iterable(k)
            self.__add__(new_k)

    def __rmul__(self, k):
        return self.__mul__(k)

if __name__ == '__main__':
    v = Vecteur(1,2)
    print(v._x)
    print(v.x)

