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

def rendre_monnaie(prix, x, y, z, a, b):
    argent = 20*x+10*y+5*z+2*a+b
    dif = argent - prix
    if dif < 0:
        return None, None, None, None, None
    a, b, c, d, e = 0, 0, 0, 0, 0
    if dif >= 20:
        a += (dif//20)
        dif -= (dif//20)*20
    if dif >= 10:
        b += (dif//10)
        dif -= (dif//10)*10
    if dif >= 5:
        c += (dif//5)
        dif -= (dif//5)*5
    if dif >= 2:
        d += (dif//2)
        dif -= (dif//2)*2
    if dif >= 1:
        e += dif
        dif -= dif
    return a, b, c, d, e

def premier(n):
    res = True
    for i in range(2, (n // 2 + 1)):
        if not n % i:
            res = False
    if n in [0, 1]:
        res = False
    return res


def prime_numbers(n):
    liste_premier = []
    i = 2
    if type(n) is not int or n < 0:
        liste_premier = None
    else:
        while len(liste_premier) < n:
            if premier(i):
                liste_premier.append(i)
            i += 1
    return liste_premier


def distance_points(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def duree(debut, fin):
    heure, minute = divmod(fin[1] - debut[1], 60)
    heure = (heure + (fin[0] - debut[0])) % 24
    return heure, minute