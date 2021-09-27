from tkinter import*
root = Tk()
root.title("GUI")
myText=Label(text="My name is ", fg="light blue",font=20).grid(row=0,column=0)
myText=Label(text="Benyaporn", fg="light green",font=20).grid(row=1,column=1)
myText=Label(text="Udomsilapasub ", fg="light pink",font=20).grid(row=2,column=2)
root.geometry("400x400")
root.mainloop()