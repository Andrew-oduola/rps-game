# Code With Drex
# Rock Paper Scissors Game

# Import Modules
from tkinter import *
import random
from PIL import Image, ImageTk

choices = ['rock', 'paper', 'scissors']
winner = ''
com_score = player_score = 0

window = Tk()
window.geometry('500x700')


main_img = Image.open('img\grps.jpg')
main_img = ImageTk.PhotoImage(main_img)

rock_img = Image.open('img\grock.webp')
resized_img = rock_img.resize((100, 100))
rock_img = ImageTk.PhotoImage(resized_img)

paper_img = Image.open('img\paper.png')
resized_img = paper_img.resize((100, 100))
paper_img = ImageTk.PhotoImage(resized_img)

scissors_img = Image.open('img\scissors.png')
resized_img = scissors_img.resize((100, 100))
scissors_img = ImageTk.PhotoImage(resized_img)


def play(button):
    global choices, winner, com_score, player_score
    winner = ''
    computer_choice = random.choice(choices)

    if computer_choice == 'rock':
        com_choice_label.configure(image=rock_img)
    elif computer_choice == 'paper':
        com_choice_label.configure(image=paper_img)
    elif computer_choice == 'scissors':
        com_choice_label.configure(image=scissors_img)


    if computer_choice == button:
        winner = 'DRAW'
    elif computer_choice == 'rock' and button == 'paper':
        winner = 'Player'
        player_score += 1
    elif computer_choice == 'rock' and button == 'scissors':
        winner = 'Computer'
        com_score += 1
    elif computer_choice == 'paper' and button == 'rock':
        winner = 'Computer'
        com_score += 1
    elif computer_choice == 'paper' and button == 'scissors':
        winner = 'Player'
        player_score += 1
    elif computer_choice == 'scissors' and button == 'paper':
        winner = 'Computer'
        com_score += 1
    elif computer_choice == 'scissors' and button == 'rock':
        winner = 'Player'
        player_score += 1

    winner_label.configure(text=f'Winner: {winner}')
    com_label.configure(text=f'Computer: {com_score}')
    player_label.configure(text=f'Player: {player_score}')





frame = Frame(window, bg='light green', height=700, width=500)
frame.place(x=0, y=0)

main_label = Label(frame, image=main_img)
main_label.place(x=120, y=10)

com_label = Label(frame, bg='light blue', text='Computer: 0', height=2, width=15, font='Arial 10 bold')
com_label.place(x=200, y=250)

com_choice_label = Label(frame)
com_choice_label.place(x=210, y=300)

winner_label = Label(frame, bg='orange', fg='white', font='Arial 10 bold')
winner_label.place(x=200, y=420)

player_label = Label(frame, bg='light blue', text='Player: 0', height=2, width=15, font='Arial 10 bold')
player_label.place(x=200, y=450)

rock_btn = Button(frame, image=rock_img, command=lambda: play('rock'))
rock_btn.place(x=25, y=550)

paper_btn = Button(frame, image=paper_img, command=lambda: play('paper'))
paper_btn.place(x = 200, y=550)

scissors_btn = Button(frame, image=scissors_img, command=lambda: play('scissors'))
scissors_btn.place(x = 375, y=550)


window.mainloop()