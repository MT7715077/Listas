conjunto_colores = {"rojo " ,"verde" , "azul"}


print(conjunto_colores )

for color in conjunto_colores:
    print(color)


    #  Muestra la informacion desordenada

print(len(conjunto_colores))    

conjunto_colores.add("negro")
print(conjunto_colores)

conjunto_colores.remove("verde")
print(conjunto_colores)