

entrada = list(map(int, input().split()))

entrada.sort(reverse = True)
maior = entrada[0]
entrada.sort()
menor = entrada[0]

print(f'maior numero: {maior}\nmenor numero: {menor}')