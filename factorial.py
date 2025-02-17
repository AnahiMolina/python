def factorial(n):
    if n==1 or n==0:
        print("El factorial es: 1")
    elif n>=0:
        resultado = 1
        for i in range(1,n+1):
            resultado *= i
        return ( print("El factorial es: ", resultado))
    else:
        print("No es entero natural")

def fibonacci(s):
    if s==0:
        print("0")
    elif s==1:
        print("1")
    elif s>1:
        for i in range(1,s+1):
            resultado = resultado+(s-i)
            print(resultado)

fibonacci(5)


factorial(n = int(input("Obtener el factorial de: ")))

