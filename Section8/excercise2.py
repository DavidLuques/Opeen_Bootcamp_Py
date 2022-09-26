import pickle


class Dog:
    breed=''
    bark=None

    def __init__(self,breed,bark):
        self.breed=breed
        self.bark=bark

    def __repr__(self):
        return f'puppie\'s breeed is : {self.breed} and bark: {self.bark}'

puppie1=Dog('Dogo',True)
print(puppie1)
#aqui guarde la classe en un archivo .bin
f=open('dogclass.bin','wb')
pickle.dump(puppie1,f)
f.close()

f=open('dogclass.bin','rb')
dog=pickle.load(f)
f.close()
print(dog)



