a = int(input("Inserir a quantidade de experimentos: "))

c = 0 
r = 0
s = 0

print("Inserir os experimentos:")
for x in range(a):
    exp =(input().split())

    a,b = exp

    if b == 'C':
        c = c + 1
    elif b == 'R':
        r = r + 1 
    else:
        s = s + 1

total = c + r + s
ps = s * total / 100
pr = r * total / 100
pc = c * total / 100

print("Total: %d cobaias" %total)
print("Coelhos:" %c)
print("Ratos:" %r)
print("Sapos:" %format.s)
print("Percentual de coelhos: %d" %pc)
print("Percentual de ratos: %d" %pr)
print("Percentual de sapos: %d" %ps)