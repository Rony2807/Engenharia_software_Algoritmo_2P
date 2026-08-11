# Leitura do número inteiro
numero = int(input("Digite um número inteiro para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")

# Estrutura de repetição para gerar a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2d} = {resultado}")