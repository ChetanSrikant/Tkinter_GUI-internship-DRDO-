import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode('light')
        super().__init__(fg_color='white')
        self.mainloop()


App()