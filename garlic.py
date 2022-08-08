import tkinter as tk
#import time

window = tk.Tk()

mainFrame = tk.Frame(master = window).pack()

window.title("Cadastro no Sistema")
#window.geometry("320x240")
getName = tk.StringVar()
getPass = tk.StringVar()

nameLabel = tk.Label(text="Digite seu nome:").pack()
enterName = tk.Entry(textvariable=getName, width=16)
enterName.pack()
passwordLabel = tk.Label(text="Digite sua senha:").pack()
enterPassword = tk.Entry(textvariable=getPass, show="*", width=16)
enterPassword.pack()


# validates username and password for admin users

def validate():
    name = enterName.get()
    password = enterPassword.get()
    if (name == "admin" and password == "nimda"):
        return True
    else: 
        return False
 
# creates the login window and calls 'validate' function to check if login is successful
    
def loginWindowValidate(): 
    boolvar = validate()
    loginWindow = tk.Tk()
    loginWindow.title("Login")
    loginFrame = tk.Frame(master = loginWindow).pack()
    # time.sleep(3)
    if (boolvar == True):
        window.destroy()
        loginSucessMessage = tk.Label(loginWindow, text="Login realizado com sucesso!").pack()
        loginSucessButton = tk.Button(loginWindow, text="OK", command=loginWindow.destroy).pack()
        loginSucess()
    else:         
        loginFail = tk.Label(loginWindow, text="Usuário/Senha Incorreto!").pack()
        loginSucessButton = tk.Button(loginWindow, text="OK", command=loginWindow.destroy).pack()        
    return None

button1 = tk.Button(
    text="Enter",
    fg="blue",
    command=loginWindowValidate
    ).pack()

window.mainloop()