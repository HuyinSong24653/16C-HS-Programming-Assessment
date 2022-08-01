#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

from tkinter import*
#Importing the GUI functions
import random 
#Importing random
import os
#Importing os
import sys
#Importing sys


def verifyage():
    #A function that contains the logic for the user's name and age
    try:
        #Try and except to prevent errors
        username = str(ent_name.get()) 
        #Getting the user's name from the entry box
        userage = int(ent_age.get()) 
        #Getting the user's age from the entry box
        if userage <= 0: 
            #If user's age is less or equal to 0
            lbl_verifage.config(text = "Invalid input! You cannot be 0 or negative years old!") 
            #Configs label to print user has invalid age
        elif userage > 0 and userage < 16: 
            #If user's age is between 0 and 16
            lbl_verifage.config(text = "You are not old enough to qualify!") 
            #Configs label to print user is too young to use program
        elif userage >= 16 and userage < 122:
            #If user's age is equal or more than 16, and between 16 to 122
            lbl_verifage.config(text = "You are qualified to use my program!") 
            #configs label to welcome the user, stating their qualified status
            lbl_welcome = Label(verification, text = "{}, Welcome!".format(username))
            #Establishing a label that welcomes the user, using their username
            lbl_welcome.place(x = 20, y = 160) 
            #Places it onto the GUI
            btn_verifproceed.place(x = 100, y = 275) 
            #Places the established button, allowing the user to proceed
        elif userage >= 122:
            #If user's age is more or equal to 122
            lbl_verifage.config(text = "Not possible!\nThe highest recorded age of humans was 122 years old!")
            #Printing an invalid input message, user is impossibly old
    except ValueError: 
        #Try and except, this prevents a value error just in case the user inputs symbols or something not a integer
        lbl_verifage.config(text = "Invalid input! Please input an integer!") 
        #Configuring the label to help users recover from their typo


def selection():
    #A function for the topic selecting page
    if topicproceedvariable == 0:
        #If topicproceedvariable = 1 (user's first time calling this function)
        verification.destroy() 
        #Destroys the verifications page, saves the user's time and effort from needing to constantly close windows
    global topicselect 
    #Setting topicselect variable globally, this allows me to make edits elsewhere
    topicselect = Tk() 
    #Initiating the topic selection window
    topicselect.title("Quiz topic selecter") 
    #Giving it a title
    topicselect.geometry("375x475") 
    #Setting the size

    lbl_quizselectwelcome = Label(topicselect, text = "What topic would you like to be tested on?", font = ("Arial", 11)) 
    #Label asking the user to choose their topic
    lbl_quizselectwelcome.place(x = 45, y = 30) 
    #Placing it, and so on with the other .place'es for the buttons
    btn_general = Button(topicselect, text = "General", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(1)) 
    #Button for General, calls quiztopic function with argument as 1
    btn_general.place(x = 25, y = 85)
    btn_emergencies = Button(topicselect, text = "Emergencies", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(2)) 
    #Button for Emergencies, calls quiztopic function with argument as 2, and so on for the other buttons
    btn_emergencies.place(x = 200, y = 85)  
    btn_parking = Button(topicselect, text = "Parking", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(3))
    btn_parking.place(x = 25, y = 180)
    btn_road = Button(topicselect, text = "Road", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(4))
    btn_road.place(x = 200, y = 180)
    btn_rules = Button(topicselect, text = "Rules", width = 14, height = 3, font = ("Arial", 12), command = lambda: quiztopic(5))
    btn_rules.place(x = 25, y = 275)
    btn_topicproceed = Button(topicselect, text = "Proceed with quiz", width = 14, height = 3, font = ("Arial", 12), bg = "#67fcd0", command = quizpage) 
    #Establishing a proceeding button for the user once topic is selected, calls quizpage function

    if topicproceedvariable == 1:
        #If topicproceedvariable = 1 (user has already chosen their topic, and is calling this function a second time)
        btn_topicproceed.place(x = 115, y = 380) 
        #Places the already established proceeding button onto the GUI for the user to click


