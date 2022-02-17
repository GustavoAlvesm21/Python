x = int(input("DIGITA O X CARAI--> "))
y = int(input("DIGITA O Y CARAI--> "))

print("1 -> ADICIONA PAI\n 2 -> MENOS É MAIS \n 3 -> MULTIPLICA SENHOR \n 4 -> SOCIALISMO")

sel_op =int(input(" OQ TU QUER FAZER HEIN--> "))

if sel_op == 1:
    resultado = x + y 
elif sel_op == 2: 
    resultado = x - y
elif sel_op == 3:
    resultado = x * y
else: 
    resultado = x / y 

print("TOMA A RESPOSTA BURRAO--> "+str(resultado))
