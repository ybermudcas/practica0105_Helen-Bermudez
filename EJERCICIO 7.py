peso = input ("¿Cuál es tu peso en Kg?")
altura = input ("¿Cuál es tu altura en metros?")
imc = round(float(peso)/float(altura)**2,2)
print ("Tu índice de masa corporal es" , str(imc))