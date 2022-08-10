import tkinter as tk
from PIL import ImageTk, Image
from garlic_admin import call_admin
#import time

# creates main window

window = tk.Tk()

# creates logo 

logo = tk.Frame(master = window).pack()
mainFrame = tk.Frame(master = window).pack()
logo_img = ImageTk.PhotoImage(Image.open("garlic-logo.png"))
logo_lbl = tk.Label(logo, image = logo_img).pack()

# creates main window properties

window.title("Cadastro no Sistema")
window.geometry("700x320")

# gets name and password from user input

getName = tk.StringVar()
getPass = tk.StringVar()

# login window widgets

nameLabel = tk.Label(text="Digite seu nome:").pack()
enterName = tk.Entry(textvariable=getName, width=16)
enterName.pack(fill=tk.X)
passwordLabel = tk.Label(text="Digite sua senha:").pack()
enterPassword = tk.Entry(textvariable=getPass, show="*", width=16)
enterPassword.pack(fill=tk.X)

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
    
    # boolvar assumes whatever validate() returns and checks if login is sucessful
    
    if boolvar:
        window.destroy()
        loginSucessMessage = tk.Label(loginWindow, text="Login realizado com sucesso!").pack()
        loginSucessButton = tk.Button(loginWindow, text="OK", command=loginWindow.destroy).pack()
        call_admin()
    else:         
        loginFail = tk.Label(loginWindow, text="Usuário/Senha Incorreto!").pack()
        loginSucessButton = tk.Button(loginWindow, text="OK", command=loginWindow.destroy).pack()        
    return None

# login button 

button1 = tk.Button(
    text="Enter",
    fg="blue",
    command=loginWindowValidate
    ).pack(pady=10)

# main loop

window.mainloop()