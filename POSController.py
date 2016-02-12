# -*- coding: utf-8 -*-
"""
Here will be all the code related to the Business Logic, Processes and checkings
"""

import POSModule
import sys


"""
Desc: check if the user entered the word cancel to exit theprogram
Param:
Return:
"""
def CancelProgram(Input):
    if Input.lower()=="cancel":
        sys.exit(0)

"""
Desc: Returns the payment types
Param:
Return: List of payment types.
"""
def GetPaymentTypesc():
    return POSModule.GetPaymentTypesm()

"""
Desc: Returns the input commands of the system that can be used by the user
Param: None
Return: Dictionary of input commands
"""
def GetInputCommand():
    return POSModule.GetInputCommands()
    
"""
Desc: Returns the wanted Article if found and if not found return Nothing
Param: Article ID of type Integer
Return: Wanted Article or None
"""
def GetArticleByIDc(ArticleID):
    return POSModule.GetArticleByIDm(ArticleID)
    
"""
Desc: Returns the wanted Customer if found and if not found return Nothing
Param: Customer ID of type Integer
Return: Wanted Customer or None
"""
def GetCustomerByIDc(CustomerID):
    return POSModule.GetCustomerByIDm(CustomerID)
    
"""
Desc: Adds new Sale to the Sales
Param: 
    ArticleID: ID of the Article
    CustomerID: ID of the Customer who bought the Article
    Quantity: Number of Articles bought
    Payment: string of the payment type
    Payment: is the payment done by the customer
Return: Success string if Operation is done
"""
def AddSalesc(Article,Customer,Quantity,PaymentType):
    return POSModule.AddSalesm(Article[0],Customer[0],Quantity,PaymentType,Quantity*Article[1][1])
    
"""
Desc: Adds new Customer
Param: Customer Name
Return: Customer ID
"""
def AddCustomerc(CustomerName):
    return POSModule.AddCustomerm(CustomerName)

"""
Desc: Getting All Customers
Param: 
Return: All Customers
"""
def GetAllCustomersc():
    return POSModule.GetAllCustomersm()

"""
Desc: Getting All Sales
Param: 
Return: All Sales
"""
def GetAllSalesc():
    return POSModule.GetAllSalesm()
    
def BuildReport():
    DaySales=POSModule.GetAllSalesm()
    AllCustomers=POSModule.GetAllCustomersm()
    AllArtiles=POSModule.GetAllArticlesm()
    newlist=[]
    for item in DaySales:
        newlist.append((AllArtiles[item[0]][0],AllCustomers[item[1]],item[2],item[3],item[4]))
    return newlist