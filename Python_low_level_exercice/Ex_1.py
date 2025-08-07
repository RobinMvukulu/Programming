#Write a program that reverses a string.
def reverse_string(word):
    return word[::-1]

#Find the number of vowels in a string.
vowels = "aeiouy"
def find_vowels(word):
    found_vowels = []
    for letter in word:
        if letter.lower() in vowels:
            found_vowels.append(letter)
    return found_vowels

#Generate a list of peer number between 1 and 50
import random
def generate_numbers():
    numbers = []
    length = random.randint(1, 50)
    while len(numbers) < length:
        n = random.randint(1, 50)
        if n % 2 == 0:
            numbers.append(n)
    return numbers

#Check if a number is a prime number
def is_prime_number(number):
    dividers = []
    for i in range(1, number+1):
        if len(dividers) >= 2:
            break
        if number % i == 0:
            dividers.append(i)

    if len(dividers) == 2:
        if dividers[0] == 1 and dividers[1] == number:
            return True
    return False

#Count the number of occurences in a sentence
import re
def count_occ(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)  #Remove punctuation with Regex
    words = sentence.split()
    dict_occ = {}
    for word in words:
        count = 0
        for word_2 in words:
            if word == word_2:
                count += 1
        dict_occ[word] = count
    return dict_occ
                
#Generate the first 10 terms of the Fibonacci sequence.
def fibonacci(n):
    fibo = [0, 1]
    for i in range(n-2):
        fibo.append(fibo[i] + fibo[i+1])
    return fibo
        
#Find the max in a list
def find_max(l):
    max_elem = l[0]
    for elem in l:
        if max_elem < elem:
            max_elem = elem
    return max_elem

#Swap the values ​​of two variables without using a temporary variable. (Without using temp)
def swap_variables(elem1, elem2):
    elem1, elem2 = elem2, elem1
    return elem1, elem2

#Check if a string is a palindrome.
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

#Convert a list of temperatures from Celsius to Fahrenheit.
def celsius_to_fahrenheit(n):
    return (n* 9/5) + 32

#Test
print("1. Reverse string test: " + str(reverse_string("dog")))
print("2. Find vowels test: " + str(find_vowels("elephant")))
print("3. Generate numbers test: " + str(generate_numbers()))
print("4. Is prime number test: " + str(is_prime_number(7)))
print("5. Count occurences test: " + str(count_occ("I am happy, he is happy, everyone is happy.")))
print("6. Fibonacci test: " + str(fibonacci(10)))
print("7. Find maximum in list: " + str(find_max([1, 5, 8, 3, 6, 9])))
print("8. Swap 2 elements without temp: " + str(swap_variables(1, 2)))
print("9. Check Palindrome: " + str(is_palindrome("rotor")))
print("10. Celsius to Fahrenheit: " + str(celsius_to_fahrenheit(18)))