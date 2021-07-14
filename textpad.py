from tkinter import *
from tkinter import messagebox, filedialog

root = Tk()
root.geometry('350x420+350+170')
main_menu = Menu(root)
root.config(menu=main_menu)

color_theme = {"Light": {"text_bg": '#fff', "text_fg": "#000", 'CURSOR': "#8000FF", "select_bg": "#777"},
               'Dark': {"text_bg": '#343D46', "text_fg": '#C9DEC1', 'CURSOR': "white", "select_bg": '#4E5A65'}}


def change_theme(theme):
    text_pad['bg'] = color_theme[theme]['text_bg']
    text_pad['fg'] = color_theme[theme]['text_fg']
    text_pad['insertbackground'] = color_theme[theme]['CURSOR']
    text_pad['selectbackground'] = color_theme[theme]['select_bg']


def about_programm():
    messagebox.showinfo(title='Блокнот Альберта', message='Программа "Блокнот Альберта". Версия 0.0.1')


def open_file():
    file_path = filedialog.askopenfile(title='Поиск файлов',
                                       filetypes=(('Текстовые документы(*.txt)', "*txt"), ("Все файлы", '*.*')))
    if file_path:
        text_pad.delete('1.0', END)
        text_pad.insert('1.0', open(file_path, encoding='utf-8').read())

        print(open(file_path, encoding='utf-8'))



def save_files():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы(*.txt)', "*txt"), ("Все файлы", '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_pad.get('1.0', END)
    f.write(text)
    f.close()


def exit():
    answer = messagebox.askokcancel(title='Выход', message='Закрыть программу?')
    if answer:
        root.destroy()


file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_files)
file_menu.add_separator()
file_menu.add_cascade(label="Выход", command=exit)
main_menu.add_cascade(label="Файл", menu=file_menu)

help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label='Светлая тема', command=lambda: change_theme("Light"))
help_menu_sub.add_command(label="Темная тема", command=lambda: change_theme("Dark"))
help_menu.add_cascade(label='Смена цветовой гаммы', menu=help_menu_sub)
main_menu.add_cascade(label='Помощь', menu=help_menu)
help_menu.add_command(label='Инфо', command=about_programm)

f_menu = Frame(root, bg='#1F252A', height=40)
f_text = Frame(root)
# f_menu.pack(fill = X)
f_text.pack(fill=BOTH, expand=1)
# l_menu = Label( f_menu, text ='Меню', bg = '#2B3239', fg = "#C9DEC1", font = "Arial 10")
# l_menu.place(x=10,y=10)

text_pad = Text(f_text, bg=color_theme['Dark']['text_bg'], fg=color_theme['Dark']['text_fg'], padx=10, pady=5,
                wrap=WORD,
                insertbackground='white',
                selectbackground=color_theme['Dark']['select_bg'], spacing3=10)
text_pad.pack(fill=BOTH, expand=1, side=LEFT)
scroll = Scrollbar(f_text, command=text_pad.yview, )
scroll.pack(fill=Y, side=LEFT)
text_pad.config(yscrollcommand=scroll.set)
root.mainloop()
