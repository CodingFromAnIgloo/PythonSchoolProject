# Assignment 4 for CST8333
# Written by Eric Bonvie
# A MVC program for manipulating csv data
# October 28, 2020

import unittest 
import bonvieEricModel
  
class SimpleTest(unittest.TestCase): 
    '''A simple proof of concept unit test'''

    def test_getter(self):
        '''A simple proof of concept unit test, testing a standard getter function'''
        caseA = bonvieEricModel.CovidObject('id', 'date', 'cases', 'deaths', 'name_fr', 'name_en')
        caseB = bonvieEricModel.DataObject('id')
        testerA = caseA.overrideMe()
        testerB = caseB.overrideMe()
        self.assertNotEqual(testerA, testerB) 
  
if __name__ == '__main__':
    '''A method that allows the tests to be run from the console''' 
    unittest.main() 