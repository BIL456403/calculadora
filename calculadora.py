import sys

class Calculadora:
    def multiplicar(self, num1, num2):
        try:
            resultado = float(num1) * float(num2)
            return resultado
        except ValueError:
            return "Por favor, ingresa dos números válidos."

if __name__ == "__main__":
    if len(sys.argv) == 3:
        num1 = sys.argv[1]
        num2 = sys.argv[2]
        calc = Calculadora()
        print(f"El resultado de la multiplicación es: {calc.multiplicar(num1, num2)}")
    else:
        print("Por favor, ingrese dos números como parámetros.")
