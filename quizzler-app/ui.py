import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362" # Background color of tkinter UI for this project

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Button
        check_img = tkinter.PhotoImage(file="images\\true.png")
        self.true_button = tkinter.Button(image=check_img, bg=THEME_COLOR, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        cross_img = tkinter.PhotoImage(file="images\\false.png")
        self.false_button = tkinter.Button(image=cross_img, bg=THEME_COLOR, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(tagOrId=self.question_text, text=q_text)
            self.buttons_enabled()
        else:
            self.canvas.itemconfig(tagOrId=self.question_text, text="You've reached the end of the quiz.")
            self.buttons_disabled()

    def is_true(self) -> None:
        self.buttons_disabled()
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self) -> None:
        self.buttons_disabled()
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool) -> None:
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

    def buttons_enabled(self) -> None:
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

    def buttons_disabled(self) -> None:
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")