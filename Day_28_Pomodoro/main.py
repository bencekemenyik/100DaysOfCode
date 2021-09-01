from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0

timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    timer_label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    ticks_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1 and reps < 9:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0 and reps < 9:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0 and reps < 9:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    if count == 0:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "✔"
        ticks_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


timer_label = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)

start_button = Button(text="Start", bg=YELLOW, command=start_timer)

reset_button = Button(text="Reset", bg=YELLOW, command=reset_timer)

ticks_label = Label(fg=GREEN, bg=YELLOW)

timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
ticks_label.grid(column=1, row=3)
reset_button.grid(column=2, row=2)







window.mainloop()