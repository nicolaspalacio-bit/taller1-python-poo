class saludo:
    def __init__(self, dato_texto):
        self.mensaje = dato_texto
        print(self.mensaje)

    def get_mensaje(self):
        return self.mensaje
    

    def set_atributo(self, dato_nuevo_mensaje):
        self.mensaje = dato_nuevo_mensaje

    
    def tomar_nombre(self):
        nombre_usuario = input ("escriba el nombre del usuario: ")
        return nombre_usuario
    
    def hacer_mensaje(self, dato_usuario):
        self.mensaje = "hola usuario" + dato_usuario
        #imprimir_mensaje(self.mensaje)
    
    def imprimir_mensaje(self, dato_mensaje):
        print(dato_mensaje)

        #********************* codigo principal ********************#
texto = "hola usuario"
obj_mensaje = saludo(texto)
aux_dato = obj_mensaje.tomar_nombre()
obj_mensaje.hacer_mensaje(aux_dato)

