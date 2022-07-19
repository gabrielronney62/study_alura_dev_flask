'''
A ideia do nosso jogo é termos que acertar um número secreto. Quando o programa estiver rodando, teremos que digitar um
número e o programa dirá se acertamos ou erramos o número, com várias tentativas e níveis.
'''

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

numero_chute = int(input("Digite um número: "))

print("Você digitou ", numero_chute)

if numero_chute == numero_secreto:
    print("Parabéns, você acertou!")
elif numero_chute < numero_secreto:
    print("Você errou! O número secreto é maior!")
elif numero_chute > numero_secreto:
    print("Você errou! O número secreto é menor!")


print("Fim do nosso jogo!")
print('#######################')