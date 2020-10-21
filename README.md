# Homework 3
For this project, you will be able to work with a partner. You can select a partner and share one of the repl.it workspaces between the two of you. Additionally, you will need to have a design document where you have the specifications of your application. This could either be a text document that lives in your repl.it workspace or you could use another collaborate platform such as Google Docs or a Microsoft Word shared document.

You will be creating a calendar that displays the current month using a graphical interface. The design and layout of the calendar will be left to you and your team.

The calendar should be able to read from a file to get events. The events themselves may be too long to display on the calendar so you need a way to let users know there is an event on a given day.

If a user selects a day, they should be able to see the events for that day listed out.

### Design Document
Create a document that sketches a visual of how your calendar will look. Where will you display the following:
- Month Name
- Week Days
- Calendar Dates
- Dates that have events
- Extra information if a date is selected

#### Design Questions
- Is there a way to see which date is selected?
- Does the information display on the main calendar or in a new window?
- How do I manage multiple events in a date
- Is my interface intuitive?
  - Can someone figure out how to use this calendar without a lot of explanation?

#### Event File
You will need to have a file in the same folder as your Calendar.py that has a listing of events.
You and your team will need to decide how to store information in this file.
- What is the format of info in the file?
  - 3 Dentist Appt
  - 3:Dentist Appt
- What happens if there are multiple events on a given day?
  - 3,Dentist Appt,Skydiving Lessons
  - 3#Dentist Appt\nSkydiving Lessons

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
- Calendar App (calendar.py & graphics.py)
- Events document
