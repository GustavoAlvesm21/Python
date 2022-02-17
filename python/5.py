
x = int(input("Digite sua idade em dias -> "))

a = x / 365 
m = (x % 365) / 30 
d = m = (x % 365) % 30

print(" %d ano(s)\n %d meses(s)\n %d dia(s)"%(a,m,d))