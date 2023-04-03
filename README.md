# Homework 3
For this project, you will be able to work with a partner. You can select a partner and share one of the repl.it workspaces between the two of you. Additionally, you will need to have a design document where you have the specifications of your application. This could either be a text document that lives in your repl.it workspace or you could use another collaborate platform such as Google Docs or a Microsoft Word shared document.

You will be creating a board game that is played using a graphical interface. The design and layout of the game will be left to you and your team.

The game should be able to read from a file to get score, players, and game-peice positions. The game status saved in the file should be thought of as a way to save your game and come back to it later. You don't need to continually update the information but you should be able to reconstruct a game based on file.

### Design Document
Create a document that sketches a visual of how your game will look. Where will you display the following:
- Game Name
- Game Spaces
- Player status
- Games pieces on a game space.
- Extra information if needed.

[Sample Design Document](https://docs.google.com/document/d/1xXQPjdLHRItnFXNEhXRUR7GD2Vof4vvSIap0wAtoHWM/edit?usp=sharing)
- Note that the sample example is for a calendar project. The ideas are the same but the code (while helpful) does not direcly apply to your current problem.

#### Design Questions
- What are the rules to the game?
  - You don't need to fully implement the game
  - How is it played, is there a dice roll or some other action?
- How are the player pieces visually identified.
- What other elements are in the game?
- What input from the user would you need to make the game go?
  - Do they click, is there text input?

#### Event File
You will need to have a file in the same folder as your BoardGame.py that has a listing of events.
You and your team will need to decide how to store information in this file.
- What is the format of info in the file?
  - Turn: Player 1
  - 3: Player 1
  - 4: Player 2
  - 17: Hotel
  - 20: Troll

- What happens if there are multiple pieces on the same spot?
  - 3: Player 1, Hotel, Troll

#### Problem Deconstruction
What functions will you use in your program?
How will using these functions help to simplify the overall design?
Who is in charge of each function (if working with a partner)?

### Drawing in Python
There are many ways to draw in Python. I have selected to use an intermediate package that makes it a lot easier to generate windows, shapes, text, and other graphical pieces.
You'll need to make sure that graphics.py is in the same project folder as your other work.  

#### Graphics API
The **graphics.py** file allows for many graphical methods to be used. There is another file, **graphics.pdf**,  that is a document that describes how they work.

### Final Submission
Your final work should include:
- Design Document
- BoardGame App (BoardGame.py & graphics.py)
  - Submit a document with link to your replit project.
- Events document
