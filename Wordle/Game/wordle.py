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



# Game Functionality
def game_phase():

    global answer
    guess = (inputSection.get(1.0, "end-1c")).lower()

    # Generating answer pattern
    output = [["", "", "", "", ""], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # Pattern LetterUsed AnswerLetterUsed

    #Green pass
    for c in range(len(guess)):
        if guess[c] == answer[c]:
            output[0][c] = "g"
            output[1][c] = 1
            output[2][c] = 1

    # Yellow pass
    for c1 in range(len(guess)):        
        for c2 in range(len(answer)):
            if output[1][c1] == 0 and output[2][c2] == 0:               
                if c1 != c2 and guess[c1] == answer[c2]:
                    output[0][c1] = "y"
                    output[1][c1] = 1
                    output[2][c2] = 1

    # Grey pass
    for c in range(len(guess)):
        if output[1][c] == 0:
            output[0][c] = "w"
            output[1][c] = 1

    display_output = [output[0], guess.upper()]
    display(display_output)

def display(output):

    colors = {"w":"grey", "g":"green", "y":"yellow"}

    for x in range(len(output[0])):
        label = tk.Label(text=output[1][x], width = 8, height = 3, background = colors[output[0][x]])
        label.grid(row=3,column=x+1, pady=10)





# --- Defining Window --- #
titleFont = ('Helvetica bold',40)
labelFont = ('Helvetica bold',20)
textFont = ('Helvetica',15)
    
root = tk.Tk()
root.geometry("490x600+1200+200")
root.config(background="#f5f5f5")
root.title("Wordle")
root.iconphoto(False, tk.PhotoImage(file='./icon.png'))

# Title Label
titleLabel = tk.Label(root, width = 15, height = 1, text="Wordle", font=titleFont, background="#f5f5f5")
titleLabel.grid(row=1,column=1, columnspan=5)

#Text Input Section
inputSection = tk.Text(root, width = 15, height = 1, font=labelFont)
inputSection.grid(row=2, column=1, columnspan=3, pady=10)

#Submit Button
submitButton = tk.Button(root, width = 10, height = 1, font=labelFont, text="Submit", command=game_phase)
submitButton.grid(row=2, column=4, columnspan=2, pady=10)



# -- Main code --- #
answers = read_answers()

# Game loop
global answer
answer = answers[r.randint(0, len(answers)-1)]
root.mainloop()



    
