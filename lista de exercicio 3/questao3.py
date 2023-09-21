import string

def is_palindrome(text):
    text = text.lower()
    text = ''.join(char for char in text if char not in string.punctuation and char != ' ')

    return text == text[::-1]

texto = input("Digite uma palavra ou frase: ")

if is_palindrome(texto):
    print(f"'{texto}' é um palíndromo!")
else:
    print(f"'{texto}' não é um palíndromo.")
