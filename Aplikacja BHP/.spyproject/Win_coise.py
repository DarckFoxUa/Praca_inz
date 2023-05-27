
from tkinter import *
win2 = Tk()

win2.config(bg='grey')
variables = IntVar()
Radiobutton(win2, bg='white', activebackground='grey', text='Urządzenie', variable=variables, value=1).place( x=0, y=0)
Radiobutton(win2, bg='white', activebackground='grey', text='Wybór plika', variable=variables, value=2).place(x=0, y=180)

x = win2.winfo_screenwidth() // 2 - 320
y = win2.winfo_screenheight() // 2 - 180
win2.title('Wybór źródła danych do otwierania')

photo = PhotoImage(file='kask.png')
win2.iconphoto(False, photo)

win2.geometry('640x360+{}+{}'.format(x, y))
win2.minsize(640, 360)
win2.resizable(False, False)
win2.grab_set() # захватываем пользовательский ввод

win2.mainloop()