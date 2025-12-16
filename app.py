
import json

#CARGAR EMPLEADOS DESDE EL ARCHIVO JSON

with open("empleados.json", "r", encoding="utf-8") as f :
    empleados = json.load(f)




while True:

    # MENÚ PRINCIPAL


    print("\nMENÚ PRINCIPAL")
    print("1. Ver lista completa")
    print("2. Añadir nuevo empleado")
    print("3. Salir")
    print("4. Eliminar empleado")

    opcion = input("Elige una opción (1-4): ")
    print("Has elegido", opcion)

    # OPCIÓN 1: VER EMPLEADOS


    if opcion == "1":
            print("\nLista actual de empleados: ")
            print("-----------------------------")

            for empl in empleados:
                print("Nombre:", empl["Nombre"])
                print("Edad:", empl["Edad"])
                print("Puesto:", empl["Puesto"])
                print("-----------------------------")

    # OPCIÓN 2: AÑADIR EMPLEADO


    elif opcion == "2":
        print("\nVamos a añadir un nuevo empleado\n")

        # PEDIMOS DATOS AL USUARIO


        nuevo_nombre = input("Nombre del nuevo empleado: ")
        nueva_edad = int(input("Edad: "))
        nuevo_puesto = input("Puesto: ")

        # CREAMOS EL DICCIONARIO


        nuevo_empleado = {
            "Nombre": nuevo_nombre,
            "Edad": nueva_edad,
            "Puesto": nuevo_puesto
        }

        # LO AÑADIMOS A LA LISTA


        empleados.append(nuevo_empleado)

        with open("empleados.json", "w", encoding="utf-8") as f:
            json.dump(empleados, f, indent =4, ensure_ascii=False)

        print("\nEmpleado añadido con éxito.\n")
        print("Lista actualizada de empleados:")
        print("---------------------------------")

        for empl in empleados:
            print("Nombre:", empl["Nombre"])
            print("Edad:", empl["Edad"])
            print("Puesto:", empl["Puesto"])
            print("-----------------------------")

    # OPCIÓN 3: SALIR


    elif opcion == "3":
        print("\nSaliendo del programa...")
        break  # Se rompe el bucle y termina

    # Opcion 4: eliminar empleado

   
    elif opcion == "4":
        print("\nEliminar empleado\n")


        # Mostrar lista numerada

        for i, empl in enumerate(empleados):
            print(i, "-", empl["Nombre"])

        numero = int(input("Introduce el numero del empleado que quieres eliminar: " ))

        
        #Eliminarlo de la lista


        eliminado = empleados.pop(numero)
        print(f"\nEmpleado '{eliminado['Nombre']}' eliminado con éxito.\n")
                                       

    # Guardar cambio en JSON


        with open("empleados.json", "w", encoding="utf-8") as f:
            json.dump(empleados, f, indent=4, ensure_ascii=False)



    # OPCIÓN INVÁLIDA


    else:       
        print("\nOpción no válida. Inténtalo de nuevo.")


