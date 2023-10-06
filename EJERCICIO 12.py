barrasdepan = int(input("Introduce el número de barras vendidas que no son del día"))
precio = 3.49
descuento = 0.6
print("Una barra del día cuesta " , precio , "€")
print("Barra de pan que no sea del día" , (descuento * 100) , "%")
print("Ganancia final" , (barrasdepan * (precio - descuento)) , "€")