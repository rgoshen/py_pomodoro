from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.75
CHECK_MARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Method to reset timer to 0, title back to 'Timer' and check marks back to zero. """
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    pomodoro_title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Method to start count down timer and change countdown for different sessions."""
    global reps
    reps += 1
    
    # convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # countdown session types
    if reps % 2 == 0:
        pomodoro_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        pomodoro_title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        pomodoro_title.config(text="Work", fg=GREEN)
        count_down(work_sec)    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Method to countdown from passed in seconds."""
    
    global timer
    
    # convert passed in total seconds to be able to be displayed as 00:00 format
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"       
    
    # updates display
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # adds check marks for each work session
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
            
        check_marks.config(text=marks)
        
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
pomodoro_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
pomodoro_title.grid(column=2, row=0)

# Background image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)

# Start button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=2)

# Check mark for small breaks taken
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14, "bold"))
check_marks.grid(column=2, row=3)

# Reset button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=3, row=2)

window.mainloop()
