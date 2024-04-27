#Ejercicio 1

nom = input ("ingrese su nombre")
apellido = input("ingrese su apellido")
apellido2  = input("ingrese su segundo apellido")

print("bienbenido estimado", nom, apellido, apellido2)

#ejercicio 2 

num = int (input("ingrese un numero entero"))
num2 = int (input("ingrese un numero entero"))

operación = input ("ingrese que operación quiere realizar: 1.suma, 2.resta, 3.multiplicación, 4.divición")

if operación == 1 :
     suma = num+num2
     print ("el resultado de la suma es", suma)
