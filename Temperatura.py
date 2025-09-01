class Invernadero:
    def __init__(self):
        pass

    def ejecutar(self):
        print("\nControl de temperatura en un invernadero.")
        while True:
            temp = float(input("Ingrese temperatura: "))
            if temp < 10:
                print("Calefactor encendido")
            elif temp <= 25:
                print("Sistema inactivo")
            else:
                print("Ventilador encendido")

            otra = input("¿Desea continuar?: ")
            if otra.lower() != "si":
                break

class Menu:
    def mostrar(self):
        while True:
            print("\n--- MENU INVERNADERO ---")
            print("1. Ejecutar Control de Temperatura")
            print("2. Repetir menu")
            print("3. Salir")

            opcion = input("Seleccione: ")
            if opcion == "1":
                Invernadero().ejecutar()
            elif opcion == "2":
                continue
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida.")

if __name__ == "__main__":
    Menu().mostrar()
