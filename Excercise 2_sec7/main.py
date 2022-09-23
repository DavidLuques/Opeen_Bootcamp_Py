import time

print(' ingrese hora')
hora=int(input())
print('ingrese minutos')
minutos=(input())

if hora>7:
    print("son mas de las 7 AM !! ")

localTime=time.localtime()
print("result:", localTime)
print("\nyear:", localTime.tm_hour)
print("tm_hour:", localTime.tm_mon)