class Car:
    encendido=True

    def apaga(self):
        self._encendido=False #debe ser self por que sino interpreta que crea una variable.

    def isEncendido(self):
        return self._encendido

    def enciende(self):
        self._encendido=True
# si la variable empieza por _ entonces no se debe tocar desde afuera, esa es una conviencion en python
#por que no existe Protected, private  todo es public .
carro1= Car()
carro1.apaga()
print(carro1.isEncendido())
carro1.enciende()
print(carro1.isEncendido())