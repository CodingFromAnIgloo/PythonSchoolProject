# Assignment 4 for CST8333
# Written by Eric Bonvie
# A MVC program for manipulating csv data
# October 28, 2020

import bonvieEricModel
import bonvieEricView

def main():
    '''A function to serve as the bootup for the program'''
    model = bonvieEricModel.CovidList()
    view = bonvieEricView.UI()

    model.createList()
    view.header()
    view.menu()
    view.clicker(model)
    
if __name__ == '__main__':
    '''A standard python function for your primary bootup file'''
    main()