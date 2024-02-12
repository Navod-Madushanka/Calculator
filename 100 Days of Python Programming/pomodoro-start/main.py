from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_all():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    task_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count = 0
    global reps
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        title_label.config(text="Work", fg=GREEN)
        count = WORK_MIN
    elif reps == 2 or reps == 4 or reps == 6:
        title_label.config(text="Break", fg=PINK)
        count = SHORT_BREAK_MIN
    else:
        reps = 1
        title_label.config(text="Break", fg=RED)
        count = LONG_BREAK_MIN

    count_down(count * 60)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        icon = "✓"
        if reps % 2 != 0:
            task_label.config(text=icon)
            icon += "✓"
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", command=reset_all)
btn_reset.grid(column=2, row=2)

task_label = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
task_label.grid(column=1, row=3)

window.mainloop()
