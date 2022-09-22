#import modules.dividir.div as d
#from modules import *
# import modules.dividir.div as d
# import modules.multiplicar.mul as m

from modules.dividir import div as d
from modules.multiplicar import mul as m
from modules.sumar import sum as s
from modules.restar import res as r

def main():
   res=d.dividir(1,2)
   print(res)

   res = m.multiplicar(1, 2)
   print(res)

   res = s.sumar(1, 2)
   print(res)

   res = r.restar(1,2)
   print(res)
if __name__== '__main__':
    main()