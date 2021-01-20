from tkinter import *
from random import randint

root = Tk()


class Func:
    def alterar_tema(self):
        tema = self.VarTheme.get()
        if tema == "Tema escuro":
            self.root.configure(bg="#156475")
            self.bt_girar["bg"] = "#101A79"
            self.bt_girar["fg"] = "white"
            self.theme["bg"] = "#101A79"
            self.theme["fg"] = "white"
            self.number["bg"] = "#156475"
            self.number["fg"] = "white"
            self.qtd["bg"] = "#156475"
            self.qtd["fg"] = "white"
        if tema == "Tema claro":
            self.root.configure(bg="#96BAF7")
            self.bt_girar["bg"] = "#3074f2"
            self.bt_girar["fg"] = "white"
            self.theme["bg"] = "#3074f2"
            self.theme["fg"] = "white"
            self.number["bg"] = "#96BAF7"
            self.number["fg"] = "white"
            self.qtd["bg"] = "#96BAF7"
            self.qtd["fg"] = "white"

    def girar_dado(self):
        número = randint(0, 6)
        self.qtd["text"] = f"{número}"


class Application(Func):
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        self.alterar_tema()
        root.mainloop()
    
    def tela(self):
        self.root.title("Dado de 6 lados")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
    
    def widgets(self):
        self.bt_girar = Button(self.root, bd=0, font=("Verdana", 20), 
        text="Girar Dado", command=self.girar_dado)
        self.bt_girar.place(rely=0.6, relx=0.35, relwidth=0.3)

        self.VarTheme = StringVar(self.root)
        self.VTheme = ("Tema escuro", "Tema claro")
        self.VarTheme.set("Tema escuro")
        self.popupMenu = OptionMenu(self.root, self.VarTheme, *self.VTheme)
        self.popupMenu.place(rely=0.93, relx=0.02)

        self.number = Label(self.root, text="Número obtido:", font=("Verdana", 20))
        self.number.place(relx=0.35, rely=0.20)

        self.qtd = Label(self.root, font=("Verdana", 20))
        self.qtd["text"] = "0"
        self.qtd.place(rely=0.4, relx=0.48)

        self.theme = Button(self.root, text="Alterar Tema", 
        command=self.alterar_tema, bd=0)
        self.theme.place(rely=0.93, relx=0.2)


Application()