def quiztopic(arg): 
    #quiztopic function called from topic selection buttons, takes argument
    global topicproceedvariable 
    #Setting topicproceedvariable as global to avoid error
    topicproceedvariable = 1
    #setting topicproceedvariable as 1
    global topic
    global topicname
    if arg == 1:
        #If argument is 1 (user clicked General topic)
        topic = General 
        #Set topic as 1 (for General)
        topicname = "General"
    elif arg == 2:
        #If argument is 2 (user clicked Emergencies topic), and so on for other topics
        topic = Emergencies 
        #Set topic as Emergencies
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
    topicselect.destroy() 
    #The program destroys the old topic selection window
    selection() 
    #And calls the selection function, which will create a new topic selection window with the proceed button present, had to do this to avoid a looping logic error


def quizpage(): 
    #A function for the actual testing page, called from the topic proceed button on the topic selection page
    if progress == 1:
        topicselect.destroy()
        #Destroys the topic selection page, in order to avoid duplicated testing pages and changing topics during a test
    global quiz
    quiz = Tk() 
    #Creating the quiz/test window
    quiz.title("Quiz Window")
    #Naming it
    quiz.geometry("750x550") 
    #Setting the sizes

    global btn_progress
    btn_progress = Button(quiz, text = "Progress", font = ("Arial", 18), width = 10, height = 1, command = progresswindow) 
    #Button for the user, will show current quiz progress
    btn_progress.place(x = 25, y = 20) #Places it at the top of the GUI
    btn_notes = Button(quiz, text = "Notes", font = ("Arial", 18), width = 10, height = 1, command = noteswindow) 
    #Notes button, will call noteswindow function to create new window for the user's notes
    btn_notes.place(x = 205, y = 20) #Placing it and so on...
    btn_hint = Button(quiz, text = "Hint", font = ("Arial", 18), width = 10, height = 1, command = hintwindow) 
    #Hints window, calls the hintwindow function which will give a hint on the current question in a small hint window
    btn_hint.place(x = 385, y = 20)
    btn_endquiz = Button(quiz, text = "End quiz", font = ("Arial", 18), width = 10, height = 1, command = quizfinish)
    #A button for the user to end the quiz prior to quiz completion
    btn_endquiz.place(x = 565, y = 20)
    lbl_question = Label(quiz, width = 64, height = 3, font = ("Arial", 15), relief = "groove")
    #A label for where the question will go
    lbl_question.place(x = 18, y = 100)
    global btn_option1 #Setting global so I can edit later
    btn_option1 = Button(quiz, width = 45, height = 6, command = choice1) 
    #A button for the user's first option
    btn_option1.place(x = 20, y = 200)
    global btn_option2
    btn_option2 = Button(quiz, width = 45, height = 6, command = choice2)
    #A button for the user's second option, and so on...
    btn_option2.place(x = 400, y = 200)
    global btn_option3
    btn_option3 = Button(quiz, width = 45, height = 6, command = choice3)
    btn_option3.place(x = 20, y = 325)
    global btn_option4
    btn_option4 = Button(quiz, width = 45, height = 6, command = choice4)
    btn_option4.place(x = 400, y = 325)
    global lbl_correctorwrong
    lbl_correctorwrong = Label(quiz, width = 20, height = 4)
    lbl_correctorwrong.place(x = 100, y = 450)

    global btn_quizproceed
    btn_quizproceed = Button(quiz, text = "Do you wish to proceed?", width = 25, height = 4, bg = "#67fcd0", command = quizpage) 
    #A button for when the user answers a question, will bring them to next question

    lbl_quizend = Label(quiz, text = "The quiz is over\nplease end the quiz")

    global ques
    if progress == 1: 
        #If progress == 1 (first question)
        ques = quesorder[0] 
        #Set question to the first value in the shuffled list
    elif progress == 2: 
        #If progress == 2 (second question)
        ques = quesorder[1] 
        #Set question to the second value in the shuffled list
    elif progress == 3: 
        #And so on...
        ques = quesorder[2] 
        #And so on...
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
    elif progress > 10:
        lbl_quizend.place(x = 500, y = 465)

    lbl_question.config(text = topic[ques]["question"]) 
    #Configure the question label to display 'topic' dictionary's first question's question
    btn_option1.config(text = topic[ques]["option1"]) 
    #Configure the first option button to display 'topic' dictionary's first question's first option
    btn_option2.config(text = topic[ques]["option2"]) 
    #and so on...
    btn_option3.config(text = topic[ques]["option3"])
    btn_option4.config(text = topic[ques]["option4"])


