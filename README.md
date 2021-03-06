# Silver-DofE - Skills

My goal throughout DofE is to improve my ability to use python to solve problems, and gain familiarity with a few different modules with a range of uses, these include: pandas, matplotlib and pygame. I will be working on this for at least one hour a week over a period of 3 months.

## Activity Log

## Week Beginning – 20/09/21 Time: 60mins

To begin I finished off my current programming project, a program and UI for encoding and decoding a Vigenère cipher given a keyword. The processing aspect of the program used the functions char() and ord() to shift letters a given amount determined by the keyword. Then using Tkinter I constructed a UI which allowed you to select a mode (Encode/Decode), the keyword and the target text.
([Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher))

![The Vigenere Interface](Vigenere_Cipher/vigenereUI.png "Vigenere Interface")

## Week Beginning – 27/09/21 Time: 60mins

I took the time this week to consider a few different ideas and plan some projects to have a got at. A few ideas were a calculator program, learning matplotlib with some relevant data and to build a game in python.

## Weeks Beginning – 04/10/21 to 11/07/21 Time: 240mins

Over the next four weeks I focused on a more developed UI for my calculator program with a constantly refreshed display showing the answer/calculation.

![The Calculator Interface](Calculator/calculatorUI.png "Calculator Interface")


When the buttons on the calculator are pressed the relevant value is concatenated onto the active string variable which is displayed. When the equals button is pressed the active string is evaluated, and the answer displayed.

## Weeks Beginning – 01/11/21 to 08/08/21 Time: 285mins

This next block of four weeks was spent learning how to use and customise graph plotting with matplotlib with some file reading to get the data. To start with I installed the module and just tried getting a line and some point on the screen and understanding the syntax.

![A simple line plot](Graphing/simplePlot.png "A simple line plot")

I wanted to apply this to some real world data and see the trends it presented. So using daily case changes for COVID-19, matplotlib and pandas produced this graph.

![Covid Line Plot](Graphing/covidPlot.png "Covid Line Plot")

This shows the first three waves from last year. The main difficulty was manipulating the x-axis to ensure not to many data labels were shown at once and rotated 90 degrees. Over the next two weeks I worked on a program that would compare carbon dioxide emissions between two countries entered by the user.  The first show in blue, the second in red.

![Polution trends](Graphing/climatePlot.png "Polution trends")

In this example The United Kingdom is shown in Blue and France shown in Red.

## Weeks Beginning – 29/11/21 to 05/09/21 Time: 285mins

For the final three weeks of Silver I decided to make a game, and to start with an attempt at the classic space invaders. After a quick bit of research I found that pygame was great for beginners making a game in python. I built it up in some key stages:

- Building the game window
- Adding the player and keyboard control
- Implementing the enemies with a class
- Making functions and scoring
- Adding victory/loss
- Adding sounds

![Game on Start](Space_Invaders/start.png "The start of the game")

This is the game after starting with the player at the bottom and rows of enemies beggining to move towards the bottom of the screen.

## Conclusion

Since finishing this I have continued to program regularly and have finished a large platformer and am currently working on a program to beat the wordle game! It has been great to learn some of the many different paths you can take with python.

All of the program files can be found here!