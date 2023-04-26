num = int(input("Digite um número: "))

# Inicializa a sequência de Fibonacci com os dois primeiros valores
fibonacci = [0, 1]

# Calcula a sequência de Fibonacci até atingir o número informado ou ultrapassá-lo
while fibonacci[-1] < num:
    next_fibonacci = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fibonacci)

# Verifica se o número informado pertence à sequência de Fibonacci
if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci!")

else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")