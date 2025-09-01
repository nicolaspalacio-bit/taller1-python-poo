class FizzBuzz:
    def __init__(self):
        pass

    def ejecutar(self):
        print("\nEste programa imprime los numeros del 1 al 100.")
        print("Si son divisibles por 3: Fizz, por 5: Buzz, por ambos: FizzBuzz.")
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

class Menu:
    def mostrar(self):
        while True:
            print("\n--- MENU FIZZBUZZ ---")
            print("1. Ejecutar FizzBuzz")
            print("2. Repetir menu")
            print("3. Salir")

            opcion = input("Seleccione: ")
            if opcion == "1":
                FizzBuzz().ejecutar()
            elif opcion == "2":
                continue
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida.")

if __name__ == "__main__":
    Menu().mostrar()
