
nombres = ["chico", "jose", "ramon"]
paises = ["china", "portugal", "corasao"]

def saludos(nombre, pais):
  for i in range(3):
    print(f"su nombre: {nombre[i]} su pais {pais[i]}")

print("\n--- Ejemplo con ciclo for ---")
saludos(nombres, paises)


## un ejemplo usando while y un contador
## lo mismo que con for pero agregando un 
## poco de complejidad inesaria 
    
numeros = [10, 20, 30, 40]
colores = ["rojo", "verde", "azul", "amarillo"]

def combinar_listas_while(lista1, lista2):
  i = 0
  while i < len(lista1):
    print(f"Número: {lista1[i]}, Color: {lista2[i]}")
    i += 1

print("\n--- Ejemplo con ciclo while ---")
combinar_listas_while(numeros, colores)