def choice1(): 
    #Function for if the user clicked the first option
    global progress
    progress += 1 
    #Set progress to progress + 1
    choice = topic[ques]["option1"] 
    #choice variable is equal to the first options's values
    global correct
    global wrong
    if choice == topic[ques]["answer"]: 
        #if user's choice/answer is equal/correct to the question's answer
        btn_option1.config(bg = "#10EE10") 
        #Config the button pressed to green indicating correct choice
        correct += 1 
        #Set correct variable to correct + 1
        lbl_correctorwrong.config(text = "Correct!") 
        #A second source of whether choice is correct or wrong
    elif choice != topic[ques]["answer"]: 
        #If user's choice is not equal to question's answer
        btn_option1.config(bg = "#EB270C") 
        #Set the button pressed to a red colour indicating incorrect/wrong answer
        wrong += 1 
        #Set wrong variable to wrong + 1
        lbl_correctorwrong.config(text = "Wrong!")
    btn_quizproceed.place(x = 275, y = 450) 
    #Place the proceed to next question button


def choice2(): 
    #Function for second option, functions nearly identically to first option
    global progress
    progress += 1
    choice = topic[ques]["option2"]
    global correct
    global wrong
    if choice == topic[ques]["answer"]:
        btn_option2.config(bg = "#10EE10")
        correct += 1
        lbl_correctorwrong.config(text = "Correct!")
    elif choice != topic[ques]["answer"]:
        btn_option2.config(bg = "#EB270C")
        wrong += 1
        lbl_correctorwrong.config(text = "Wrong!")
    btn_quizproceed.place(x = 275, y = 450)


def choice3(): 
    #3rd option
    global progress
    progress += 1
    choice = topic[ques]["option3"]
    global correct
    global wrong
    if choice == topic[ques]["answer"]:
        btn_option3.config(bg = "#10EE10")
        correct += 1
        lbl_correctorwrong.config(text = "Correct!")
    elif choice != topic[ques]["answer"]:
        btn_option3.config(bg = "#EB270C")
        wrong += 1
        lbl_correctorwrong.config(text = "Wrong!")
    btn_quizproceed.place(x = 275, y = 450)


def choice4(): 
    #And 4th option
    global progress
    progress += 1
    choice = topic[ques]["option4"]
    global correct
    global wrong
    if choice == topic[ques]["answer"]:
        btn_option4.config(bg = "#10EE10")
        correct += 1
        lbl_correctorwrong.config(text = "Correct!")
    elif choice != topic[ques]["answer"]:
        btn_option4.config(bg = "#EB270C")
        wrong += 1
        lbl_correctorwrong.config(text = "Wrong!")
    btn_quizproceed.place(x = 275, y = 450)


def progresswindow():
    #Function for when progress button is clicked
    btn_progress.config(text = "{}/10".format(progress))
    #Configs the progress button to display currect progress out of 10 questions


def hintwindow():
    #When the hint button is pressed, it runs this function
    hintpopup = Tk()
    #Creating the hint GUI window
    hintpopup.title("Hint!")
    #Naming the hint GUI window as "Hint!"
    hintpopup.geometry("300x35")
    #Setting the size of the window
    lbl_hint = Label(hintpopup)
    #Establishing a label
    lbl_hint.pack()
    #Packing the label in
    lbl_hint.config(text = topic[ques]["hint"])
    #Configure the hint label inside the hint window to display the 'topic' dictionary's first question's hint
    global hintuses
    hintuses += 1
    #Everytime user accesses a hint, set hintuses to hintuses + 1, to count how many times hints were used


def noteswindow():
    notespopup = Tk()
    #Creating the notes GUI window
    notespopup.title("Notes!") 
    #Naming the notes GUI window as "Notes!"
    notespopup.geometry("450x350") 
    #Setting the size of the window
    global ent_notes 
    #Setting the entry containing the user's notes as global, will be used later to be viewed by the user
    ent_notes = Text(notespopup, font = ("Arial", 12)) 
    #Setting the entry as Text onto the notes window, with Arial as the font and 12 as the font size
    ent_notes.place(x = 2, y = 2, width = 445, height = 295) 
    #Placing it, and setting the appropriate width and height sufficient for the user's notes
    btn_savenotes = Button(notespopup, text = "Save current notes", bg = "#67fcd0", command = notes) 
    #Establishing a button for the user to save their currently written notes, calls 'notes' function upon click
    btn_savenotes.place(x = 160, y = 310) 
    #and placing it onto the notes window
    global lbl_notesavestatus 
    #Setting the notesavestatus as global as it will be used in the 'notes' function called
    lbl_notesavestatus = Label(notespopup) 
    #Establishing a blank label in notes window, will be used to show note's save status
    lbl_notesavestatus.place(x = 300, y = 313) 
    #Placing it in a easy to see spot


