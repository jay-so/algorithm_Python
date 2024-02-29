import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

def solution(numer1, denom1, numer2, denom2):
    lcm_value = lcm(denom1, denom2)
    numer1 = int(numer1 * (lcm_value // denom1))
    numer2 = int(numer2 * (lcm_value // denom2))
    numerator = numer1 + numer2
    answer = [numerator, lcm_value]

    gcd_value = math.gcd(*answer)
    answer = [value // gcd_value for value in answer]

    return answer