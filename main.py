from tkinter import *
from tkinter import ttk

class login:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('250x300')
        self.root.resizable(False,False)
        self.root.title('Login')
        self.root.config(bg = '#ADF3C9')
        self.root.iconbitmap('.\\imagens\\login-icone.ico')
    
    def interface(self):

        #Frame
        frame_principal = Frame(self.root, bg='#ADF3C9')
        frame_principal.place(width=300, height=250)

        frame_inferior = Frame(self.root,bg = '#ADF3C9')
        frame_inferior.place(width=300, height=30, y = 270)

        #Label
        email_label = Label(frame_principal, text='Email', bg = '#ADF3C9', fg = 'black')
        email_label.place(width=60, height=40, x=10, y = 16)

        senha_label = Label(frame_principal, text='Senha', bg= '#ADF3C9', fg = 'black')
        senha_label.place(width=60, height=40, x = 10, y = 96)

        rodape_label = Label(frame_inferior, text='* Todos os direitos reservados',bg = '#ADF3C9',fg='black')
        rodape_label.place(width=200, height=20, x = 50, y = 5)

        #Entry
        email_entry = ttk.Entry(frame_principal)
        email_entry.place(width=190, height=24, x = 30, y = 60)

        senha_entry = ttk.Entry(frame_principal, show='*')
        senha_entry.place(width=190, height=24, x = 30, y = 140)

        #Botão
        botao = ttk.Button(frame_principal, text='Entrar')
        botao.place(width=60, height=40,x = 95, y = 196)

    def execultar(self):
        janela.interface()
        self.root.mainloop()

janela = login()
janela.execultar()
