# cola_guiada.py
from collections import deque

cola = deque()

def registrar_paciente(nombre):
    cola.append(nombre)
    print(f"Registrado en cola: {nombre}")

def atender_paciente():
    if not cola:
        print("No hay pacientes en espera.")
    else:
        paciente = cola.popleft()
        print(f"Atendiendo a: {paciente}")

def mostrar_cola():
    if not cola:
        print("La cola está vacía.")
    else:
        print("Pacientes en espera:")
        for posicion, paciente in enumerate(cola, 1):
            print(f"{posicion}. {paciente}")

def main():
    while True:
        print("\n--- CLÍNICA MÉDICA (COLAS) ---")
        print("1. Registrar paciente")
        print("2. Atender siguiente paciente")
        print("3. Mostrar cola de espera")
        print("4. Salir")
        
        opc = input("Elija una opción (1-4): ").strip()
        if opc == "1":
            nombre = input("Nombre del paciente: ").strip()
            if nombre:
                registrar_paciente(nombre)
            else:
                print("El nombre no puede estar vacío.")
        elif opc == "2":
            atender_paciente()
        elif opc == "3":
            mostrar_cola()
        elif opc == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()