from __future__ import print_function
import urllib2
import urllib
import csv
import re

keepGoing = True

def dateupdated():
    url = "https://github.com/dale3h/alexa-skills-list/blob/master/skills.csv"
    file = urllib.urlopen(url)
    text = file.read()
    datelocation = 'datetime="(.+?)Z'
    datepattern = re.compile(datelocation)
    date = re.findall(datepattern,text)
    print(date)
    return


def downloadcsv():
    url = 'https://github.com/dale3h/alexa-skills-list/raw/master/skills.csv'
    urllib.urlretrieve(url, "skills.csv")
    print("Download of csv file completed.")
    return


def numberofskills():
    ifile  = open('skills.csv', "rb")
    cr = csv.reader(ifile)
    data = []
    count = 0
    for row in cr:
        count = int(count) + 1
    count = count - 1
    number = str(count)
    report = "Currently, there are " + number + " skills"
    print(report)
    ifile.close()
    return


def searchbyname(name):
    ifile  = open('skills.csv', "rb")
    cr = csv.reader(ifile)
    data = []
    skillname = ""
    for row in cr:
        skillname = row[0]
        if name in skillname.lower():
            data.append(row[0])
    nameskills = '. '.join(data)
    if nameskills == "":
        text = "There are no skills with the name " + name
    else:
        text = "Here are the skills with the name " + name + ". " + nameskills
    print(text)
    ifile.close()
    return


def searchbydate(date):
    ifile  = open('skills.csv', "rb")
    cr = csv.reader(ifile)
    data = []
    for row in cr:
        if date in row[8]:
            data.append(row[0])
    datereleased = '. '.join(data)
    if datereleased == "":
        text = "There were no skills released on " + date
    else:
        text = "Here are the skills released on " + date + ". " + datereleased
    print(text)
    ifile.close()
    return


def searchbydescription(name):
    ifile  = open('skills.csv', "rb")
    cr = csv.reader(ifile)
    data = []
    descriptionword = ""
    for row in cr:
        descriptionword = row[3]
        if name in descriptionword.lower():
            match = "DESCRIPTION " + descriptionword
            data.append(match)
    descriptionmatch = '. '.join(data)
    if descriptionmatch == "":
        text = "No descriptions matched with " + name
    else:
        text =  descriptionmatch
    print(text)
    ifile.close()
    return


def searchbyauthor(author):
    ifile  = open('skills.csv', "rb")
    cr = csv.reader(ifile)
    data = []
    authorname = ""
    for row in cr:
        authorname = row[2]
        if author in authorname.lower():
            skillsbyauthor = row[2] + ":" + row[0]
            data.append(skillsbyauthor)
    authorskills = '. '.join(data)
    if authorskills == "":
        text = "There were no skills by " + author
    else:
        text = "Here are the skills released by " + author + " " + authorskills
    print(text)
    ifile.close()
    return


def searchbyrating(rating):
    ifile  = open('skills.csv', "rb")
    cr = csv.reader(ifile)
    data = []
    for row in cr:
        if rating in row[4]:
            score = row[0] + ":" + row[4]
            data.append(score)
    ratedskills = '. '.join(data)
    if ratedskills == "":
        text = "There were no skills with that rating"
    else:
        text = "Here are the skills released ", ratedskills
    print(text)
    ifile.close()
    return

def searchforinvocation(name):
    ifile  = open('skills.csv', "rb")
    cr = csv.reader(ifile)
    data = []
    invoke = ""
    for row in cr:
        invoke = row[9]
        if name in invoke.lower():
            saying = row[9]
            data.append(saying)
    invocation = '. '.join(data)
    if invocation == "":
        text = "I'm sorry could not find that information"
    else:
        text = "Say " + invocation
    print(text)
    ifile.close()
    return

def getinfotitle(name):
    ifile  = open('skills.csv', "rb")
    cr = csv.reader(ifile)
    data = []
    infotitle = ""
    for row in cr:
        infotitle = row[0]
        if name in infotitle.lower():
            temp = row[8]
            reldate = temp.split(" ")

            info = row[0] + " written by " + row[2] + ". The description is " + row[3] + ". It has rating of " + row[4] + ".  The number of reviews is " + row[5] + ". It was released on " + reldate[0] + ". Say " + row[9] + " to launch the skill."
            data.append(info)
    allinfo = '. '.join(data)
    if allinfo == "":
        text = "I'm sorry could not find that information"
    else:
        text = allinfo
    print(text)
    ifile.close()
    return

def help():
    print("Here are the commands that can entered:")
    print("when #Shows date when csv file was updated")
    print("down #Downloads the csv file to the same directory as this script.")
    print("number #Shows the current number of skills.")
    print("date 2016-08-12 #Displays all skills released on that date.")
    print("name yeti #Shows all skills that matched the name entered.")
    print("desc yeti #Shows the description of the skill entered")
    print("author james #Shows all skills created by the author's name.")
    print("how yeti #Shows the invocation for the skill.")
    print("info yeti #Shows complete information for the skill entered.")

    return

while keepGoing:
    command = raw_input("Enter command> ")

    # Quit if given the command "quit"
    if command == "quit":
        keepGoing = False

    parts = command.split(" ")

    if parts[0] == "name":
        searchbyname(" ".join(parts[1:]))
    elif parts[0] == "author":
        searchbyauthor(" ".join(parts[1:]))
    elif parts[0] == "when":
        dateupdated()
    elif parts[0] == "number":
        numberofskills()
    elif parts[0] == "rate":
        searchbyrating(" ".join(parts[1:]))
    elif parts[0] == "desc":
        searchbydescription(" ".join(parts[1:]))
    elif parts[0] == "down":
        downloadcsv()
    elif parts[0] == "date":
        searchbydate(" ".join(parts[1:]))
    elif parts[0] == "how":
        searchforinvocation(" ".join(parts[1:]))
    elif parts[0] == "info":
        getinfotitle(" ".join(parts[1:]))
    elif parts[0] == "help":
        help()
