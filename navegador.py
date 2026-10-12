# reto2_navegador.py

historial_paginas = []

def visitar_pagina(url):
    historial_paginas.append(url)
    print(f"Visitando: {url}")

def regresar_pagina():
    if len(historial_paginas) <= 1:
        print("No existen páginas anteriores.")
        return None
    # Quitamos la página actual
    historial_paginas.pop()
    # Retornamos la nueva página actual (tope)
    print(f"Regresando... Página actual: {historial_paginas[-1]}")
    return historial_paginas[-1]

def consultar_actual():
    if not historial_paginas:
        print("El navegador está en blanco.")
    else:
        print(f"Página actual: {historial_paginas[-1]}")

def mostrar_historial():
    if not historial_paginas:
        print("Historial vacío.")
    else:
        print("Historial pendiente de retroceso:", historial_paginas)

def ejecutar_prueba_obligatoria():
    print("\n--- EJECUTANDO PRUEBA OBLIGATORIA ---")
    visitar_pagina("uam.edu.ni")
    visitar_pagina("python.org")
    visitar_pagina("github.com")
    
    print("\nRegresando 3 veces:")
    regresar_pagina() # Debe quedar python.org
    regresar_pagina() # Debe quedar uam.edu.ni
    regresar_pagina() # Mensaje: No existen páginas anteriores

def main():
    while True:
        print("\n--- SIMULADOR DE NAVEGADOR WEB ---")
        print("1. Visitar nueva página web")
        print("2. Regresar a página anterior (Pop)")
        print("3. Consultar página actual")
        print("4. Mostrar historial completo")
        print("5. Ejecutar prueba obligatoria (UAM, Python, GitHub)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            url = input("Ingrese la URL de la página: ").strip()
            if url:
                visitar_pagina(url)
            else:
                print("URL vacía.")
        elif opcion == "2":
            regresar_pagina()
        elif opcion == "3":
            consultar_actual()
        elif opcion == "4":
            mostrar_historial()
        elif opcion == "5":
            ejecutar_prueba_obligatoria()
        elif opcion == "6":
            print("Cerrando navegador.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()