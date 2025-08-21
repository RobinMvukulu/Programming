#Fonction somme : Écris une fonction somme(a, b) qui retourne la somme de a et b.
def calculate_sum(a, b):
    result = a + b
    return result

#Maximum de deux nombres : Écris une fonction maximum(a, b) qui retourne le plus grand des deux nombres.
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

#Pair ou impair : Écris une fonction est_pair(n) qui retourne True si n est pair, sinon False.
def parity(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Longueur d’une chaîne : Écris une fonction longueur(chaine) qui retourne la longueur de la chaîne donnée.
def string_length(string):
    return len(string)

#Inverser une chaîne : Écris une fonction inverse(chaine) qui retourne la chaîne donnée inversée.
def reverse_string(string):
    return string[::-1]

#Factorielle d’un nombre : Écris une fonction factorielle(n) qui retourne n! (n factorielle).
def factorial(n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result
        
#Nombre premier : Écris une fonction est_premier(n) qui retourne True si n est un nombre premier, sinon False.
def is_prime(n):
    if n == 1 or n == 2:
        return True
    for i in range(n):
        if n%i == 0:
            return False
    return True

#Compter les voyelles : Écris une fonction compter_voyelles(chaine) qui retourne le nombre de voyelles (a, e, i, o, u, y) dans une chaîne.
def count_vowels(string):
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    for i in range(0, len(string)):
        if string[i] in vowels:
            count +=1
    return count

#Somme des éléments d’une liste : Écris une fonction somme_liste(liste) qui retourne la somme des éléments d’une liste de nombres.
def sum_list(l):
    result = 0
    for n in l:
        result += n
    return result

#Table de multiplication : Écris une fonction table_multiplication(n) qui affiche la table de multiplication de n jusqu’à n × 10.
def mult_table(n):
    results = []
    for i in range(1, 11):
        results.append(n*i)
    return results
        