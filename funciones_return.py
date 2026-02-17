
## funcion que acepta valores
## los procesa y no solo regresa un valor
def proceso(a,b):
  suma = a + b
  resta = a - b
  return suma, resta ## si no que puede regresar varios



resultado1, resultado2 = proceso(5,10)   ## que podemos guardarlo dentro de variables separadas

print(resultado1)
print(resultado2)

## recibir varioss parametros
def datos_persona(nombre, edad, ciudad):
    saludo = f"Hola, soy {nombre}"
    info_edad = f"Tengo {edad} años"
    ubicacion = f"Vivo en {ciudad}"
    return saludo, info_edad, ubicacion  ## regresamos una tupla


## guardamos todo dentro de una variable
resultado = datos_persona("Carlos", 30, "Madrid")


## que despues recorremos
for valor in resultado:
    print(valor)