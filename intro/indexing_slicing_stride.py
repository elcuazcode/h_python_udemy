#indexing
nombres = ["Juan", "Pedro", "Hemilio", "Chus"]
print(nombres[1])

tuplas = ("juan", "pedro", "hemilio", "chus")
print(nombres[-1])

origen = {
  "chepe": "Guatemala",
  "jose": "El Salvador",
  "mario": "Panama",
  "kike": "Canada"
}

print(origen["kike"])

## Slicing
nombres = ["Juan", "Pedro", "Hemilio", "Chus"]
## Elegir un rango hasta donde deba imprimirse
print(nombres[0:])


tuplas = ("juan", "pedro", "hemilio", "chus")
print(nombres[2:])


## stride

# Stride con lista
nombres = ["Juan", "Pedro", "Hemilio", "Chus"]
print(nombres[::2])  # cada 2 elementos

# Stride con tupla
tuplas = ("juan", "pedro", "hemilio", "chus")
print(tuplas[1::2])  # comenzar en índice 1, cada 2 elementos

# Stride inverso
print(nombres[::-1])  # invertir lista