from py_expression_eval import Parser
from Tkinter import *

class Application:
    def __init__(self, master=None):

        #cria os containers
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        #funcao
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        #A
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        #B
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        #epsilon
        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        #botao
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        #nome do metodo
        self.titulo = Label(self.primeiroContainer, text = "Metodo de Bisseccao")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        #cria os labels
        self.funcaoLabel = Label(self.segundoContainer, text = "Funcao:", font = self.fontePadrao)
        self.funcaoLabel.pack(side = LEFT)

        self.funcao = Entry(self.segundoContainer)
        self.funcao["width"] = 30
        self.funcao["font"] = self.fontePadrao
        self.funcao.pack(side = LEFT)

        self.aLabel = Label(self.terceiroContainer, text = "A:", font = self.fontePadrao)
        self.aLabel.pack(side = LEFT)

        self.aVariavel = Entry(self.terceiroContainer)
        self.aVariavel["width"] = 30
        self.aVariavel["font"] = self.fontePadrao
        self.aVariavel.pack(side = LEFT)

        self.bLabel = Label(self.quartoContainer, text = "B:", font = self.fontePadrao)
        self.bLabel.pack(side = LEFT)

        self.bVariavel = Entry(self.quartoContainer)
        self.bVariavel["width"] = 30
        self.bVariavel["font"] = self.fontePadrao
        self.bVariavel.pack(side = LEFT)

        self.epsilonLabel = Label(self.quintoContainer, text = "Epsilon:", font = self.fontePadrao)
        self.epsilonLabel.pack(side = LEFT)

        self.epsilon = Entry(self.quintoContainer)
        self.epsilon["width"] = 30
        self.epsilon["font"] = self.fontePadrao
        self.epsilon.pack(side = LEFT)

        self.calcular = Button(self.sextoContainer)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.bisseccao
        self.calcular.pack()

        #mostra o resultado final
        self.resultado = Label(self.sextoContainer, text = "", font = self.fontePadrao)
        self.resultado.pack()

    #metodo de bisseccao
    def bisseccao(self):

        parser = Parser()

        expressao = self.funcao.get()
        a = float(self.aVariavel.get())
        b = float(self.bVariavel.get())
        epsilon = float(self.epsilon.get())

        #

        #Seta o primeiro valor de x
        x = float((a + b) / 2)

        fA = float(parser.parse(expressao).evaluate({'x' : a}))
        fB = float(parser.parse(expressao).evaluate({'x' : b}))
        fX = float(parser.parse(expressao).evaluate({'x' : x}))

        i = 1

        maiorErro = True
        while(maiorErro):
            i += 1
            #suplemento do excel -> steam table
            #Seta o primeiro valor de x

            if((fA > 0 and fX > 0) or (fA < 0 and fX < 0)):
                a = x
            else:
                b = x
    

            #Seta o enesimo valor de x
            x = float((a + b) / 2)

            fA = float(parser.parse(expressao).evaluate({'x' : a}))
            fB = float(parser.parse(expressao).evaluate({'x' : b}))
            fX = float(parser.parse(expressao).evaluate({'x' : x}))

            aux = float(b - a)
    
            if(b - a <= epsilon):
                maiorErro = False
        #joga resultado final na variavel resultado e seta o texto do resultado como sendo ela
        resultado = "Iteracao: " + str(i) + "\na: " + str(a) + "\nb: " + str(b) + "\nx: " + str(x) + "\nf(a): " + str(fA) + "\nf(b): " + str(fB) + "\nf(x): " + str(fX) + "\nErro: " + str(b - a)
        self.resultado["text"] = resultado
            #
root = Tk()
Application(root)
root.mainloop()