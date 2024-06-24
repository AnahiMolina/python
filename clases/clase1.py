class Operaciones:

    def __init__(self, tipo_operacion, num1, num2):
        if (tipo_operacion == "suma"):
            self.suma(num1, num2)
        elif(tipo_operacion == "resta"):
            self.resta(num1, num2)
        elif(tipo_operacion == "multiplicacion"):
            self.multiplicacion(num1, num2)
        elif(tipo_operacion == "division"):
            self.division(num1, num2)
        else:
            print("Operacion no soportada")
    
    def suma (self, num1, num2):
        print (num1 + num2)
    
    def resta (self, num1, num2):
        print (num1 - num2)
    
    def multiplicacion (self, num1, num2):
        print (num1 * num2)

    def division (self, num1, num2):
        print (num1 / num2)    