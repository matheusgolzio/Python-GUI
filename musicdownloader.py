import pafy
from tkinter import *
from tkinter import filedialog as dlg
from time import sleep


pw = Tk()


class Functions():
    def selectlocal(self):
        self.filename = dlg.askdirectory()

    def mudartema(self):
        theme = self.TemaVar.get()
        if theme == "Tema Claro":
            self.pw.configure(background="#00BFFF")
            self.local["fg"] = "white"
            self.local["bg"] = "#0080FF"
            self.url["bd"] = 0
            self.labelurl["fg"] = "white"
            self.labelurl["bg"] = "#00BFFF"
            self.local["bd"] = 0
            self.download["fg"] = "white"
            self.download["bg"] = "#0080FF"
            self.download["bd"] = 0
            self.temabt["fg"] = "white"
            self.temabt["bg"] = "#0080FF"
            self.temabt["bd"] = 0
            self.title["fg"] = "white"
            self.title["bg"] = "#00BFFF"
            self.info["bg"] = "#00BFFF"
            self.popupmenu["bg"] = "#0080FF"
            self.popupmenu["fg"] = "white"
            self.popupmenu["bd"] = 0
        
        elif theme == "Tema Escuro":
            self.pw.configure(background="#0000FF")
            self.local["fg"] = "black"
            self.local["bg"] = "#01A9DB"
            self.url["bd"] = 0
            self.labelurl["fg"] = "black"
            self.labelurl["bg"] = "#0000FF"
            self.local["bd"] = 0
            self.download["fg"] = "black"
            self.download["bg"] = "#01A9DB"
            self.download["bd"] = 0
            self.temabt["fg"] = "black"
            self.temabt["bg"] = "#01A9DB"
            self.temabt["bd"] = 0
            self.title["fg"] = "black"
            self.title["bg"] = "#0000FF"
            self.info["bg"] = "#0000FF"
            self.popupmenu["bg"] = "#01A9DB"
            self.popupmenu["fg"] = "black"
            self.popupmenu["bd"] = 0
    
    def baixar(self):
        self.link = self.url.get()
        self.music = pafy.new(self.link)
        self.best = self.music.getbestaudio(preftype="m4a")
        self.best.download(self.filename)
        self.info["text"] = "Baixado."


class Application(Functions):
    def __init__(self):
        self.pw = pw
        self.tela()
        self.widgets()
        self.mudartema()
        pw.mainloop()
    
    def tela(self):
        self.pw.title("Music Downloader - Made by Matheus Rodrigues Golzio")
        self.pw.resizable(False, False)
        self.pw.geometry("700x500")

    def widgets(self):
        self.title = Label(self.pw, text="Music Downloader", font=("Verdana", 22))
        self.title.place(relx=0.32, rely=0.1)

        self.labelurl = Label(self.pw, text="URL", font=("Verdana", 15))
        self.labelurl.place(relx=0.20, rely=0.35)

        self.url = Entry(self.pw)
        self.url.place(relx=0.30, rely=0.36, relwidth=0.5)

        self.local = Button(self.pw, text="Selecionar local", font=("Verdana", 12),
        command=self.selectlocal)
        self.local.place(relx=0.20, rely=0.44)

        self.download = Button(self.pw, text="Baixar", font=("Verdana", 12),
        command=self.baixar)
        self.download.place(relx=0.45, rely=0.44, relwidth=0.35)

        self.info = Label(self.pw, font=("Verdana", 12))
        self.info.place(relx=0.45, rely=0.54)

        self.TemaVar = StringVar(self.pw)
        self.TVar = ("Tema Claro", "Tema Escuro")
        self.TemaVar.set("Tema Claro")
        self.popupmenu = OptionMenu(self.pw, self.TemaVar, *self.TVar)
        self.popupmenu.place(relx=0, rely=0.94)

        self.temabt = Button(self.pw, text="Alterar", command=self.mudartema)
        self.temabt.place(relx=0.2, rely=0.94)


Application()
