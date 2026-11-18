import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = math.lcm(denom1,denom2)
    b = (a//denom1)*numer1 + (a//denom2)*numer2
    
    g = math.gcd(a,b)
    return [b//g, a//g]