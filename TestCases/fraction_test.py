from fractions import Fraction

class Ratio:
    def __init__(self, n, d) -> None:
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self) -> str:
        return '{0}/{1}'.format(self.numer, self.denom)
    
    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n//g, d//g)
    
    def __float__(self):
        return self.numer / self.denom
    
    __radd__ = __add__
    
def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n - d)

if __name__ == "__main__":
    f = Fraction(1,2)
    print(f)