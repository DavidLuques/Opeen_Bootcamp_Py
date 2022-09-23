import time


print('quieres saber si es hora de volver a casa?  escribe: si')
resp=input()
if(resp=='si'):
    localTime = time.localtime()
    hora=localTime.tm_hour
    minuto=localTime.tm_min


    if(hora>19):
        print('tiempo de volver a casa!')
    else:
        horaFaltante=18-hora
        minutoFaltante=60-minuto

        print(f'faltan {horaFaltante} Horas y {minutoFaltante} minutos')
        print('lo siento =C')



