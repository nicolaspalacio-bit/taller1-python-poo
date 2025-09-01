class AccesoTienda:
    def __init__(self):
        pass

    def ejecutar(self):
        print("\nAcceso permitido solo con membresia valida y en horario de atencion, o si es empleado.")
        while True:
            membresia = input("Tiene membresia?: ") == "si"
            horario = input("Es horario de atencion?: ") == "si"
            empleado = input("Es empleado?: ") == "si"

            if (membresia and horario) or empleado:
                print("Acceso permitido")
            else:
                print("Acceso denegado")

            seguir = input("¿Desea continuar?: ")
            if seguir.lower() != "si":
                break

class Menu:
    def mostrar(self):
        while True:
            print("\n--- MENU ACCESO TIENDA ---")
            print("1. Ejecutar control de acceso")
            print("2. Repetir menu")
            print("3. Salir")

            opcion = input("Seleccione: ")
            if opcion == "1":
                AccesoTienda().ejecutar()
            elif opcion == "2":
                continue
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida.")

if __name__ == "__main__":
    Menu().mostrar()
