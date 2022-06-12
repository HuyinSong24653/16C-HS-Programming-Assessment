#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

from tkinter import*

verification = Tk()
verification.title("Verifications window")
verification.geometry("350x350")

lbl_verifage = Label(verification)
lbl_verifage.place(x = 20, y = 200)

def verifyage():
    try:
        username = str(ent_name.get())
        userage = int(ent_age.get())
        if userage <= 0:
            lbl_verifage.config(text = "Invalid input! You cannot be 0 or negative years old!")
        elif userage > 0 and userage < 16:
            lbl_verifage.config(text = "You are not old enough to qualify!")
        elif userage >= 16 and userage < 122:
            lbl_verifage.config(text = "You are qualified to use my program!")
            lbl_welcome = Label(verification, text = "{}, Welcome!".format(username))
            lbl_welcome.place(x = 20, y = 160)
            btn_verifproceed.place(x = 100, y = 275)
        elif userage >= 122:
            lbl_verifage.config(text = "Invalid input!\nThe highest recorded age of humans was 122 years old!")
    except ValueError:
        lbl_verifage.config(text = "Invalid input! Please input an integer!")

def selection():
    verification.destroy()
    global topicselect
    topicselect = Tk()
    topicselect.title("Quiz topic selecter")
    topicselect.geometry("375x450")

    lbl_quizselectwelcome = Label(topicselect, text = "What topic would you like to be tested on?", font = ("Arial", 11))
    lbl_quizselectwelcome.place(x = 45, y = 30)
    btn_general = Button(topicselect, text = "General", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(1))
    btn_general.place(x = 25, y = 85)
    btn_emergencies = Button(topicselect, text = "Emergencies", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(2))
    btn_emergencies.place(x = 200, y = 85)  
    btn_parking = Button(topicselect, text = "Parking", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(3))
    btn_parking.place(x = 25, y = 180)
    btn_road = Button(topicselect, text = "Road", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(4))
    btn_road.place(x = 200, y = 180)
    btn_rules = Button(topicselect, text = "Rules", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(5))
    btn_rules.place(x = 25, y = 275)
    btn_driver = Button(topicselect, text = "Driver", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(6))
    btn_driver.place(x = 200, y = 275)

    btn_sus = Button(topicselect, text = "Proceed with quiz", width = 14, height = 3, font = ("Arial", 12), bg = "#67fcd0", command = quizpage)
    btn_sus.pack()

def quiztopic(arg):
    if arg == 1:
        print("general")
    elif arg == 2:
        print("emergencies")
    elif arg == 3:
        print("sus")
    elif arg == 4:
        print("sus")
    elif arg == 5:
        print("sus")
    elif arg == 6:
        print("sus")

def quizpage():
    topicselect.destroy()
    quiz = Tk()
    quiz.title("Quiz Window")
    quiz.geometry("750x750")

    btn_progress = Button(quiz, text = "Progress", font = ("Arial", 18), width = 10, height = 2)
    btn_progress.place(x = 25, y = 20)
    btn_notes = Button(quiz, text = "Notes", font = ("Arial", 18), width = 10, height = 2)
    btn_notes.place(x = 205, y = 20)
    btn_hint = Button(quiz, text = "Hint", font = ("Arial", 18), width = 10, height = 2)
    btn_hint.place(x = 385, y = 20)
    btn_endquiz = Button(quiz, text = "End quiz", font = ("Arial", 18), width = 10, height = 2)
    btn_endquiz.place(x = 565, y = 20)
    lbl_question = Label(quiz, text = "Question here", width = 64, height = 2, font = ("Arial", 15), relief = "groove")
    lbl_question.place(x = 18, y = 125)

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

btn_verifproceed = Button(verification, text = "Proceed with program", bg = "#67fcd0", command = selection)

#DEVELOPER SHORTCUT
btn_dev = Button(verification, text = "dev", bg = "#67fcd0", command = selection)
btn_dev.pack()


verification.mainloop()