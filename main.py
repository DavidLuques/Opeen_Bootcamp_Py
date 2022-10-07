import tkinter

window= tkinter.Tk()
print(type(window))

label_saludo= tkinter.Label(window,text="hola!", bg="yellow", fg="blue")
label_saludo.pack(ipadx=50,ipady=100,fill='x')

label_adios= tkinter.Label(window, text='adios! ', bg='red',fg='black')
label_adios.pack(ipadx=50,ipady=50,fill='x')

label_mm=tkinter.Label(window,text='MMMM', bg='purple',fg='gray')
label_mm.pack(ipadx=15,ipady=15,fill='x')

label_aa=tkinter.Label(window,text='AAAAA', bg='gray',fg='white')
label_aa.pack(ipadx=50,ipady=50,side='right')

window.mainloop()