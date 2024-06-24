#clase
class HolaMundo2:
    #Entradas y salidas
    def suma(self, valor1,valor2):
        return(valor1+valor2)
    
    #Sin entradas y salidas
    def saludo(self):
        print("Saludos")

    #Entradas y salidas
    def resta(self, valor1,valor2):
        print("La resta es: " + str(valor1-valor2))

    #Solo salidas
    def pi(self):
        return 3.1415
    

if __name__ == "__main__":
    miclase = HolaMundo2()
    suma = miclase.suma(5, 8)
    print(suma)

    miclase.saludo()
    miclase.resta(10,1)

    pi = miclase.pi()
    print(pi)
