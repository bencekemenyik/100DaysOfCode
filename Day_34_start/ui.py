from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.timer = ""

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150,125, text="asdasd", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def change_buttons_state(self, state):
        self.true_button.config(state=state)
        self.false_button.config(state=state)

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.change_buttons_state(ACTIVE)
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="Quiz over! Restart the app to start a new quiz.")
            self.change_buttons_state(DISABLED)

    def true_button_pressed(self):
        self.change_buttons_state(DISABLED)
        self.give_feedback(self.quiz.check_answer("True"))


    def false_button_pressed(self):
        self.change_buttons_state(DISABLED)
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        timer = self.window.after(1000, self.get_next_question)






