from granja import Granja
from cultivo import Cultivo
from animal import Animal
from datetime import datetime # Para la fecha en el reporte

#Funciones auxiliares para entrada de datos
def solicitar_dato(mensaje, tipo_dato=str, permitir_vacio_edicion=False):
    """Solicita un dato al usuario, con validación de tipo y opción para permitir vacío en edición."""
    while True:
        valor_str = input(mensaje).strip()
        if permitir_vacio_edicion and valor_str == "":
            return None # Indica que no se quiere cambiar este valor
        
        if not valor_str and not permitir_vacio_edicion and tipo_dato is str : # Para str no permitir vacio al crear
             print("Este campo no puede estar vacío.")
             continue

        if tipo_dato == float:
            try:
                valor_num = float(valor_str)
                if valor_num < 0:
                    print("El valor numérico no puede ser negativo. Intente de nuevo.")
                    continue
                return valor_num
            except ValueError:
                print("Entrada inválida. Se esperaba un número (ej: 10.5). Intente de nuevo.")
        elif tipo_dato == int: # Aunque no lo usamos mucho, por completitud
            try:
                valor_num = int(valor_str)
                if valor_num < 0:
                    print("El valor numérico no puede ser negativo. Intente de nuevo.")
                    continue
                return valor_num
            except ValueError:
                print("Entrada inválida. Se esperaba un número entero. Intente de nuevo.")
        elif tipo_dato == str:
            return valor_str # Ya se validó que no esté vacío si es necesario

