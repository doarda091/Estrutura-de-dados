palavra = input("Digite uma palavra: ")

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

palavra = palavra.lower()

for letra in palavra:
    if letra == 'a':
        contador_a += 1
    elif letra == 'e':
        contador_e += 1
    elif letra == 'i':
        contador_i += 1
    elif letra == 'o':
        contador_o += 1
    elif letra == 'u':
        contador_u += 1

print("Quantidade de 'a':", contador_a)
print("Quantidade de 'e':", contador_e)
print("Quantidade de 'i':", contador_i)
print("Quantidade de 'o':", contador_o)
print("Quantidade de 'u':", contador_u)

total_vogais = contador_a + contador_e + contador_i + contador_o + contador_u
print("Total de vogais na string:", total_vogais)
