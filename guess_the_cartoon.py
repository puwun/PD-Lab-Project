import random
from tkinter import *
from PIL import Image, ImageTk
import playsound
import threading

answer = {0: 'Mickey Mouse', 1: 'Lion King', 2: 'Dora', 3: 'Dragon Ball Z', 4: 'Pink Panther', 5: 'Oswald', 6: 'Popeye', 7: 'Doraemon', 8: 'Batman', 9: 'Mr Bean', 10: 'Looney Tunes', 11: 'Powerpuff Girls', 12: 'SpongeBob', 13: 'Justice League', 14: 'Tom and Jerry'}

timer = 20
score = 0


def correct_sound():
    threading.Thread(target=playsound.playsound, args=(r"C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\ting.mp3",)).start()
def wrong_sound():
    threading.Thread(target=playsound.playsound, args=(r"C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\wrongbuzz.mp3",)).start()




def start_game():
    next_btn.config()
    correct_answer.config(text='')
    reaction.config(text='')
    global random_num, timer
    timer = 20
    displayimg = update_image()
    Question_label.config(image=displayimg)
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
            correct_answer.config(text='Correct \nanswer \nis: \n' + answer[random_num], fg='blue')
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
    random_num = random.randint(0,14)
    print(random_num)
    image_path = f"C:\\Users\\ASUS\\pavan^^\\PycharmProjects\\finalProject\\cartoonimages\\testimg{random_num}.png"

    image = PhotoImage(file=image_path)

    image_label.config(image=image)
    image_label.image = image 
    image_label.place(x=125, y=130)



def reset():
    global timer , score
    timer = 20
    score = 0
    score_label.config(text='Your Score : ' + str(score))
    time_label.config(text='20')
    # start_button.config(state=NORMAL)
    # next_btn.config()
    ans_entry.delete(0, END)



root = Tk()

root.geometry('612x608')
root.title('Guess the Gibberish')
root.resizable(False, False)


image1 = Image.open(r"C:\Users\ASUS\pavan^^\PycharmProjects\finalProject\cartoonbg.jpg")                 #ikde ti blackboard wali img
test = ImageTk.PhotoImage(image1)
Label(image= test).place(x=0, y=0)


Question_label = Label(root,text='', bg='#f0566e' ,font='Helvetica 20 bold')
Question_label.place(x=85, y=150)


time_label = Label(root, text= '20', font='Helvetica 25 bold', fg='white', bg='#f4a69c')
time_label.place(x=540, y=20)


score_label = Label(root, text= 'Your Score : '+str(score), font='Helvetica 17 bold', fg='black', bg='white')
score_label.place(x = 227, y=340)


ans_entry = Entry(root, width=25,  bd=0,font='Helvetica 12 bold', justify=CENTER)
ans_entry.place(x = 192, y= 455)


next_btn = Button(root, text='Next', width=6, height=0,font='Helvetica 9 bold',bd = 0 ,padx=13, bg='white', command= start_game)
next_btn.place(x=480, y=464)


reaction = Label(root, text='',fg='white', bg='#9e53e4', font='Helvetica 13 bold')
reaction.place(x = 470, y = 400)  #9e53e4


correct_answer = Label(root, font='Helvetica 12 bold', fg='black', bg='#f9575f')
correct_answer.place(x = 5, y = 410)     #f9575f   #acacac


start_button = Button(root, text='Start',font='Helvetica 9 bold' ,width=16, bd = 0 , padx = 13, pady=10, bg='white', command= start_game)
start_button.place(x=152, y=555)
Button(root, text='reset', width=16, font='Helvetica 10 bold' ,bd = 0 , padx = 13, pady=10, bg='white', command = reset).place(x=311, y=555)


image_label = Label(root)
image_label.pack()

root.mainloop()
