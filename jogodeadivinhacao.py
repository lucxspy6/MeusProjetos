import random


print('*******************')
print('JOGO DE ADIVINHAÇÃO')
print('*******************')

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 0

print('Qual a dificuldade? ')
print('''[1] fácil
[2] médio
[3] difícil
''')

nivel = int(input('Informe o nível: '))

while nivel not in [1,2,3]:
    nivel = int(input('Nível inexistente. Por favor, informe um nível válido: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2: 
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}.')
    chute_str = input('Digite um número entre 1 e 100: ')
    print('Você digitou:', chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print('Você deve digitar um número de 1 a 100. \n')
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print(f'Você acertou. Você fez {pontos} pontos.')
    else:
        if (maior):
            print('Você errou. Você digitou um número maior que o número secreto.')
        elif (menor):
            print('Você errou. Você digitou um número menor que o número secreto.\n')
        pontos = pontos - (abs(numero_secreto - chute))

        
print('Fim de jogo.')