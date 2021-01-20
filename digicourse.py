from tkinter import *


root = Tk()


# back-end
class Funcoes:
    def limpartela(self):
        self.entry_nome.delete(0, END)

    def limpardigi(self):
        self.digitar_entry.delete(0, END)

    def trocarfase(self):
        # obtendo fase
        self.fase = self.Tipvar.get()

        # listas
        self.itensf1 = ("fazer", "coisa", "amigo", "amizade", "zebra", "abacaxi", "morango", "thing")
        self.itensf2 = ("eu sou um cara maneiro", "meu amigo gosta de biscoito",
                        "fica frio ae meu chapa", "o rato roeu a roupa do rei de roma",
                        "ps2 muito melhor que muito console")
        self.itensf3 = ("também", "amém", "têm", "você")
        self.itensf4 = ("Matheus", "Tietê", "Roma", "Romero Brito", "Afonso", "Natal")
        self.itensf5 = ("Ei cara!", "O que foi meu chapa?",
                        "Nada não, só queria dizer que você é gay.", "Ah tá.",
                        "Seu gay.")
        self.itensf6 = ("Hoje", "Frase", "Programação", "Jantar", "Casar")
        self.itensf7 = ("Eu e meu amigo somos otários.", "Como é bom jogar vídeo-game!",
                        "Eu adoro tomar suquin de manhã")
        self.itensf8 = ("Neném", "Coé", "Menó", "Filé")
        self.itensf9 = ("Tu é gay meu parceirin?", "Eu amo programar!", "Só sei que nada sei.",
                        "Todo mundo sabe que hqs são melhores que livros.", "Código bugou?")
        self.itensf10 = ("Fala galera, deixa o like!", "Eu estou estudando digitação",
                         "Eu amo o Matheus", "Eu não tive escolha, tive que escrever...",
                         "Você é do mal Matheus?")
        self.itensf11 = ("Continue praticando.", "Depois que acabar, faça tudo novamente.",
                         "Sem preguiça!", "Matheus falou tá falado!")
        self.itensf12 = ("Amar", "Odiar", "Praça", "Guerra", "Kratos", "Olimpo", "Páscoa")
        self.itensf13 = ("Roubar", "Jogar", "Kibe", "Coxinha", "Frangão", "Goku")
        self.itensf14 = ("Repita tudo, amigo.", "Chapa", "A Terra é redonda, seu burro.",
                         "Desulpa, errei, é quadrada.", "Pedro easter-eggs")

        # label itens padrão
        self.labelitens = Label(self.frame1, text="", fg="white", bg="black",
                                font=("Verdana", 15))

        # label status padrão
        self.labelstatus = Label(self.frame3, text="", font=("Verdana", 20))
        self.labelstatus.place(relx=0.70, rely=0.5)

        if self.fase == "Palavras":
            self.labelitens["text"] = f"{self.itensf1}"
            self.labelitens.place(relx=0, rely=0.3, relwidth=1, relheight=0.3)

        elif self.fase == "Frases":
            self.labelitens["text"] = f"{self.itensf2}"
            self.labelitens["font"] = ("Verdana", 11)
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4)

        elif self.fase == "Palavras com acentos":
            self.labelitens["text"] = f"{self.itensf3}"
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Palavras com Letras Maiúsculas":
            self.labelitens["text"] = f"{self.itensf4}"
            self.labelitens.place(relx=0, rely=0.3, relwidth=1, relheight=0.4)

        elif self.fase == "Frases com Pontuação":
            self.labelitens["text"] = f"{self.itensf5}"
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4)

        elif self.fase == "Palavras2":
            self.labelitens["text"] = f"{self.itensf6}"
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Frases2":
            self.labelitens["text"] = f"{self.itensf7}"
            self.labelitens["font"] = ("Verdana", 11)
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Palavras com acentos2":
            self.labelitens["text"] = f"{self.itensf8}"
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Frases3":
            self.labelitens["text"] = f"{self.itensf9}"
            self.labelitens["font"] = ("Verdana", 11)
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Frases4":
            self.labelitens["text"] = f"{self.itensf10}"
            self.labelitens["font"] = ("Verdana", 11)
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Frases5":
            self.labelitens["text"] = f"{self.itensf11}"
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Palavras3":
            self.labelitens["text"] = f"{self.itensf12}"
            self.labelitens["font"] = ("Verdana", 11)
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Palavras4":
            self.labelitens["text"] = f"{self.itensf13}"
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

        elif self.fase == "Treino":
            self.labelitens["text"] = f"{self.itensf14}"
            self.labelitens.place(relx=0, rely=0.3, relheight=0.4, relwidth=1)

    def bt_enviar(self):
        # resultado obtido pela entry
        self.resultado = self.digitar_entry.get()

        # contadores
        countf1, countf2, countf3, countf4, countf5, countf6, countf7, countf8,\
            countf9, countf10, countf11, countf12, \
        countf13, countf14 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        # Fase 1
        for palavraf1 in self.itensf1:
            if palavraf1 in self.resultado:
                countf1 += 1
                if countf1 == len(self.itensf1):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 2
        for palavraf2 in self.itensf2:
            if palavraf2 in self.resultado:
                countf2 += 1
                if countf2 == len(self.itensf2):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 3
        for palavraf3 in self.itensf3:
            if palavraf3 in self.resultado:
                countf3 += 1
                if countf3 == len(self.itensf3):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 4
        for palavraf4 in self.itensf4:
            if palavraf4 in self.resultado:
                countf4 += 1
                if countf4 == len(self.itensf4):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 5
        for palavraf5 in self.itensf5:
            if palavraf5 in self.resultado:
                countf5 += 1
                if countf5 == len(self.itensf5):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 6
        for palavraf6 in self.itensf6:
            if palavraf6 in self.resultado:
                countf6 += 1
                if countf6 == len(self.itensf6):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 7
        for palavraf7 in self.itensf7:
            if palavraf7 in self.resultado:
                countf7 += 1
                if countf7 == len(self.itensf7):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 8
        for palavraf8 in self.itensf8:
            if palavraf8 in self.resultado:
                countf8 += 1
                if countf8 == len(self.itensf8):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 9
        for palavraf9 in self.itensf9:
            if palavraf9 in self.resultado:
                countf9 += 1
                if countf9 == len(self.itensf9):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 10
        for palavraf10 in self.itensf10:
            if palavraf10 in self.resultado:
                countf10 += 1
                if countf10 == len(self.itensf10):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 11
        for palavraf11 in self.itensf11:
            if palavraf11 in self.resultado:
                countf11 += 1
                if countf11 == len(self.itensf11):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 12
        for palavraf12 in self.itensf12:
            if palavraf12 in self.resultado:
                countf12 += 1
                if countf12 == len(self.itensf12):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 13
        for palavraf13 in self.itensf13:
            if palavraf13 in self.resultado:
                countf13 += 1
                if countf13 == len(self.itensf13):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"

        # Fase 14
        for palavraf14 in self.itensf14:
            if palavraf14 in self.resultado:
                countf14 += 1
                if countf14 == len(self.itensf14):
                    self.limpardigi()
                    self.labelstatus["fg"] = "green"
                    self.labelstatus["text"] = "Fase Concluída!"
                else:
                    self.limpardigi()
                    self.labelstatus["fg"] = "red"
                    self.labelstatus["text"] = "Tente Novamente!"


