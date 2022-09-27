# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y
# realizará una suma de todos estos elementos obtenidos mediante reduce.
import random
from functools import reduce


def filtrar(x):
    if (x%2==0):
        return False
    else:
        return True

def suma(a,b):
    return a+b


print('crearemos la lista')

lista1=[]
quiere=input('diga si si quiere agregar numeros a la lista, no para terminar')
cuanto=int(input('cuantos nros quiere agregar a la lista?'))

if(quiere=='si'):
    for i in range(0,cuanto):
        lista1.append(random.randint(0,cuanto))

listFiltered=filter(filtrar,lista1)
result=filter(lambda x: x%2!=0,lista1)

print(type(listFiltered))
print(type(result))
print(list(listFiltered))
print(list(result))

list2=list(result)
listreduced=reduce(lambda a,b: a+b,list2,0)
print(listreduced)

