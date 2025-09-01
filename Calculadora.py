class Calculadora:
    def __init__(self):
        pass

    def ejecutar(self):
        print("\nEste programa realiza operaciones basicas (+, -, *, /).")
        while True:
            num1 = float(input("Ingrese primer numero: "))
            num2 = float(input("Ingrese segundo numero: "))
            op = input("Operacion (+, -, *, /): ")

            if op == "+":
                print("Resultado:", num1 + num2)
            elif op == "-":
                print("Resultado:", num1 - num2)
            elif op == "*":
                print("Resultado:", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("No se puede dividir entre 0")
            else:
                print("Operacion no valida.")

            otra = input("¿Desea continuar? (s/n): ")
            if otra.lower() != "s":
                break

class Menu:
    def mostrar(self):
        while True:
            print("\n--- MENU CALCULADORA ---")
            print("1. Ejecutar Calculadora")
            print("2. Repetir menu")
            print("3. Salir")

            opcion = input("Seleccione: ")
            if opcion == "1":
                Calculadora().ejecutar()
            elif opcion == "2":
                continue
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida.")

if __name__ == "__main__":
    Menu().mostrar()
