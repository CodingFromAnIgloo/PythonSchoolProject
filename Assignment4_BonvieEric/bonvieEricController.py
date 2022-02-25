# Assignment 4 for CST8333
# Written by Eric Bonvie
# A MVC program for manipulating csv data
# October 28, 2020

import bonvieEricModel
import bonvieEricView
import csv

class Navigation:
    ''' A class created to respond to the user's input'''
    def __init__(self):
        '''A standard function to appear in a python class, given a meaningless body because python doesn't like it if it's empty'''
        self.id = 1

    def saveList(self, obj):
        '''A function for saving the current dataset to a new file in the current working directory'''
        listEntries = obj.caseList

        with open('saveFile', 'w', newline='') as file:
            '''Opening the new csv file for writing'''
            writer = csv.writer(file)
            
            for i in listEntries:
                '''A function for writing out the csv rows into the new file. If I made the CovidList into a dictionary, this section could potentially be made cleaner.'''
                a = str(i.id)
                b = str(i.date)
                c = str(i.cases)
                d = str(i.deaths)
                e = str(i.nameFrench)
                f = str(i.nameEnglish)

                writer.writerow([a, b, c, d, e, f])
                print('record added')
        file.close()
        print('File Saved by Eric Bonvie')

    def printList(self, obj):
        '''A function for printing the csv data to the screen. I chose to incorporate the 100 entry limit here, as the csv files we are working with are small enough to load the full file'''
        
        i = 0
        while i < len(obj.caseList):
            '''
            A simple do-while to print the first five stored data rows.
            Could be altered to allow user to choose specific rows or attributes,
            this is sufficient for the purposes of demonstration for this assignment
            '''
            print(obj.caseList[i].id, obj.caseList[i].date, obj.caseList[i].cases, obj.caseList[i].deaths, obj.caseList[i].nameFrench, obj.caseList[i].nameEnglish)
            if i % 10 == 0:
                '''A function to break up the stream of data every ten entries'''
                print('This is a program demonstration')
                print("Written by Eric Bonvie")
            i = i+1

    def addEntry(self, obj):
        '''A function that adds a new entry to the end of the list'''
        listEntries = obj
        caseID = str(input("What is the ID? :"))
        caseDate = str(input("What is the Date? :"))
        cases = str(input("How many cases? :"))
        deaths = str(input("How many deaths? :"))
        french = str(input("What is the French region name? :"))
        english = str(input("What is the English region name? :"))

        newData = bonvieEricModel.CovidObject(caseID, caseDate, cases, deaths, french, english)
        listEntries.caseList.append(newData)
        print('Your entry has been added (Eric Bonvie)')


    def editEntry(self, obj):
        '''A function for editing a single entry. As part of it's function, it also prints a single data row to the terminal'''
        listEntries = obj.caseList
        i = int(input("Which case would you like to edit? :"))
        print('You have selected...')
        
        print(listEntries[i].id)
        print(listEntries[i].date)
        print(listEntries[i].cases)
        print(listEntries[i].deaths)
        print(listEntries[i].nameFrench)
        print(listEntries[i].nameEnglish)

        caseID = str(input("New ID :"))
        caseDate = str(input("New Date :"))
        cases = str(input("New Cases :"))
        deaths = str(input("New Deaths :"))
        french = str(input("New French region name :"))
        english = str(input("New English region name :"))

        newData = bonvieEricModel.CovidObject(caseID, caseDate, cases, deaths, french, english)
        listEntries[i] = newData
        print("That record has been altered (Eric Bonvie)")

    def deleteEntry(self, obj):
        '''A very simple function for deleting a data row'''
        i = int(input("Which case would you like to delete? :"))
        del obj.caseList[i]
        print("Case deleted (Eric Bonvie)")
    
    def searchList(self, obj):
        '''A function for printing a selection of data rows to the console based on user input.'''
        print("This function will search through all the data and print out every file that meets your specifications. Blank parameters are treated as wild cards.")

        searchID = str(input("Search by Id :"))
        searchDate = str(input("Search by Date :"))
        searchCases = str(input("Search by Cases :"))
        searchDeaths = str(input("Search by Deaths :"))
        searchFrench = str(input("Search by region name :"))
        searchEnglish = str(input("Search by region name :"))
        
        i = 0

        if searchID == '':
            parId = False
        else:
            parId = True
        if searchDate == '':
            parDate = False
        else:
            parDate = True
        if searchCases == '':
            parCases = False
        else:
            parCases = True
        if searchDeaths == '':
            parDeaths = False
        else:
            parDeaths = True
        if searchFrench == '':
            parFrench = False
        else:
            parFrench = True
        if searchEnglish == '':
            parEnglish = False
        else:
            parEnglish = True

        while i < len(obj.caseList):
            '''
            A do-while to print all stored data rows that meet user parameters.
            '''
            valid = True

            if parId == True: 
                if str(obj.caseList[i].id) != searchID:
                    valid = False
            if parDate == True: 
                if str(obj.caseList[i].date) != searchDate:
                    valid = False
            if parCases == True: 
                if str(obj.caseList[i].cases) != searchCases:
                    valid = False            
            if parDeaths == True: 
                if str(obj.caseList[i].deaths) != searchDeaths:
                    valid = False
            if parFrench == True: 
                if str(obj.caseList[i].nameFrench) != searchFrench:
                    valid = False
            if parEnglish == True: 
                if str(obj.caseList[i].nameEnglish) != searchEnglish:
                    valid = False

            if valid == True:
                print(obj.caseList[i].id, obj.caseList[i].date, obj.caseList[i].cases, obj.caseList[i].deaths, obj.caseList[i].nameFrench, obj.caseList[i].nameEnglish)              
            i = i+1
        

        

    