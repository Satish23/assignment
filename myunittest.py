#!/usr/bin/python
import unittest, sys
import  summary

class SharePrices(unittest.TestCase):
     def 	setUp(self):
         		pass
                   
     def 	TestMaxSharePrice(self):
         		fields=["YEAR","MONTH","CMP1","CMP2","CMP3","CMP4","CMP5"]
         		li=[1990,"Jan",20,13,40,22,12]
         		pass #Test Case for MAX Share price calculation
returnString = summary.getMaxShare(li, fields)
self.failIf( len(returnString) == 0 )
                      
def 	TestprocessCSVFile(self):
         		pass #Test Case for processCSVFile API with -v option and -f option
returnString = summary.processCSVFile("test.csv")
self.failIf( returnString != 1 )

if __name__ == '__main__':
   unittest.main()
