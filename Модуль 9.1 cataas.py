from tkinter import *
from PIL import Image, ImageTk
import requests
from io import Bytes

from pygame.examples.aliens import load_image

IOError


window=Tk()
window.title("Cats!")
window.geometry("600x480")


label=Label()
label.pack()

url="https://github.com/dzhuliayak/cats"
img=load_image(url)

if img:
    label.config(image=img)
    label.image=img

window.mainloop()




