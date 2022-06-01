from tkinter import Frame
import constants as c
import helper
class Game(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.bind("<Key>", self.key_down)

    def key_down(self, event):
        key = repr(event.char)
        print(key)