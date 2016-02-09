# -*- coding: utf-8 -*-
"""
Here will be all the code related to ou data, Add, Update, Delete, and Get
"""

#Dictionary of Articles
Articles={
          1: ("Book: Lean Analytics",100),
          2: ("Book: Lean Start-Up",200),
          3: ("Book: Data Mining",300),
          4: ("Book: Why Nations Fail",400),
          5: ("Book: Getting to Yes",500),
          6: ("Music: Passion Pit",600)
          }

#Dictionary of customers
Customers={1: "Rahul",
           2: "Xuan",
           3: "Carlos",
           4: "Ahmed",
           5: "Gaille"}

#List of Lists of sales (ArticleID, CustomerID, Quantity, Cash or Credit, Payment)
Sales=[
    [1,1,10,"cash",1000],
    [1,2,10,"credit",2000],
    [2,1,10,"cash",1000],
    [2,1,10,"credit",1000],
    [2,3,10,"cash",3000],
    [2,3,10,"credit",3000]
        ]


#List with allowed payment methods
PaymentMethod=["cash","credit"]

#Choices of inputs to the console that can be done by the user
InputCommand={"S":"[S] Add a sale",
         "R":"[R] Generate Report",
         "CRM":"[CRM] CRM",
         "D":"[D] Close of Day",
         "AC":"[AC] Add New Customer",
         "Q":"[Q] Quit",
         "AllC":"[AllC] Show All Customers"
         }


"""
Desc: Returns the payment types
Param:
Return: List of payment types.
"""
def GetPaymentTypesm():
    return PaymentMethod

"""
Desc: Returns the input commands of the system that can be used by the user
Param:
Return: Dictionary of input commands
"""
def GetInputCommands():
    return InputCommand

"""
Desc: Returns the wanted Article if found and if not found return Nothing
Param: Article ID of type Integer
Return: Wanted Article or None
"""
def GetArticleByIDm(ArticleID):
    return GetItemByID(ArticleID,Articles)
    
"""
Desc: Returns the wanted Customer if found and if not found return Nothing
Param: Customer ID of type Integer
Return: Wanted Customer or None
"""
def GetCustomerByIDm(CustomerID):
    return GetItemByID(CustomerID,Customers)


"""
Desc: Returns the wanted generic item if found and if not found return Nothing
Param: Generic Item ID of type Integer
Return: Wanted Item or None
"""
def GetItemByID(ItemID, Items):
    if ItemID in Items:
        return Items[ItemID]
    return None #this will be executed if the if condition is false


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
def AddSalesm(ArticleID,CustomerID,Quantity,PaymentType,Payment):
    Sales.append((ArticleID,CustomerID,Quantity,PaymentType,Payment))
    return "Success"
    

"""
Desc: Adds new Customer
Param: Customer Name
Return: Customer ID
"""
def AddCustomerm(CustomerName):
    NewID=len(Customers)+1
    Customers[NewID]=CustomerName
    return NewID
    
"""
Desc: Getting All Customers
Param: 
Return: All Customers
"""
def GetAllCustomersm():
    return Customers


"""
Desc: Getting All Sales
Param: 
Return: All Sales
"""
def GetAllSalesm():
    return Sales
    
"""
Desc: Getting All Articles
Param: 
Return: All Articles
"""
def GetAllArticlesm():
    return Articles
    