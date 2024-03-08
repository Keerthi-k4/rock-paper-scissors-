from tkinter import *
from PIL import Image, ImageTk

#assigning values to player 1
def rock1():
    canvas.create_image(0, 100, anchor=NW, image=rock_img)
    global player1
    player1 = 'rock'

def paper1():
    canvas.create_image(0, 100, anchor=NW, image=paper_img)
    global player1
    player1 = 'paper'

def scissor1():
    canvas.create_image(0, 100, anchor=NW, image=scissors_img)
    global player1
    player1 = 'scissor'


#checking for winner
def rock():
    winner = ''
    canvas.create_image(500, 100, anchor=NW, image=rock_img)
    if player1 == "paper":
        winner = "Player 1 won !"
    elif player1 == "scissor":
        winner = "Player 2 won !"
    elif player1 == "rock":
        winner  ="       Tie     !   "
    canvas.create_text(410, 420, text= winner,
                       fill="white", font=('Bambi Bold', 30), tag='result')
def paper():
    winner = ''
    canvas.create_image(500, 100, anchor=NW, image=paper_img)
    if player1 == "paper":
        winner = "       Tie     !   "
    elif player1 == "scissor":
        winner = "Player 1 won !"
    elif player1 == "rock":
        winner = "Player 2 won !"
    canvas.create_text(410, 420, text= winner,
                       fill="white", font=('Bambi Bold', 30), tag='result')
def scissors():
    canvas.create_image(500, 100, anchor=NW, image=scissors_img)
    winner = ''
    if player1 == "paper":
        winner = "Player 2 won !"
    elif player1 == "scissor":
        winner = "       Tie     !   "
    elif player1 == "rock":
        winner = "Player 1 won !"
    canvas.create_text(410, 420, text=winner,
                       fill="white", font=('Bambi Bold', 30), tag='result')

# Function for clear button
def clear():
    # Removes result from canvas
    canvas.delete("all")


# main window object
screen2 = Tk()
# Title of GUI window
screen2.title('Rock Paper Scissor')
# Size of window
screen2.geometry('800x680')

screen2.configure(bg='#01CBC2')
# Creating canvas
canvas = Canvas(screen2, width=800, height=680, bg='#01CBC2')
canvas.grid(row=0, column=0)

# Creating labels on GUI window
l1 = Label(screen2, text='Player 1', font=('Bambi Bold', 30), bg='#01CBC2', fg='white')
l2 = Label(screen2, text='Player 2', font=('Bambi Bold', 30), bg='#01CBC2', fg='white')
l3 = Label(screen2, text='Vs', font=('Bambi Bold', 40), bg='#01CBC2', fg='white')

# Placing all the labels on window
l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)

#opening the images
all_img = ImageTk.PhotoImage(Image.open('selection.jpg').resize((320, 210)))
rock_img= ImageTk.PhotoImage(Image.open('rock.png').resize((300, 300)))
paper_img= ImageTk.PhotoImage(Image.open('paper.png').resize((300, 300)))
scissors_img= ImageTk.PhotoImage(Image.open('scissor.png').resize((300, 300)))

Label(screen2,image=all_img).place(x=-10,y=467)
Label(screen2,image=all_img).place(x=495,y=467)

#player 1 buttons

r=Button(screen2,text='Rock',command=rock1,font=('Times', 10, 'bold'))
r.place(x=35, y=487)

p=Button(screen2,text='Paper',command=paper1,font=('Times', 10, 'bold'))
p.place(x=128, y=487)

s=Button(screen2,text='Scissor',command=scissor1,font=('Times', 10, 'bold'))
s.place(x=220, y=487)

#player 2 buttons
r2=Button(screen2,text='Rock',command=rock,font=('Times', 10, 'bold'))
r2.place(x=540, y=487)

p2=Button(screen2,text='Paper',command=paper,font=('Times', 10, 'bold'))
p2.place(x=635,y=487)

s2=Button(screen2,text='Scissor',command=scissors,font=('Times', 10, 'bold'))
s2.place(x=730, y=487)

# Button for clear
clear_b = Button(screen2, text='CLEAR', font=('Times', 10, 'bold'),
                 width=10, command=clear).place(x=370, y=28)

screen2.mainloop()