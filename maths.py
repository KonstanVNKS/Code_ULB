from math import sqrt


def rac_eq_2nd_deg(a, b, c):
    d = b**2 - 4*a*c
    x1 = (-b + d) / 2*a
    x2 = (-b - d) / 2*a
    if d < 0:
        return ()
    elif d == 0:
        return (-b/2*a ,)
    else:
        return (min(x1,x2), max(x1,x2))


def catalan(n):
    if n >= 0:
        return 2*fact(n) / fact(n+1)*fact(n)


def sin_approx(x: float):
    res, k = 0, 0
    while abs(add) < 10 ** -6:
        add = float((((-1)**k)*(x**(2*k+1))))
        f = fact(2*k+1)
        add /= f
        if abs(add) < 10 ** -6:
            done = True
        else:
            res += add
        k += 1
    return res


def fact(n: int):
    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    return fact


def volume(a: str, b: float):
    if a == 'T':
        return (sqrt(2)/12)*b**3
    elif a == 'C':
        return b**3
    elif a == 'O':
        return (sqrt(2)/3)*b**3
    elif a == 'D':
        return ((15+(7*sqrt(5)))/4)*b**3
    elif a == 'I':
        return ((5*(3+sqrt(5)))/12)*b**3
    else:
        return "Polyèdre non connu"