import numpy as np

#Convert in upper the string
def convert_to_upper(string):
    string = string.upper()
    return string

#Show common element between 2 list
def common_elem(l1, l2):
    l_common = []
    for elem in l1:
        if elem in l2:
            l_common.append(elem)
    return l_common

def factorial(n):
    result = 1
    
    if n < 0:
        print("Not working for negative value")
        return 0
    
    for i in range(1, n+1):
        result *= i
    return result

def sum_list(l):
    result = 0
    for elem in l:
        result += elem
    return result


def square_matrix(n):
    M = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            M[i, j] = (i + j) % 2
    return M

def sort_list(l):
    l_copy = l.copy()
    l_sorted = []
    for i in range(len(l)):
        min_elem = min(l_copy)
        l_sorted.append(min_elem)
        l_copy.remove(min_elem)
    return l_sorted

def is_leap_year(year):
    if year % 4 == 0:
        return True
    return False

def generate_square():
    list_square = []
    for i in range(1, 101):
        list_square.append(i*i)
    return list_square

def count_letters(word):
    letters = list(word)
    return len(letters)
        
def make_dict(l):
    return dict(l)
#Test
string = "coucou"
l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 4, 9]
n = 4
year = 2024
l3 = [("hand",2), ("leg",2), ("head",1)]

print("1. String converted in upper: " + str(convert_to_upper(string)))
print("2. Common elements: " + str(common_elem(l1, l2)))
print("3. Factorial " + str(n) + ": " + str(factorial(n)))
print("4. Sum of list l1: " + str(sum_list(l1)))
print("5. Square matrix n with zero and one alterned: " + str(square_matrix(n)))
print("6. returned sorted list l2 without using sort(): " + str(sort_list(l2)))
print("7. Is " + str(year) + " a leap year: " + str(is_leap_year(year)))
print("8. Generate square of numbers from 1 to 100: " + str(generate_square()))
print("9. Number of letters in the word " + string + " is: "  + str(count_letters(string)))
print("10. Dictionnary from a list of tuples(key, value) l3: " + str(make_dict(l3)))