# front-end
class Application(Funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.fases()
        self.digitar()
        self.telapalavras()
        self.trocarfase()
        self.bt_enviar()
        root.mainloop()

    def tela(self):
        self.root.resizable(True, True)
        self.root.title("Digi Course 1.5")
        self.root.geometry("1280x720")

    def frames(self):
        # local das palavras
        self.frame1 = Frame(self.root, bg="black")
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=0.4)

        # fases
        self.frame4 = Frame(self.root, bg="#2f2830")
        self.frame4.place(relx=0, rely=0.4, relwidth=0.2, relheight=0.6)

        # digitar palavras
        self.frame3 = Frame(self.root)
        self.frame3.place(relx=0.2, rely=0.4, relwidth=0.8, relheight=0.6)

    def fases(self):
        # titulo
        self.title_fases = Label(self.frame4, text="Selecione a fase:", fg="#830094",
                                 font=("Verdana", 13, 'bold'), bg="#2f2830")
        self.title_fases.place(relx=0.18, rely=0.02)


        # lista de fases
        self.Tipvar = StringVar(self.frame4)
        self.TipV = ("Palavras", "Frases", "Palavras com acentos",
                     "Palavras com Letras Maiúsculas", "Frases com Pontuação", "Palavras2",
                     "Frases2", "Palavras com acentos2", "Frases3",
                     "Frases4", "Frases5", "Palavras3", "Palavras4", "Treino")
        self.Tipvar.set("Palavras")
        self.popupMenu = OptionMenu(self.frame4, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0, rely=0.1, relwidth=1)

        # botão mudar
        self.mudarfase = Button(self.frame4, text="Mudar Fase", font=("Verdana", 13),
                                fg="#830094", command=self.trocarfase)
        self.mudarfase.place(relx=0.28, rely=0.4)

    def digitar(self):
        # dedos
        self.posicao = Label(self.frame3, text="Posição dos dedos:", font=("Verdana", 15, 'bold'))
        self.posicao.place(relx=0.2, rely=0)

        # label digitar
        self.digitar = Label(self.frame3, text="Digitar", font=("Verdana", 13, 'bold'),
                             fg="#830094")
        self.digitar.place(relx=0.28, rely=0.81)

        # entry digitar
        self.digitar_entry = Entry(self.frame3, bd=4)
        self.digitar_entry.place(relx=0.10, rely=0.91, relwidth=0.445, relheight=0.06)

        # botão enviar
        self.btenviar = Button(self.frame3, text="Enviar", fg="purple", font=("Verdana", 10, 'bold'),
                               command=self.bt_enviar)
        self.btenviar.place(relx=0.55, rely=0.91)

        # imagem
        imagem = PhotoImage(file="C:/Users/user/OneDrive/Imagens/qwerty-home-keys-position.png")
        w = Label(self.frame3, image=imagem)
        w.imagem = imagem
        w.place(relx=0.1, rely=0.1)

    def telapalavras(self):
        # title
        self.titletela = Label(self.frame1,
                               text="Digite as palavras (de espaço a cada palavra e/ou frase digitada):",
                               font=("Verdana", 15), fg="green", bg="black")
        self.titletela.place(relx=0, rely=0)


Application()
