#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

import tkinter as tk

verification = tk.Tk()
verification.geometry("350x350")

lbl_verifage = tk.Label(verification)
lbl_verifage.place(x = 20, y = 200)

def verifyage():
    userage = int(ent_age.get())
    username = str(ent_name.get())
    if userage >= 16:
        lbl_verifage.config(text = "You are qualified to use my program!")
        btn_proceed.place(x = 100, y = 275)
        lbl_welcome = tk.Label(verification, text = "{}, Welcome!".format(username))
        lbl_welcome.place(x = 20, y = 160)
    elif userage < 16:
        lbl_verifage.config(text = "You are not old enough to qualify")

def quizselect():
    quizselect = tk.Tk()
    quizselect.geometry("350x350")
    verification.destroy()

lbl_name = tk.Label(verification, text = "What is your name?")
lbl_name.place(x = 20, y = 20)

lbl_age = tk.Label(verification, text = "What is your age?")
lbl_age.place(x = 20, y = 60)

ent_name = tk.Entry(verification)
ent_name.place(x = 150, y = 20)

ent_age = tk.Entry(verification)
ent_age.place(x = 150, y = 60)

btn_age = tk.Button(verification, text = "Verify your age!", bg = "#67fcd0", command = verifyage)
btn_age.place(x = 100, y = 100)

btn_proceed = tk.Button(verification, text = "Proceed with program", bg = "#67fcd0", command = quizselect)

verification.mainloop()