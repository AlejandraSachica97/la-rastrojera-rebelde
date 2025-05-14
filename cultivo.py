from produccion import Produccion

class Cultivo(Produccion):
 
    # Representa un cultivo en la granja.
    # Hereda de la clase Produccion.

    def __init__(self, nombre, tipo, area_cultivo, rendimiento_por_hectarea):
        super().__init__(nombre)
        self.__tipo = ""
        self.__area_cultivo = 0.0  # en hectáreas
        self.__rendimiento_por_hectarea = 0.0  # ej: kg/hectárea

        self.set_tipo(tipo)
        self.set_area_cultivo(area_cultivo)
        self.set_rendimiento_por_hectarea(rendimiento_por_hectarea)

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        if isinstance(tipo, str) and tipo.strip():
            self.__tipo = tipo
        else:
            print(f"Error al asignar tipo al cultivo '{self.get_nombre()}': El tipo no puede estar vacío.")
            # Podríamos asignar un valor por defecto o mantener el anterior si es una edición
            if not self.__tipo: self.__tipo = "Desconocido"


    def get_area_cultivo(self):
        return self.__area_cultivo

    def set_area_cultivo(self, area_cultivo):
        try:
            area = float(area_cultivo)
            if area >= 0:
                self.__area_cultivo = area
            else:
                print(f"Error al asignar área al cultivo '{self.get_nombre()}': El área no puede ser negativa.")
        except ValueError:
            print(f"Error al asignar área al cultivo '{self.get_nombre()}': El área debe ser un número.")

    def get_rendimiento_por_hectarea(self):
        return self.__rendimiento_por_hectarea

    def set_rendimiento_por_hectarea(self, rendimiento):
        try:
            rend_val = float(rendimiento)
            if rend_val >= 0:
                self.__rendimiento_por_hectarea = rend_val
            else:
                print(f"Error al asignar rendimiento al cultivo '{self.get_nombre()}': El rendimiento no puede ser negativo.")
        except ValueError:
            print(f"Error al asignar rendimiento al cultivo '{self.get_nombre()}': El rendimiento debe ser un número.")

    def calcular_produccion(self):
       # Calcula la producción total del cultivo y retorna: producción total (ej: en kg).
      
        return self.get_area_cultivo() * self.get_rendimiento_por_hectarea()

    def __str__(self):
        return (f"Cultivo: {self.get_nombre()} (Tipo: {self.get_tipo()}, "
                f"Área: {self.get_area_cultivo():.2f} ha, "
                f"Rendimiento/ha: {self.get_rendimiento_por_hectarea():.2f} unidades/ha, "
                f"Producción Total: {self.calcular_produccion():.2f} unidades)")