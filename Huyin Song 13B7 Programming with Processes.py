#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

from tkinter import* #Importing the GUI
import random
from unicodedata import name #Importing random to use

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
    if topicproceedvariable == 0: #If topicproceedvariable = 1 (user's first time calling this function)
        verification.destroy() #Destroys the verifications page, saves the user's time and effort from needing to constantly close windows
    global topicselect #Setting topicselect variable globally, this allows me to make edits elsewhere
    topicselect = Tk() #Initiating the topic selection window
    topicselect.title("Quiz topic selecter") #Giving it a title
    topicselect.geometry("375x475") #Setting the size

    lbl_quizselectwelcome = Label(topicselect, text = "What topic would you like to be tested on?", font = ("Arial", 11)) #Label asking the user to choose their topic
    lbl_quizselectwelcome.place(x = 45, y = 30) #Placing it, and so on with the other .place'es for the buttons
    btn_general = Button(topicselect, text = "General", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(1)) #Button for General, calls quiztopic function with argument as 1
    btn_general.place(x = 25, y = 85)
    btn_emergencies = Button(topicselect, text = "Emergencies", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(2)) #Button for Emergencies, calls quiztopic function with argument as 2, and so on for the other buttons
    btn_emergencies.place(x = 200, y = 85)  
    btn_parking = Button(topicselect, text = "Parking", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(3))
    btn_parking.place(x = 25, y = 180)
    btn_road = Button(topicselect, text = "Road", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(4))
    btn_road.place(x = 200, y = 180)
    btn_rules = Button(topicselect, text = "Rules", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(5))
    btn_rules.place(x = 25, y = 275)
    btn_driver = Button(topicselect, text = "Driver", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(6))
    btn_driver.place(x = 200, y = 275)
    btn_topicproceed = Button(topicselect, text = "Proceed with quiz", width = 14, height = 3, font = ("Arial", 12), bg = "#67fcd0", command = quizpage) #Establishing a proceeding button for the user once topic is selected, calls quizpage function

    if topicproceedvariable == 1: #If topicproceedvariable = 1 (user has already chosen their topic, and is calling this function a second time)
        btn_topicproceed.place(x = 115, y = 380) #Places the already established proceeding button onto the GUI for the user to click

def quiztopic(arg): #quiztopic function called from topic selection buttons, takes argument
    global topicproceedvariable #Setting topicproceedvariable as global to avoid error
    topicproceedvariable = 1 #setting topicproceedvariable as 1
    global topic
    global topicname
    if arg == 1: #If argument is 1 (user clicked General topic)
        topic = 1 #Set topic as 1 (for General)
        topicname = "General"
    elif arg == 2: #If argument is 2 (user clicked Emergencies topic), and so on for other topics
        topic = Emergencies #Set topic as Emergencies
        topicname = "Emergencies"
    elif arg == 3:
        topic = Parking
        topicname = "Parking"
    elif arg == 4:
        topic = Road
        topicname = "Road"
    elif arg == 5:
        topic = Rules
        topicname = "Rules"
    elif arg == 6:
        topic = Driver
        topicname = "Driver"
    topicselect.destroy() #The program destroys the old topic selection window
    selection() #And calls the selection function, which will create a new topic selection window with the proceed button present, had to do this to avoid a looping logic error

