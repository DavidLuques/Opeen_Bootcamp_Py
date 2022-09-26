f=open('./text','w')

for i in range(0,7):
    datos=f.writelines(f'me escribieron en el archivo {i+1}veces\n')


f.close()
f=open('./text','r')


datos=f.readlines()
for linea in datos:
    print(linea)
f.close()

