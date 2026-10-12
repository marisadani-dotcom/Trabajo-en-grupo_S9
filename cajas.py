# reto1_bodega.py

def mostrar_menu():
    print("\n--- SISTEMA DE CONTROL DE BODEGA (PILAS) ---")
    print("1. Apilar caja")
    print("2. Desapilar caja")
    print("3. Consultar tope")
    print("4. Mostrar pila y cantidad de cajas")
    print("5. Salir")

def main():
    pila_cajas = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            codigo = input("Ingrese el código único de la caja: ").strip()
            if not codigo:
                print("Error: El código no puede estar vacío.")
            elif codigo in pila_cajas:
                print(f"Error: El código '{codigo}' ya existe en la pila (duplicado).")
            else:
                pila_cajas.append(codigo)
                print(f"Caja '{codigo}' apilada exitosamente.")
                
        elif opcion == "2":
            if not pila_cajas:
                print("Error: No se puede desapilar, la pila está vacía.")
            else:
                caja_retirada = pila_cajas.pop()
                print(f"Caja retirada del tope: {caja_retirada}")
                
        elif opcion == "3":
            if not pila_cajas:
                print("La bodega está vacía. No hay tope.")
            else:
                print(f"Caja en el tope de la pila: {pila_cajas[-1]}")
                
        elif opcion == "4":
            if not pila_cajas:
                print("La pila de cajas está vacía.")
            else:
                print("Pila actual (base a tope):", pila_cajas)
                print(f"Cantidad total de cajas en la bodega: {len(pila_cajas)}")
                
        elif opcion == "5":
            print("Saliendo del sistema de bodega. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor ingrese un número entre 1 y 5.")

if __name__ == "__main__":
    main()