def notes():
    #notes function, called when the user clicked to save their notes
    global usernote
    usernote = str(ent_notes.get("1.0", "end-1c")) 
    #Takes the user's written notes starting from line 1, 0th character until the end and minusing 1 character off (the useless space), and saves it as 'usernote'
    lbl_notesavestatus.config(text = "Saved!")
    #Configures the save status label to display "Saved!" to let the user know their notes are saved
    with open(os.path.join(sys.path[0], 'user_notes.txt'), "w") as f:
        #Opens a file called "user_notes.txt" located in the same folder directory as the program, opens to write.
        f.write(usernote)
        #Writes into the file with the variable "usernote"
        f.close()
        #Closes the file


def quizfinish():
    #Function for when the user ends the quiz
    quizending = Tk() 
    #Establish the quizending qindow
    quizending.title("Well done! Quiz is over, here are your scores") 
    #Message/title for the window
    quizending.geometry("410x365")
    #Setting size

    lbl_endtopic = Label(quizending, text = "Topic tested on: {}".format(topicname), width = 25, height = 2, bg = "#67fcd0", relief = "groove")
    #Label displaying the topic the user just tested on
    lbl_endtopic.place(x = 10, y = 10)
    lbl_endprogress = Label(quizending, text = "Progress: {}/10".format(progress), width = 25, height = 2, bg = "#67fcd0", relief = "groove")
    #Displays the progress out of 10 questions
    lbl_endprogress.place(x = 220, y = 10)
    lbl_endcorrect = Label(quizending, text = "Num. Correct answers: {}/10".format(correct), width = 25, height = 2, bg = "#67fcd0", relief = "groove") 
    #Displays the number of correct answers out of 10 questions
    lbl_endcorrect.place(x = 10, y = 70)
    lbl_endwrong = Label(quizending, text = "Num. Wrong answers: {}/10".format(wrong), width = 25, height = 2, bg = "#67fcd0", relief = "groove") 
    #Shows number of wrong answers out of 10 questions
    lbl_endwrong.place(x = 220, y = 70)
    lbl_endhintsused = Label(quizending, text = "Num. Hints used: {}".format(hintuses), width = 25, height = 2, bg = "#67fcd0", relief = "groove") 
    #Shows the number of hints used throughout their quiz
    lbl_endhintsused.place(x = 10, y = 130)
    lbl_endnotes = Label(quizending, text = usernote, bg = "#67fcd0", font = ("Arial", 10), width = 48, height = 10, wraplength = 380, justify = "center", relief = "groove") 
    #Displays the notes written during their quiz, will display "none" if nothing were wrote
    lbl_endnotes.place(x = 10, y = 190)


verification = Tk() 
#Creating the first GUI window the user will see, this will check the user's verification and welcomes them if they meet the requirements
verification.title("Verifications window") 
#Setting the GUI's title, otherwise will just be "tk"
verification.geometry("350x350") 
#Setting the size of the GUI window

lbl_verifage = Label(verification) 
#Label used to give information regarding verification, is empty now but is configured once verification button is pressed
lbl_verifage.place(x = 20, y = 200)

lbl_name = Label(verification, text = "What is your name?") 
#Asking user's name
lbl_name.place(x = 20, y = 20)
lbl_age = Label(verification, text = "What is your age?")
#Asking user's age
lbl_age.place(x = 20, y = 60)
ent_name = Entry(verification) 
#A entry box for user to input their name
ent_name.place(x = 150, y = 20)
ent_age = Entry(verification) 
#Then their age
ent_age.place(x = 150, y = 60)
btn_age = Button(verification, text = "Verify your age!", bg = "#67fcd0", command = verifyage) 
#A button for the user's to verify after they have inputted name and age
btn_age.place(x = 100, y = 100)

