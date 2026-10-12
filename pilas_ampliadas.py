# pila_acciones.py

acciones = []

def registrar_accion(descripcion):
    acciones.append(descripcion)
    print(f"Acción registrada: '{descripcion}'")

def deshacer():
    if not acciones:
        print("No existen acciones para deshacer.")
        return
    ultima = acciones.pop()
    print(f"Se deshizo la acción: '{ultima}'")

def historial():
    if not acciones:
        print("No hay acciones pendientes en el historial.")
    else:
        print("Acciones pendientes:", acciones)

def main():
    while True:
        print("\n--- MENÚ EDITOR DE TEXTO (DESHACER) ---")
        print("1. Registrar nueva acción")
        print("2. Deshacer última acción")
        print("3. Ver historial pendiente")
        print("4. Salir")
        
        opcion = input("Elija una opción (1-4): ").strip()
        
        if opcion == "1":
            desc = input("Descripción de la acción: ").strip()
            if desc:
                registrar_accion(desc)
            else:
                print("La descripción no puede estar vacía.")
        elif opcion == "2":
            deshacer()
        elif opcion == "3":
            historial()
        elif opcion == "4":
            print("Saliendo del editor.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()