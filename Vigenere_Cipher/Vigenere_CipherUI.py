# Tom Simpson
# Vigeniere Cypher

# Importing Modules
import tkinter as tk

# Defing Methods
global mode
mode = "encode"

# Mode button functions
def setTypeEncode():
    global mode
    mode = "encode"
def setTypeDecode():
    global mode
    mode = "decode"



# Shift algorithm functions
# Encoding message
def encodeMessage(plainText, keyWord):

    cipherText = ""
    keyCount = 0

    for x in range(len(plainText)):

        chrValue = ord(plainText[x])

        if (chrValue > 64 and chrValue < 91) or (chrValue > 96 and chrValue < 123): # If letter
            if plainText[x].islower():
                base = ord("a")
            if plainText[x].isupper():
                base = ord("A")
                
            shift = ord(keyWord[keyCount%len(keyWord)]) - 97 #Lower case keyword
            keyCount += 1 #Doesn't advance keyword pointer if non-letter

            newCharacter = ((chrValue + shift) - base) % 26
            cipherText += chr(newCharacter + base)

        else:
            cipherText += chr(chrValue)

    return(cipherText)



# Decoding message    
def decodeMessage(plainText, keyWord):

    cipherText = ""
    keyCount = 0

    for x in range(len(plainText)):

        chrValue = ord(plainText[x])

        if (chrValue > 64 and chrValue < 91) or (chrValue > 96 and chrValue < 123): # If letter
            if plainText[x].islower():
                base = ord("a")
            if plainText[x].isupper():
                base = ord("A")
                
            shift = ord(keyWord[keyCount%len(keyWord)]) - 97 #Lower case keyword
            keyCount += 1 #Doesn't advance keyword pointer if non-letter

            newCharacter = ((chrValue - shift) - base) % 26
            cipherText += chr(newCharacter + base)

        else:
            cipherText += chr(chrValue)

    return(cipherText)



# Enter button functions
def process():

    global mode

    plain_text = inputSection.get(1.0, "end-1c")
    keyword = keySection.get(1.0, "end-1c")

    if mode == "encode":
        cipher_text = encodeMessage(plain_text, keyword)
    if mode == "decode":
        cipher_text = decodeMessage(plain_text, keyword)

    displayText.set(cipher_text)



# TK Inter UI pieces
root = tk.Tk()
root.geometry("850x600+300+300")
root.config(background = "#cccccc")
root.title("Vigenere Cipher Tool")

titleFont = ('Helvetica bold',40)
labelFont = ('Helvetica bold',20)
textFont = ('Helvetica',15)

# Title Label
titleLabel = tk.Label(root, width = 15, height = 2, text="Vigenere Cipher", font=titleFont, background="#cccccc")
titleLabel.grid(row=1,column=2, columnspan=2)

#Text Input Section
inputLabel = tk.Label(root, width=8, height=2, text="Input:", font=labelFont, background="#cccccc")
inputLabel.grid(row=2,column=1,padx=5)
inputSection = tk.Text(root, width = 55, height = 5, font=textFont)
inputSection.grid(row=2, column=2, columnspan=2, pady=5)

# Mode Button
modeLabel = tk.Label(root, width=8, height=2, text="Mode:", font=labelFont, background="#cccccc")
modeLabel.grid(row=4,column=1,padx=5)
encode = tk.Button(root, width=18, height=2, command=setTypeEncode, text="Encode", background="#99c2ff")
encode.grid(row=4,column=2,pady=5)
decode = tk.Button(root, width=18, height=2, command=setTypeDecode, text="Decode", background="#99c2ff")
decode.grid(row=4,column=3,pady=5)

# Keyword Input Section
keyLabel = tk.Label(root, width=8, height=2, text="Key:", font=labelFont, background="#cccccc")
keyLabel.grid(row=3, column=1,padx=5)
keySection = tk.Text(root, width = 55, height = 2, font=textFont)
keySection.grid(row=3, column=2, columnspan=2, pady=5)

# Submit Button
submit = tk.Button(root, width=25, height=2, command=process, text="Submit", background="#ffb3b3")
submit.grid(row=5, column=2, columnspan=2)

# Text Output section
displayText = tk.StringVar()

outputLabel = tk.Label(root, width=8, height=2, text="Output:", font=labelFont, background="#cccccc")
outputLabel.grid(row=6, column=1,padx=5)
outputSection = tk.Label(root, textvariable=displayText, width = 50, height = 5, background="#ffffff", font=textFont)
outputSection.grid(row=6, column=2, columnspan=2, pady=5)


# --- Running Loop --- #

running = True
while running:

    root.update_idletasks()
    root.mainloop()

