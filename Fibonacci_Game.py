import random

# Gera um número aleatório da sequência de Fibonacci
fibonacci = [0, 1]
while len(fibonacci) < 21:  # escolha quantos numeros da sequencia farão parte do jogo
    next_fibonacci = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fibonacci)
random_num = random.choice(fibonacci)

print("Bem-vindo ao mini game da sequência de Fibonacci!")
print(f"Tente adivinhar o número que pertence à sequência de Fibonacci escolhido pelo sistema: ")

guess = int(input("Digite o seu palpite: "))
while True:
    if guess in fibonacci:
        if guess == random_num:
            print("Parabéns, você acertou o número escolhido pelo sistema!")
            break
        elif guess < random_num:
            print("O número escolhido pelo sistema é maior!")
        else:
            print("O número escolhido pelo sistema é menor!")
        guess = int(input("Digite o seu novo palpite: "))
    else:
        print("O número digitado não pertence à sequência de Fibonacci. Você Perdeu!")
        break
