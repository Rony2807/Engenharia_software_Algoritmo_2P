def obter_maior(a, b):
    if a > b:
        return a
    else:
        return b


# Exemplo de uso da função:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

maior = obter_maior(num1, num2)

if num1 == num2:
    print("Os dois números são iguais.")
else:
    print(f"O maior número é: {maior}")