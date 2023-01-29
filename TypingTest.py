from tkinter import *
import random
from tkinter import messagebox

Mainscreen = Tk()
Mainscreen.geometry('1000x600')
Mainscreen.title('MakeUseOf Typing Game')
Mainscreen.config(bg="aqua")

file1 = open('words.txt', 'r')
words = file1.read().split()
score = missed = count1 = 0
time = 60

def giventime():
    global time, score, missed
    if time > 0:
        time -= 1
        timercount.configure(text=time)
        timercount.after(1000, giventime)
    else:
        startlabel.configure(text='Game Over!')
        gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score, missed, score - missed))
        rr = messagebox.askokcancel('Game Over!', 'Press Ok to Exit')
        if rr == True:
            exit()

def game(event):
    global score, missed
    if time == 10:
        giventime()
    startlabel.configure(text='Continue..')
    gameinstruction.configure(text='Hit Enter After Typing The Word ')
    if wordentry.get() == labelforward['text']:
        score += 1
        scorelabelcount.configure(text=score)
    else:
        missed += 1
    random.shuffle(words)
    labelforward.configure(text=words[0])
    wordentry.delete(0, END)

startlabel = Label(Mainscreen, text='Typing Game', font=('arial', 30, 'italic bold'), bg='black', fg='white')
startlabel.place(x=375, y=50)

random.shuffle(words)
labelforward = Label(Mainscreen, font=('arial', 45, 'italic bold'), fg='green')
labelforward.place(x=350, y=240)

scorelabel = Label(Mainscreen, text='Your Score:', font=('arial', 25, 'italic bold'), fg='maroon')
scorelabel.place(x=110, y=100)

scorelabelcount = Label(Mainscreen, text=score, font=('arial', 25, 'italic bold'), fg='purple')
scorelabelcount.place(x=250, y=180)

labelfortimer = Label(Mainscreen, text='Time Left:', font=('arial', 25, 'italic bold'), fg='maroon')
labelfortimer.place(x=700, y=100)

timercount = Label(Mainscreen, text=time, font=('arial', 25, 'italic bold'), fg='purple')
timercount.place(x=700, y=180)

gameinstruction = Label(Mainscreen, text='Press Enter To Begin The Game', font=('arial', 25, 'italic bold'),fg='grey')
gameinstruction.place(x=250, y=500)

wordentry = Entry(Mainscreen, font=('arial', 25, 'italic bold'), bd=10, justify='center')
wordentry.place(x=350, y=330)
wordentry.focus_set()

Mainscreen.bind('<Return>', game)
mainloop()
