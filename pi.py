import math
from decimal import *
getcontext().prec = 100

pi = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")

def factorial(n):
  res = Decimal(1)
  for x in range(1, n+1):
    res *= Decimal(x)
  return res

def chudnovsky_term(n):
  sign = Decimal(1) if n%2 == 0 else Decimal(-1)
  x = factorial(6*n)/(factorial(n)**3)/factorial(3*n)
  x *= (Decimal(13591409)+Decimal(545140134)*Decimal(n))/(Decimal(640320)**(Decimal(3)*Decimal(n)))
  return sign*Decimal.sqrt(Decimal(10005))/Decimal(4270934400)*x
  
def chudnovsky(n_terms):
    ch = Decimal(0)
    for n in range(n_terms):
        ch += chudnovsky_term(n)
    print "pi=",1/ch,"\n"
    print("{0} terms: Delta = {1}".format(n_terms, float(Decimal(1)/ch-pi)))


chudnovsky(n_terms=1)
chudnovsky(n_terms=2)
chudnovsky(n_terms=3)
chudnovsky(n_terms=4)
chudnovsky(n_terms=5)
chudnovsky(n_terms=6)
chudnovsky(n_terms=107)
