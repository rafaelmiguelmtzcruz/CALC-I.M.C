#Se le pide al usuario que ingrese su nombre 
nombre = input("Ingresa tu nombre(s): ")
while not nombre:
    nombre = input("Por favor, introduce tu nombre para poder continuar: ")

#Se le pide al usuario que ingrese su apellido paterno
apellido_paterno = input("Ingresa tu apellido paterno: ")
while not apellido_paterno:
    apellido_paterno = input("Porfavor, introduce tu apellido paterno para poder continuar: ")

#Se le pide al usuario que ingrese su apellido materno
apellido_materno = input("Ingresa tu apellido materno: ")
while not apellido_materno:
    apellido_materno = input("Por favor, introduce tu apellido materno para poder continuar: ")

#Se le pide al usuario que ingrese su edad
while True:
    try:
        edad = int(input("Por favor, ingresa tu edad: "))
        break
    except ValueError:
        print("(ERROR) Por favor, ingresa una edad válida.")

#Se le pide al usuario que ingrese su peso
while True:
    try:
        peso = float(input("Por favor, ingresa tu peso (en kilogramos): "))
        break
    except ValueError:
        print("(ERROR) Por favor, ingresa un peso válido.")

#Se le pide al usuario que ingrese su estatura
while True:
    try:
        estatura = float(input("Por favor, ingresa tu estatura (en metros): "))
        break
    except ValueError:
        print("(ERROR) Por favor, ingresa una estatura válida.")

#Se calcula el IMC
imc = peso / estatura ** 2

#Se muestra los datos ingresados por el usuario y su IMC
print("Tu nombre completo es:", nombre, apellido_paterno, apellido_materno)
print("Tu edad es:", edad, "años")
print("Tu peso es:", peso, "kilogramos")
print("Tu estatura es:", estatura, "metros")
print("Tu índice de masa corporal es:", imc)
