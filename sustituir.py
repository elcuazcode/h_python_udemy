## Sustituir sobre una lista
nombres = ["Juan", "Pedro", "Hemilio", "Chus"]
nombres[0] = "CHONITO"
print(nombres)

## No se puede sobre una lista
tuplas = ("juan", "pedro", "hemilio", "chus")


## Utilizando la clava cambiar un dato sobre el diccionario
origen = {
  "chepe": "Guatemala",
  "jose": "El Salvador",
  "mario": "Panama",
  "kike": "Canada"
}

origen["kike"] = "MAZATENANGO"
print(origen)
