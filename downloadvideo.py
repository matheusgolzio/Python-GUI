from tkinter import *
from pytube import YouTube


root = Tk()


class Application:
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()

    # configuração da tela
    def tela(self):
        self.root.title("Video Downloader 3.0")
        self.root.resizable(False, False)
        self.root.configure(background="#04B404")
        self.root.geometry('700x500')

    def widgets(self):
        # titulo
        self.titulo = Label(self.root, text="YouTube Downloader", font=("Verdana", 20), bg="#04B404")
        self.titulo.place(relx=0.3, rely=0.01)

        # versao
        self.version = Label(self.root, text="Versão: 3.0", font=("Verdana", 10), bg="#04B404")
        self.version.place(relx=0.88, rely=0.96)

        # url
        self.url_label = Label(self.root, text='URL', font=("Verdana", 15), bg="#04B404")
        self.url_label.place(relx=0.2, rely=0.1)

        # url-entry
        self.url_entry = Entry(self.root, bd=0)
        self.url_entry.place(relx=0.28, rely=0.112, relwidth=0.6, relheight=0.04)

        # resolução
        self.Tipvar = StringVar(self.root)
        self.TipV = ("360p", "480p", "720p")
        self.Tipvar.set("720p")
        self.popupmenu = OptionMenu(self.root, self.Tipvar, *self.TipV)
        self.popupmenu.place(relx=0.57, rely=0.3, relheight=0.052)

        # local
        self.local_label = Label(self.root, text='Local', font=("Verdana", 15), bg="#04B404")
        self.local_label.place(relx=0.2, rely=0.2)

        # local-entry
        self.local_entry = Entry(self.root, bd=1)
        self.local_entry.place(relx=0.28, rely=0.212, relwidth=0.6, relheight=0.04)

        # download
        self.downbutton = Button(self.root, text="Download", command=self.download)
        self.downbutton.place(relx=0.47, rely=0.3)

        # limpar
        self.limpar = Button(self.root, text="Limpar", command=self.limpartela)
        self.limpar.place(relx=0.40, rely=0.3)

    def limpartela(self):
        self.local_entry.delete(0, END)
        self.url_entry.delete(0, END)

    def download(self):
        # processando-url
        self.url = self.url_entry.get()
        self.youtube = YouTube(self.url)
        self.streams = self.youtube.streams

        # procsssando-resolução
        self.res = self.Tipvar.get()
        if self.res == "720p":
            self.video = self.youtube.streams.get_by_itag(22)
        elif self.res == "360p":
            self.video = self.youtube.streams.get_by_itag(18)
        elif self.res == "480p":
            self.video = self.youtube.streams.get_by_itag(244)

        # obtendo local
        self.local = self.local_entry.get()

        # download
        self.video.download(self.local)


Application()
