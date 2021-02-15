from Tkinter import *
from time import sleep
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0')
it = util.Iterator(board)
it.start()
board.digital[7].write(0)



class screen:
    def __init__(self, master=None):
        window.title("Pomodoro project")
        self.font = ("Arial", "15")
        self.color1 = "green"
        self.color2 = "orange"
        self.color3 = "red"

        self.container0 = Frame(master)
        self.container0.pack()
        self.container0["padx"] = 120
        self.container0["pady"] = 120

        self.color0 = self.container0.cget("bg")

        self.container1 = Frame(master)
        self.container1["padx"] = 30
        self.container1["pady"] = 8
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 30 
        self.container2["pady"] = 18
        self.container2.pack()
        
        self.container3 = Frame(master)
        self.container3["padx"] = 30
        self.container3["pady"] = 8
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 30
        self.container4["pady"] = 8
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 30
        self.container5["pady"] = 8
        self.container5.pack()

        

        self.texto0 = Label(self.container0, text="Bem vindo ao Projeto pomodoro")
        self.texto0["font"] = ("Arial", "20")
        self.texto0.pack()

        self.texto1 = Label(self.container1)
        self.texto1["width"] = 35
        self.texto1["height"] = 2
        self.texto1["font"] = self.font
        self.texto1.pack()
        
        self.texto2 = Label(self.container2)
        self.texto2["width"] = 35
        self.texto2["height"] = 2
        self.texto2["font"] = self.font
        self.texto2.pack()

        self.texto3 = Label(self.container3)
        self.texto3["width"] = 35
        self.texto3["height"] = 2
        self.texto3["font"] = self.font
        self.texto3.pack()

        self.msg = Label(self.container5)
        self.msg["width"] = 30
        self.msg["text"] = ""
        self.msg["font"] = self.font
        self.msg.pack()

        self.action = Button(self.container4)
        self.action["text"] = "Iniciar"
        self.action["font"] = self.font
        self.action["width"] = 30
        self.action["command"] = self.t1
        self.action.pack()

   

    def t1(self):
        self.msg["background"] = "white"
        self.texto1["background"] = self.color1
        self.texto1["text"] = "Working...."
        self.msg["text"] = "Work Time"
        self.action["text"] = "Start Timer"
        sleep(0.5)
        self.action["command"] = self.timer1
        

    def timer1(self):
        sleep(5400)
        board.digital[7].write(1)
        sleep(0.08)
        board.digital[7].write(0)
        self.texto1["text"] = ""
        self.texto1["background"] = self.color0
        self.action["text"] = "Start timer"
        self.action["command"] = self.timer2
        self.texto2["background"] = self.color2
        self.msg["text"] = "Break Time"
        self.texto2["text"] = "Its break time !!!"
        
    def timer2(self):
        sleep(1200)
        board.digital[7].write(1)
        sleep(0.08)
        board.digital[7].write(0)
        self.texto2["text"] = ""
        self.texto2["background"] = self.color0
        self.action["command"] = self.timer3
        self.action["text"] = "Next"
        self.msg["text"] = "End"
    def timer3(self):
        self.texto3["background"] = self.color3
        self.texto3["text"] = "Finally done"
        self.action["command"] = self.reset
        self.msg["text"] = ""
        self.msg["background"] = self.color0
        self.action["text"] = "Finish"

        
    def reset(self):
        sleep(0.5)
        self.texto1["background"] = self.color0
        self.texto2["background"] = self.color0
        self.texto3["background"] = self.color0
        self.texto3["text"] = ""
        self.action["command"] = self.t1
        self.action["text"] = "Iniciar"
        self.msg["text"] = ""


window = Tk()
screen(window)
window.mainloop()


