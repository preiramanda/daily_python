from tkinter import *
import pandas as pd 
import random as r

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") #gathering the dict per word


def next_card(): 
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = r.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(2000,func=flipcard)


def flipcard():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_bg, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



# _______ WINDOW SETTINGS______
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(2000,func=flipcard)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400,263,image=card_front_img)
canvas.grid(row=0,column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400,150, text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text= "",font=("Ariel",60,"bold"))

no = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=no,highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

yes = PhotoImage(file="images/right.png")
known_button = Button(image=yes,highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)







next_card()


window.mainloop()