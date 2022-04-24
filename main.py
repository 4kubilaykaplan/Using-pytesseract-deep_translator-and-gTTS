import time

from PIL import Image
from pytesseract import pytesseract
from deep_translator import GoogleTranslator
import gtts
from pygame import mixer
from tkinter import Tk, Button, PhotoImage, messagebox, filedialog, Canvas
import tkinter
import os
import sys
root= Tk()
def resource_path0(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
def openfile():
    global file
    file=tkinter.filedialog.askopenfilename(filetypes =[('PNG', '*.png'),('JPG','*.jpg')])
    if(len(file)>1):
        my_canvas.itemconfig(LocationError, text=file, fill="#6D76CD", font=("Aharoni",10))
        saveImg['text']='REOPEN'
        saveImg['bg']='#D0CECE'
        Common1=(os.path.basename(file).split('.')[0])
        path1=os.path.dirname(file)
    else:
        my_canvas.itemconfig(LocationError, text="Please Choose the Image", fill="#6D76CD", font=("Aharoni",10))
        saveImg['text']='OPEN'
        saveImg['bg']="#82CC6C"
def Check():
    if(len(file)>1):
        change(file)
    else:
        messagebox.showerror("Error","Please open your image!") 

img=Image.open(file)
patht=resource_path0("Tesseract\Tesseract-OCR\Tesseract.exe")#make sure you install the tesseract module inside the folder Tesseract.
pytesseract.pytesseract.tesseract_cmd=patht

print("---------Elde Edilen Metin---------")

text = pytesseract.image_to_string(img)
to_translate = text

print(text[:-1])
translated = GoogleTranslator(source='auto', target='turkish').translate(to_translate)

print("---------Cevirilen Metin---------")
print(translated)
language = 'tr'
tts = gtts.gTTS(text=translated, lang=language, slow=False)
tts.save("text.mp3")

mixer.init()
mixer.music.load("text.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
