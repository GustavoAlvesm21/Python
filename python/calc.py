# Calculadora igual a outra mas em python.

import math 

def baskhara(a,b,c):
    
    d = b*b - 4*a*c 

    if d < 0:
        
        print("Erro, delta negativo")
    
    else:

        x1 = (-b + math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a

        print("x1: %d \n x2: %d" %(x1,x2))     

###################################################################################

def elevar(a,b):

    for i in range (b):

        r = a * a 
        r = r * a

    print("%d" %r) 

###################################################################################

print("1 - adicao \n 2 - subtracao \n 3 - multiplicacao \n 4 - divicao \n 5 - bhaskara \n 6 - Raiz \n 7 - Elevar a 2 \n 8 - Elevar B em A \n")

s = int(input("Operação: "))

if s == 1:
    
    a = int(input("A:"))
    b = int(input("B:"))

    r = a + b 

    print("Resp: %d" %r)

elif s == 2: 
    
    a = int(input("A:"))
    b = int(input("B:"))

    r = a - b 

    print("Resp: %d" %r)

elif s == 3:

    a = int(input("A:"))
    b = int(input("B:"))

    r = a * b 

    print("Resp: %d" %r)

elif s == 4:

    a = int(input("A:"))
    b = int(input("B:"))

    r = a / b 

    print("Resp: %d" %r)

elif s == 5: 

    a = int(input("A:"))
    b = int(input("B:"))
    c = int(input("C:"))

    r = baskhara(a,b,c)

elif s == 6:

    a = int(input("A:"))
    
    r = math.sqrt(a)

    print("resp: %d" %r)

elif s == 7: 

    a = int(input("A:"))
    
    r = a * a 

    print("resp: %d" %r)

elif s == 8:

    a = int(input("A:"))
    b = int(input("B:"))

    r = elevar(a,b)

else:

    print("Operação invalida")     