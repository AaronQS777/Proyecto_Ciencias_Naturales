print("\n========== Aplicación de Física - MRU ==========\n")
print("Movimiento Rectilíneo Uniforme (MRU)")
print("Fórmula principal: distancia = velocidad x tiempo\n")

while True:
    print("\n" + "="*50)
    print("¿Qué quieres calcular?")
    print("  1 → Distancia (d = v x t)")
    print("  2 → Velocidad   (v = d / t)")
    print("  3 → Tiempo      (t = d / v)")
    print("-"*50)

    while True:
        opcion = input("Elige 1, 2 o 3: ").strip()
        if opcion in ["1", "2", "3"]:
            break
        print("Opción inválida. Escribe 1, 2 o 3.")

    try:
        if opcion == "1":
            print("\n→ Calcular DISTANCIA")
            velocidad = float(input("Velocidad (m/s)   → "))
            tiempo    = float(input("Tiempo (segundos) → "))
            
            if velocidad < 0 or tiempo < 0:
                print("Error Velocidad y tiempo no pueden ser negativos.")
                continue
                
            distancia = velocidad * tiempo
            print(f"\nResultado → La distancia recorrida es {distancia:.2f} metros")

        elif opcion == "2":
            print("\n→ Calcular VELOCIDAD")
            distancia = float(input("Distancia (metros) → "))
            tiempo    = float(input("Tiempo (segundos)  → "))
            
            if tiempo <= 0:
                print("Error El tiempo debe ser mayor que 0.")
                continue
                
            velocidad = distancia / tiempo
            print(f"\nResultado → La velocidad es {velocidad:.2f} m/s")

        elif opcion == "3":
            print("\n→ Calcular TIEMPO")
            distancia = float(input("Distancia (metros)  → "))
            velocidad = float(input("Velocidad (m/s)     → "))
            
            if velocidad <= 0:
                print("Error La velocidad debe ser mayor que 0.")
                continue
                
            tiempo = distancia / velocidad
            print(f"\nResultado → El tiempo es {tiempo:.2f} segundos")

    except ValueError:
        print("\nError: Debes ingresar números válidos. Intenta de nuevo.")
        continue

    while True:
        continuar = input("\n¿Quieres resolver otro ejercicio? (si/no): ").lower().strip()
        if continuar in ["si", "sí", "s", "no", "n"]:
            break
        print("Por favor responde 'si' o 'no'.")

    if continuar in ["no", "n"]:
        print("\n¡Gracias por usar el programa! Hasta la próxima.")
        break


    print("\n" + "-"*60)