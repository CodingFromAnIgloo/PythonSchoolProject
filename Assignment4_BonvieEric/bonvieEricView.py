# Assignment 4 for CST8333
# Written by Eric Bonvie
# A MVC program for manipulating csv data
# October 28, 2020

import os
import bonvieEricModel
import bonvieEricController
import runMe
import time

class UI:
    '''A class to create a makeshift U/I via the terminal'''
    def __init__(self):
        '''A standard constructor method for python classes'''
        self.id = 1   
    
    def header(self):
        '''A function for clearing the erminal and printing the header'''
        os.system('cls')
        print('This is a program demonstration')
        print('Written by Eric Bonvie')
 
    def menu(self):
        '''A function for displaying menu options'''
        print('Please select an option')
        print('1: Reload Data')
        print('2: Save Data')
        print('3: Print all Entries')
        print('4: Add An Entry')
        print('5: Edit An Entry')
        print('6: Delete An Entry')
        print('7: Print a custom list of entries (Assignment 4 search function)')
    
    def clicker(self, obj):
        '''How the UI passes data to the controller. Could also have been reasonably placed in the controller file.'''
        controller = bonvieEricController.Navigation()
        model = obj
        
        try:
            '''A user prompt for input'''
            choice = int(input("What would you like to do?:"))
        except ValueError:
            '''Error catching'''
            print("That is not a valid selection. Go away.")
            quit()
    
        if  choice == 1: 
            '''Menu option 1'''
            runMe.main()
        elif choice == 2 : 
            '''Menu option 2'''
            controller.saveList(model)
        elif choice == 3 : 
            '''Menu option 3'''
            controller.printList(model)
        elif choice == 4 : 
            '''Menu option 4'''
            controller.addEntry(model)
            time.sleep(2)
            self.menu()
            self.clicker(model)
        elif choice == 5 : 
            '''Menu option 5'''
            controller.editEntry(model)
            time.sleep(2)
            self.menu()
            self.clicker(model)
        elif choice == 6 : 
            '''Menu option 6'''
            controller.deleteEntry(model)
            time.sleep(2)
            self.menu()
            self.clicker(model)
        elif choice == 7 : 
            '''Menu option 7'''
            controller.searchList(model)
        else : 
            '''More error catching'''
            print("That is not a valid selection. Go away.")
            quit()

