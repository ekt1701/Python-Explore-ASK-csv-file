This is a Python script that downloads the Alexa Skills listings csv file.  Then you can explore through the listing file by date, name of skill, author, description and ratings.  The script can also check when the csv file was last updated.

The reason I made this as a script instead of a skill, is that once you download the csv file, there is no delay in accessing the data.  With a skill, there can be a delay in reading the csv file (1.5MB in size) over the internet.  I don't know if there is a way to cache the file during a session.  Also, depending on what you search for, there can be a lot of information, so its easier to read it.

Wishlist: I want to call the functions through the command line input, so it can be more interactive.  However, I don't now how to input a command that has arguments to a function.

