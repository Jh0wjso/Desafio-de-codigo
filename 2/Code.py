numero = int(input("Informe um número: "))

fibonacci = [0, 1]

while fibonacci[-1] < numero:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if fibonacci[-1] == numero:
    print(numero, "pertence à sequência de Fibonacci!")
else:
    print(numero, "não pertence à sequência de Fibonacci.")
