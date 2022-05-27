#Huyin Song, Started on 6/05/2022
#Improved interactivity quiz as described in Critical Inquiry Assessment

from tkinter import*
root = Tk()
root.geometry("500x500")


lname = Label(root, text = "What is your name?")
lname.pack()
lname.place(x = 20, y = 20)

lage = Label(root, text = "What is your age?")
lage.pack()
lage.place(x = 20, y = 60)

ename = Entry(root)
ename.pack()
ename.place(x = 150, y = 20)


eage = Entry(root)
eage.pack()
eage.place(x = 150, y = 60)





root.mainloop()