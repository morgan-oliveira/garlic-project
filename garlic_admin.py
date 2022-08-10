from tkinter import *


# cria a janela de ferramentas do administrador

def call_admin():

    adminWindow = Tk()
    adminWindow.title("Administrador do Sistema")
    adminWindow.geometry("800x420")
    adminFrame = Frame(master = adminWindow).pack()


# seleção de comandos

# funções do botão de novo funcionário

    #def newUser():
    #    pass

# botão para cadastrar novo empregado

    newEmployee = Button (
    
        master = adminFrame,
        width=45,
        height=5,
        text="Cadastrar novo funcionário",
        fg="blue"
        #command=newUser
   
    ).pack(pady=50)

# botão para migrar para tela de cadastro de conveniado

    conv_migrate = Button (
    
        master = adminFrame,
        width=45,
        height=5,
        text="Cadastrar novo conveniado",
        fg="green"
        #command=call_conv
    
    ).pack(pady=50)

# loop

    adminWindow.mainloop()
