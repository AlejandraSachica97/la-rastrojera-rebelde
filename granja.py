from cultivo import Cultivo
from animal import Animal

class Granja:
    # Representa la granja y gestiona los cultivos y animales.
    # Utiliza composición para mantener listas de cultivos y animales.
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__cultivos = []
        self.__animales = []

    def get_nombre(self):
        return self.__nombre

    # --- Métodos para Cultivos ---
    def agregar_cultivo(self, cultivo):
        if isinstance(cultivo, Cultivo):
            if not self.consultar_cultivo(cultivo.get_nombre()): # Evitar duplicados por nombre
                self.__cultivos.append(cultivo)
                print(f"Cultivo '{cultivo.get_nombre()}' agregado a la granja.")
            else:
                print(f"Error: Ya existe un cultivo con el nombre '{cultivo.get_nombre()}'.")
        else:
            print("Error: Solo se pueden agregar objetos de la clase Cultivo.")

    def consultar_cultivo(self, nombre_cultivo):
        for cultivo in self.__cultivos:
            if cultivo.get_nombre().lower() == nombre_cultivo.lower():
                return cultivo
        return None

    def editar_cultivo(self, nombre_cultivo, nuevo_tipo=None, nueva_area=None, nuevo_rendimiento=None):
        cultivo_a_editar = self.consultar_cultivo(nombre_cultivo)
        if cultivo_a_editar:
            if nuevo_tipo is not None and nuevo_tipo.strip():
                cultivo_a_editar.set_tipo(nuevo_tipo)
            if nueva_area is not None: # La validación numérica se hace en el setter
                cultivo_a_editar.set_area_cultivo(nueva_area)
            if nuevo_rendimiento is not None: # La validación numérica se hace en el setter
                cultivo_a_editar.set_rendimiento_por_hectarea(nuevo_rendimiento)
            print(f"Cultivo '{nombre_cultivo}' actualizado.")
            return True
        print(f"Error: Cultivo '{nombre_cultivo}' no encontrado para editar.")
        return False

    def eliminar_cultivo(self, nombre_cultivo):
        cultivo_a_eliminar = self.consultar_cultivo(nombre_cultivo)
        if cultivo_a_eliminar:
            self.__cultivos.remove(cultivo_a_eliminar)
            print(f"Cultivo '{nombre_cultivo}' eliminado de la granja.")
            return True
        print(f"Error: Cultivo '{nombre_cultivo}' no encontrado para eliminar.")
        return False

    def listar_cultivos(self):
        print("\n--- Listado de Cultivos ---")
        if not self.__cultivos:
            print("No hay cultivos registrados.")
            return
        for c in self.__cultivos:
            print(c)

    def calcular_produccion_total_cultivos(self):
        total = 0
        for cultivo in self.__cultivos:
            total += cultivo.calcular_produccion()
        return total

    # --- Métodos para Animales ---
    def agregar_animal(self, animal_obj):
        if isinstance(animal_obj, Animal):
            if not self.consultar_animal(animal_obj.get_nombre()): # Evitar duplicados por ID
                self.__animales.append(animal_obj)
                print(f"Animal '{animal_obj.get_nombre()}' agregado a la granja.")
            else:
                print(f"Error: Ya existe un animal con el ID '{animal_obj.get_nombre()}'.")
        else:
            print("Error: Solo se pueden agregar objetos de la clase Animal.")

    def consultar_animal(self, nombre_identificador):
        for animal_obj in self.__animales:
            if animal_obj.get_nombre().lower() == nombre_identificador.lower():
                return animal_obj
        return None

    def editar_animal(self, nombre_identificador, nueva_especie=None, nueva_raza=None, nueva_edad=None, nuevo_peso=None, nueva_prod_individual=None):
        animal_a_editar = self.consultar_animal(nombre_identificador)
        if animal_a_editar:
            if nueva_especie is not None and nueva_especie.strip():
                animal_a_editar.set_especie(nueva_especie)
            if nueva_raza is not None and nueva_raza.strip():
                animal_a_editar.set_raza(nueva_raza)
            if nueva_edad is not None:
                animal_a_editar.set_edad(nueva_edad)
            if nuevo_peso is not None:
                animal_a_editar.set_peso(nuevo_peso)
            if nueva_prod_individual is not None:
                animal_a_editar.set_produccion_individual(nueva_prod_individual)
            print(f"Animal '{nombre_identificador}' actualizado.")
            return True
        print(f"Error: Animal '{nombre_identificador}' no encontrado para editar.")
        return False

    def eliminar_animal(self, nombre_identificador):
        animal_a_eliminar = self.consultar_animal(nombre_identificador)
        if animal_a_eliminar:
            self.__animales.remove(animal_a_eliminar)
            print(f"Animal '{nombre_identificador}' eliminado de la granja.")
            return True
        print(f"Error: Animal '{nombre_identificador}' no encontrado para eliminar.")
        return False

    def listar_animales(self):
        print("\n--- Listado de Animales ---")
        if not self.__animales:
            print("No hay animales registrados.")
            return
        for a in self.__animales:
            print(a)

    def calcular_produccion_total_ganado(self):
        total = 0
        for animal_obj in self.__animales:
            total += animal_obj.calcular_produccion()
        return total

    # --- Métodos Generales de la Granja ---
    def calcular_produccion_total_granja(self):
        produccion_cultivos = self.calcular_produccion_total_cultivos()
        produccion_ganado = self.calcular_produccion_total_ganado()
        return produccion_cultivos + produccion_ganado

    def generar_reporte_produccion(self):
        print(f"\n--- Reporte de Producción: {self.get_nombre()} ---")
        print(f"--- Fecha del Reporte: {self.get_fecha_actual()} ---") # Uso de nueva función
        print("\n** Cultivos **")
        if not self.__cultivos:
            print("No hay cultivos registrados.")
        else:
            for cultivo in self.__cultivos:
                # print(f"- {cultivo.get_nombre()}: {cultivo.calcular_produccion():.2f} unidades")
                print(f"- {cultivo}") # Usar __str__ para más detalle
        print(f"Producción Total de Cultivos: {self.calcular_produccion_total_cultivos():.2f} unidades")

        print("\n** Ganado **")
        if not self.__animales:
            print("No hay animales registrados.")
        else:
            for animal_obj in self.__animales:
                # print(f"- {animal_obj.get_nombre()} ({animal_obj.get_especie()}): {animal_obj.calcular_produccion():.2f} unidades")
                print(f"- {animal_obj}") # Usar __str__ para más detalle
        print(f"Producción Total de Ganado: {self.calcular_produccion_total_ganado():.2f} unidades")

        print("\n--------------------------------------------------")
        print(f"PRODUCCIÓN TOTAL DE LA GRANJA: {self.calcular_produccion_total_granja():.2f} unidades")
        print("--------------------------------------------------")

    def get_fecha_actual(self):
        from datetime import datetime
        # Asegurándonos que la fecha se actualice cada vez que se llama.
        # Formato: YYYY-MM-DD HH:MM:SS
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")