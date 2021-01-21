from calculadora_utils.inputs import getnumber, getoperacion
from calculadora_utils.operaciones import suma, resta

def calculadora_run():
    valor1, valor2 = getnumber()
    operacion = getoperacion()

    #### "" --> str no "" --> variable ##CONDICIONALES
    if operacion == "suma":
        resultado = suma(valor1, valor2)
    elif operacion == "resta":
        resultado = resta(valor1, valor2)
    else:
        resultado = ""
        print("error_valor")
    return(resultado)  
