from time import sleep
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0')

it = util.Iterator(board)
it.start()

valD13 = board.get_pin('d:13:1')
valD12 = board.get_pin('d:12:1')
valD11 = board.get_pin('d:11:1')

board.digital[7].write(0)
stateb1 = True
stateb2 = True 
stateb3 = True

def timer():
    initial = 11
    while initial > 0:
        initial = initial-1
        print(initial)
        sleep(1)

def work():
    sleep(0.5)
    print("Work time will begin in 10 seconds")
    timer()
    print("Time to produce ")
    board.digital[10].write(1)
    sleep(5400)
    board.digital[10].write(0)
    board.digital[7].write(1)
    sleep(0.08)
    board.digital[7].write(0)
    stop()

def stop():
    sleep(0.5)
    board.digital[9].write(1)
    print('Take a break \nPress the yellow buttom to confirm the break')
    sleep(0.5)
    if b2state == 1:
        relax()
    

def relax():
    board.digital[9].write(0)
    sleep(0.5)
    board.digital[8].write(1)
    print('Its break time, you have 20 minutes')
    sleep(1200)
    board.digital[7].write(1)
    sleep(0.08)
    board.digital[7].write(0)
    print("End of the break \nPress the red buttom to go back work ")
    if b3state == 1: 
        endofbreak()

def endofbreak():
    board.digital[8].write(0)
    sleep(1)
    print('Lets go back to work')
    work()

while True:
    b1state = valD13.read()
    b2state = valD12.read()
    b3state = valD11.read()

    if b1state == 1:
        work()

    if b2state == 1:
        relax()
    
    if b3state == 1: 
        endofbreak()

