#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de
# definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Student:
    name='penelope'
    score=7
    def __init__(self):
        self.nombre=''
        self.score=0.0

    def setValues(self,na, sc):
        self.name=na
        self.score=sc

    # def __repr__ (self):
    #     return 'MyClass(nombre=' + self.nombre + ' ,y=' + str(self.score) + ')'

    def __str__ (self):
        return 'MyClass(nombre=' + self.name + ' ,y=' + str(self.score) + ')'

student1=Student()
print('please gimme ur score')
scor=float(input())
student1.setValues('rynho',scor)
print(student1)

#did he pass the exam?

if(student1.score>7.0):
    print("paso el examen!")
else:
    print("no paso")





