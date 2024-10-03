from tkinter import *
from tkinter import ttk
import ctypes
import services
 
def main():
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome, email, senha)

    def listar_usuario():
        usuarios = services.listar_usuario()

        listar_janela = Toplevel()
        listar_janela.geometry('400x300')
        listar_janela.title('Listar Usuario')

        tree = ttk.Treeview(listar_janela, columns=('ID', 'Nome', 'Email'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')

        # criar botao de voltar que fecha a tela de lista us
        voltar= Button(listar_janela, text="Voltar", width=10, command=listar_janela)
        voltar.pack(fill=BOTH, expand=True, side=BOTTOM)

        tree.pack(fill=BOTH, expand=True)

        # inserir os dados do usuario na treeview
        for usuario in usuarios:
            # END vai inseir o item no final da tabela
            tree.insert('', END, values=usuario)

    janela = Tk()
    janela.geometry('500x400')
    janela.title('Sistema de Gerenciamento de Usuário')
    #janela.configure(bg='lightblue')
 
    titulo = Label(janela, text='CRUD', font=('Comic Sans MS', 20))
    titulo.pack(pady=30)
 
    # Nome
    nome = Label(janela, text='Nome:')
    nome.place(x=50, y=100)
 
    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=115, y=100)
 
    # Email
    email = Label(janela, text='Email:')
    email.place(x=50, y=130)
 
    global emailEntry
    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=115, y=130)
 
    #Senha
    senha = Label(janela, text='Senha:')
    senha.place(x=50, y=160)
 
    #Comando show para esconder a senha
    global senhaEntry
    senhaEntry = Entry(janela, width=30, show="*")
    senhaEntry.place(x=115, y=160)
 
    enviar = Button(janela, text='Cadastrar', width=10)
    enviar.place(x=125, y=200)
 
    listar = Button(janela, text='Listar Usuários', width=15)
    listar.place(x=225, y=200)
 
   #passion = Label(janela, text='grahphic design is my passion', width=40)
   #passion.place(x=5, y=300)
 
    janela.mainloop()
 
if __name__ == '__main__':
    main()