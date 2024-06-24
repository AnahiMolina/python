from clase1 import Operaciones
from clase2 import Mensajes
from clase2 import Colores
if __name__ == "__main__":

    mensajes = Mensajes()
    print(mensajes.hola_mundo())
    print(mensajes.bienvenida('Alma'))

    colores = Colores()
    print(colores.color('Azul'))



    suma = Operaciones ('suma',5,6)
    resta = Operaciones ('resta',5,6)
    multiplicacion = Operaciones ('multiplicacion',5,6)
    division = Operaciones ('division',5,6)