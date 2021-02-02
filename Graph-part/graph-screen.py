from Tkinter import *
from time import sleep


class screen:
    def __init__(self, master=None):
        
        window.title("Pomodoro project")

        self.container1 = Frame(master)
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2.pack()
        
        self.container3 = Frame(master)
        self.container3.pack()

        

        self.texto1 = Label(self.container1, text="Bem vindo ao Projeto pomodoro", bg="blue")
        self.texto1["font"] = ("Arial", "10")
        self.texto1.pack()

        
        
        self.texto2 = Label(self.container2, text="Segundo container", bg="red")
        self.texto2["font"] = ("Arial", "10")
        self.texto2.pack()

        self.texto3 = Label(self.container3, text="Terceiro container", bg="orange")
        self.texto3["font"] = ("Arial", "10")
        self.texto3.pack()


        self.teste = Button(self.container3)
        self.teste["text"] = "Trocar cor"
        self.teste["font"] = ("Calibri", "9")
        self.teste["width"] = 10
        self.teste["command"] = self.color
        self.teste.pack()

    def color(self):
        sleep(3)
        self.texto1["background"] ="yellow"
        self.teste["command"] = self.color2
    def color2(self):
        sleep(3)
        self.texto2["background"] = "purple"
        self.teste["command"] = self.color3
    def color3(self):
        sleep(3)
        self.texto3["background"] = "red"


        


window = Tk()
screen(window)
window.mainloop()