def quizpage(): #A function for the actual testing page, called from the topic proceed button on the topic selection page
    if progress == 1:
        topicselect.destroy() #Destroys the topic selection page, in order to avoid duplicated testing pages and changing topics during a test
    global quiz
    quiz = Tk() #Creating the quiz/test window
    quiz.title("Quiz Window") #Naming it
    quiz.geometry("750x750") #Setting the sizes

    global btn_progress
    btn_progress = Button(quiz, text = "Progress", font = ("Arial", 18), width = 10, height = 1, command = progresswindow) #Button for the user, will show current quiz progress
    btn_progress.place(x = 25, y = 20) #Places it at the top of the GUI
    btn_notes = Button(quiz, text = "Notes", font = ("Arial", 18), width = 10, height = 1, command = noteswindow) #Notes button, will call noteswindow function to create new window for the user's notes
    btn_notes.place(x = 205, y = 20) #Placing it and so on...
    btn_hint = Button(quiz, text = "Hint", font = ("Arial", 18), width = 10, height = 1, command = hintwindow) #Hints window, calls the hintwindow function which will give a hint on the current question in a small hint window
    btn_hint.place(x = 385, y = 20)
    btn_endquiz = Button(quiz, text = "End quiz", font = ("Arial", 18), width = 10, height = 1, command = quizfinish) #A button for the user to end the quiz prior to quiz completion
    btn_endquiz.place(x = 565, y = 20)
    lbl_question = Label(quiz, width = 64, height = 3, font = ("Arial", 15), relief = "groove") #A label for where the question will go
    lbl_question.place(x = 18, y = 100)
    global btn_option1 #Setting global so I can edit later
    btn_option1 = Button(quiz, width = 45, height = 6, command = choice1) #A button for the user's first option
    btn_option1.place(x = 20, y = 500)
    global btn_option2
    btn_option2 = Button(quiz, width = 45, height = 6, command = choice2) #A buutton for the user's second option, and so on...
    btn_option2.place(x = 400, y = 500)
    global btn_option3
    btn_option3 = Button(quiz, width = 45, height = 6, command = choice3)
    btn_option3.place(x = 20, y = 625)
    global btn_option4
    btn_option4 = Button(quiz, width = 45, height = 6, command = choice4)
    btn_option4.place(x = 400, y = 625)

    global btn_quizproceed
    btn_quizproceed = Button(quiz, text = "Do you wish to proceed?", width = 15, height = 3, bg = "#67fcd0", command = quizpage)

    global ques
    if progress == 1:
        ques = quesorder[0]
    elif progress == 2:
        ques = quesorder[1]
    elif progress == 3:
        ques = quesorder[2]
    elif progress == 4:
        ques = quesorder[3]
    elif progress == 5:
        ques = quesorder[4]
    elif progress == 6:
        ques = quesorder[5]
    elif progress == 7:
        ques = quesorder[6]
    elif progress == 8:
        ques = quesorder[7]
    elif progress == 9:
        ques = quesorder[8]
    elif progress == 10:
        ques = quesorder[9]

    lbl_question.config(text = topic[ques]["question"]) #Configure the question label to display 'topic' dictionary's first question's question
    btn_option1.config(text = topic[ques]["option1"]) #Configure the first option button to display 'topic' dictionary's first question's first option
    btn_option2.config(text = topic[ques]["option2"]) #and so on...
    btn_option3.config(text = topic[ques]["option3"])
    btn_option4.config(text = topic[ques]["option4"])

def choice1():
    global progress
    progress += 1
    choice = topic[ques]["option1"]
    global correct
    global wrong
    if choice == topic[ques]["answer"]:
        btn_option1.config(bg = "#10EE10")
        correct += 1
    elif choice != topic[ques]["answer"]:
        btn_option1.config(bg = "#EB270C")
        wrong += 1
    btn_quizproceed.pack()

def choice2():
    global progress
    progress += 1
    choice = topic[ques]["option2"]
    global correct
    global wrong
    if choice == topic[ques]["answer"]:
        btn_option2.config(bg = "#10EE10")
        correct += 1
    elif choice != topic[ques]["answer"]:
        btn_option2.config(bg = "#EB270C")
        wrong += 1
    btn_quizproceed.pack()

def choice3():
    global progress
    progress += 1
    choice = topic[ques]["option3"]
    global correct
    global wrong
    if choice == topic[ques]["answer"]:
        btn_option3.config(bg = "#10EE10")
        correct += 1
    elif choice != topic[ques]["answer"]:
        btn_option3.config(bg = "#EB270C")
        wrong += 1
    btn_quizproceed.pack()

