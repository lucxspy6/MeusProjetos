from random import randint


vitorias = 0

while True:
    num_comp = randint(0, 10)
    meu_num = int(input('Digite um valor: '))
    par_ou_impar = input('Par ou ímpar? ').upper().strip()
    print(f'Eu digitei {num_comp}.')
    soma = num_comp + meu_num
    if soma % 2 == 0:  
        if par_ou_impar in 'PAR':  
            print('Você ganhou.')
        else:  
            break
    else:   
        if par_ou_impar in 'IMPAR':  
            print('Você ganhou')
        else:  
            break 
    
    vitorias += 1

print('Você perdeu')
print(f'Você ganhou {vitorias} vezes seguidas. ')