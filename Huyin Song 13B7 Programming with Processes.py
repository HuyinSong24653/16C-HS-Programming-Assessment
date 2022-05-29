#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

import tkinter as tk

window = tk.Tk()
window.geometry("350x350")

lbl_verifage = tk.Label(window)
lbl_verifage.place(x = 20, y = 200)

def quizselect():
    quizselect = tk.Tk()
    quizselect.geometry("350x350")


def verifyage():
    if ent_age.get() >= "16":
        lbl_verifage.config(text = "You are qualified to use my program!")
        btn_proceed.place(x = 100, y = 275)
    
    if ent_age.get() < "16":
        lbl_verifage.config(text = "You are not old enough to qualify")
#9 = qualified, 10 = not qualified, 15 = not qualified, 16 = qualified, 16+ = qualified, 100 = not qualified, 159 not qualified, 160 qualified
#Seems to be an error somewhere, maybe something to do with the significant figures or position of numbers

lbl_name = tk.Label(window, text = "What is your name?")
lbl_name.place(x = 20, y = 20)

lbl_age = tk.Label(window, text = "What is your age?")
lbl_age.place(x = 20, y = 60)

ent_name = tk.Entry(window)
ent_name.place(x = 150, y = 20)

ent_age = tk.Entry(window)
ent_age.place(x = 150, y = 60)

btn_age = tk.Button(window, text = "Verify your age!", bg = "#67fcd0", command = verifyage)
btn_age.place(x = 100, y = 100)

btn_proceed = tk.Button(window, text = "Proceed with program", bg = "#67fcd0", command = quizselect)

window.mainloop()