btn_verifproceed = Button(verification, text = "Proceed with program", bg = "#67fcd0", command = selection) 
#A button note present yet, this appears after name and age verified, takes user to topic selection

topicproceedvariable = 0 
#Used this to fix some looping logic, starts at 0 and will update to 1

quesorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
#A list of questions
random.shuffle(quesorder) 
#Using random to shuffle the list of questions, making questions randomly generated

progress = 1 
#Establishing and setting different variables to 1, 0, or NONE
choice = NONE
topic = NONE
topicname = NONE
correct = 0
wrong = 0
hintuses = 0
usernote = NONE

General = { 
    #'General' topic dictionary
    1: {"question" : "What rule should you use to judge a safe following distance in wet or frosty conditions if driving a car?", "option1" : "Two-second rule", "option2" : "Four-second rule", "option3" : "100 meter rule", "option4" : "Six-second rule", "hint" : "The answer involves time", "answer" : "Four-second rule"}, #2
    2: {"question" : "Your vehicle has a current Warrant of Fitness but a rear red stop light is not working\nWhat should you do?", "option1" : "You can drive with it until your next WOF", "option2" : "You must fix it immediately", "option3" : "Only use the vehicle during daylight hours", "option4" : "You have 48 hours to drive until it needs fixing", "hint" : "Rear stop lights are crucial", "answer" : "You must fix it immediately"}, #2
    3: {"question" : "If you're under 20 and you're caught with any level of blood alcohol by the police, what is the minimum penalty?", "option1" : "$200 fine and 50 demerit points", "option2" : "Your licence will be suspended", "option3" : "$100 fine and 35 demerit points", "option4" : "Nothing on the first offence", "hint" : "Not either extremes", "answer" : "$200 fine and 50 demerit points"}, #1
    4: {"question" : "What does a blue sign with a person walking mean?", "option1" : "Dance classes ahead", "option2" : "No route for pedestrians", "option3" : "A route for motorists only", "option4" : "A route for pedestrians only", "hint" : "Definitely not 'Dance classes ahead'", "answer" : "A route for pedestrians only"}, #4
    5: {"question" : "When should you apply the four-second rule?", "option1" : "If your brakes are almost worn out", "option2" : "If the road is wet or frosty\nor you are towing a trailer", "option3" : "If you are travelling faster than 100km/h", "option4" : "Driving at night", "hint" : "When the road limits your abilities", "answer" : "If the road is wet or frosty\nor you are towing a trailer"}, #2
    6: {"question" : "What class of licence do you need to drive a car?", "option1" : "Class 1", "option2" : "Class 2", "option3" : "Class A", "option4" : "Class B", "hint" : "It's a number", "answer" : "Class 1"}, #1
    7: {"question" : "Which part of the car prevents too much sound and gas from entering the car?", "option1" : "Windows", "option2" : "Exhaust and silencer", "option3" : "Heater and AC", "option4" : "Mudguards and mud flaps", "hint" : "Definitely not mudgaurds and mud flaps", "answer" : "Exhaust and silencer"}, #2
    8: {"question" : "What should you do when you want to turn left?", "option1" : "Give 3 seconds warning by indicating", "option2" : "Give 2 seconds warning by indicating", "option3" : "No need to indicate if no one is behind you", "option4" : "Give 1 second of warning by indicating", "hint" : "Always indicate when turning", "answer" : "Give 3 seconds warning by indicating"}, #1
    9: {"question" : "What must be displayed on the back of a trailer being towed at night?", "option1" : "A white light", "option2" : "A yellow light", "option3" : "A green light", "option4" : "A red light", "hint" : "A highly visible light, but not excessive", "answer" : "A red light"}, #4
    10: {"question" : "What does reflective triangles placed by the side of the road mean?", "option1" : "Roadworks ahead", "option2" : "Breakdown or crash ahead", "option3" : "Special event ahead", "option4" : "One way bridge ahead\nand they have right of way", "hint" : "Think of signs that match situations", "answer" : "Breakdown or crash ahead"}, #2
}

