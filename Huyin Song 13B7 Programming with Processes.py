#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

from tkinter import* #Importing the GUI
import random #Importing random to use

def verifyage(): #A function that contains the logic for the user's name and age
    try: #Try and except to prevent errors
        username = str(ent_name.get()) #Getting the user's name from the entry box
        userage = int(ent_age.get()) #Getting the user's age from the entry box
        if userage <= 0: #If user's age is less or equal to 0
            lbl_verifage.config(text = "Invalid input! You cannot be 0 or negative years old!") #Configs label to print user has invalid age
        elif userage > 0 and userage < 16: #If user's age is between 0 and 16
            lbl_verifage.config(text = "You are not old enough to qualify!") #Configs label to print user is too young to use program
        elif userage >= 16 and userage < 122: #If user's age is equal or more than 16, and between 16 to 122
            lbl_verifage.config(text = "You are qualified to use my program!") #configs label to welcome the user, stating their qualified status
            lbl_welcome = Label(verification, text = "{}, Welcome!".format(username)) #Establishing a label that welcomes the user, using their username
            lbl_welcome.place(x = 20, y = 160) #Places it onto the GUI
            btn_verifproceed.place(x = 100, y = 275) #Places the established button, allowing the user to proceed
        elif userage >= 122: #If user's age is more or equal to 122
            lbl_verifage.config(text = "Invalid input!\nThe highest recorded age of humans was 122 years old!") #Printing an invalid input message, user is impossibly old
    except ValueError: #Try and except, this prevents a value error just in case the user inputs symbols or something not a integer
        lbl_verifage.config(text = "Invalid input! Please input an integer!") #Configuring the label to help users recover from their typo

def selection(): #A function for the topic selecting page
    if topicproceedvariable == 0: #A little way to prevent a looping error
        verification.destroy() #Destroys the verifications page, saves the user's time and effort from needing to constantly close windows
    global topicselect #Setting topicselect variable globally, this allows me to make edits elsewhere
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
    btn_notes = Button(quiz, text = "Notes", font = ("Arial", 18), width = 10, height = 1, command = noteswindow)
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

    if mode == 2:
        lbl_question.config(text = Emergencies[quesfirst]["question"]) #Configuring the question into the question label
        btn_option1.config(text = Emergencies[quesfirst]["option1"]) #Configuring the first option
        btn_option2.config(text = Emergencies[quesfirst]["option2"]) #Configuring the second option
        btn_option3.config(text = Emergencies[quesfirst]["option3"]) #Configuring the third option
        btn_option4.config(text = Emergencies[quesfirst]["option4"]) #Configuring the fourth option

    elif mode == 3:
        lbl_question.config(text = Parking[quesfirst]["question"])
        btn_option1.config(text = Parking[quesfirst]["option1"])
        btn_option2.config(text = Parking[quesfirst]["option2"])
        btn_option3.config(text = Parking[quesfirst]["option3"])
        btn_option4.config(text = Parking[quesfirst]["option4"])

    elif mode == 4:
        lbl_question.config(text = Road[quesfirst]["question"])
        btn_option1.config(text = Road[quesfirst]["option1"])
        btn_option2.config(text = Road[quesfirst]["option2"])
        btn_option3.config(text = Road[quesfirst]["option3"])
        btn_option4.config(text = Road[quesfirst]["option4"])

    elif mode == 5:
        lbl_question.config(text = Rules[quesfirst]["question"])
        btn_option1.config(text = Rules[quesfirst]["option1"])
        btn_option2.config(text = Rules[quesfirst]["option2"])
        btn_option3.config(text = Rules[quesfirst]["option3"])
        btn_option4.config(text = Rules[quesfirst]["option4"])

    elif mode == 6:
        lbl_question.config(text = Driver[quesfirst]["question"])
        btn_option1.config(text = Driver[quesfirst]["option1"])
        btn_option2.config(text = Driver[quesfirst]["option2"])
        btn_option3.config(text = Driver[quesfirst]["option3"])
        btn_option4.config(text = Driver[quesfirst]["option4"])

def hintwindow(): #When the hint button is pressed, it runs this function
    hintpopup = Tk() #Creating the hint GUI window
    hintpopup.title("Hint!") #Naming the hint GUI window as "Hint!"
    hintpopup.geometry("250x100") #Setting the size of the window
    lbl_hint = Label(hintpopup) #Establishing a label
    lbl_hint.pack() #Packing the label in

    if mode == 2:
        lbl_hint.config(text = Emergencies[quesfirst]["hint"]) #Configuring the label with the hint associated with the current question

    elif mode == 3:
        lbl_hint.config(text = Parking[quesfirst]["hint"])

    elif mode == 4:
        lbl_hint.config(text = Road[quesfirst]["hint"])

    elif mode == 5:
        lbl_hint.config(text = Rules[quesfirst]["hint"])

    elif mode == 6:
        lbl_hint.config(text = Driver[quesfirst]["hint"])

def noteswindow():
    notespopup = Tk() #Creating the notes GUI window
    notespopup.title("Notes!") #Naming the notes GUI window as "Notes!"
    notespopup.geometry("450x350") #Setting the size of the window
    global ent_notes
    ent_notes = Text(notespopup, font = ("Arial", 12))
    ent_notes.place(x = 2, y = 2, width = 445, height = 295)
    btn_savenotes = Button(notespopup, text = "Save current notes", bg = "#67fcd0", command = notes)
    btn_savenotes.place(x = 160, y = 310)
    global lbl_notesavestatus
    lbl_notesavestatus = Label(notespopup)
    lbl_notesavestatus.place(x = 300, y = 313)

