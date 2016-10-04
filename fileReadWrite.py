# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:28:55 2016

@author: Angel Maredia
"""

def main():
    addName('howon', 'names.txt')
    namesList = listOfNames('names.txt')
    print(namesList)

#Takes a name, appends name to file
def addName(name, filename):
    file = open(filename,'a+')
    name+='\n'
    file.write(name)

#returns list of names in file
def listOfNames(filename):
    namesList = []
    file = open(filename, 'r')
    for line in file:
        line = line.rstrip();
        namesList.append(line)
    
    return namesList
    
main()
