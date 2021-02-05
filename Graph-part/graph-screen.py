from Tkinter import *
from time import sleep
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB1')
it = util.Iterator(board)
it.start()
board.digital[7].write(0)



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

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 4
        self.container4.pack()

        

        self.texto0 = Label(self.container0, text="Bem vindo ao Projeto pomodoro")
        self.texto0["font"] = ("Arial", "10")
        self.texto0.pack()

        self.texto1 = Label(self.container1, text="Working....", bg="gray", width=20)
        self.texto1["font"] = ("Arial", "10")
        self.texto1.pack()
        
        self.texto2 = Label(self.container2, text="Its break time!!!", bg="gray",width=20)
        self.texto2["font"] = ("Arial", "10")
        self.texto2.pack()

        self.texto3 = Label(self.container3, text="Finally finished", bg="gray",width=20)
        self.texto3["font"] = ("Arial", "10")
        self.texto3.pack()

        self.msg = Label(self.container4, bg="white", width=15)
        self.msg["text"] = ""
        self.msg["font"] = ("Arial", "10")
        self.msg.pack()

        self.action = Button(self.container3)
        self.action["text"] = "Iniciar"
        self.action["font"] = ("Calibri", "9")
        self.action["width"] = 10
        self.action["command"] = self.t1
        self.action.pack()

    def c1(self):
        sleep(0.5)
        self.msg["text"] = "Press"
        self.action["command"] = self.t1

    def t1(self):
        self.texto1["background"] = self.color1
        self.msg["text"] = "Work Time"
        self.action["text"] = "Start Timer"
        sleep(0.5)
        self.action["command"] = self.timer1
    def t2(self):
        self.texto2["background"] = self.color2
        sleep(0.5)
        self.action["text"] = "Press"
        self.msg["text"] = "Break Time"

    def timer1(self):
        sleep(5400)
        board.digital[7].write(1)
        sleep(0.08)
        board.digital[7].write(0)
        self.action["command"] = self.t2
        self.msg["text"] = "Break"
    def timer2(self):
        sleep(1200)
        board.digital[7].write(1)
        sleep(0.08)
        board.digital[7].write(0)
        self.action["command"] = self.timer3
        self.action["text"] = "Next"
        self.msg["text"] = "End"
    def timer3(self):
        self.texto3["background"] = self.color3
        self.action["command"] = self.reset
        self.msg["text"] = ""
        self.action["text"] = "Finish"

        
    def reset(self):
        sleep(0.5)
        self.texto1["background"] = self.color0
        self.texto2["background"] = self.color0
        self.texto3["background"] = self.color0
        self.action["command"] = self.c1
        self.action["text"] = "Iniciar"
        self.msg["text"] = ""


window = Tk()
screen(window)
window.mainloop()


