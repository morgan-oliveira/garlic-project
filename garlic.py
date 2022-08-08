import tkinter as tk
import time

window = tk.Tk()

mainFrame = tk.Frame(master = window).pack()

window.title("Cadastro no Sistema")
#window.geometry("320x240")
name = tk.Label(text="Digite seu nome:").pack()
enterName = tk.Entry().pack()
password = tk.Label(text="Digite sua senha:").pack()
enterPassword = tk.Entry().pack()

def validate(loginSucess):
    
    #if loginSucess == True: 
     #   print("works")
    #else:
     #   print("works even better")
        
def loginWindow (): 
    loginSucessWindow = tk.Tk()
    loginSucessWindow.title("Login")
    loginFrame = tk.Frame(master = loginSucessWindow).pack()
    time.sleep(3)
    loginSucessMessage = tk.Label(loginSucessWindow, text="Login realizado com sucesso!").pack()
    validate(False)
    window.destroy()
    return None      

button1 = tk.Button(
    text="Enter",
    fg="blue",
    command=loginWindow
    ).pack()
