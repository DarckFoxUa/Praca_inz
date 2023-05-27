NAME = "Start_page"


def new_win():
    cmd = 'Start_page.py'
    call(['python', cmd])


def win_view():  # okno widok
    win1 = Toplevel()

    win1.config(bg='grey')
    x = win1.winfo_screenwidth() // 2 - 320
    y = win1.winfo_screenheight() // 2 - 180
    win1.title('Widok')

    photo = PhotoImage(file='kask.png')
    win1.iconphoto(False, photo)

    win1.geometry('640x360+{}+{}'.format(x, y))
    win1.minsize(640, 360)
    win1.resizable(False, False)
    win1.grab_set()  # захватываем пользовательский ввод


def win_coise():  # okno wyboru
    def open_file():
        global file
        file = fd.askopenfilename(filetypes=[("Video files", "*.AVI *.MP4 *.MKV")])
        with open('way.txt', 'w') as f:
            f.write(str(file))
        win2.destroy()

        print(file)
        cmd = 'yolo.py'
        call(['python', cmd])

    def camera():
        win2.destroy()

        cmd = 'yolo1.py'
        call(['python', cmd])



    win2 = Toplevel()

    win2.config(bg='grey')

    x = win2.winfo_screenwidth() // 2 - 320
    y = win2.winfo_screenheight() // 2 - 180
    win2.title('Wybór źródła danych do otwierania')

    photo = PhotoImage(file='kask.png')
    win2.iconphoto(False, photo)

    win2.geometry('640x360+{}+{}'.format(x, y))
    win2.minsize(640, 360)
    win2.resizable(False, False)
    win2.grab_set()  # захватываем пользовательский ввод

    Label(win2, bg='grey', activebackground='white', text='Wybór urządzenia').place(x=0, y=0)
    btn2 = Button(win2, text='Otworzyć z dostępnej kamery', command=camera)
    btn2.place(x=50, y=40)

    Label(win2, bg='grey', activebackground='white', text='Wybór plika').place(x=0, y=180)
    btn2 = Button(win2, text='Otwożyć plik', command=open_file)
    btn2.place(x=50, y=220)

    # btn3 = Button(win2, text='OK', width=10, command=0)
    # btn3.place(x=550, y=330)


def win_sn():  # okno SN
    win3 = Toplevel()

    win3.config(bg='grey')
    x = win3.winfo_screenwidth() // 2 - 320
    y = win3.winfo_screenheight() // 2 - 180
    win3.title('Ustawienia SN')

    photo = PhotoImage(file='kask.png')
    win3.iconphoto(False, photo)

    win3.geometry('640x360+{}+{}'.format(x, y))
    win3.minsize(640, 360)
    win3.resizable(False, False)
    win3.grab_set()  # захватываем пользовательский ввод


from tkinter import filedialog as fd
from tkinter import *
from subprocess import call

win = Tk()
x = (win.winfo_screenwidth() - win.winfo_reqwidth())
y = (win.winfo_screenheight() - win.winfo_reqheight())
win.wm_geometry("+%d+%d" % (x, y))

photo = PhotoImage(file='kask.png')
win.iconphoto(False, photo)
win.config(bg='grey')
win.title('Aplikacja BHP')

main_menu = Menu(win)
win.config(menu=main_menu)

main_menu.add_cascade(label='Nowe okno', command=new_win)
main_menu.add_cascade(label='Widok', command=win_view)
main_menu.add_cascade(label='Wybór źródła danych', command=win_coise)
main_menu.add_cascade(label='Ustawienia SN', command=win_sn)

x = win.winfo_screenwidth() // 2 - 480
y = win.winfo_screenheight() // 2 - 270
win.geometry('960x540+{}+{}'.format(x, y))
win.minsize(640, 360)

btn = Button(win, text='Wybierz źródło danych do otwierania', command=win_coise)
btn.pack(expand=1)

win.mainloop()
