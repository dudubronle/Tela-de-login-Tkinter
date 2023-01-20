from tkinter import *
import customtkinter as ct
from tkinter import messagebox

# Criando a classe para os arquivos se alto plugarem
class Application:

    def __init__(self):
        pass
        ct.janela=janela
        tema()
        tela()
        tela_login()
        janela.mainloop()

    # Criação da tela de login

janela = ct.CTk()


def tema():
    ct.set_appearance_mode('White')
    ct.set_default_color_theme('dark-blue')

# Criação da tela
def tela():
    janela.geometry('700x400')
    janela.title('Login')
    janela.iconbitmap('lobo.ico')
    janela.resizable(False, False)


def tela_login():
    img = PhotoImage(file='login.png')
    label_img= ct.CTkLabel(master= janela, image= img, text=None)
    label_img.place(x=3, y=1)

    # Criação dos frames
    frame = ct.CTkFrame(master= janela, width= 300, height= 396)
    frame.pack(side='right')


    label = ct.CTkLabel(master=frame, text='', font=('Roboto-Condensed.ttf', 80))
    label.place(x=25, y=5)

    #Usuário
    ct.CTkEntry(master=frame, placeholder_text='Nome de usuário', width=250, font=('Roboto', 15)).place(x=25, y=78)
    ct.CTkLabel(master=frame, text='Usuário:', text_color='white', font=('Roboto-Condensed.ttf', 20)).place(x=15, y=45)
    #Senha
    ct.CTkEntry(master=frame, placeholder_text='Digite sua senha', width=250, show='*', font=('Roboto', 15)).place(x=25,                                                                                                              y=175)
    ct.CTkLabel(master=frame, text='Senha:', text_color='white', font=('Roboto-Condensed.ttf', 20)).place(x=15, y=130)

    ct.CTkCheckBox(master=frame, text='Lembrar login').place(x=25, y=275)

    def confirmarlogin():

        pass
    botao_de_login = ct.CTkButton(frame, text='confirmar', fg_color='black', width=20, command=confirmarlogin).place(x=25, y=320)


    # Sistema de Cadastro
    def on_button_press():

# Remove o campo de login
        frame.pack_forget()


        #Cria um frame novo

        rg = ct.CTkFrame(master=janela, width=300, height=396)
        rg.pack(side=RIGHT)

        #Sistema de novo cadastro
        ct.CTkLabel(rg, text='Cadastro', font=('Roboto-Condensed.ttf', 50)).place(x=50, y=10)

        span = ct.CTkLabel(rg, text='Preencha corretamente os dados!!!', text_color='gray', font=('Roboto', 13)).place(x=15, y=309)

        #Campo do novo usuário
        ct.CTkLabel(rg, text='Novo usuário:',font=('Roboto', 15)).place(x=15, y=95)
        ct.CTkEntry(rg, placeholder_text='Digite seu usuario', font=('Roboto', 15),width=250,).place(x=15, y=125)

        #Campo de Email
        email = ct.CTkLabel(rg, text='Digite seu Email:', font=('Roboto', 15)).place(x=15, y=165)
        emailbox = ct.CTkEntry(rg, placeholder_text='Email', font=('Roboto', 15), width=250).place(x=15, y=200)

        #Campo de senha
        senha = ct.CTkLabel(rg, text='Digite sua Senha', font=('Roboto', 15)).place(x=15, y=240)
        senhabox = ct.CTkEntry(rg, placeholder_text='Digite sua senha',width=250,font=('Roboto', 15)).place(x=15, y=280)

        ct.CTkButton(rg, text='Voltar', command=lambda : [rg.pack_forget(),frame.pack(side='right')],).place(x=15, y=350)

        def register():
            msg = messagebox.showinfo(title='Registro', message='Cadastro efetuado com sucesso')
            pass
        regis = ct.CTkButton(rg, text='Novo cadastro',command=register, width=40).place(x=185, y=350)



    ct.CTkButton(master=frame, text='registrar-se', fg_color='black', width=150, command=on_button_press).place(x=105, y=320)





Application()