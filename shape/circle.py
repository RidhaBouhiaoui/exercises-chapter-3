from numbers import Number


class Circle:

    def __init__(self, centre, radius):
         self.centre = centre
         self.radius = radius
    

    def __contains__(self, x):
        if len(x) == 2 and isinstance(x[0],Number) and isinstance(x[1],Number):
            d_2 = (self.centre[0]-x[0])**2 + (self.centre[1]-x[1])**2
            d = d_2**0.5
            if d < self.radius:
               return True
            else:
                return False
        else:
            return NotImplemented
