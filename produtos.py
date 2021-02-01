total_gasto = mais_mil = nome_menor = cont = menor_preco = 0

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    cont += 1
    total_gasto += preco
    if preco > 1000:
        mais_mil += 1
    if cont == 1:
        menor_preco = preco
        nome_menor = nome
    elif cont > 1 and preco > menor_preco:
        menor_preco = preco
        nome_menor = nome 
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? ').upper().strip()
    if continuar in 'N':
        break

print(f'O total gasto é de: {total_gasto}.')
print(f'{mais_mil} produtos custam mais de R$1000.00')
print(f'O nome do menor produto é: {nome}')