# Python-Explore-ASK-csv-file

This is a Python script that downloads the Alexa Skills listings csv file.  Then you can explore through the listing file by date, name of skill, author, description and ratings.  The script can also check when the csv file was last updated.

The reason I made this as a script instead of a skill, is that once you download the csv file, there is no delay in accessing the data.  With a skill, there can be a delay in reading the csv file (1.5MB in size) over the internet.  I don't know if there is a way to cache the file during a session.  Also, depending on what you search for, there can be a lot of information, so its easier to read it.

With the help of James Church https://github.com/jcchurch, this script has a command line option while running in the terminal.

At the command prompt you can enter the following commands:

help #Shows the commands available.

when #Shows date when csv file was updated.

down #Downloads the csv file to the same directory as this script.

number #Shows the current number of skills.

date 2016-08-12 #Displays all skills released on that date.

name yeti #Shows all skills that matched the name entered.

desc yeti #Shows the description of the skill entered
author james #Shows all skills created by the author's name.
how yeti #Shows the invocation for the skill.
info yeti #Shows complete information for the skill entered


