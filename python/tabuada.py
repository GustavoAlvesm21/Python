# Gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.

x = int(input())

for i in range(11):
    r = x * i 
    print("%d X %d = %d"%(x,i,r)) 