import random

#Determine o vencedor
def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

#Função principal
def main():
    opcoes = ["pedra", "papel", "tesoura"]

    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

    if escolha_usuario not in opcoes:
        print("Opção inválida. Escolha entre pedra, papel ou tesoura.")
    else:
        escolha_computador = random.choice(opcoes)
        print(f"O computador escolheu {escolha_computador}.")
        
        resultado = determinar_vencedor(escolha_usuario, escolha_computador)
        print(resultado)

if __name__ == "__main__":
    main()
