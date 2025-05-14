from produccion import Produccion

class Animal(Produccion):
    """
    Representa un animal en la granja.
    Hereda de la clase Produccion. El 'nombre' de Produccion será el identificador del animal.
    """
    def __init__(self, nombre_identificador, especie, raza, edad, peso, produccion_individual):
        super().__init__(nombre_identificador)
        self.__especie = ""
        self.__raza = ""
        self.__edad = 0.0  # en años
        self.__peso = 0.0  # en kg
        self.__produccion_individual = 0.0 # ej: litros de leche/día, kg de carne total, huevos/semana

        self.set_especie(especie)
        self.set_raza(raza)
        self.set_edad(edad)
        self.set_peso(peso)
        self.set_produccion_individual(produccion_individual)

    def get_especie(self):
        return self.__especie

    def set_especie(self, especie):
        if isinstance(especie, str) and especie.strip():
            self.__especie = especie
        else:
            print(f"Error al asignar especie al animal '{self.get_nombre()}': La especie no puede estar vacía.")
            if not self.__especie: self.__especie = "Desconocida"


    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        if isinstance(raza, str) and raza.strip():
            self.__raza = raza
        else:
            print(f"Error al asignar raza al animal '{self.get_nombre()}': La raza no puede estar vacía.")
            if not self.__raza: self.__raza = "Desconocida"

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        try:
            edad_val = float(edad)
            if edad_val >= 0:
                self.__edad = edad_val
            else:
                print(f"Error al asignar edad al animal '{self.get_nombre()}': La edad no puede ser negativa.")
        except ValueError:
            print(f"Error al asignar edad al animal '{self.get_nombre()}': La edad debe ser un número.")

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        try:
            peso_val = float(peso)
            if peso_val >= 0:
                self.__peso = peso_val
            else:
                print(f"Error al asignar peso al animal '{self.get_nombre()}': El peso no puede ser negativo.")
        except ValueError:
            print(f"Error al asignar peso al animal '{self.get_nombre()}': El peso debe ser un número.")

    def get_produccion_individual(self):
        return self.__produccion_individual

    def set_produccion_individual(self, produccion):
        try:
            prod_val = float(produccion)
            if prod_val >= 0:
                self.__produccion_individual = prod_val
            else:
                print(f"Error al asignar producción al animal '{self.get_nombre()}': La producción no puede ser negativa.")
        except ValueError:
            print(f"Error al asignar producción al animal '{self.get_nombre()}': La producción debe ser un número.")

    def calcular_produccion(self):
        """
        Retorna la producción individual del animal.
        """
        return self.get_produccion_individual()

    def __str__(self):
        return (f"Animal ID: {self.get_nombre()} (Especie: {self.get_especie()}, "
                f"Raza: {self.get_raza()}, Edad: {self.get_edad():.1f} años, "
                f"Peso: {self.get_peso():.2f} kg, "
                f"Producción: {self.calcular_produccion():.2f} unidades)")