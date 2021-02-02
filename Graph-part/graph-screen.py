from Tkinter import *
from time import sleep


class screen:
    def __init__(self, master=None):
        window.title("Pomodoro project")
        self.color0 = "gray"
        self.color1 = "green"
        self.color2 = "orange"
        self.color3 = "red"

        self.container0 = Frame(master)
        self.container0.pack()

        self.container1 = Frame(master)
        self.container1["padx"] = 30
        self.container1["pady"] = 4
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20 
        self.container2["pady"] = 4
        self.container2.pack()
        
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 4
        self.container3.pack()

        

        self.texto0 = Label(self.container0, text="Bem vindo ao Projeto pomodoro")
        self.texto0["font"] = ("Arial", "10")
        self.texto0.pack()

        self.texto1 = Label(self.container1, text="Primeiro container", bg="gray", width=20)
        self.texto1["font"] = ("Arial", "10")
        self.texto1.pack()
        
        self.texto2 = Label(self.container2, text="Segundo container", bg="gray",width=20)
        self.texto2["font"] = ("Arial", "10")
        self.texto2.pack()

        self.texto3 = Label(self.container3, text="Terceiro container", bg="gray",width=20)
        self.texto3["font"] = ("Arial", "10")
        self.texto3.pack()


        self.teste = Button(self.container3)
        self.teste["text"] = "Trocar cor"
        self.teste["font"] = ("Calibri", "9")
        self.teste["width"] = 10
        self.teste["command"] = self.c1
        self.teste.pack()

    def c1(self):
        sleep(3)
        self.texto1["background"] = self.color1
        self.teste["command"] = self.c2
    def c2(self):
        sleep(3)
        self.texto2["background"] = self.color2
        self.teste["command"] = self.c3
    def c3(self):
        sleep(3)
        self.texto3["background"] = self.color3
        self.teste["command"] = self.c0 
    def c0(self):
        sleep(1)
        self.texto1["background"] = self.color0
        self.texto2["background"] = self.color0
        self.texto3["background"] = self.color0


        


window = Tk()
screen(window)
window.mainloop()