def choice4():
    global progress
    progress += 1
    choice = topic[ques]["option4"]
    global correct
    global wrong
    if choice == topic[ques]["answer"]:
        btn_option4.config(bg = "#10EE10")
        correct += 1
    elif choice != topic[ques]["answer"]:
        btn_option4.config(bg = "#EB270C")
        wrong += 1
    btn_quizproceed.pack()

def progresswindow():
    btn_progress.config(text = "{}/10".format(progress))

def hintwindow(): #When the hint button is pressed, it runs this function
    hintpopup = Tk() #Creating the hint GUI window
    hintpopup.title("Hint!") #Naming the hint GUI window as "Hint!"
    hintpopup.geometry("300x35") #Setting the size of the window
    lbl_hint = Label(hintpopup) #Establishing a label
    lbl_hint.pack() #Packing the label in
    lbl_hint.config(text = topic[ques]["hint"]) #Configure the hint label inside the hint window to display the 'topic' dictionary's first question's hint
    global hintuses
    hintuses += 1

def noteswindow():
    notespopup = Tk() #Creating the notes GUI window
    notespopup.title("Notes!") #Naming the notes GUI window as "Notes!"
    notespopup.geometry("450x350") #Setting the size of the window
    global ent_notes #Setting the entry containing the user's notes as global, will be used later to be viewed by the user
    ent_notes = Text(notespopup, font = ("Arial", 12)) #Setting the entry as Text onto the notes window, with Arial as the font and 12 as the font size
    ent_notes.place(x = 2, y = 2, width = 445, height = 295) #Placing it, and setting the appropriate width and height sufficient for the user's notes
    btn_savenotes = Button(notespopup, text = "Save current notes", bg = "#67fcd0", command = notes) #Establishing a button for the user to save their currently written notes, calls 'notes' function upon click
    btn_savenotes.place(x = 160, y = 310) #and placing it onto the notes window
    global lbl_notesavestatus #Setting the notesavestatus as global as it will be used in the 'notes' function called
    lbl_notesavestatus = Label(notespopup) #Establishing a blank label in notes window, will be used to show note's save status
    lbl_notesavestatus.place(x = 300, y = 313) #Placing it in a easy to see spot

def notes(): #notes function, called when the user clicked to save their notes
    global usernote
    usernote = str(ent_notes.get("1.0", "end-1c")) #Takes the user's written notes starting from line 1, 0th character until the end and minusing 1 character off (the useless space), and saves it as 'usernote'
    lbl_notesavestatus.config(text = "Saved!") #Configures the save status label to display "Saved!" to let the user know their notes are saved

def quizfinish():
    quizending = Tk()
    quizending.title("Well done! Quiz is over, here are your scores")
    quizending.geometry("410x365")

    lbl_endtopic = Label(quizending, text = "Topic tested on: {}".format(topicname), width = 25, height = 2, bg = "#67fcd0", relief = "groove")
    lbl_endtopic.place(x = 10, y = 10)
    lbl_endprogress = Label(quizending, text = "Progress: {}/10".format(progress), width = 25, height = 2, bg = "#67fcd0", relief = "groove")
    lbl_endprogress.place(x = 220, y = 10)
    lbl_endcorrect = Label(quizending, text = "Num. Correct answers: {}/10".format(correct), width = 25, height = 2, bg = "#67fcd0", relief = "groove")
    lbl_endcorrect.place(x = 10, y = 70)
    lbl_endwrong = Label(quizending, text = "Num. Wrong answers: {}/10".format(wrong), width = 25, height = 2, bg = "#67fcd0", relief = "groove")
    lbl_endwrong.place(x = 220, y = 70)
    lbl_endhintsused = Label(quizending, text = "Num. Hints used: {}".format(hintuses), width = 25, height = 2, bg = "#67fcd0", relief = "groove")
    lbl_endhintsused.place(x = 10, y = 130)
    lbl_endnotes = Label(quizending, text = usernote, bg = "#67fcd0", font = ("Arial", 10), width = 48, height = 10, wraplength = 380, justify = "center", relief = "groove")
    lbl_endnotes.place(x = 10, y = 190)

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

