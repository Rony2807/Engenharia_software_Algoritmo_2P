soma = 0

while True:
    numero = float(input("Digite um número (ou 0 para sair): "))
    
    # Condição de parada do laço
    if numero == 0:
        break
        
    soma += numero

print(f"\nA soma de todos os números digitados é: {soma}")