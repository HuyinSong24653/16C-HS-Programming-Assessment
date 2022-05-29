#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

import tkinter as tk
window = tk.Tk()
window.geometry("500x500")


lbl_verifage = tk.Label(window)
lbl_verifage.place(x = 150, y = 150)

def verifyage():
    if ent_age.get() <= "16":
        lbl_verifage.config(text = "You are qualified to use my program!")
    
    if ent_age.get() > "16":
        lbl_verifage.config(text = "You are not old enough to qualify")


lbl_name = tk.Label(window, text = "What is your name?")
lbl_name.place(x = 20, y = 20)

lbl_age = tk.Label(window, text = "What is your age?")
lbl_age.place(x = 20, y = 60)

ent_name = tk.Entry(window)
ent_name.place(x = 150, y = 20)

ent_age = tk.Entry(window)
ent_age.place(x = 150, y = 60)

bnt_age = tk.Button(window, text = "Verify your age!", bg = "#67fcd0", command = verifyage)
bnt_age.place(x = 20, y = 150)

window.mainloop()