from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text='Timer')
    timer_text
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    checkMarkLabel.config(text='')
    btn_start.config(state='active')

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    window.attributes('-topmost', 0)
    global reps
    reps += 1
    work_sec = (WORK_MIN * 5)
    short_break_sec = (SHORT_BREAK_MIN * 60)
    long_break_sec = (LONG_BREAK_MIN * 60)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)



def count_down(count):

        count_min = math.floor(count / 60)
        count_sec = count % 60

        if count_sec > 0:
            btn_start.config(state='disabled')

        if count_sec < 10:
            count_sec = f"0{count_sec}"




        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count -1)
        else:
            window.attributes('-topmost', 1)
            start_timer()
            marks = ""
            work_sessions = math.floor(reps / 2)
            for _ in range(0, work_sessions):
                marks += '✔'
            checkMarkLabel.config(text=marks)




# ---------------------------- COUNTDOWN MECHANISM -------------------------------






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)





canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="5",fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1,row=1)
title_label = Label(text="Timer", font=(FONT_NAME, 36, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)



btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)
btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(column=2, row=2)

checkMarkLabel = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14, 'bold'))
checkMarkLabel.grid(column=1, row=3)


window.mainloop()
