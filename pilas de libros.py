# pila_guiada.py

pila = []

def apilar(libro):
    pila.append(libro)
    print(f"Libro agregado: {libro}")

def desapilar():
    if len(pila) == 0:
        print("La pila está vacía")
    else:
        libro = pila.pop()
        print(f"Libro retirado: {libro}")

def mostrar_pila():
    if not pila:
        print("No hay libros en la pila.")
    else:
        print("Pila actual:", pila)
        print("Libro en el tope:", pila[-1])

# Interacción dinámica solicitada en el Paso 4
print("--- Registro inicial de libros ---")
for i in range(3):
    nombre_libro = input(f"Ingrese el nombre del libro #{i+1}: ").strip()
    if nombre_libro:
        apilar(nombre_libro)
    else:
        print("Nombre vacío. Se omitió.")

mostrar_pila()

print("\n--- Retirando el último libro (LIFO) ---")
desapilar()
mostrar_pila()