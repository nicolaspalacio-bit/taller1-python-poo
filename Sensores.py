class Seguridad:
    def __init__(self):
        self.alarma = False

    def ejecutar(self):
        print("\nSistema de seguridad: Se activa si al menos 2 sensores detectan movimiento y es de noche.")
        while True:
            s1 = input("Sensor 1: ") == "si"
            s2 = input("Sensor 2: ") == "si"
            s3 = input("Sensor 3: ") == "si"
            noche = input("Es de noche?: ") == "si"

            if (s1 + s2 + s3) >= 2 and noche:
                print("ALARMA ACTIVADA!")
            else:
                print("Todo en orden.")

            seguir = input("¿Desea continuar?: ")
            if seguir.lower() != "si":
                break

class Menu:
    def mostrar(self):
        while True:
            print("\n--- MENU SEGURIDAD ---")
            print("1. Ejecutar detección de intrusos")
            print("2. Repetir menu")
            print("3. Salir")

            opcion = input("Seleccione: ")
            if opcion == "1":
                Seguridad().ejecutar()
            elif opcion == "2":
                continue
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida.")

if __name__ == "__main__":
    Menu().mostrar()
