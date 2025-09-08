#Basic python functions
def somme(a, b):
    return a + b

def parité(n):
    if n%2 == 0:
        return "pair"
    else:
        return "impair"

def factorielle(n):
    prod = 1
    for i in range(n):
        prod *= i
    return prod

def max_list(lst):
    max(lst)

def compt_voyelles(texte):
    compteur = 0
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    for l in texte:
        if l in voyelles:
            compteur += 1
    return compteur

def est_palindrome(mot):
    inv = mot[::-1]
    if inv == mot:
        return True
    return False

def inv_chaine(texte):
    return texte[::-1]

def est_premier(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n/i == 1:
            return True
    return False

def fibonacci(n):
    list_fibo = []
    for i in range(n):
        a, b = 0, 1
        list_fibo.append(a)
        a, b = b, a+b
    return list_fibo

def trier_liste(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst