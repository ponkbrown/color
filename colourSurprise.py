from Tkinter import Tk
import serial

def leeClip():
    r = Tk()
    r.withdraw()
    regresa = r.clipboard_get()
    r.destroy()
    return regresa

while True:
    
    color = leeClip()

    color = color[4:-1]
#    print color
    arduino = serial.Serial('/dev/ttyUSB0', 9600)

    arduino.write(color+'\n')

    arduino.close()
