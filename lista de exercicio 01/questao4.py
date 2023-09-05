#Solicitar a lista de numeros ao usuario
entrada= input("Digite a lista de numeros separados por espaços:")

#Divida a entrada em uma lista de strings
numeros_str=entrada.split()

#Converta os numeros de strings para inteiros
numeros= [int(numero)for numero in numeros_str]

#Verifice se a lista nao esta vazia
if len(numeros)== 0:
    print("A lista esta vazia.nao e possivel encontrar o maior e o menor valor.")
else:

    #Encontrar o maior e o menor valor
    maior_valor=max(numeros)
    menor_valor=min(numeros)

    #Mostre os resultados
    print("maior valor da lista:", maior_valor)
    print("menor valor da lista", menor_valor)