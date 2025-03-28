from tkinter import *
from word_detection import display_sentence,word_detection
from pynput import keyboard

THEME_COLOR = "#dcd5cd"

class TypingTestUI:
    def __init__(self):

        self.timer = 60
        self.window = Tk()
        self.window.title("Typing Test")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas_frame = Frame(self.window)
        self.canvas_frame.grid(row=1, column=0, columnspan=7, pady=10)

        self.canvas = Canvas(self.canvas_frame, width=800, height=300, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        # --- Canvas with scrollbar ---

        self.scrollbar = Scrollbar(self.canvas_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.word_ids = []
        self.word_objects = []
        self.generate_new_sentence()


        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.CPM_label = Label(text="Correct CPM", bg=THEME_COLOR, font=('Arial', 18))
        self.CPM_label.grid(row=0, column=0)

        self.DISPLAY_CPM_label = Label(text="   ?", font=('Arial', 18))
        self.DISPLAY_CPM_label.grid(row=0, column=1)

        self.WPM_label = Label(text="WPM", bg=THEME_COLOR, font=('Arial', 18))
        self.WPM_label.grid(row=0, column=2)

        self.DISPLAY_WPM_label = Label(text="   ?", font=('Arial', 18))
        self.DISPLAY_WPM_label.grid(row=0, column=3)

        self.TIMER_label = Label(text="Time left", bg=THEME_COLOR, font=('Arial', 18))
        self.TIMER_label.grid(row=0, column=4)

        self.DISPLAY_TIMER_label = Label(text=f" {self.timer}", font=('Arial', 18))
        self.DISPLAY_TIMER_label.grid(row=0, column=5)

        self.RESET_btn = Button(text="Reset", width=13, command=self.reset_button, font=('Arial', 18))
        self.RESET_btn.grid(row=0, column=6)

        self.input_text_entry = Entry(width=55, font=('arial.ttf', 20))
        self.input_text_entry.grid(row=2, column=0, columnspan=7)
        self.timer_started = False

        self.input_text_entry.bind("<KeyPress>", self.star_typing)
        self.input_text_entry.bind("<space>", self.detectword)
        self.typed_word = None
        self.timer_callback = None
        self.list_pointer = 0
        self.CPM_counter = 0
        self.WPM_counter = 0
        self.ready_for_input = False
        self.window.mainloop()

    def start_timer(self):
        self.timer_started = True
        if self.timer > 0:
            self.timer -= 1
            self.DISPLAY_TIMER_label.config(text=f" {self.timer}")
            self.timer_callback=self.window.after(1000, self.start_timer)


    def reset_button(self):

        if self.timer_callback is not None:
            self.window.after_cancel(self.timer_callback)
            self.timer_callback = None
        self.ready_for_input = False
        self.timer=60
        self.timer_started = False  # <--- reset here
        self.DISPLAY_TIMER_label.config(text=f" {self.timer}")
        self.DISPLAY_WPM_label.config(text="   ?")
        self.DISPLAY_CPM_label.config(text="   ?")
        self.list_pointer =0
        self.CPM_counter = 0
        self.WPM_counter = 0

        self.input_text_entry.config(state='normal')
        self.input_text_entry.delete(0,'end')

        self.input_text_entry.focus_set()

        self.clear_canvas_words()
        self.generate_new_sentence()

    def star_typing(self, event):
        if not event.char or not event.char.isalpha():
            return
        self.window.after(100, self._check_and_start_timer)

    def _check_and_start_timer(self):
        typed = self.input_text_entry.get().strip()
        if typed and not self.timer_started:
            self.timer_started = True
            self.ready_for_input = True
            self.start_timer()

    def generate_new_sentence(self):

        self.word_list = display_sentence()
        self.word_ids = []

        x, y = 10, 10
        line_height = 50
        max_width = 780  # same as your canvas width - a bit of margin
        for word in self.word_list:
            word_id = self.canvas.create_text(x, y, anchor=NW, text=word, font=('Arial', 40), tags="word")
            self.canvas.update_idletasks()  # 👈 Force update

            bbox = self.canvas.bbox(word_id)
            if not bbox:
                continue  # skip if bbox fails (unlikely now)

            word_width = bbox[2] - bbox[0]

            if x + word_width > max_width:
                x = 10
                y += line_height
                self.canvas.delete(word_id)  # Remove previous word that didn’t fit
                word_id = self.canvas.create_text(x, y, anchor=NW, text=word, font=('Arial', 40), tags="word")
                self.canvas.update_idletasks()
                bbox = self.canvas.bbox(word_id)
                word_width = bbox[2] - bbox[0]

            self.word_ids.append(word_id)
            self.word_objects.append(word_id)
            x = bbox[2] + 20

    def clear_canvas_words(self):
        for obj in getattr(self, 'word_objects', []):
            self.canvas.delete(obj)
        self.word_ids.clear()
        self.word_objects.clear()

    def detectword(self, event):

        if not self.ready_for_input:
            return
        typed = self.input_text_entry.get().strip()
        self.input_text_entry.delete(0, 'end')

        if self.timer <= 0 or self.list_pointer >= len(self.word_list):
            return
        print(self.word_list[self.list_pointer])
        correct = typed == self.word_list[self.list_pointer]
        word_id = self.word_ids[self.list_pointer]

        if correct:
            self.canvas.itemconfig(word_id, fill="green")
            self.CPM_counter += len(typed)
            self.WPM_counter += 1
        else:
            self.canvas.itemconfig(word_id, fill="red")

        self.DISPLAY_CPM_label.config(text=f"{self.CPM_counter}")
        self.DISPLAY_WPM_label.config(text=f"{self.WPM_counter}")
        self.list_pointer += 1

        # Scroll if the current word is going off screen
        bbox = self.canvas.bbox(word_id)
        if bbox:
            _, y_top, _, y_bottom = bbox
            canvas_height = int(self.canvas['height'])

            current_scroll = self.canvas.canvasy(0)

            # Check if word is below visible area
            if y_bottom > current_scroll + canvas_height:
                self.canvas.yview_scroll(5, "units")


