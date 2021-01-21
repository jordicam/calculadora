#####DEFINICION
def getnumber():
    valor1 = float(input('Enter your input number 1:'))
    valor2 = float(input('Enter your input number 2:'))
    return valor1, valor2 #####!!!!!!!


def getoperacion():
    operacion = input('Qué operación quieres hacer?')
    return(operacion)


def seleccion():
    print("1. Banco\n 2. Calculadora\n 3. Salir")
    select = int(input('Qué quieres hacer?'))
    return select
