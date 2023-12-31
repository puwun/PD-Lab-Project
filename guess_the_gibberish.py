import random
from tkinter import *
from PIL import Image, ImageTk
import playsound
import threading


question = {1: 'Pretty Shack Scent',2: 'Wheel Yum Hairy Me' ,3: 'Wand Her Womb Hen',4: 'Knee Code Low Eon', 5: 'Sea Yule Hater', 6: 'Why Tail Huff Hunt', 7: 'Mike Ranch Healed Wren', 8: 'Ail Huck Each Arm',9:'Hay a Lick Sour', 10: 'Isle of View',11: 'Spar Cling What Her',12: 'Arrest Mike Ace',13: 'Law San Jail Lus', 14: 'Law Duff There Inks', 15: 'Moe’s Art', 16: 'Pay Perk Lips', 17: 'Sand Ta Claws', 18: 'Prey Tee Womb Anne', 19: 'Ew Nigh Ted Kink Dumb', 20: 'Foyer Inn Form Hay Shun', 21: 'Zola Reek Lips', 22: 'Welk Hum Ohm', 23: 'Kenya Ear Mean How', 24: 'Tack Seed Rye Fur', 25: 'Come Pew Turf Wire Us', 26: 'Oar He Oak Hooky', 27: 'Rome He Owe Hand Jewelry\n Yet', 28: 'Par Keens Pace', 29: 'Sadder Dane Height', 30: 'Lee On Hard Odie Cap Rio', 31: 'Soon Knees Hide Up', 32: 'Freeze Ham Pulse'}

answer = {1: 'British Accent',2: 'Will You Marry Me', 3: 'Wonder Woman',4: 'nickelodeon',5: 'See You Later', 6: 'White Elephant', 7: 'My Grandchildren', 8: 'A Lucky Charm',9: 'Hey Alexa', 10: 'I Love You', 11: 'Sparkling Water', 12: 'I Rest My Case', 13: 'Los Angeles', 14: 'Lord of the Rings', 15: 'Mozart', 16: 'Paper Clips', 17: 'Santa Claus', 18: 'Pretty Woman', 19: 'United Kingdom', 20: 'For Your Information', 21: 'Solar Eclipse', 22: 'Welcome Home', 23: 'Can You Hear Me Now', 24: 'Taxi Driver', 25: 'Computer Virus', 26: 'Oreo Cookie', 27: 'Romeo And Juliet', 28: 'Parking Soace', 29: 'Saturday Night', 30: 'Leonardo Dicaprio', 31: 'Sunny Side Up', 32: 'Free Samples'}



score = 0
timer = 20


def correct_sound():
    threading.Thread(target=playsound.playsound, args=(r"C:\Users\ASUS\pavan^^\PycharmProjects\Guess the Gibberish\ting.mp3",)).start()
def wrong_sound():
    threading.Thread(target=playsound.playsound, args=(r"C:\Users\ASUS\pavan^^\PycharmProjects\Guess the Gibberish\wrongbuzz.mp3",)).start()



def start_game():
    # correct_answer.config(text='')
    # reaction.config(text='')
    global random_num, timer
    timer = 20
    random_num = random.randint(1,32)
    question_label.config(text=question[random_num])
    hint_label.config(text = 'Hint -> Number of words is : '+str(len(answer[random_num].split())))
    startcountdown()
    ans_entry.bind('<Return>', check_answer)
    correct_answer.config(text='')


def reset():
    global timer , score
    timer = 20
    score = 0
    score_label.config(text='Your Score : ' + str(score))
    time_label.config(text='20')
    question_label.config(text='Guess The Gibberish')
    hint_label.config(text='Hint -> Number of words is : ')
    ans_entry.delete(0, END)



def startcountdown():
    global timer
    if timer >= 0:
        time_label.config(text=str(timer))
        timer -= 1
        time_label.after(1000, startcountdown)
        if timer == -1:
            next_btn.config(state=NORMAL)
            correct_answer.config(text='Correct answer\nis :\n' + answer[random_num].lower(), fg='#1a759f')
            ans_entry.delete(0,END)





def check_answer(par):
    global score
    user = str(ans_entry.get())
    if user.lower() == answer[random_num].lower():
        score += 1
        score_label.config(text = 'Your Score : ' + str(score))
        ans_entry.delete(0, END)
        positive_outputs = ['NICE\n(～￣▽￣)～', 'GOOD JOB!\n(★ω★)','ATTABOYY!\n╰(￣ω￣ｏ)', 'YESS BOSS!\nᕙ(⇀‸↼‶)ᕗ', 'SPOT ON!\n(◕‿◕✿))', 'EXACTLY!\n♥‿♥', 'CORRECT!\n(>ω<)', 'OHH YEAHH!\n(≧▽≦)']  
        reaction.config(text=str(random.choice(positive_outputs)), fg='green')
        correct_sound()
    else:
        ans_entry.delete(0, END)
        reaction.config(text='WRONG\n(ー_ー;)', fg= 'red')
        wrong_sound()








root = Tk()

root.geometry('610x607')
root.title('Guess the Gibberish')
root.resizable(False, False)


root.iconbitmap(r"C:\Users\ASUS\pavan^^\PycharmProjects\Guess the Gibberish\LOGO.ico")
image1 = Image.open(r"C:\Users\ASUS\pavan^^\PycharmProjects\Guess the Gibberish\gibbbg.jpg")                 #ikde ti blackboard wali img
test = ImageTk.PhotoImage(image1)
Label(image= test).place(x=0, y=0)


question_label = Label(root, font='Helvetica 20 bold', bg = '#5b825d', fg='white')
question_label.place(x=130, y=220)


time_label = Label(root, text= '20', width=2,height=1,font='Helvetica 26 bold', fg='black', bg='#e99d62')
time_label.place(x=525, y=29)


score_label = Label(root, text= 'Your Score : '+str(score), font='Helvetica 12 bold', fg='black', bg='white')
score_label.place(x = 250, y=400)


ans_entry = Entry(root, width=25, bd=0,font='Helvetica 12 bold', justify=CENTER)
ans_entry.place(x = 190, y= 475)


hint_label = Label(root, text= 'Hint -> Number of words is : ', fg='#ffff63', bg='#5b825d')
hint_label.place(x=105, y=347)


next_btn = Button(root, text='Next', width=10,font='Helvetica 10 bold', bd = 0 , bg='white', command= start_game)
next_btn.place(x=483, y=480.5)


reaction = Label(root, text='',fg='black', bg='#ffcc6a', font='Helvetica 13 bold')
reaction.place(x = 480, y = 425)


correct_answer = Label(root, text= ' ', font='Helvetica 12 bold', fg='black', bg='#ff73b8')
correct_answer.place(x = 2, y = 470)


start_button = Button(root, text='Start',font='Helvetica 9 bold' ,width=16, bd = 0 , padx = 10, pady=10, bg='white', command= start_game)
start_button.place(x=179, y=563)
Button(root, text='reset', width=16, font='Helvetica 9 bold' ,bd = 0 , padx = 10, pady=10, bg='white', command = reset).place(x=321, y=563)

root.mainloop()



