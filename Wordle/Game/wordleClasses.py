# Wordle Game (TKinter)
# Tom Simpson

# Importing Modules
import tkinter as tk
import random as r

# --- Defining Methods --- #
# Generating possible answer list
def read_answers():

    answers = []
    with open("../Solver/guesses.txt", "r") as f:
        for line in f:
             answers.append(line.strip())
    return answers



# --- Defining Window --- #
class wordleUI:

    def __init__(self, master):

        # Initialising Gameplay stuff
        self.answers = read_answers()
        self.answer = self.answers[r.randint(0, len(self.answers)-1)]
        self.height = 1

        # Initialising Tk stuff
        self.titleFont = ('Helvetica bold',40)
        self.labelFont = ('Helvetica bold',20)

        master.geometry("500x600+1200+200")
        master.config(background="#0000ff")
        master.title("Wordle")
        master.iconphoto(False, tk.PhotoImage(file='./icon.png'))

        frame = tk.Frame(master)
        frame.grid(row=1,column=1)
        frame.config(background="#ff0000")

        self.feedback = tk.Frame(master)
        self.feedback.grid(row=2,column=1)
        self.feedback.config(background="#00ff00")

        # Making widgets
        self.titleLabel = tk.Label(frame, width = 15, height = 1, text="Wordle", font=self.titleFont)
        self.titleLabel.grid(row=1,column=1,columnspan=5)

        self.inputSection = tk.Text(frame, width = 15, height = 1, font=self.labelFont)
        self.inputSection.grid(row=2, column=1, columnspan=3, pady=10)

        self.submitButton = tk.Button(frame, width = 10, height = 1, font=self.labelFont, text="Submit", command=self.game_phase)
        self.submitButton.grid(row=2, column=4, columnspan=2, pady=10)



    # Game Functionality
    def game_phase(self):

        guess = (self.inputSection.get(1.0, "end-1c")).lower()

        # Generating answer pattern
        output = [["", "", "", "", ""], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # Pattern LetterUsed AnswerLetterUsed

        #Green pass
        for c in range(len(guess)):
            if guess[c] == self.answer[c]:
                output[0][c] = "g"
                output[1][c] = 1
                output[2][c] = 1

        # Yellow pass
        for c1 in range(len(guess)):        
            for c2 in range(len(self.answer)):
                if output[1][c1] == 0 and output[2][c2] == 0:               
                    if c1 != c2 and guess[c1] == self.answer[c2]:
                        output[0][c1] = "y"
                        output[1][c1] = 1
                        output[2][c2] = 1

        # Grey pass
        for c in range(len(guess)):
            if output[1][c] == 0:
                output[0][c] = "w"
                output[1][c] = 1

        display_output = [output[0], guess.upper()]

        # --- Displaying --- #
        colors = {"w":"grey", "g":"green", "y":"yellow"}

        for x in range(len(display_output[0])):
            label = tk.Label(self.feedback, text=display_output[1][x], width = 8, height = 3, background = colors[display_output[0][x]])
            label.grid(row=self.height,column=x+1,pady=8,padx=5)
        self.height += 1



# -- Main code --- #
root = tk.Tk()
wordle = wordleUI(root)
root.mainloop()



    
