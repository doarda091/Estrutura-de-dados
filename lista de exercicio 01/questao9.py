#Filtre os nomes que começam com 'A'
def nomes_com_a(lista_nomes):
    nomes_filtrados = [nome for nome in lista_nomes if nome.startswith('A') or nome.startswith('a')]
    return nomes_filtrados

#Função principal
def main():
    lista_nomes = input("Digite os nomes separados por vírgula: ").split(',')
    nomes_filtrados = nomes_com_a(lista_nomes)

    if nomes_filtrados:
        print("Nomes que começam com 'A':")
        for nome in nomes_filtrados:
            print(nome.strip())  # strip() remove espaços em branco extras
    else:
        print("Nenhum nome na lista começa com 'A'.")

if __name__ == "__main__":
    main()
