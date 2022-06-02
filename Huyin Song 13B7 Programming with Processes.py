#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

from tkinter import*

verification = Tk()
verification.title("Verifications window")
verification.geometry("350x350")

lbl_verifage = Label(verification)
lbl_verifage.place(x = 20, y = 200)

def verifyage():
    userage = int(ent_age.get())
    username = str(ent_name.get())
    if userage >= 16:
        lbl_verifage.config(text = "You are qualified to use my program!")
        btn_proceed.place(x = 100, y = 275)
        lbl_welcome = Label(verification, text = "{}, Welcome!".format(username))
        lbl_welcome.place(x = 20, y = 160)
    elif userage < 16:
        lbl_verifage.config(text = "You are not old enough to qualify")

def selection():
    quizselect = Tk()
    quizselect.title("Quiz topic selecter")
    quizselect.geometry("375x375")
    verification.destroy()

    lbl_quizselectwelcome = Label(quizselect, text = "What topic would you like to be tested on?", font = ("Arial", 11))
    lbl_quizselectwelcome.place(x = 45, y = 30)
    btn_general = Button(quizselect, text = "General", width = 14, height = 3, font = ("Arial", 12))
    btn_general.place(x = 25, y = 85)
    btn_emergencies = Button(quizselect, text = "Emergencies", width = 14, height = 3, font = ("Arial", 12))
    btn_emergencies.place(x = 200, y = 85)
    btn_parking = Button(quizselect, text = "Parking", width = 14, height = 3, font = ("Arial", 12))
    btn_parking.place(x = 25, y = 180)
    btn_road = Button(quizselect, text = "Road", width = 14, height = 3, font = ("Arial", 12))
    btn_road.place(x = 200, y = 180)
    btn_rules = Button(quizselect, text = "Rules", width = 14, height = 3, font = ("Arial", 12))
    btn_rules.place(x = 25, y = 275)
    btn_driver = Button(quizselect, text = "Driver", width = 14, height = 3, font = ("Arial", 12))
    btn_driver.place(x = 200, y = 275)

lbl_name = Label(verification, text = "What is your name?")
lbl_name.place(x = 20, y = 20)

lbl_age = Label(verification, text = "What is your age?")
lbl_age.place(x = 20, y = 60)

ent_name = Entry(verification)
ent_name.place(x = 150, y = 20)

ent_age = Entry(verification)
ent_age.place(x = 150, y = 60)

btn_age = Button(verification, text = "Verify your age!", bg = "#67fcd0", command = verifyage)
btn_age.place(x = 100, y = 100)

btn_proceed = Button(verification, text = "Proceed with program", bg = "#67fcd0", command = selection)


#DEVELOPER SHORTCUT
btn_dev = Button(verification, text = "dev", bg = "#67fcd0", command = selection)
btn_dev.pack()


verification.mainloop()