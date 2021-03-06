from tkinter import *
import math


#----------------------------------------------------
timer =0
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
counter = 0
text =""

def check_disappear():
    global counter, text

    if counter >= 0 and counter <= 10:
        results()


    if text == textbox.get(1.0, END):
        if counter == 10:
            window.after(1000, reset_text)
            counter = -1
        window.after(1000, check_disappear)
        counter += 1
    else:
        window.after(1000, check_disappear)
        text = textbox.get(1.0,END)
        counter = 0




# ----------------------------Calculate Results-------------------------------------------

def results():
    test_text = textbox.get("1.0", END)
    list =[]
    count =0
    for char in test_text:
        if char==" ":
            count +=1
            char = "SPACE"
            list.append(char)
        else:
            list.append(char)
    canvas.itemconfig(count_text,text= f"Word Count: {count}")

# ----------------------------Timer Reset-------------------------------------------
def reset_text():
    canvas.itemconfig(count_text,text="Word Count: 0")
    test_text = textbox.get("1.0", END)
    textbox.delete("1.0",END)




#---------------------------UI SETUP------------------------------------

window = Tk()
window.title('Speed Test')
window.config(padx=100,pady=50, bg='grey')

test_var = StringVar()


title_label = Label(pady=20,padx=50,text="Disappearing Text", fg=GREEN, font=(FONT_NAME,35,'bold'), bg=YELLOW)
title_label.grid(column=0,columnspan=3,row=0)

inst_label = Label(pady=20,padx=50,text="Instructions:Start Typing, Don't Stop,(11 secs) Everything will be scrapped", fg=RED, font=(FONT_NAME,10,'bold'), bg=YELLOW)
inst_label.grid(column=0,columnspan=3,row=1)



#Text
textbox = Text(height=20, width=75)
#Puts cursor in textbox.
textbox.focus()
#Get's current value in textbox at line 1, character 0
print(textbox.get("1.0", END))
textbox.grid(column=0,columnspan=3,row=4)



canvas = Canvas(width=200,height=40,bg=YELLOW, highlightthickness=0)
count_text = canvas.create_text(100,20,text="Word Count: 0", fill="black",font=(FONT_NAME,12,'bold'))
canvas.grid(column=0,columnspan=3,row=5)







#---------------------------Text bind------------------------------------
# textbox.bind('<Key>', check_disappear)




window.after(1000, check_disappear)
window.mainloop()