Emergencies = { 
    #'Emergencies' topic dictionary
    1: {"question" : "Who can put a blue sign up?", "option1" : "An ambulance driver", "option2" : "A police officer", "option3" : "A council officer", "option4" : "A member of the public", "hint" : "Blue signs are compulsary\nplaced by people with control over traffic", "answer" : "A police officer"}, #2
    2: {"question" : "When must you pull over and allow an ambulance or fire engine to pass?", "option1" : "If it is travelling faster than you want to", "option2" : "You don't need to let it past\nyou can speed up so you're not holding it up", "option3" : "If its siren and/or red flashing lights are on", "option4" : "At all times", "hint" : "Only when urgent, what shows urgency?", "answer" : "If its siren and/or red flashing lights are on"}, #3
    3: {"question" : "If you get into a collision, what would be the first step you would take?", "option1" : "Call the police", "option2" : "Call the ambulance", "option3" : "Call your insurance company", "option4" : "Check for injuries", "hint" : "What is most important?", "answer" : "Check for injuries"}, #4
    4: {"question" : "If a moving car's front left tire burst, what would happen to the car?", "option1" : "The car will sway from side to side", "option2" : "The car would be pulled towards the left", "option3" : "The car would be pulled towards the right", "option4" : "The car would start spinning", "hint" : "Which side the tire is on directly affects the car", "answer" : "The car would be pulled towards the left"}, #2
    5: {"question" : "If you get flashed by oncoming traffic, where would you look?", "option1" : "Top left", "option2" : "Top right", "option3" : "Bottom left", "option4" : "Bottom right", "hint" : "Away from sources of light", "answer" : "Bottom left"}, #3
    6: {"question" : "What will happen if your car hits a body of water from a height?", "option1" : "You will float on the water", "option2" : "You will fall through the water", "option3" : "You will hit water like it was a solid", "option4" : "You will bounce off the water", "hint" : "Think about jumping into a swimming pool", "answer" : "You will hit water like it was a solid"}, #3
    7: {"question" : "If your car is sinking, how and when should you get out?", "option1" : "Open and escape through a window\nbefore the water is higher than the window", "option2" : "Escape through the boot once the car fills up", "option3" : "Break the front glass as the car is sinking", "option4" : "Use the doors once the car comes to a standstill", "hint" : "Think in terms of water pressure", "answer" : "Open and escape through a window\nbefore the water is higher than the window"}, #1
    8: {"question" : "When should you use your hazard lights?", "option1" : "Reversing from a driveway when view is unclear", "option2" : "Your vehicle is a temporary hazard", "option3" : "To scare tailgaters off", "option4" : "You have parked on a yellow line", "hint" : "The answer is in the name", "answer" : "Your vehicle is a temporary hazard"}, #2
    9: {"question" : "Driving past parked cars when a ball rolls out, what do you do?", "option1" : "Flash your headlights", "option2" : "Maintain speed and hit it", "option3" : "Accelerate past it", "option4" : "Slow and prepare to stop", "hint" : "What if a kid follows the ball?", "answer" : "Slow and prepare to stop"}, #4
    10: {"question" : "What do you do if there are flashing lights outside of a fire station?", "option1" : "Slow down and prepare to stop", "option2" : "Stop until lights stop flashing", "option3" : "Accelerate past it", "option4" : "Go tell them they left the lights on", "hint" : "The path out should always be available", "answer" : "Stop until lights stop flashing"}, #2
}

