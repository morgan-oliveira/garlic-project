from tkinter import *
import sqlite3


# chama a database e cria as tables devidas

init = sqlite3.connect('garlic-db.db')
#init.execute(''' DROP TABLE FUNC ''')
init.execute(''' CREATE TABLE IF NOT EXISTS FUNC(ID INT                  PRIMARY KEY,
                                                 MAIL TEXT               NOT NULL,
                                                 NAME TEXT               NOT NULL,
                                                 AGE INTEGER             NOT NULL,
                                                 FUNC_CODE TEXT          NOT NULL);''')



# insere os valores dos novos funcionarios na table da database
    
def db_insert():
    init.execute("INSERT INTO FUNC (MAIL, NAME, AGE, FUNC_CODE) VALUES (?, ?, ?, ?)", (mail, name, age, passw))
    sucessWindow()
# verificar se o usuario de fato deseja cadastrar o funcionário

def verify_sign():
    ver = Tk()
    ver.title("Confirmar cadastro")
    verMsg = Label(ver, text="Deseja cadastrar novo funcionário?").pack()
    ver_ok = Button(
        ver,
        text="Sim",
        command=db_insert
    ).pack(pady=5)
    ver_no = Button(
        ver,
        text="Cancelar",
    ).pack(pady=5)
    
# janela de sucesso no cadastro do funcionário

def sucessWindow():
    sucs = Tk()
    sucs.title("Cadastro realizado")
    sucsMsg = Label(text="Cadastro realizado com sucesso!").pack()
    sucsBtn = Button(
        sucs,
        text="OK",
        fg="blue",
        command=lambda:[sucs.destroy(), close_adm()]
    ).pack()

# fecha a janela 

def close_adm():
    admin_func.destroy()
    
    
# cria a janela de ferramentas do administrador

def call_func():
    admin_func = Tk()
    adm_frm = Frame(master = admin_func).pack()
    admin_func.title("Cadastro de novo funcionário")
    
# variáveis das entrys       
        
    func_name = StringVar()
    func_age = IntVar()
    func_email = StringVar()
    func_pass = StringVar()
    
    name_lbl = Label(admin_func, text="Nome:").pack()
    name_etry = Entry(admin_func, textvariable=func_name)
    name_etry.pack()
    age_lbl = Label(admin_func, text="Idade:").pack()
    age_etry = Entry(admin_func, textvariable=func_age)
    age_etry.pack()
    mail_lbl = Label(admin_func, text="Email:").pack()
    mail_etry = Entry(admin_func, textvariable=func_email)
    mail_etry.pack()
    num_lbl = Label(admin_func, text="Senha:").pack()
    num_etry = Entry(admin_func, textvariable=func_pass, show = '*')
    num_etry.pack()  
    
    func_btn = Button(
        admin_func,
        text="Cadastrar",
        fg="blue",
        command=verify_sign
    ).pack()
    
# inicializacao das variaveis de texto

  
name = name_etry.get()
age = age_etry.get()
mail = mail_etry.get()
passw = num_etry.get()   
    

def call_admin():

    adminWindow = Tk()
    adminWindow.title("Administrador do Sistema")
    adminWindow.geometry("800x420")
    adminFrame = Frame(master=adminWindow).pack()


# seleção de comandos

# funções do botão de novo funcionário
       

# botão para cadastrar novo empregado

    newEmployee = Button (
    
        master=adminFrame,
        width=45,
        height=5,
        text="Cadastrar novo funcionário",
        fg="blue",
        command=call_func
   
    ).pack(pady=50)

# botão para migrar para tela de cadastro de conveniado

    conv_migrate = Button (
    
        master=adminFrame,
        width=45,
        height=5,
        text="Cadastrar novo conveniado",
        fg="green"
        #command=call_conv
    
    ).pack(pady=50)

# loop

    adminWindow.mainloop()
