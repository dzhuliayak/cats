from tkinter import *
from PIL import Image, ImageTk
import requests
from io import Bytes, BytesIO

from bottle import response
from pygame.examples.cursors import image


def loade_image():
    try:
        response=requests.get(url)
        response.raise_for_status()
        image_data=BytesIO(response.content)
        img =Image.open(image_data)
        return  ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"произошла ошибка : {e}")
        return None


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




