ventas = []
while True:
    print("\nMENÚ DE ANÁLISIS DE VENTAS")
    print("1. Ingresar lista de ventas (valores enteros positivos)")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular la venta más alta y la más baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuántos días superaron los Q1000")
    print("6. Buscar si una venta específica existe en la lista")
    print("7. Clasificar cada venta: alta (>1000), media (500–1000), baja (<500)")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            while True:
                num_dias = input("¿Cuántos días de ventas desea ingresar? ")
                if num_dias.isdigit() and int(num_dias) > 0:
                    num_dias = int(num_dias)
                    break
                else:
                    print("Por favor, ingrese un número entero mayor a 0.")
            for i in range(num_dias):
                while True:
                    venta = input(f"Ingrese la venta del día {i + 1}: ")
                    if venta.isdigit() and int(venta) >= 0:
                        ventas.append(int(venta))
                        break
                    else:
                        print("La venta debe ser un número entero positivo.")

        case "2":
            if ventas:
                print("Ventas ingresadas:")
                for venta in ventas:
                    print(venta)
            else:
                print("No hay ventas ingresadas.")

        case "3":
            if ventas:
                print(f"Venta más alta: {max(ventas)}")
                print(f"Venta más baja: {min(ventas)}")
            else:
                print("No hay ventas ingresadas.")

        case "4":
            if ventas:
                promedio = sum(ventas) / len(ventas)
                print(f"Promedio de ventas: {promedio:.2f}")
            else:
                print("No hay ventas ingresadas.")