Parking = { 
    #'Parking' topic dictionary
    1: {"question" : "How far should you part from someone's driveway?", "option1" : "1 meter", "option2" : "2 meters", "option3" : "5 meters", "option4" : "0.5 meters", "hint" : "A decent distance, but not excessive", "answer" : "1 meter"}, #1
    2: {"question" : "Ethically, should you park very close behind someone else?", "option1" : "Yeah sure, no big deal", "option2" : "Only if they can drive out through the front", "option3" : "No, you should never", "option4" : "Only for smaller cars", "hint" : "Try to be thoughtful and think 'just in case'", "answer" : "Only if they can drive out through the front"}, #2
    3: {"question" : "Can you stop on a bus parking lane", "option1" : "Yes, if you are driving a bus", "option2" : "No, never", "option3" : "Only if there are no more parking spots", "option4" : "Only if your friends dare you to", "hint" : "Disregard what your friends say", "answer" : "Yes, if you are driving a bus"}, #1
    4: {"question" : "When may you park your vehicle over a fire hydrant?", "option1" : "Anytime you want", "option2" : "Never should", "option3" : "Only if the vehicle can be moved", "option4" : "Only if you don't think fires will be happening", "hint" : "As long as it doesn't block it", "answer" : "Only if the vehicle can be moved"}, #3
    5: {"question" : "What does a disability sign painted on the parking spot mean?", "option1" : "Park/stop here if you have mobility parking permit", "option2" : "Just another empty parking spot", "option3" : "If you have a broken leg", "option4" : "Just stopping for 5 minutes won't hurt", "hint" : "Evidence will tell", "answer" : "Park/stop here if you have mobility parking permit"}, #1
    6: {"question" : "How close can you park from an intersection?", "option1" : "1 meter away", "option2" : "3 meters away", "option3" : "6 meters away", "option4" : "10 meters away", "hint" : "Far away", "answer" : "6 meters away"}, #3
    7: {"question" : "Can you park on the right side of the road?", "option1" : "Only if there are marked bays", "option2" : "Never", "option3" : "Always", "option4" : "Only on a one way road", "hint" : "Yes, under specific circumstances", "answer" : "Only on a one way road"}, #4
    8: {"question" : "What does a red x on a blue sign with 'ends' mean?", "option1" : "You can stop after you pass this sign", "option2" : "You can stop before the sign\nbut not after", "option3" : "The sign doesn't matter", "option4" : "You cannot stop until permission is given", "hint" : "What does x usually mean?", "answer" : "You can stop after you pass this sign"}, #1
    9: {"question" : "Is it alright to park on someone else's driveway?", "option1" : "Only if permission is given", "option2" : "No never", "option3" : "Only if the owners aren't home", "option4" : "Yeah sure, its all public property", "hint" : "Don't be rude", "answer" : "Only if permission is given"}, #1
    10: {"question" : "What happens if you park blocking someone's driveway?", "option1" : "The council is called and your car is moved", "option2" : "Your car is legally theirs now", "option3" : "The owners cannot do anything about it", "option4" : "Car won't be moved, you will be fined", "hint" : "No extreme measures will be taken", "answer" : "The council is called and your car is moved"}, #1
}

Road = { 
    #'Road' topic dictionary
    1: {"question" : "Which road may cause the most damage to oncoming traffic?", "option1" : "Grassy/Offroad roads", "option2" : "Concrete roads", "option3" : "Asphalt roads", "option4" : "Unsealed/pebble rock roads", "hint" : "Which road may cause flying objects?", "answer" : "Unsealed/pebble rock roads"}, #4
    2: {"question" : "What is the general rule of priority for T intersections?", "option1" : "The turning cars always have priority", "option2" : "As long as indicators are used, everybody can go", "option3" : "It doesn't matter.\ntraffic lights control T intersections", "option4" : "The straight road has right of way", "hint" : "Think what might happen if...", "answer" : "The straight road has right of way"}, #4
    3: {"question" : "Who do you give way to in a roundabout?", "option1" : "Nobody", "option2" : "The left", "option3" : "The right", "option4" : "There will be traffic lights", "hint" : "Oncoming traffic", "answer" : "The right"}, #3
    4: {"question" : "What do you do as you leave a roundabout?", "option1" : "Indicate left", "option2" : "Indicate right", "option3" : "No need to indicate", "option4" : "Flash your lights", "hint" : "Show you are taking the exit", "answer" : "Indicate left"}, #1
    5: {"question" : "What must you do at an intersection controlled by a stop sign?", "option1" : "Slow to a stop", "option2" : "Just needs to slow down", "option3" : "Park there", "option4" : "Only stop if there are other people", "hint" : "The answer is in the name", "answer" : "Slow to a stop"}, #1
    6: {"question" : "What's the most important rule for approaching an intersection?", "option1" : "Indicate for atleast a second", "option2" : "Be prepared to stop", "option3" : "Use your horn to warn others", "option4" : "Flash your lights to worn others", "hint" : "Safety first", "answer" : "Be prepared to stop"}, #2
    7: {"question" : "What do you do if there is a marked left arrow on your lane's ground?", "option1" : "Turn left", "option2" : "Go straight", "option3" : "Turn right", "option4" : "No need to indicate", "hint" : "The answer is in the arrow", "answer" : "Turn left"}, #1
    8: {"question" : "What do you do if there is a marked right arrow on your lane's ground?", "option1" : "Turn left", "option2" : "Go straight", "option3" : "Turn right", "option4" : "No need to indicate", "hint" : "The answer is in the arrow", "answer" : "Turn right"}, #3
    9: {"question" : "What do you do if there is a marked straight arrow on your lane's ground?", "option1" : "Turn left", "option2" : "Go straight", "option3" : "Turn right", "option4" : "No need to indicate", "hint" : "The answer is in the arrow", "answer" : "Go straight"}, #2
    10: {"question" : "How far can a private vehicle (car, motorbike or truck) drive in a bus only lane?", "option1" : "25m", "option2" : "50m", "option3" : "75m", "option4" : "100m", "hint" : "A decent distance, but not too far", "answer" : "50m"}, #2
}

