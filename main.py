"""x=int(input("Ingrese dato: "))
y=int(input("Ingrese dato: "))
print(x+y)
#comentarios

a=3

if a>3:
    print("hola")
    print("mundo")
elif a<5:
    print("No es menor")
else:
    print("No es mayor")"""
"""a=3
b=4"""
""" while a==7:
    print("Estoy en el while")
    a=int(input("Ingrese el valor de a: "))
    if a !=7:
        break """

"""if a==3 and b==4:
    print("es correcto")"""

#for i in range(0,5):
    #print(i)

num1 = int(input("num 1: "))
num2 = int(input("num 2: "))


while True:
    opcion = input("Ingrese S - suma. R - resta. M - multiplicacion. D -division ")
    if opcion=='S':
        print(num1+num2)
        break
    elif opcion=='R':
        print(num1-num2)
        break
    elif opcion=='M':
        if num==0:
            print("no se puede realizar la division por 0, intenet de nuevo")
        else:
            print(num1*num2)
        break
    elif opcion=='D':
        print(num1/num2)
        break
    else:
        print(input("opcion no valida"))



