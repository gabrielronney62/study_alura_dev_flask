'''
A ideia do nosso jogo é termos que acertar um número secreto. Quando o programa estiver rodando, teremos que digitar um
número e o programa dirá se acertamos ou erramos o número, com várias tentativas e níveis.
'''

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

# Descomentar em caso de utilização com o laço While
# rodada = 1

# Adicionando laço com While
# while(rodada <= total_de_tentativas):

# Adicionando mesma condição com laço For
for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

# Descomentar em caso de utilização com o laço While
#     rodada = rodada + 1


print("Fim do nosso jogo!")
print('#######################')