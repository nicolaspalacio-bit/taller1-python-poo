class AireAcondicionado:
    def __init__(self):
        pass

    def ejecutar(self):
        print("\nEl aire se enciende si la temperatura es mayor a 28°C y la humedad mayor a 60%,")
        print("o si la temperatura es mayor a 30°C sin importar la humedad.")
        while True:
            temp = float(input("Temperatura: "))
            hum = float(input("Humedad: "))

            if (temp > 28 and hum > 60) or temp > 30:
                print("Aire acondicionado encendido")
            else:
                print("Aire acondicionado apagado")

            seguir = input("¿Desea continuar?: ")
            if seguir.lower() != "s":
                break

class Menu:
    def mostrar(self):
        while True:
            print("\n--- MENU AIRE ACONDICIONADO ---")
            print("1. Ejecutar control de aire")
            print("2. Repetir menu")
            print("3. Salir")

            opcion = input("Seleccione: ")
            if opcion == "1":
                AireAcondicionado().ejecutar()
            elif opcion == "2":
                continue
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida.")

if __name__ == "__main__":
    Menu().mostrar()
