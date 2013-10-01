#!/usr/bin/python
import csv,os, sys

def getMaxShare(line, fields):
      yearMonth=line[2:len(line)]
      return line[0],line[1],max(yearMonth), "     " + fields[line.index(max(yearMonth))]

summaryList=[]

# Function to parse the CSV file to get the heighest share prices of each company per month and year
def processCSVFile(inFile):
    pass #Calculate maximum share for all companies based on year and date
    try:
      	infile=open("test.csv","rb")
      	rows=csv.reader(infile)
        print "YEAR","MONTH", "HI-SHARE", "COMPANY NAME"
      	rownum=0
      	for row in rows:
           #Save header now
           if rownum == 0:
           	fieldnames = row
           else:
                if (len(row)<1): 
                  continue
                else :
                    record=getMaxShare(row, fieldnames); 
                    summaryList.append(record)
           rownum = rownum  + 1
        if rownum <=1:
            print "ERROR:", "EMPTY FILE, NO DATA IN CSV FILE"
    except IOError as e:
       		print "ERROR:", e
    finally:
    	infile.close()
    return 1

returnValue=processCSVFile("test.csv")
if (returnValue!= 1):
   print "ERROR:", "in processing CSV File"

for list in summaryList:
    print ','.join(list)