def notes():
    usernote = str(ent_notes.get("1.0", "end-1c"))
    print(usernote)
    lbl_notesavestatus.config(text = "Saved!")

verification = Tk() #Creating the first GUI window the user will see, this will check the user's verification and welcomes them if they meet the requirements
verification.title("Verifications window") #Setting the GUI's title, otherwise will just be "tk"
verification.geometry("350x350") #Setting the size of the GUI window

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
btn_dev = Button(verification, text = "dev", bg = "#67fcd0", command = selection) #A button only meant for the developer(me) to use, will be removed upon program completion
btn_dev.pack() #Simply packing it onto the GUI, may change location later

topicproceedvariable = 0 #Used this to fix some looping logic, starts at 0 and will update to 1

quesorder = [1] #A list of questions
random.shuffle(quesorder) #Using random to shuffle the list of questions, making questions randomly generated

quesfirst = quesorder[0]

Emergencies = { #A dictionary for the questions present in topic Emergencies
    1: {"question" : "Who can put a blue sign up?", "option1" : "An ambulance driver", "option2" : "A police officer", "option3" : "A council officer", "option4" : "A member of the public", "hint" : "Blue signs are compulsary\nplaced by people with control over traffic"}, #2
    2: {"question" : "When must you pull over and allow an ambulance or fire engine to pass?", "option1" : "If it is travelling faster than you want to", "option2" : "You don't need to let it past - you can speed up so you're not holding it up", "option3" : "If its siren and/or red flashing lights are on", "option4" : "At all times", "hint" : "Only when urgent, what shows urgency?"}, #3
    3: {"question" : "If you get into a collision, what would be the first step you would take?", "option1" : "Call the police", "option2" : "Call the ambulance", "option3" : "Call your insurance company", "option4" : "Check for injuries", "hint" : "What is most important?"}, #4
    4: {"question" : "If a moving car's front left tire burst, what would happen to the car?", "option1" : "The car will sway from side to side", "option2" : "The car would be pulled towards the left", "option3" : "The car would be pulled towards the right", "option4" : "The car would start spinning", "hint" : "Which side the tire is on directly affects the car"}, #2
    5: {"question" : "If you get flash by oncoming traffic, where would you look?", "option1" : "Top left", "option2" : "Top right", "option3" : "Bottom left", "option4" : "Bottom right", "hint" : "Away from sources of light"}, #3
    6: {"question" : "What will happen if your car hits a body of water from a height?", "option1" : "You will float on the water", "option2" : "You will fall through the water", "option3" : "You will hit water like it was a solid", "option4" : "You will bounce off the water", "hint" : "Think about jumping into a swimming pool"}, #3
    7: {"question" : "If your car is sinking, how and when should you get out?", "option1" : "Open and escape through a window\nbefore the water is higher than the window", "option2" : "Escape through the boot once the car fills up", "option3" : "Break the front glass as the car is sinking", "option4" : "Use the doors once the car comes to a standstill", "hint" : "Think in terms of water pressure"}, #1
    8: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    9: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    10: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
}

Parking = {
    1: {"question" : "How far should you part from someone's driveway?", "option1" : "1 meter", "option2" : "2 meters", "option3" : "5 meters", "option4" : "0.5 meters", "hint" : "A decent distance, but not excessive"}, #1
    2: {"question" : "Ethically, should you park very close behind someone else?", "option1" : "Yeah sure, no big deal", "option2" : "Only if they can drive out through the front", "option3" : "No, you should never", "option4" : "Only for smaller cars", "hint" : "Try to be thoughtful and think 'just in case'"}, #2
    3: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    4: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    5: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    6: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    7: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    8: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    9: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    10: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
}

Road = {
    1: {"question" : "Which road may cause the most damage to oncoming traffic?", "option1" : "Grassy/Offroad roads", "option2" : "Concrete roads", "option3" : "Asphalt roads", "option4" : "Unsealed/pebble rock roads", "hint" : "Which road may cause flying objects?"}, #4
    2: {"question" : "What is the general rule of priority for T intersections?", "option1" : "The turning cars always have priority", "option2" : "As long as indicators are used, everybody can go", "option3" : "It doesn't matter.\ntraffic lights control T intersections", "option4" : "The straight road has right of way", "hint" : "Think what might happen if..."}, #4
    3: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    4: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    5: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    6: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    7: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    8: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    9: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    10: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
}

Rules = {
    1: {"question" : "What does a white sign with a red circle around 60 mean?", "option1" : "All cars must drive faster than 60km/h", "option2" : "The speed limit is 60km/h", "option3" : "Your average speed should be around 60km/h", "option4" : "60km/h speed limit only for civilian vehicles", "hint" : "Too obvious, read road code again."}, #2
    2: {"question" : "Can restricted licensed drivers bring passengers?", "option1" : "No, absolutely not", "option2" : "Yes, they can bring anyone", "option3" : "Only with supervision, and special cases without", "option4" : "As long as your passengers have full licence", "hint" : "The freedom doesn't come until full license"}, #3
    3: {"question" : "Can you drink and drive while under 16 years of age?", "option1" : "As long as your friends say it's going to be fine", "option2" : "Drink water first to dilute alcohol", "option3" : "No, shouldn't be drinking anyway", "option4" : "Yes, only if alcohol is under acceptable limits", "hint" : "Think in terms of drinking age limit"}, #3
    4: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    5: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    6: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    7: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    8: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    9: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    10: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
}

Driver = {
    1: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    2: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    3: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    4: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    5: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    6: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    7: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    8: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    9: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    10: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
}

verification.mainloop()