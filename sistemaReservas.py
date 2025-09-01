class Cine:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.asientos = [False] * capacidad

    def mostrar_asientos(self):
        print("\nEstado de los asientos:")
        for i in range(self.capacidad):
            estado = "Ocupado" if self.asientos[i] else "Libre"
            print("Asiento " + str(i+1) + ": " + estado)

    def reservar(self, num):
        if num < 1 or num > self.capacidad:
            print("Numero fuera de rango.")
        elif self.asientos[num-1]:
            print("Ese asiento ya esta ocupado.")
        else:
            self.asientos[num-1] = True
            print("Asiento " + str(num) + " reservado con exito.")


def main():
    cine = Cine(5)  
    while True:
        print("\nMENU DE RESERVAS")
        print("1. Mostrar asientos")
        print("2. Reservar asiento")
        print("3. Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            cine.mostrar_asientos()
        elif opcion == "2":

            try:
                num = int(input("Numero de asiento a reservar: "))
                cine.reservar(num)
            except ValueError:
                print("Debes ingresar un numero valido.")
        elif opcion == "3":
            print("Gracias por usar el sistema de reservas. Hasta luego.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
