# -*- coding: utf-8 -*-
"""
Here will be all the code related to the view (screen)
"""

import POSController
import os

#Getting the inputs commands to show it to the user
InputCommands=POSController.GetInputCommand()
#Intializing the User choice value with empty string
UserChoice=""

"""
Desc: Gets the user choice of the operation he wants to perform
Param:
Return: string of the user input
"""
def GetUserChoice():
    InputStr=input("Please select an operation by writing the letter(s) in the brackets[]:")
    InputStr=InputStr.strip()
    POSController.CancelProgram(InputStr)
    return InputStr


"""
Desc: Print the welcome message to the screen with POS menu
Param:
Return:
"""
def WelcomeMessage():
    print("""
    \t\tWelcome to POS system\n
    POS Menu:""")
    for item in InputCommands:
        print("\t",InputCommands[item])
    print("\n")
    print("Note: if you want to exist the program at anytime type cancel\n")


"""
Desc: Main function of the program
Param:
Return:
"""
def main():
    WelcomeMessage()
    UserChoice=GetUserChoice()
    # FUCK PYTHON, for no reason the following line sometimes works and sometimes not
    #Fuck Python
    #while UserChoice.lower() not in (str(InputCommands.keys()).lower()):
    while UserChoice not in InputCommands.keys():
        print("\nWrong Selection!")     
        UserChoice=GetUserChoice()
    print("Your Selection was",InputCommands[UserChoice],"\n")
    ProceedWithUserSelection(UserChoice)
    return UserChoice


"""
Desc: Checking on the user input selection to start the appropriate process
Param: string of the user input to check on it
Return:
"""
def ProceedWithUserSelection(UserChoice):
    if UserChoice.lower()=="s":
        AddSales()
    elif UserChoice.lower()=="ac":
        AddCustomer()
    elif UserChoice.lower()=="d":
        CloseOfDay()
    elif UserChoice.lower()=="r":
        GenerateReport()
    elif UserChoice.lower()=="crm":
        GetCRM()
    elif UserChoice.lower()=="allc":
        GetAllCustomers()
    elif UserChoice.lower()=="q":
        print("\nThanks for using POS System\n")
    PressEnterToContinue()
    os.system('cls')

"""
Desc: Just to pause the program, was made to use after finishing each process
Param:
Return:
"""
def PressEnterToContinue():
    return input("Press Any Key to Continue!!")

"""
Desc: Add a new sale
Param: 
Return: 
"""
def AddSales():
    Article=GetArticleByID()
    print("\n")
    Customer=GetCustomerByID()
    print("\n")
    Quantity=GetQuantity()
    print("\n")
    Payment=GetPaymentType()
    print("\n")
    Status=POSController.AddSalesc(Article,Customer,Quantity,Payment)
    if Status=="Success":
        print("The Sale successfuly added for:")
        print("Article:",Article[1][0])
        print("Customer:",Customer[1])
        print("Quantity:",Quantity)
        print("Payment:",Payment)
        print("\n")
    else:
        print("Error: Sales couldn't be added")
"""
Desc: Takes the ID input from the user, whether this ID is for Artice or Customer etc..
Param: string of name of the item
Return: Item ID of type string
"""
def EnterID(Item):
    nstr="Please Enter the ID of the "+Item+" to sale: "
    InputStr=input(nstr)
    InputStr=InputStr.strip()
    POSController.CancelProgram(InputStr)
    while not InputStr.isnumeric():
        print("This is not a number")
        InputStr=input(nstr)
        POSController.CancelProgram(InputStr)
    return int(InputStr)
    
"""
Desc: print out that this item (Article or Customer, etc..) is not found
Param: string of name of the item
Return:
"""
def ItemNotFound(item):
    print("The ",item," wasn't found, please re-enter it again")

"""
Desc: Return the Article that the user wants
Param: 
Return: Article that the user wants
"""
def GetArticleByID():
    ArticleID=EnterID("Article")
    Article=POSController.GetArticleByIDc(ArticleID)
    while Article is None:
        ItemNotFound("Article")
        ArticleID=EnterID("Article")
    print("The Article that was choosed is ", Article[0]," and its price is ",Article[1])
    return (ArticleID,Article)

"""
Desc: Return the Customer that the user wants
Param: 
Return: Customer that the user wants
"""
def GetCustomerByID():
    CustomerID=EnterID("Customer")
    Customer=POSController.GetCustomerByIDc(CustomerID)
    while Customer is None:
        ItemNotFound("Customer")
        CustomerID=EnterID("Customer")
    print("The Customer that was choosed is ", Customer)
    return (CustomerID,Customer)


"""
Desc: Takes the quantity of sales from the user.
Param: 
Return: Quantity as string
"""
def EnterQuantity():
    InputStr=input("Please Enter the quantity:")
    InputStr=InputStr.strip()
    POSController.CancelProgram(InputStr)
    return InputStr
    

    
    
"""
Desc: Return the Quantity that the user wants
Param: 
Return: Quantity as interger number
"""
def GetQuantity():
    InputStr=EnterQuantity()
    while not InputStr.isnumeric():
        print("This is not a valid number, please enter a valid one")
        InputStr=EnterQuantity()
    while int(InputStr)<0:
        print("This is a negative number, please enter a valid positive number")
        InputStr=EnterQuantity()
    return int(InputStr)

"""
Desc: Takes the payment of sales from the user.
Param: 
Return: Payment as string
"""
def EnterPayment():
    nstr="Please choose the payment type "+ POSController.GetPaymentTypesc().__str__()+" :"
    InputStr=input(nstr)
    InputStr=InputStr.strip()
    POSController.CancelProgram(InputStr)
    return InputStr

"""
Desc: Return the Payment that the user wants
Param: 
Return: Payment as string
"""
def GetPaymentType():
    InputStr=EnterPayment()
    Payments=POSController.GetPaymentTypesc()
    while InputStr not in Payments:
        print("This is not a valid payment, please enter a valid one")
        InputStr=EnterPayment()
    return InputStr

"""
Desc: Takes the Customer Name from the user.
Param: 
Return: Customer Name as string
"""
def EnterCustomerName():
    CustomerName=input("Please Enter the Customer Name: ")
    CustomerName=CustomerName.strip()
    return CustomerName


"""
Desc: Adding New Customer
Param: 
Return:
"""
def AddCustomer():
    CustomerName=EnterCustomerName()
    while CustomerName=="":
        print("Wrong Entry")
        CustomerName=EnterCustomerName()
    NewCustomerID=POSController.AddCustomerc(CustomerName)
    if NewCustomerID>0:
        print("The Customer ",CustomerName," was successfuly added with new ID:",NewCustomerID)
    else:
        print("Error: Customer couldn't be added")

"""
Desc: Showing All Customers
Param: 
Return:
"""
def GetAllCustomers():
    print(POSController.GetAllCustomersc())
    
def GenerateReport():
    print(POSController.BuildReport())
#Launch the program
while UserChoice != "Q":
    UserChoice=main()