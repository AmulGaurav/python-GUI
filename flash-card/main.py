import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {} # Initialized empty dictionary
current_card = {} # Initialized empty dictionary

# <-------------------------Create New Flash Cards------------------------>
# 
try:
    data = pandas.read_csv("data\words_to_learn.csv")
except:
    original_data = pandas.read_csv("data\\french_words.csv")
    # parameter orient="records" is used to store data in the form of: [{french_word: english_word}, ...]
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

# <---------------------------Functionality------------------------------->
# is_known() is triggered when user clicks on check button which means user already knows what's written on the card
def is_known():
    # remove current card from the data_dict
    data_dict.remove(current_card)
    # creates a pandas dataframe from data_dict which includes the only data which user doesn't know and wants to learn
    to_learn = pandas.DataFrame(data=data_dict)
    # creates a csv file from the to_learn dataframe
    to_learn.to_csv("data\words_to_learn.csv", index=False)
    # next_card() function is called in order to show the next card with new data
    next_card()

# next_card() function is trigerred when user clicks on cross button whch means user doesn't know the meaning of the french word shown on the card and wants to learn it in future
def next_card():
    # To modify global variables
    global current_card, flip_timer
    # To end the window.after() function
    window.after_cancel(flip_timer)
    # randomly chose a piece of data from data_dict which is a list of dictionary
    current_card = random.choice(data_dict)
    # To configure canvas text
    canvas.itemconfig(tagOrId=card_title, text="French", fill="black")
    canvas.itemconfig(tagOrId=card_word, text=current_card["French"], fill="black")
    # To change the image
    canvas.itemconfig(tagOrId=canvas_img, image=card_front_img)
    # To delay the screen for 3 seconds and call the flip_card() function which shows the english meaning of the french word
    flip_timer = window.after(ms=3000, func=flip_card)

# flip_card() functions triggered automatically whenever the next_card() function is called
def flip_card():
    # To configure canvas text
    canvas.itemconfig(tagOrId=card_title, text="English", fill="white")
    canvas.itemconfig(tagOrId=card_word, text=current_card["English"], fill="white")
    # To change the image
    canvas.itemconfig(tagOrId=canvas_img, image=card_back_img)

# <---------------------------------UI------------------------------------->
window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# To delay the screen for 3 seconds and call the flip_card() function which shows the english meaning of the french word
flip_timer = window.after(ms=3000, func=flip_card)

# Canvas
canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(file="images\card_front.png")
card_back_img = tkinter.PhotoImage(file="images\card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
# Save image path to a variable using PhotoImage() class because image_path can't directly given to a Canvas widget
cross_img = tkinter.PhotoImage(file="images\wrong.png")
# Creating image inside the canvas
unknown_button = tkinter.Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Save image path to a variable using PhotoImage() class because image_path can't directly given to a Canvas widget
check_img = tkinter.PhotoImage(file="images\\right.png")
# Creating image inside the canvas
known_button = tkinter.Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# next_card() function is called in order to show a random card whenver program runs for the first time
next_card()

window.mainloop()