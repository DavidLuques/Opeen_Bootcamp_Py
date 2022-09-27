# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países
# repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

print('bienvenido ! ')
fin=True
paises = []

while(fin):
    agregar = input("ingrese un pais")
    if agregar in paises:
        print("ya existe el pais")
    else:
        paises.append(agregar)
    termina=input('ingrese si para continuar, no para finalizar')

    if(termina=='no'):
        fin=False
    

print(paises)