#DEVELOPER COPY AND PASTE
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10

quesorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #A list of questions
random.shuffle(quesorder) #Using random to shuffle the list of questions, making questions randomly generated

progress = 1
choice = NONE
topic = NONE
topicname = NONE
correct = 0
wrong = 0
hintuses = 0
usernote = NONE

Emergencies = { #A dictionary for the questions present in topic Emergencies
    1: {"question" : "Who can put a blue sign up?", "option1" : "An ambulance driver", "option2" : "A police officer", "option3" : "A council officer", "option4" : "A member of the public", "hint" : "Blue signs are compulsary\nplaced by people with control over traffic", "answer" : "A police officer"}, #2
    2: {"question" : "When must you pull over and allow an ambulance or fire engine to pass?", "option1" : "If it is travelling faster than you want to", "option2" : "You don't need to let it past\nyou can speed up so you're not holding it up", "option3" : "If its siren and/or red flashing lights are on", "option4" : "At all times", "hint" : "Only when urgent, what shows urgency?", "answer" : "If its siren and/or red flashing lights are on"}, #3
    3: {"question" : "If you get into a collision, what would be the first step you would take?", "option1" : "Call the police", "option2" : "Call the ambulance", "option3" : "Call your insurance company", "option4" : "Check for injuries", "hint" : "What is most important?", "answer" : "Check for injuries"}, #4
    4: {"question" : "If a moving car's front left tire burst, what would happen to the car?", "option1" : "The car will sway from side to side", "option2" : "The car would be pulled towards the left", "option3" : "The car would be pulled towards the right", "option4" : "The car would start spinning", "hint" : "Which side the tire is on directly affects the car", "answer" : "The car would be pulled towards the left"}, #2
    5: {"question" : "If you get flashed by oncoming traffic, where would you look?", "option1" : "Top left", "option2" : "Top right", "option3" : "Bottom left", "option4" : "Bottom right", "hint" : "Away from sources of light"}, #3
    6: {"question" : "What will happen if your car hits a body of water from a height?", "option1" : "You will float on the water", "option2" : "You will fall through the water", "option3" : "You will hit water like it was a solid", "option4" : "You will bounce off the water", "hint" : "Think about jumping into a swimming pool", "answer" : ""}, #3
    7: {"question" : "If your car is sinking, how and when should you get out?", "option1" : "Open and escape through a window\nbefore the water is higher than the window", "option2" : "Escape through the boot once the car fills up", "option3" : "Break the front glass as the car is sinking", "option4" : "Use the doors once the car comes to a standstill", "hint" : "Think in terms of water pressure", "answer" : ""}, #1
    8: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : "", "answer" : ""}, #
    9: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
    10: {"question" : "", "option1" : "", "option2" : "", "option3" : "", "option4" : "", "hint" : ""}, #
}

Parking = {
    1: {"question" : "How far should you part from someone's driveway?", "option1" : "1 meter", "option2" : "2 meters", "option3" : "5 meters", "option4" : "0.5 meters", "hint" : "A decent distance, but not excessive", "answer" : "1 meter"}, #1
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
    1: {"question" : "Which road may cause the most damage to oncoming traffic?", "option1" : "Grassy/Offroad roads", "option2" : "Concrete roads", "option3" : "Asphalt roads", "option4" : "Unsealed/pebble rock roads", "hint" : "Which road may cause flying objects?", "answer" : "Unsealed/pebble rock roads"}, #4
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
    1: {"question" : "What does a white sign with a red circle around 60 mean?", "option1" : "All cars must drive faster than 60km/h", "option2" : "The speed limit is 60km/h", "option3" : "Your average speed should be around 60km/h", "option4" : "60km/h speed limit only for civilian vehicles", "hint" : "Too obvious, read road code again", "answer" : "The speed limit is 60km/h"}, #2
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