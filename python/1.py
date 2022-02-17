valor = int(input("Insira o valor: "))

notas_100 = valor / 100 
notas_50 = (valor % 100) / 50
notas_20 = ((valor % 100) % 50) / 20 
notas_10 = (((valor % 100) % 50) % 20) / 10
notas_5 = ((((valor % 100) % 50) % 20) % 10) / 5
notas_2 = (((((valor % 100) % 50) % 20) % 10) % 5) / 2
notas_1 = ((((((valor % 100) % 50) % 20) % 10) % 5) % 2) / 1

print("%d nota(s) de 100" %(notas_100))
print("%d nota(s) de 50" %(notas_50))
print("%d nota(s) de 20" %(notas_20))
print("%d nota(s) de 10" %(notas_10))
print("%d nota(s) de 5" %(notas_5))
print("%d nota(s) de 2" %(notas_2))
print("%d nota(s) de 1" %(notas_1))