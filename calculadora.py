####IMPORTS
from calculadora_utils.inputs import seleccion
from calculadora_utils.run import calculadora_run

def main():
    select = seleccion()
    while select != 3:
        if select == 1:
            pass
        elif select == 2:
            resultado = calculadora_run()
            print(f"El resultado de la calculadora es: {resultado}")
        select= seleccion()



####EJECUTO
if __name__ == "__main__":
    value = main()

