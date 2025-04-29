#Ejercicio #1
def sumar_numeros():
        N = int(input("Ingrese la cantidad de números (N): "))
        SUM = 0
        for i in range(N):
            x = float(input(f"Ingrese x_{i+1}: "))
            SUM += x
        print("La suma es:", SUM)

def main():
    sumar_numeros()

if __name__ == "__main__":
    main()