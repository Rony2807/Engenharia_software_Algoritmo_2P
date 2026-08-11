soma = 0.0

for i in range(1, 11):
    num = float(input(f"Digite o {i}º número: "))
    soma += num

media = soma / 10

print(f"\nA soma dos números é: {soma}")
print(f"A média dos números é: {media:.2f}")