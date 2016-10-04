# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 22:03:26 2016

@author: Angel Maredia
"""

import unittest
import fileReadWrite
import os

class TestFileReadWrite(unittest.TestCase):
    
    def test_addName(self):
        #Opens file, adds names to file for testing
        file = open("test.txt", 'w+')
        names = ["angel","laura","harambe"]
        for name in names:
            fileReadWrite.addName(name, "test.txt")

        #iterates through file, checking to make sure input matches file
        namesIndex=0
        for line in file:
            line = line.rstrip();
            self.assertEqual(line, names[namesIndex])
            namesIndex = namesIndex+1
        

        file.close()
        os.remove("test.txt")
        
    def test_listOfNames(self):
        names = ["angel","laura","harambe"]
        for name in names:
            fileReadWrite.addName(name, "test.txt")
        
        namesList = fileReadWrite.listOfNames("test.txt")
        self.assertEquals(namesList, names)
        
        os.remove("test.txt")
        
            
if __name__ == '__main__':
    unittest.main()