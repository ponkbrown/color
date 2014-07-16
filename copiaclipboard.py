from Tkinter import Tk

def leeClipboard():
    ''' Esta funcion lee lo que esta en  el clipboard y lo regresa '''
    r = Tk()
    r.withdraw()
    regresa = r.clipboard_get()
    r.destroy()

    return regresa
