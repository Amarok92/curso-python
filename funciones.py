# def hello(nombre):
#     print("Hola " + nombre)

# hello("Andres")

# def comoestas(saludo="no quiero "):
#     print("como estas " + saludo)

# comoestas("Hoy")
# comoestas()

# def add(numeroOne, numeroDos):
#      return numeroOne + numeroDos

# print(add(10, 30))
# print(add(600, 30))

add = lambda numeroOne, numeroDos: numeroOne + numeroDos
print(add(10, 30))