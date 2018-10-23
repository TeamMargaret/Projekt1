from tkinter import Tk, Frame, Label, Button
from time import sleep
import tkinter as tk

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Brawo!")
            right += 1
        else:
            label = Label(view, text="Buuuu...")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window, text="Quiz zakończony! " + str(right) + " poprawnych odpowiedzi na " + str(number_of_questions) + " pytań.").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = tk.Tk()
window.title("hello")
#title = tk.Label(text="lala")
tekst = tk.Label(window)
okno = Tk()
okno.geometry("400x400")
etykieta = Label(okno, text='Witaj! Jeżeli chcesz\
sprawdzić stan swej wiedzy matematycznej, to ten quiz jest właśnie dla Ciebie!\
                 Odpowiedz na 10 pytań wybierając jedną z sugerowanych\
                 odpowiedzi. Na końcu wyświetlone zostanie podsumowanie.\
                 Stosunek liczby pop')

etykieta.pack()
# wstaw początkowy tekst
#tekst.insert(0, "Tutaj wpisz cokolwiek...")
window.geometry("400x400")
button = tk.Button(window,text="Start",command=askQuestion)
button.pack()
window.mainloop()