Rules = { 
    #'Rules' topic dictionary
    1: {"question" : "What does a white sign with a red circle around 60 mean?", "option1" : "All cars must drive faster than 60km/h", "option2" : "The speed limit is 60km/h", "option3" : "Your average speed should be around 60km/h", "option4" : "60km/h speed limit only for civilian vehicles", "hint" : "Too obvious, read road code again", "answer" : "The speed limit is 60km/h"}, #2
    2: {"question" : "Can restricted licensed drivers bring passengers?", "option1" : "No, absolutely not", "option2" : "Yes, they can bring anyone", "option3" : "Only with supervision, and special cases without", "option4" : "As long as your passengers have full licence", "hint" : "The freedom doesn't come until full license", "answer" : "Only with supervision, and special cases without"}, #3
    3: {"question" : "Can you drink and drive while under 16 years of age?", "option1" : "As long as your friends say it's going to be fine", "option2" : "Drink water first to dilute alcohol", "option3" : "No, shouldn't be drinking anyway", "option4" : "Yes, only if alcohol is under acceptable limits", "hint" : "Think in terms of drinking age limit", "answer" : "No, shouldn't be drinking anyway"}, #3
    4: {"question" : "What is the minimum tread depth required for car tyres?", "option1" : "1mm", "option2" : "2mm", "option3" : "3mm", "option4" : "1.5mm", "hint" : "Between 1mm and 3mm, not inclusive", "answer" : "1.5mm"}, #4
    5: {"question" : "Driving a car and trailer with full licence, what is weight limit?", "option1" : "4000kg", "option2" : "5000kg", "option3" : "6000kg", "option4" : "7000kg", "hint" : "Quite a lot, but not too much", "answer" : "6000kg"}, #3
    6: {"question" : "You are carring a load that is not properly secured, what are you allowed to do?", "option1" : "You can drive until your destination", "option2" : "Cannot drive until it is secured", "option3" : "You can drive for 200 meters", "option4" : "You can drive for 2 kilometers", "hint" : "The obvious", "answer" : "Cannot drive until it is secured"}, #2
    7: {"question" : "If you are driving with a space saver wheel, what must you do?", "option1" : "The space saver wheel is no different, do whatever", "option2" : "Drive under 80km/h\nto a place you can fix the wheel", "option3" : "Only drive under 100km/h", "option4" : "Only drive under 60km/h", "hint" : "The space saver wheel is not incredible", "answer" : "Drive under 80km/h\nto a place you can fix the wheel"}, #2
    8: {"question" : "What is the maximum distance a load may overhang your vehicle behind the rear axle?", "option1" : "1m", "option2" : "2m", "option3" : "3m", "option4" : "4m", "hint" : "Quite a large distance", "answer" : "4m"}, #4
    9: {"question" : "What should you do before any modification is carried out on your vehicle?", "option1" : "Its all OK as long as\nits from a reputable seller", "option2" : "Check with an authorised vehicle inspector", "option3" : "Get a certificate with the police", "option4" : "All modifications are not okay", "hint" : "Someone needs to check", "answer" : "Check with an authorised vehicle inspector"}, #2
    10: {"question" : "Which person can legally stop and perform a roadside check of your vehicle?", "option1" : "Ambulance driver", "option2" : "Police officer", "option3" : "Tow truck driver", "option4" : "Nobody", "hint" : "These guys have lots of authority", "answer" : "Police officer"}, #2
}

verification.mainloop()