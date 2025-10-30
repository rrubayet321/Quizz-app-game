from tkinter import *
import os
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz= quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.geometry("350x550")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20))
        self.score_label.grid(row=0, column=1, pady=(10, 15))


        self.canvas = Canvas(bg="white", height=300, width=300, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(20,30))
        self.canvas_text = self.canvas.create_text(150, 150, text="Some text",
                                                   font=("Arial", 18, "italic"),
                                                   fill=THEME_COLOR,
                                                   width=280)

        # Load button images safely
        true_path = "images/true.png"
        false_path = "images/false.png"

        self.true_image = PhotoImage(file=true_path) if os.path.exists(true_path) else None
        self.false_image = PhotoImage(file=false_path) if os.path.exists(false_path) else None

        self.button_frame = Frame(self.window, bg=THEME_COLOR)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=(0,0))

        # True Button
        if self.true_image:
            self.true_button = Button(self.button_frame, image=self.true_image, highlightthickness=0, bg=THEME_COLOR, command= self.true_checker)
        else:
            self.true_button = Button(self.button_frame, text="True", font=("Arial", 14), bg="green", fg="white")
        self.true_button.grid(row=0, column=0, padx=20)

        # False Button
        if self.false_image:
            self.false_button = Button(self.button_frame, image=self.false_image, highlightthickness=0, bg=THEME_COLOR, command= self.false_checker)
        else:
            self.false_button = Button(self.button_frame, text="False", font=("Arial", 14), bg="red", fg="white")
        self.false_button.grid(row=0, column=1, padx=20)
        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the maximum number of questions and also the end of the quiz.")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_checker(self):
        self.feedback_giver(self.quiz.check_answer("True"))

    def false_checker(self):
        is_right= self.quiz.check_answer("False")
        self.feedback_giver(is_right)

    def feedback_giver(self, is_right):
        if is_right:
            self.canvas.config(bg='light green')
        else:
            self.canvas.config(bg='#FF7F7F')  # or 'light coral'
        self.window.after(1000, self.get_next_question)





# QuizInterface()
