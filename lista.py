#quantidade = int(input())
#lista = []

#um valor por linha
#for i in range(quantidade):
    #numero = int(input())
    #lista.append(numero)

#print(lista)

#dois valores por linha
#tamanho,numero = map(int, input().split())
#print(f'Tamanho: {tamanho}\nNumero: {numero}')

# N valores em um linha
#entrada = list(map(int, input().split()))
#print(entrada)
#print(sum(entrada))
#entrada.sort()
#entrada.sort(reverse = true)
#print(entrada)

lista = []
quantidade = int(input())

for i in range(quantidade):
    cidade, pessoas = map(str, input().split())
    lista.append([cidade,pessoas])

print(lista)