def mostrar_menu_principal(nombre_granja):
    print(f"\n--- Menú Principal - Granja {nombre_granja} ---")
    print(f"--- Fecha y Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    print("1. Gestionar Cultivos")
    print("2. Gestionar Animales")
    print("3. Generar Reporte de Producción Total")
    print("4. Salir")

def mostrar_submenu(tipo_entidad_plural):
    print(f"\n--- Menú Gestionar {tipo_entidad_plural} ---")
    print(f"1. Agregar {tipo_entidad_plural[:-1] if tipo_entidad_plural.endswith('s') else tipo_entidad_plural}") # Singulariza simple
    print(f"2. Editar {tipo_entidad_plural[:-1] if tipo_entidad_plural.endswith('s') else tipo_entidad_plural}")
    print(f"3. Eliminar {tipo_entidad_plural[:-1] if tipo_entidad_plural.endswith('s') else tipo_entidad_plural}")
    print(f"4. Listar {tipo_entidad_plural}")
    print("5. Volver al Menú Principal")


def gestionar_cultivos(granja_obj):
    while True:
        mostrar_submenu("Cultivos")
        opcion = input("Seleccione una opción para Cultivos: ").strip()

        if opcion == '1': # Agregar Cultivo
            print("\n-- Agregar Nuevo Cultivo --")
            nombre = solicitar_dato("Nombre del cultivo: ")
            if granja_obj.consultar_cultivo(nombre):
                print(f"Error: Ya existe un cultivo con el nombre '{nombre}'. No se puede agregar.")
                continue
            tipo = solicitar_dato("Tipo de cultivo (Ej: Grano, Hortaliza): ")
            area = solicitar_dato("Área de cultivo (hectáreas, ej: 10.5): ", float)
            rendimiento = solicitar_dato("Rendimiento por hectárea (ej: 5000): ", float)
            nuevo_cultivo = Cultivo(nombre, tipo, area, rendimiento)
            granja_obj.agregar_cultivo(nuevo_cultivo)

        elif opcion == '2': # Editar Cultivo
            print("\n-- Editar Cultivo --")
            nombre_buscar = solicitar_dato("Nombre del cultivo a editar: ")
            cultivo_existente = granja_obj.consultar_cultivo(nombre_buscar)
            if cultivo_existente:
                print(f"Editando: {cultivo_existente}")
                print("Deje el campo en blanco y presione Enter si no desea cambiar un valor.")
                nuevo_tipo = solicitar_dato(f"Nuevo tipo (actual: {cultivo_existente.get_tipo()}): ", permitir_vacio_edicion=True)
                nueva_area_str = input(f"Nueva área (actual: {cultivo_existente.get_area_cultivo()} ha): ").strip()
                nueva_area = None
                if nueva_area_str: nueva_area = solicitar_dato(f"Confirme nueva área '{nueva_area_str}': ", float)

                nuevo_rend_str = input(f"Nuevo rendimiento/ha (actual: {cultivo_existente.get_rendimiento_por_hectarea()}): ").strip()
                nuevo_rend = None
                if nuevo_rend_str: nuevo_rend = solicitar_dato(f"Confirme nuevo rendimiento '{nuevo_rend_str}': ", float)
                
                granja_obj.editar_cultivo(nombre_buscar, nuevo_tipo, nueva_area, nuevo_rend)
            else:
                print(f"Cultivo '{nombre_buscar}' no encontrado.")

        elif opcion == '3': # Eliminar Cultivo
            print("\n-- Eliminar Cultivo --")
            nombre_eliminar = solicitar_dato("Nombre del cultivo a eliminar: ")
            granja_obj.eliminar_cultivo(nombre_eliminar)

        elif opcion == '4': # Listar Cultivos
            granja_obj.listar_cultivos()

        elif opcion == '5': # Volver
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def gestionar_animales(granja_obj):
    while True:
        mostrar_submenu("Animales")
        opcion = input("Seleccione una opción para Animales: ").strip()

        if opcion == '1': # Agregar Animal
            print("\n-- Agregar Nuevo Animal --")
            id_animal = solicitar_dato("Identificador del animal (Ej: V001): ")
            if granja_obj.consultar_animal(id_animal):
                print(f"Error: Ya existe un animal con el ID '{id_animal}'. No se puede agregar.")
                continue
            especie = solicitar_dato("Especie (Ej: Bovino, Porcino): ")
            raza = solicitar_dato("Raza (Ej: Holstein, Duroc): ")
            edad = solicitar_dato("Edad (años, ej: 2.5): ", float)
            peso = solicitar_dato("Peso (kg, ej: 600.0): ", float)
            prod_ind = solicitar_dato("Producción individual (unidades, ej: 20): ", float)
            nuevo_animal = Animal(id_animal, especie, raza, edad, peso, prod_ind)
            granja_obj.agregar_animal(nuevo_animal)

        elif opcion == '2': # Editar Animal
            print("\n-- Editar Animal --")
            id_buscar = solicitar_dato("ID del animal a editar: ")
            animal_existente = granja_obj.consultar_animal(id_buscar)
            if animal_existente:
                print(f"Editando: {animal_existente}")
                print("Deje el campo en blanco y presione Enter si no desea cambiar un valor.")
                nueva_especie = solicitar_dato(f"Nueva especie (actual: {animal_existente.get_especie()}): ", permitir_vacio_edicion=True)
                nueva_raza = solicitar_dato(f"Nueva raza (actual: {animal_existente.get_raza()}): ", permitir_vacio_edicion=True)
                
                nueva_edad_str = input(f"Nueva edad (actual: {animal_existente.get_edad()} años): ").strip()
                nueva_edad = None
                if nueva_edad_str: nueva_edad = solicitar_dato(f"Confirme nueva edad '{nueva_edad_str}': ", float)

                nuevo_peso_str = input(f"Nuevo peso (actual: {animal_existente.get_peso()} kg): ").strip()
                nuevo_peso = None
                if nuevo_peso_str: nuevo_peso = solicitar_dato(f"Confirme nuevo peso '{nuevo_peso_str}': ", float)

                nueva_prod_str = input(f"Nueva producción individual (actual: {animal_existente.get_produccion_individual()}): ").strip()
                nueva_prod = None
                if nueva_prod_str: nueva_prod = solicitar_dato(f"Confirme nueva producción '{nueva_prod_str}': ", float)

                granja_obj.editar_animal(id_buscar, nueva_especie, nueva_raza, nueva_edad, nuevo_peso, nueva_prod)
            else:
                print(f"Animal con ID '{id_buscar}' no encontrado.")

        elif opcion == '3': # Eliminar Animal
            print("\n-- Eliminar Animal --")
            id_eliminar = solicitar_dato("ID del animal a eliminar: ")
            granja_obj.eliminar_animal(id_eliminar)

        elif opcion == '4': # Listar Animales
            granja_obj.listar_animales()

        elif opcion == '5': # Volver
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def main():
    nombre_granja = "La Rastrojera Rebelde"
    mi_granja = Granja(nombre_granja)
    print(f"¡Bienvenido al Sistema de Gestión de la Granja '{nombre_granja}'!")
    print(f"Fecha y Hora de inicio: {mi_granja.get_fecha_actual()}")


    while True:
        mostrar_menu_principal(nombre_granja)
        opcion_principal = input("Seleccione una opción del menú principal: ").strip()

        if opcion_principal == '1':
            gestionar_cultivos(mi_granja)
        elif opcion_principal == '2':
            gestionar_animales(mi_granja)
        elif opcion_principal == '3':
            mi_granja.generar_reporte_produccion()
        elif opcion_principal == '4':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción principal no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()