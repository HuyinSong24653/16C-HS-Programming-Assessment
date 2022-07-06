#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

from tkinter import* #Importing the GUI
import random #Importing random to use

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
    if topicproceedvariable == 0:
        verification.destroy()
    global topicselect
    topicselect = Tk()
    topicselect.title("Quiz topic selecter")
    topicselect.geometry("375x475")

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
    btn_topicproceed = Button(topicselect, text = "Proceed with quiz", width = 14, height = 3, font = ("Arial", 12), bg = "#67fcd0", command = quizpage)

    if topicproceedvariable == 1:
        btn_topicproceed.place(x = 115, y = 380)

def quiztopic(arg):
    global topicproceedvariable
    topicproceedvariable = 1
    global mode
    if arg == 1:
        mode = 1
    elif arg == 2:
        mode = 2
    elif arg == 3:
        mode = 3
    elif arg == 4:
        mode = 4
    elif arg == 5:
        mode = 5
    elif arg == 6:
        mode = 6
    topicselect.destroy()
    selection()

def quizpage():
    topicselect.destroy()
    quiz = Tk()
    quiz.title("Quiz Window")
    quiz.geometry("750x750")

    btn_progress = Button(quiz, text = "Progress", font = ("Arial", 18), width = 10, height = 1)
    btn_progress.place(x = 25, y = 20)
    btn_notes = Button(quiz, text = "Notes", font = ("Arial", 18), width = 10, height = 1)
    btn_notes.place(x = 205, y = 20)
    btn_hint = Button(quiz, text = "Hint", font = ("Arial", 18), width = 10, height = 1, command = hintwindow)
    btn_hint.place(x = 385, y = 20)
    btn_endquiz = Button(quiz, text = "End quiz", font = ("Arial", 18), width = 10, height = 1)
    btn_endquiz.place(x = 565, y = 20)
    lbl_question = Label(quiz, width = 64, height = 3, font = ("Arial", 15), relief = "groove")
    lbl_question.place(x = 18, y = 100)
    btn_option1 = Button(quiz, width = 45, height = 6)
    btn_option1.place(x = 20, y = 500)
    btn_option2 = Button(quiz, width = 45, height = 6)
    btn_option2.place(x = 400, y = 500)
    btn_option3 = Button(quiz, width = 45, height = 6)
    btn_option3.place(x = 20, y = 625)
    btn_option4 = Button(quiz, width = 45, height = 6)
    btn_option4.place(x = 400, y = 625)

    lbl_question.config(text = Emergencies[quesfirst]["question"])
    btn_option1.config(text = Emergencies[quesfirst]["option1"])
    btn_option2.config(text = Emergencies[quesfirst]["option2"])
    btn_option3.config(text = Emergencies[quesfirst]["option3"])
    btn_option4.config(text = Emergencies[quesfirst]["option4"])

def hintwindow():
    hintpopup = Tk()
    hintpopup.title("Hint!")
    hintpopup.geometry("250x100")
    lbl_hint = Label(hintpopup)
    lbl_hint.pack()
    lbl_hint.config(text = Emergencies[quesfirst]["hint"])

verification = Tk()
verification.title("Verifications window")
verification.geometry("350x350")

lbl_verifage = Label(verification)
lbl_verifage.place(x = 20, y = 200)

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

topicproceedvariable = 0

quesorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(quesorder)

quesfirst = quesorder[0]

Emergencies = {
    1: {"question" : "Who can put a blue sign up?", "option1" : "An ambulance driver", "option2" : "A police officer", "option3" : "A council officer", "option4" : "A member of the public", "hint" : "Blue signs are compulsary, placed by people with control over traffic"}, #2
    2: {"question" : "When must you pull over and allow an ambulance or fire engine to pass?", "option1" : "If it is travelling faster than you want to", "option2" : "You don't need to let it past - you can speed up so you're not holding it up", "option3" : "If its siren and/or red flashing lights are on", "option4" : "At all times", "hint" : "Only when urgent, what shows urgency?"}, #3
    3: {"question" : "If you get into a collision, what would be the first step you would take?", "option1" : "Call the police", "option2" : "Call the ambulance", "option3" : "Call your insurance company", "option4" : "Check for injuries", "hint" : "What is most important?"}, #4
    4: {"question" : "If a moving car's front left tire burst, what would happen to the car?", "option1" : "The car will sway from side to side", "option2" : "The car would be pulled towards the left", "option3" : "The car would be pulled towards the right", "option4" : "The car would start spinning", "hint" : "Which side the tire is on directly affects the car"}, #2
    5: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : ""}, #
    6: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : ""}, #
    7: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : ""}, #
    8: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : ""}, #
    9: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : ""}, #
    10: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : ""}, #
}

verification.mainloop()