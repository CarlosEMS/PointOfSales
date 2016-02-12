# -*- coding: utf-8 -*-
"""
Here will be all the code related to the view (screen)
"""

import POSController
import os

#Getting the inputs commands to show it to the user
#InputCommands=POSController.GetInputCommand()
#Intializing the User choice value with empty string
UserChoice=""


"""
Desc: Main function of the program
Param:
Return:
"""
def main():
    WelcomeMessage()
    UserChoice=GetUserChoice()
    newchoice=[]
    Status=POSController.ProceedWithUserSelection(UserChoice,newchoice)
    UserChoice=newchoice[0]
    if Status=="Report":
        ShowReport(POSController.PrepareReport())
    elif Status=="CRM":
        ShowCRM(POSController.PrepareCRM())
    else:
        print(Status)
    PressEnterToContinue()
    os.system('cls')
    return UserChoice

"""
Desc: Print the sales amount Report
Param:
Return:
"""
def ShowReport(ReportList):
    print("\nThe Sales Amount Report Broken down by payment type:")
    for item in ReportList:
        if item[0]=="Cash":
            print("Cash Sales Amount: ",item[1])
        else:
            print("Credit Sales Amount: ",item[1])


"""
Desc: Print the CRM Report
Param:
Return:
"""
def ShowCRM(CRMDictionary):
    print("\nCRM Report:")
    for item in CRMDictionary.keys():
        print("Customer: ",item," made sales of ",CRMDictionary[item])

"""
Desc: Print the welcome message to the screen with POS menu
Param:
Return:
"""
def WelcomeMessage():
    print("""
    \t\tWelcome to POS system\n
    For adding sales, please use one of the following examples
    (1) Sale #Amount# – Cash sale of that amount number, i.e. Sale 1000
    (2) Sale #SKU:number – Sale of a item in stock, i.e. Sale SKU:10
    (3) Sale #Amount# #CC# - Credit card sales, i.e. Sale 1000 CC
    (4) Sale #Amount# #ID:9alfanumeric – Sale to a registered customer, i.e. Sale 90 ID:213dhj
    
    For adding new customer:
    Customer name ID:9alfanumeric” – New customer, i.e. Customer Peter ID:19beta
    
    For Close of Sales Day, just write Close day
    To Print sales for the day , write Report
    To print breakdown of sales for the day by client, write CRM
    To quit the menu, write quit
    """)
    print("Note: if you want to exist the program at anytime type cancel\n")


"""
Desc: Gets the user choice of the operation he wants to perform
Param:
#InputStr=InputFromUser("Please enter the operation you want to perform: ")
Return: string of the user input
"""
def GetUserChoice():
    InputStr=InputFromUser("Please enter the operation you want to perform: ")
    POSController.CancelProgramCheck(InputStr)
    return InputStr


"""
Desc: Gets the user input and trim the white spaces 
Param:
Return: string of the user input
"""
def InputFromUser(Msg):
    InputStr=input(Msg)
    InputStr=InputStr.strip() #Removing white spaces on left or right of the whole string
    return InputStr
    
"""
Desc: Print the message to the user, this was made to encapsulate the print command,
    so controller can call this function without caring how actually the print is done
Param:
Return: 
"""
def PrintToUser(Msg):
    return print(Msg)
    
"""
Desc: Just to pause the program, was made to use after finishing each process
Param:
Return:
"""
def PressEnterToContinue():
    return input("Press Enter to Continue!!")

    
"""
Desc: print out that this item (Article or Customer, etc..) is not found
Param: string of name of the item
Return:
"""
def ItemNotFound(item):
    print("The ",item," wasn't found, please re-enter it again")

