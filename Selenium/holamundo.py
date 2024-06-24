#clase
class HolaMundo:
    def pedir_datos(self):
        nombre = input("Ingresa tu nombre: ")
        print('Bienvenido: ', nombre)

if __name__ == "__main__":
    miclase = HolaMundo()
    miclase.pedir_datos()



#script
nombre = input("Ingresa nombre: ")
print(nombre)