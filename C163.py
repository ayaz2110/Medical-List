from tkinter import *
root = Tk()
root.title("Fever_Report")
root.geometry("600 x 600")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text="Dou You Have A Headache Or A Sore Throat?")
Question1.pack()
question1_r1=Radiobutton(root, text="Yes", variable-question1_radioButton, value="Yes")
