print("Vamos a elegir una forma para saber su Perimetro y su Area")
print("1. Cuadrado 2. Circulo 3. Triangulo 4. Rectangulo")

seleccion=(input("Decime sobre que figura queres tener informacion indicando su numero:"))
cuadrado = 1
circulo = 2
triangulo = 3
rectangulo = 4

if seleccion == "1":
#Cuadrado
    print("CUADRADO")
    print("Necesitaria un dato!")
#Datos a pedir
    lado=int(input("Medida del lado del cuadrado en metros(solo numero): "))
#Operaciones
    perimetro=lado * 4
    area= lado * lado
#Resultado
    print("El perimetro es:")
    print(perimetro)
    print("El area es:")
    print(area)
elif seleccion == "2":
#Circulo
    print("CIRCULO!")
#Datos a pedir
    print("Un numerito por favor!")
    diametro=int(input("Medida de diametro de la circunferencia: "))
#Operaciones
    circunferencia= 3.14 * diametro
    area= (diametro/2) * 3.14 **2
#Resultado
    print("El perimetro es:")
    print(circunferencia)
    print("El area es:")
    print(area)
elif seleccion == "3":
#Triangulo
    print("TRIANGULO!")
#Datos a pedir
    print("Antes de empezar necesito algunos numeritos!")
    lado1=int(input("El primer lado del triangulo: "))
    lado2=int(input("El segundo lado del triangulo: "))
    base=int(input("La base del triangulo: "))
#Operaciones
    perimetro= lado1 + lado2 + base
    area= ((lado1**2) - (base/2)**2)/2.0
#Resultado
    print("El perimetro es:")
    print(perimetro)
    print("El area es:")
    print(area)
elif seleccion == "4":
    print("RECTANGULO")
#Datos a pedir
    print("Pasame los datos!")
    alt= int(input("La altura es de: "))
    base= int(input("La base mide: "))
#Operaciones
    per=alt*2 + base*2
    area= base * alt
#Resultado
    print("El perimetro es:")
    print(per)
    print("El area es:")
    print(area)


