## operadores de pertenencia

nombres = ["erik", "jonathan", "miguel"]

print("erik" in nombres)
print("perro" not in nombres)

pais = {"juan":"Honduras", "ramon":"China"}

## solo funciona sobre las llaves de una diccionario
## no se puede usar sobre los valores
print("ramon" in pais)


## Operadores logicos

# and
# or
# not


## operadores de identidad

# is
# is not


## Ejemplos de operadores lógicos
edad = 25
tiene_licencia = True

# and - ambas condiciones deben ser verdaderas
puede_conducir = (edad >= 18) and (tiene_licencia)
print(f"¿Puede conducir? {puede_conducir}")

# or - al menos una condición debe ser verdadera
es_fin_de_semana = False
es_feriado = True
puede_descansar = (es_fin_de_semana or es_feriado)
print(f"¿Puede descansar? {puede_descansar}")

# not - invierte el valor booleano
esta_lloviendo = False
puede_salir = not esta_lloviendo
print(f"¿Puede salir? {puede_salir}")


## Ejemplos de operadores de identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

# is - verifica si son el mismo objeto en memoria
print(f"lista1 is lista2: {lista1 is lista2}")  # False (diferentes objetos)
print(f"lista1 is lista3: {lista1 is lista3}")  # True (mismo objeto)

# is not - verifica si NO son el mismo objeto
print(f"lista1 is not lista2: {lista1 is not lista2}")  # True

# Comparación con == (compara valores, no identidad)
print(f"lista1 == lista2: {lista1 == lista2}")  # True (mismos valores)