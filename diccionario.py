diccionario_colores = {"red":"rojo", "blue": "azul", "yellow": "amarillo"}
print(diccionario_colores)
print(diccionario_colores["red"])
print(diccionario_colores["yellow"])
diccionario_colores["black"]="negro"
print(diccionario_colores)


diccionario_colores.pop("yellow")
print(diccionario_colores)


del(diccionario_colores["black"])
print(diccionario_colores)

