# Assignment 4 for CST8333
# Written by Eric Bonvie
# A MVC program for manipulating csv data
# October 28, 2020

import csv

class DataObject:
    def __init__(self, id):
        ''' A default constructor for the class'''
        self.id = id
        self.num = 0
    
    def setId(self, arg):
        '''A setter for the variable'''
        self.id = arg
    
    def getId(self):
        '''A getter for the variable'''
        return self.id
    
    def __iter__(self):
        '''A function required to make the class iterable'''
        return self

    def __next__(self):
        ''' A function required to make the class iterable'''
        num = self.num
        self.num += 1
        return num
    
    def overrideMe(self):
        i = 'I am a return from the superclass.'
        return i

class CovidObject(DataObject):
    ''' A class for storing a CSV row in an object '''
    def __init__(self, id, date, cases, deaths, nameFrench, nameEnglish):
        super().__init__(id)
        ''' A default constructor for the class'''
        self.date = date
        self.cases = cases
        self.deaths = deaths
        self.nameFrench = nameFrench
        self.nameEnglish = nameEnglish
        
    def setId(self, arg):
        '''A setter for the variable'''
        self.id = arg
    def setDate(self, arg):
        '''A setter for the variable'''
        self.date = arg        
    def setCases(self, arg):
        '''A setter for the variable'''
        self.cases = arg
    def setDeaths(self, arg):
        '''A setter for the variable'''
        self.deaths = arg
    def setNameFrench(self, arg):
        '''A setter for the variable'''
        self.nameFrench = arg   
    def setNameEnglish(self, arg):
        '''A setter for the variable'''
        self.nameEnglish = arg   

    def getId(self):
        '''A getter for the variable'''
        return self.id
    def getDate(self):
        '''A getter for the variable'''
        return self.date       
    def getCases(self):
        '''A getter for the variable'''
        return self.cases
    def getDeaths(self):
        '''A getter for the variable'''
        return self.deaths
    def getNameFrench(self):
        '''A getter for the variable'''
        return self.nameFrench   
    def getNameEnglish(self):
        '''A getter for the variable'''
        return self.nameEnglish 
    
    def overrideMe(self):
        i = 'I am a subclass overriding a super class.'
        return i

class CovidList:
    '''A list as a class, for storing csv rows as objects'''
    def __init__(self):
        ''' A default constructor for the class'''
        self.caseList = []
        self.num = 0
    
    def __iter__(self):
        ''' A function required to make the class iterable'''
        return self.caseList[self.num]

    def __next__(self):
        ''' A function required to make the class iterable'''
        num = self.num
        self.num += 1
        return num

    def createList(self):
        '''A function to populate the list with csv data, and create the program's primary object'''
        self.caseList.clear()
        with open('InternationalCovid19Cases.csv', 'r') as csvFile:
            '''
            Starting file i/o in order to read data
            opening with read only privilege, 
            call the reader on the file, 
            create an empty list for storage
            '''
            csvReader = csv.DictReader(csvFile)

            for line in csvReader:
                '''
                create an object to store the row data, 
                append the object to the list, 
                rinse and repeat for each row of data
                '''
                case = CovidObject(line['id'], line['date'], line['cases'], line['deaths'], line['name_fr'], line['name_en']) 
                if case.getId() == '':
                    ''' error checking for empty values '''
                    case.setId('Missing Value')
                if case.getDate() == '':
                    ''' error checking for empty values '''
                    case.setDate('Missing Value')
                if case.getCases() == '':
                    ''' error checking for empty values '''
                    case.setCases('Missing Value')
                if case.getDeaths() == '':
                    ''' error checking for empty values '''
                    case.setDeaths('Missing Value')
                if case.getNameFrench() == '':
                    ''' error checking for empty values '''
                    case.setNameFrench('Missing Value')
                if case.getNameEnglish() == '':
                    ''' error checking for empty values '''
                    case.setNameEnglish('Missing Value')
                self.caseList.append(case)       
            csvFile.close()

