from __future__ import print_function
import urllib2
import urllib
import csv
import re
import cmd
import sys

ifile  = open('skills.csv', "rb")
cr = csv.reader(ifile)
data = []

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
    return


def numberofskills():
    count = 0
    for row in cr:
        count = int(count) + 1
    count = count - 1
    number = str(count)
    report = "Currently there are " + number + " skills"
    print(report)
    return


def byname(name):
    skillname = ""
    for row in cr:
        skillname = row[0]
        if name in skillname.lower():
            data.append(row[0])
    newskills = '. '.join(data)

    if newskills == "":
        text = "There were no skills with that name"
    else:
        text = "Here are the skills released ", newskills

    print(text)
    return


def bydate(date):
    for row in cr:
        if date in row[8]:
            data.append(row[0])
    newskills = '. '.join(data)

    if newskills == "":
        text = "There were no skills released on the date chosen"
    else:
        text = "Here are the skills released on " + date + " " + newskills

    print(text)
    return


def bydescription(name):
    descriptionword = ""
    for row in cr:
        descriptionword = row[3]
        if name in descriptionword.lower():
            match = "DESCRIPTION " + descriptionword
            data.append(match)
    descriptionmatch = '. '.join(data)

    if descriptionmatch == "":
        text = "No descriptions matched with that word"
    else:
        text =  descriptionmatch

    print(text)
    return


def byauthor(author):
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
    return


def byrating(rating):
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
    return

""" Uncomment the function you want to use, then run the script. """

#dateupdated()
#downloadcsv()
#numberofskills()
#bydate('2016-08-13')
#byname('space')
#bydescription(' cave ')
#byrating('5')
#byauthor('john')

"""
I wanted to input the functions at the commandline prompt, however,
the following code only works for functions without arguments.

function_dict = {'date':dateupdated, 'number':numberofskills,'download' :downloadcsv}
func = raw_input('Enter command >')
function_dict[func]()
"""
