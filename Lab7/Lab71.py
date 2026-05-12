def calcular_factorial():
    try:
        n = int(input("Introduce un número N para calcular su factorial: "))
        if n < 0:
            print("El factorial no está definido para números negativos.")
            return
        
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
            
        print(f"El factorial de {n} es: {factorial}")
    except ValueError:
        print("Error: Por favor introduce un número entero válido.")

if __name__ == "__main__":
    calcular_factorial()