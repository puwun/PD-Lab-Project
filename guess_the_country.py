import random
from tkinter import *
from PIL import Image, ImageTk
import playsound
import threading

answer = {0: 'Iceland', 1: 'China', 2: 'Japan', 3: 'Belgium', 4: 'Spain', 5: 'Ukraine', 6: 'Oman', 7: 'Serbia', 8: 'Germany', 9: 'Thailand', 10: 'Iran', 11: 'New Zealand', 12: 'Taiwan', 13: 'Botswana', 14: 'Chile', 15: 'Romania', 16: 'Turkey', 17: 'Poland', 18: 'India', 19: 'Madagascar', 20: 'Wales', 21: 'Denmark', 22: 'Singapore', 23: 'Cambodia', 24: 'Finland', 25: 'Kuwait'}


score = 0
timer = 20


def correct_sound():
    threading.Thread(target=playsound.playsound, args=(r"C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\ting.mp3",)).start()

def wrong_sound():
    threading.Thread(target=playsound.playsound, args=(r"C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\wrongbuzz.mp3",)).start()




def start_game():
    # correct_answer.config(text='')
    # reaction.config(text='')
    global random_num, timer
    timer = 20
    displayimg = update_image()
    question_label.config(image=displayimg)
    startcountdown()
    ans_entry.bind('<Return>', check_answer)
    correct_answer.config(text='')




def startcountdown():
    global timer
    if timer >= 0:
        time_label.config(text=str(timer))
        timer -= 1
        time_label.after(1000, startcountdown)
        if timer == -1:
            # next_btn.config(state=NORMAL)
            correct_answer.config(text='Correct\nanswer\nis:\n' + answer[random_num], fg='blue')
            ans_entry.delete(0,END)




def check_answer(par):
    global score
    user = str(ans_entry.get())
    if user.lower() == answer[random_num].lower():
        score += 1
        score_label.config(text='Your Score : ' + str(score))
        ans_entry.delete(0, END)
        positive_outputs = ['NICE\n(～￣▽￣)～', 'GOOD JOB!\n(★ω★)','ATTABOYY!\n╰(￣ω￣ｏ)', 'YESS BOSS!\nᕙ(⇀‸↼‶)ᕗ', 'SPOT ON!\n(◕‿◕✿))', 'EXACTLY!\n♥‿♥', 'CORRECT!\n(>ω<)', 'OHH YEAHH!\n(≧▽≦)']  
        reaction.config(text=str(random.choice(positive_outputs)), fg='green')
        correct_sound()
    else:
        ans_entry.delete(0, END)
        reaction.config(text='WRONG\n(ー_ー;)', fg='red')
        wrong_sound()




def update_image():
    global random_num
    random_num = random.randint(0,25)
    image_path = f"C:\\Users\\ASUS\\pavan^^\\PycharmProjects\\finalProject\\countryimages\\testimg{random_num}.png"
    image = PhotoImage(file=image_path)

    image_label.config(image=image)
    image_label.image = image
    image_label.place(x=115, y=182)




def reset():
    global timer , score
    timer = 20
    score = 0
    score_label.config(text='Your Score : ' + str(score))
    time_label.config(text='20')
    ans_entry.delete(0, END)





root = Tk()
root.geometry('610x607')
root.title('Guess the Country?!')
root.resizable(False, False)


image1 = Image.open(r"C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\countrybg.jpg")                 
test = ImageTk.PhotoImage(image1)
Label(image= test).place(x=0, y=0)


#responsible for displaying the image/text
question_label = Label(root,fg='white', bg='black', font='Helvetica 15 bold')
question_label.place(x=75, y=135)


time_label = Label(root, text= '20', font='Helvetica 20 bold', fg='white', bg='black')
time_label.place(x=76, y=87)


score_label = Label(root, text= 'Your Score : '+str(score), font='Helvetica 19 bold', fg='black', bg='white')
score_label.place(x = 228, y=371)


ans_entry = Entry(root, width=17,bd=0, font='Helvetica 19 bold', justify=CENTER)
ans_entry.place(x = 195, y= 460)


next_btn = Button(root, text='Next', width=7, height= 1,font='Helvetica 9 bold', bd = 0, padx=10, bg='white', command= start_game)
next_btn.place(x=472, y=474)


reaction = Label(root, text='',fg='white', bg='#eeeeee', font='Helvetica 13 bold')
reaction.place(x = 465, y = 398)


correct_answer = Label(root, text= ' ', font='Helvetica 12 bold', fg='black', bg='#acacac')
correct_answer.place(x = 2, y = 410)


start_button = Button(root, text='Start',font='Helvetica 11 bold' ,width=2, bd = 0 , padx=40, bg='white', command= start_game)
start_button.place(x=195, y=570)
Button(root, text='reset',font='Helvetica 11 bold' ,width=2, bd = 0 , padx=40, bg='white',  command = reset).place(x=333, y=570)


image_label = Label(root)
image_label.pack()

root.mainloop()
