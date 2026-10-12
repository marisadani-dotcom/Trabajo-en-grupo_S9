# reto3_atencion.py
from collections import deque

def mostrar_menu():
    print("\n--- SISTEMA DE ATENCIÓN AL CLIENTE (COLAS) ---")
    print("1. Registrar turno y cliente")
    print("2. Atender al siguiente cliente (FIFO)")
    print("3. Consultar próximo cliente sin retirarlo")
    print("4. Mostrar todos los clientes en espera")
    print("5. Mostrar cantidad de pendientes")
    print("6. Salir")

def main():
    cola_clientes = deque()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ").strip()
            if not nombre:
                print("Error: El nombre no puede estar vacío.")
            else:
                cola_clientes.append(nombre)
                print(f"Turno registrado para: {nombre}")
                
        elif opcion == "2":
            if not cola_clientes:
                print("La cola está vacía. No hay clientes para atender.")
            else:
                atendido = cola_clientes.popleft()
                print(f"Atendiendo ahora a: {atendido}")
                
        elif opcion == "3":
            if not cola_clientes:
                print("La cola está vacía.")
            else:
                print(f"Próximo cliente a ser atendido: {cola_clientes[0]}")
                
        elif opcion == "4":
            if not cola_clientes:
                print("No hay clientes en espera.")
            else:
                print("Clientes en espera (orden de llegada):")
                for i, cliente in enumerate(cola_clientes, 1):
                    print(f"  {i}. {cliente}")
                    
        elif opcion == "5":
            print(f"Cantidad de clientes pendientes: {len(cola_clientes)}")
            
        elif opcion == "6":
            print("Saliendo del sistema de atención. ¡Gracias!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()