from random import shuffle
from time import sleep


print('\033[36m* SORTEADOR DE TIMES *\033[m')
names = input('Digite os nome dos jogadores: \n').split()
n1 = int(input('Quantos jogadores há no time 1? '))
n2 = int(input('Quantos jogadores há no time 2? '))

shuffle(names)

timeum = names[:n1]
timedois = names[n1:n1+n2]

def times(qual_time, quantos_jog, time):
    print('\033[1;35m===TIME{}===\033[m'.format(qual_time))
    for c in range(0, quantos_jog, +1):
        print(time[c])
    print('\033[1;35m=\033[m'*11, '\n')

times(1, n1, timeum)
sleep(1)
times(2, n2, timedois)