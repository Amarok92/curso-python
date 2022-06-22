#Escriba un programa que reciba el año del nacimiento de un usuario	y retorna su edad en años en el año 2022.

year = input("Digite el año de su nacimiento:")
edge = 2022 - int(year)
print(f'En el 2022 tienes {edge}.')

#Escriba un programa que reciba	las	informaciones sobre	el peso	(kilos)	y la altura	(metros)	 de un usuario e imprima su índice de masa corporal (IMC).Para obtener el IMC debemos dividir	el peso del usuario por su altura elevada al cuadrado.


peso= input("Digite su peso (kilos):")
altura= input("Digite su altura (metros):")
imc= float(peso)/(float(altura)**2)
print(f'Su IMC es {imc}.')

