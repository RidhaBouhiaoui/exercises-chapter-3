from ast import Return
from numbers import Number
from re import L

from numpy import integer, isin


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree())
            selfn = self.coefficients + (0,)*(other.degree()-common)
            othern = other.coefficients + (0,)*(self.degree()-common)
            coefs = tuple(a - b for a, b in zip(selfn,
                                                othern))

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented
    
    
    def __rsub__(self, other):
       
       if isinstance(other, Number):
           l = self.degree() + 1
           othern = (0,)*l
           otherp = ((othern[0] + other,) + othern[1:])

           return Polynomial(otherp) - self
       

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            _s = list(self.coefficients)
            _v = list(other.coefficients)
            res = [0]*(len(_s)+len(_v)-1)
            for selfpow,selfco in enumerate(_s):
                for valpow,valco in enumerate(_v):
                    res[selfpow+valpow] += selfco*valco
            final = ()
            for i in range(len(res)):
                final += (res[i],)
            return Polynomial(final)

        elif isinstance(other, Number):
            res = [co*other for co in self.coefficients]
            final = ()
            for i in range(len(res)):
                final += (res[i],)
            return Polynomial(final)
             
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return self*other


    def __call__(self,x):
        if isinstance(x, Number):
            l = 0
            for i in range(self.degree()+1):
                 l += self.coefficients[i]*(x**i)
            return l
        else:
            return NotImplemented

    def dx(self):
        if isinstance(self,Polynomial):
             l = ()
             if self.degree() == 0:
                 return Polynomial((0,))
             else:

                for i in range(1, self.degree()+1):
                    l += (i*self.coefficients[i],)
                return Polynomial(l)
    
        elif isinstance(self, Number):
             return Polynomial((0,))
        
        else:
            return NotImplemented


    def __pow__(self, other):

        if isinstance(other, integer):
            otherf = (1)
            for i in range(1,other):
                otherf = otherf*other
            return otherf

        else:
             return NotImplemented
      
def derivative(fn):
        return fn.dx()
    