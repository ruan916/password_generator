from tkinter import *
import random

class password_generator_window:
    caracthers = ['a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v','w','x','y',
    'z','A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0',
    '1','2','3','4','5','6','7','8','9',]
    especial_caracthers = [' ','"',"'",'!','@','#','$','%','&',
    '*','(',')','[',']','{','}','´','`','/','?',':',';','<',
    '>',',','.','|','-','_','=','+','~','^']

    def __init__(self):
        self.password_window=Tk()
        self.password_window.config(bg='#000033')
        self.password_window.resizable(False,False)
        self.password_window.title("Password Generator")

        
        
        self.password_window.mainloop()

class main_window:
    caracthers = ['a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v','w','x','y',
    'z','A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0',
    '1','2','3','4','5','6','7','8','9',]
    especial_caracthers = [' ','"',"'",'!','@','#','$','%','&',
    '*','(',')','[',']','{','}','´','`','/','?',':',';','<',
    '>',',','.','|','-','_','=','+','~','^']

    def generator(self):
        try:
            password_generator_window()
        except:
            raise Exception("The register window cannot running")

    def __init__(self):
        self.root=Tk()
        self.root.config(bg='#000033')
        self.root.resizable(False,False)
        self.root.title("Home")

        Label(self.root,text="Welcome!\n\n Primarily, you need a password with\n specials caracthers?\n",font="Helvetica, 22",bg='#000033',fg='#D9E7FF').grid(row=0,column=0,padx=20,sticky=W+E)

        self.root.mainloop()

try:
    main_window()
except:
    raise Exception("AN ERROR OCCURRED")