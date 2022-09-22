# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas

class vehiculo:
    color=''
    ruedas=''
    puertas=''

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada


class coche(vehiculo):
    def __init__(self):
        self.velocidad=0
        self.cilindrada=0.0
    def __repr__(self):
        return "This is object of class A"

    def __str__(self):
        return str(self.velocidad)+'\n'+str(self.cilindrada)



# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
carro1=coche()
print(carro1)