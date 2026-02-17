edad = 90
nacionalidad = "suecia"

acceso = [40, 45, 50, 60, 70]
pais = ["china", "corea", "suecia"]

if edad in acceso:
  print("Pase papa")
elif edad not in acceso and nacionalidad in pais:
  print(f"exelente rey, ustes es bienbenido hermano de {nacionalidad}")
else:
  print("No puede pasar papa")

