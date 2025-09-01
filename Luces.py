class Luces:
    def __init__(self):
        pass

    def ejecutar(self):
        print("\nControl de luces: Se encienden si es de noche y hay movimiento.")
        while True:
            noche = input("Es de noche?: ") == "si"
            movimiento = input("Hay movimiento?: ") == "si"

            if noche and movimiento:
                print("Luces encendidas")
            else:
                print("Luces apagadas")

            seguir = input("¿Desea continuar?: ")
            if seguir.lower() != "si":
                break

class Menu:
    def mostrar(self):
        while True:
            print("\n--- MENU LUCES ---")
            print("1. Ejecutar control de luces")
            print("2. Repetir menu")
            print("3. Salir")

            opcion = input("Seleccione: ")
            if opcion == "1":
                Luces().ejecutar()
            elif opcion == "2":
                continue
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida.")

if __name__ == "__main__":
    Menu().mostrar()
