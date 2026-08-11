# Lista para armazenar os 5 números
numeros = []

# Leitura dos 5 números
for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

# Obtenção do maior e menor valor utilizando as funções nativas min() e max()
maior = max(numeros)
menor = min(numeros)

# Exibição dos resultados
print(f"\nO maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")