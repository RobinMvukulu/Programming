#Basic python functions
def pgcd(a, b):
    if (b==0):
        return a
    else:
        r = a % b
        return PGCD(b, r)

def produit_scalaire(v1, v2):
    list_prod = []
    for i in range(len(v1)):
        prod = v1[i] * v2[i]
        list_prod.append(prod)
    return list_prod

def est_parfait(n):
    sum = 0
    for i in range(n):
        if n % i == 0:
            sum+= i
    if sum == n:
        return true
    return false

def pyramide(n):
    for i in range(n):
        print '*' * n

def rotation(liste, k):
    result = []
    for item in range(len(liste) - k, len(liste)):
        result.append(liste[item])
    for item in range(0, len(liste) - k):
        result.append(liste[item])
    return result

def compresser(texte):
    result = ""
    compt = 0
    for i in range(texte):
        if texte[i] == texte[i+1]:
            compt += 1
            result += texte[i]
        else:
            result += str(compt)
            compt = 0
    return result

def transpose(matrice):
    return [list(row) for row in zip(*matrice)] #déplie la liste en colonne

def somme_chiffres(n):
    sum = 0
    for i in range(n):
        sum += n[i:i++]
    return sum

def compter_lettres(texte):
    dict = {}
    for i in range(texte):
        compt = 0
        for j in range(texte):
            if texte[i] == texte[j]:
                compt+=1
        dict[texte[i]] = compt
    return dict

def fusion(l1, l2):
    i, j = 0, 0
    resultat = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            resultat.append(l1[i])
            i += 1
        else:
            resultat.append(l2[j])
            j += 1

    resultat.extend(l1[i:])
    resultat.extend(l2[j:])

    return resultat
