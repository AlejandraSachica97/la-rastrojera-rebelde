class Produccion:  
   # Clase base

    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            print("Error: El nombre no puede estar vacío.")

    def calcular_produccion(self):
       # Método abstracto que será implementado por las clases hijas.
        
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def __str__(self):
        return f"Entidad de Producción: {self.get_nombre()}"