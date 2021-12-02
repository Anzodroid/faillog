#!/bin/env python3

import sys
import re 
import datetime 
import os

from datetime import datetime

try:
    option = str(sys.argv[1]) # 1st Argument

    if(option == "-v"):

            file = str(sys.argv[2]) # 2nd Argument
            if (len(sys.argv) == 3):
        
                if (os.access(file, os.R_OK) & os.access(file, os.F_OK) & os.path.isfile(file)):
                    print("Michael Anziliero : 11126570 : 22/05/2021")
                else:
                    sys.exit("Sorry the file you have entered appears to be invalid")    
            else:
                sys.exit('Sorry, Please check you have supplied the correct number of arguments')

    elif(option == "-a"):
            
        file = str(sys.argv[2]) # 2nd Argument
        if (os.access(file, os.R_OK) & os.access(file, os.F_OK) & os.path.isfile(file)):
            if (len(sys.argv) == 3):
                with open(file, "r") as f:
                    count = len(f.readlines())
                    if (count == 0):
                        print("No usernames found")
                    else: 
                        user = []
                        with open(file, "r") as f:
                            data = f.readlines()
                            for line in data:
                                line = line.rstrip('\n')
                                x = line.split()[0]
                                if x:
                                    user.append(x)
                        userlist = [] 
                        for e in user:
                            if e not in userlist:
                                userlist.append(e)
                        print("Usernames:")
                        for e in userlist:
                            print(e, end="\n")                           
            else:
                sys.exit('Sorry, Please check you have supplied the correct number of arguments')  
        else:
            sys.exit("Sorry the file you have entered appears to be invalid")

    elif(option == "-u"):

        if (len(sys.argv) ==4):
            file = str(sys.argv[3]) # 3rd Argument

            if (os.access(file, os.R_OK) & os.access(file, os.F_OK) & os.path.isfile(file)):
                    name = str(sys.argv[2]) # 2nd Argument 
                    nameRe = str("^"+name+"\s+")
                    regexMatch = []
                        
                    with open(file, "r") as f:
                        data = f.readlines()
                        
                    for line in data:
                        line = line.rstrip('\n')
                        x = re.search(nameRe,line)
                        if x:
                            regexMatch.append(x)
                    count = len(regexMatch)
                        
                    if (count == 0):
                        print("No events found for the given username")
                        
                    else: 
                        with open(file, "r") as f:
                            data = f.readlines()
                        print("Events for user: " + name)
                        for line in data:
                            line = line.rstrip('\n')
                            x = re.search(nameRe,line)
                            if x:         
                                print(line)
            else:
                sys.exit("Sorry the file you have entered appears to be invalid")
        else:
            sys.exit('Sorry, Please check you have supplied the correct number of arguments')

    elif(option == "-t"):

        if (len(sys.argv) ==5):
            dateString = str(sys.argv[2]) # 2nd Argument 
            timeString = str(sys.argv[3]) # 3rd Argument 
            file = str(sys.argv[4]) # 4th Argument 
            if (os.access(file, os.R_OK) & os.access(file, os.F_OK) & os.path.isfile(file)):
                with open(file, "r") as f:
                    count = len(f.readlines())
                    if (count == 0):
                        print("No events found for the given date/time")
                    else: 
                        dateTimeString = dateString + " " +timeString
                        dateInput = datetime.strptime(dateTimeString, '%d/%m/%Y %H:%M:%S')
                        dateSplit = str(" ")
                        dataList = []
                        trueFalse = []
                        dateMatch = []
                        timeLast = []
                        timelist = []
                        dateTimeConversion = []
                        dateCheck = []

                        with open(file, "r") as f:
                            data = f.readlines()
                            count = len(f.readlines())
                            for line in data:
                                line = line.rstrip('\n')
                                timeLast.append(line[-19:])
                            
                            for line in timeLast:
                                line = line.rstrip('\n')
                                x = datetime.strptime(line, '%d/%m/%Y %H:%M:%S')
                                dateTimeConversion.append(x)

                            for line in dateTimeConversion:
                                    dateCheck.append(dateInput)
                            
                            for i in range(len(dateCheck)):
                                if (dateCheck[i] <= dateTimeConversion[i]):
                                    trueFalse.append("True")
                                else:
                                    trueFalse.append("False")

                            with open(file, "r") as f:
                                data = f.readlines()
                                for line in data:
                                    line = line.rstrip('\n')
                                    dataList.append(line)
                        
                            for i in range(len(data)):
                                if (trueFalse[i] == "True"):
                                    print(dataList[i])
            else:
                sys.exit("Sorry, the file you have entered appears to be invalid")
        else:
            sys.exit("Sorry, please ensure you select a date (dd/mm/yyyy), a time (hh/mm/ss) and a valid file")
    else: 
        sys.exit("Sorry, the option you have selected is invalid")
except IndexError:
    sys.exit("Sorry, please ensure you have selected a valid option and file")
