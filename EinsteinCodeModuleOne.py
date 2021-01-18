# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:48:32 2020

@author: yasmi
"""
import json
from json import JSONEncoder

import pymongo 
from pymongo import MongoClient

from bson.binary import Binary
import pickle

import bcrypt

from getpass import getpass
from pymongo import MongoClient

import tkinter 

import constraint
from constraint import *
from constraint import Problem

              
def verifiyingMongopassword():   
    client =  MongoClient("localhost", 27017)
    return client

    #The code below is storing the username and password in mongoDB.
    #Try & except is for exception handling. Python will stop running code if an error occurs.
    #getpass Prompts the user to enter a password without echoing. But if not available (mine) a default warning message will appear in console.
    #The password is encoded so that only an authorized person can read it with a corresponding Key.
    #Hashed password is created with bcrypt.hashpw() taking cleartext and salt as an argument.
    #Password is NOT stored as plaintext in my database but in hashed values.
    #Hashed password ensures security, turning the password into another string. This is a one way transformation, cannot see the plaintext password.
    #Salt creates unquie hashes for every user input.
    
try: #try block lets you test a block of code for errors
    user_data = {}
    print("Hi before you can use MongoDB to please enter your username and password")
    user_data["Username"] = input("Username:   ")
    password = getpass(prompt="Password:  ").encode('utf-8')  #utf-8 One of the most commonly used encodings 
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt) #creating a hash password
    user_data["Password"] = hashed_password 
    client = verifiyingMongopassword()
    db = client.security # database called 'security'
    collection = db.AuthenticationMongoDB  # username and password hash stored in this collection
    result = collection.insert_one(user_data)  # insert the user data into the collection
    print("username and password stored in database")
except Exception as e:
      print("Exception:",e) #Let's us handle the error 

#Checking user password against hash value
password = user_data["Password"]
hashed = bcrypt.hashpw(password, bcrypt.gensalt() )
print(hashed) # The hashed password 

#compare hash password in DB with cleartext password
if bcrypt.checkpw(password, hashed):
    print("Passwords match!, continue to MongoDB")    
else:
    ("It didn't match, please try again.")


#MongoDB 
client = MongoClient("localhost", 27017) #Establishing conntection, 27017 = port-number
db = client['datacampdb']  #creating a database
coll = db.einsteinCollection  #creating a collection in the database

#class Person contains a list of the nationalities in the riddle 
#nationality has a double underscore making it a private variable
class Person:
    def __init__(self, nationality = []): # __init__ A constructor class. self = the instance of the object 
        self.__nationality = []
        
    # My getters and setters to ensure encapsulation    
    def set_nationality(self, nationality): #used to set the values in the private variable
          self.__nationality  = nationality
    def get_nationality(self): #used to access the private variable outside the class
        return self.__nationality

 
personone = Person()  #creating an instance of my person class
personone.set_nationality(["Brit", "German", " Danish", " Swedish", " Norwegian"])

            
class PersonEncoder(JSONEncoder):  #converting class object into JSON
        def default(self, o):
            return o.__dict__
    

#Encode Person Object into JSON
personJson = json.dumps(personone.get_nationality(), indent=4, cls=PersonEncoder) #json.dumps() converting object into json string
personData = pickle.dumps(personJson) #python pickle used to serialize. Object data is stored in DB using pickle.dump() < put the object you want to store in the parameters
coll.insert_one({'bin-data': Binary(personData)}) #inserting data in mongoDB

print(personJson) #prints the JSON 
#print(db.list_collection_names()) #get then names of my collections in DB 
 
#retriving data from mongodb - Retrieving a Single Document with find_one()
print(coll.find_one({'bin-data': Binary(personData)})) 
# Above code means Find a document in the collection coll where bin-data is equal to Binary(personData)

#Repeat above code with the other classes. 
class Drink :
    def __init__(self, drink = []):
        self.__drink = []
        
    def set_drink(self, drink):
          self.__drink  = drink
    def get_drink(self):
        return self.__drink
    
drinkone = Drink()
drinkone.set_drink(["Water", "Tea", "Milk", " Coffee", " Beer"])

class DrinkEncoder(JSONEncoder): 
        def default(self, o):
            return o.__dict__

drinkJson = json.dumps(drinkone.get_drink(), indent=4, cls=DrinkEncoder)
drinkData = pickle.dumps(drinkJson)
coll.insert_one({'bin-data': Binary(drinkData)})

print(drinkJson)
print(coll.find_one({'bin-data': Binary(drinkData)})) 


class Pet :
    def __init__(self, pet =[]):
        self.__pet = []
        
    def set_pet(self, pet):
          self.__pet  = pet
    def get_pet(self):
        return self.__pet
    
petone = Pet()
petone.set_pet(["Cats", "Horses","Birds"," Fish", " Dogs"])


class PetEncoder(JSONEncoder): 
        def default(self, o):
            return o.__dict__

petJson = json.dumps(petone.get_pet(), indent=4, cls=PetEncoder)
petData = pickle.dumps(petJson)
coll.insert_one({'bin-data': Binary(petData)})

print(petJson)
print(coll.find_one({'bin-data': Binary(petData)})) 

class House :
    def __init__(self, colour = []):
        self.__colour = []
        # self.__number = []
        
    def set_colour(self, colour):
          self.__colour  = colour
    def get_colour(self):
        return self.__colour
    
    # def set_number(self, number):
    #       self.__number  = number
    # def get_number(self):
    #     return self.__number
    
colourone = House()
colourone.set_colour(["Yellow", " Blue", " Red", " Green", " White"])

# numberone = House()
# numberone.set_number(1,2,3,4,5) 


class HouseEncoder(JSONEncoder): 
        def default(self, o):
            return o.__dict__

#colour data
colourJson = json.dumps(colourone.get_colour(), indent=4, cls=HouseEncoder)
colourData = pickle.dumps(colourJson)
coll.insert_one({'bin-data': Binary(colourData)})

print(colourJson)
print(coll.find_one({'bin-data': Binary(colourData)})) 

# #number data 
# numberJson = json.dumps(numberone.get_number(), indent=4, cls=HouseEncoder)
# numberData = pickle.dumps(numberJson)
# coll.insert_one({'bin-data': Binary(numberData)})

# print(numberJson)
# print(coll.find_one({'bin-data': Binary(numberData)})) 

class Smoke_brand :
    def __init__(self, smoke =[]):
        self.__smoke = []
        
    def set_smoke(self, smoke):
          self.__smoke  = smoke
    def get_smoke(self):
        return self.__smoke
    
smokeone = Smoke_brand()
smokeone.set_smoke(["PallMall", " Dunhill", " Blends", " BlueMaster", " Prince"])

class SmokeEncoder(JSONEncoder): 
        def default(self, o):
            return o.__dict__

smokeJson = json.dumps(smokeone.get_smoke(), indent=4, cls=SmokeEncoder)
smokeData = pickle.dumps(smokeJson)
coll.insert_one({'bin-data': Binary(smokeData)})

print(smokeJson)
print(coll.find_one({'bin-data': Binary(smokeData)})) 


#Storing and retriving my 12 hints from MongoDB  
class Hints:
    def _init_(self, hint = []):
        self.__hint = hint
    
    def set_hint(self, hint):
        self.__hint = hint 
    def get_hint(self):
        return self.__hint
    
    # def add_hints(self, hints):  
    #     self.__hint.append(hints)
    # def get_hints(self, index):
    #     return self.__hint[index]
    
hintOne = Hints()
hintOne.set_hint(["Brit", "Red"])

hintTwo = Hints()
hintTwo.set_hint(["Swedish", "Dog"])

hintThree = Hints()
hintThree.set_hint(["Danish", "Tea"])

hintFour = Hints()
hintFour.set_hint(["Green", "White"])

hintFive = Hints()
hintFive.set_hint(["Green", "Coffee"])

hintSix = Hints()
hintSix.set_hint(["PallMall", "Birds"])

hintSeven = Hints()
hintSeven.set_hint(["Yellow", "Dunhill"])

hintEight = Hints()
hintEight.set_hint(["Center", "Milk"])

hintNine = Hints()
hintNine.set_hint(["Norweigen", "One"])

hintTen = Hints()
hintTen.set_hint(["Blends", "Cats"])

hint11 = Hints()
hint11.set_hint(["Horses", "Dunhill"])

hint12 = Hints()
hint12.set_hint(["Bluemaster", "Beer"])

hint13 = Hints()
hint13.set_hint(["German", "Prince"])

hint14 = Hints()
hint14.set_hint(["Norwegin", "Blue"])



class HintsEncoder(JSONEncoder): 
        def default(self, o):
            return o.__dict__

hintJson = json.dumps(hintOne.get_hint(), indent=4, cls=HintsEncoder)
hintData = pickle.dumps(hintJson)
coll.insert_one({'bin-data': Binary(hintData)})

print(hintJson)
print(coll.find_one({'bin-data': Binary(hintData)})) 

        
 
#Username and password stored and hashpassword + the user input (cleartext password) is compared to access programe
       
def solvingPuzzel():   
    client =  MongoClient("localhost", 27017)
    return client

try:
    user_data2 = {}
    print("Hi before you can use the puzzel Programe to please enter your username and password")
    user_data2["Username"] = input("Username:   ")
    password = getpass(prompt="Password:  ").encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password, salt)
    user_data2["Password"] = hash_password
    client = solvingPuzzel()
    db = client.security
    collection = db.AuthenticationPrograme
    result = collection.insert_one(user_data2)  # username and password hash stored in MongoDB
    print("username and password stored in database")
except Exception as e:
      print("Exception:",e)

 
password = user_data2["Password"]
hashed = bcrypt.hashpw(password, bcrypt.gensalt() )

print(hashed) # this is our hashed password

#compare hash password in DB with plain text password
if bcrypt.checkpw(password, hashed):
    print("Passwords match, you can continue to the programe!")    
else:
    ("It didn't match, please try again.")    
 


 
class puzzle_GUI:
    def __init__(self):
        #Main window 
        self.mw = tkinter.Tk()
        #Set the title of the main window
        self.mw.title("Puzzle Solver")
        
        #Frames in the main window that will group diffrent widgets
        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)
           
        #Widgets for the top frame
        self.question_label = tkinter.Label(self.top_frame, text = "Who owns the fish?")
        
        self.result = tkinter.StringVar()
        
        #Label that will be used to display the answer to the riddle 
        self.result_label = tkinter.Label(self.bottom_frame, textvariable = self.result)
        
        #Pack the widgets for middle frame
        self.question_label.pack(side = "left")
        self.result_label.pack(side = "left")
        
        #Widgets for the bottom frame
        #Used bg to make the buttons different colour 
        self.solve_button = tkinter.Button(self.mid_frame, text = "Solve Puzzle", bg = "green", command = self.solve_puzzle)
        self.quit_button = tkinter.Button(self.mid_frame, text = "Quit", bg = "red", command = self.mw.destroy)
        
        #pack the buttons for bottom window
        self.solve_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        #pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
      
        tkinter.mainloop() #Tells python to run the tkinter event loop 

    def solve_puzzle(self):
         
        problem = constraint.Problem()  #This is a function from the constraint class
        #class used to define a problem and retrive solutions 
        #A type of declarative programming - used to describe the goal and the computer gives a solution 
        
        #My instances from my variable classes above
        personone = Person() 
        colourone = House()
        smokeone = Smoke_brand()
        petone = Pet()
        drinkone = Drink()
        
        #defining our constraints 
        personone = ["Brit", "German", "Danish", "Swedish", "Norwegian"]
        colourone = ["Yellow", "Blue", "Red", "Green", "White"]
        smokeone = ["PallMall", "Dunhill", "Blends", "BlueMaster", "Prince"]
        petone = ["Cats", "Horses","Birds", "Fish", "Dogs"]
        drinkone = ["Water", "Tea", "Milk", "Coffee", "Beer"]
        
        rules = personone + colourone + smokeone + petone + drinkone # setting my criteria in 'rules'
        problem.addVariables(rules,[1,2,3,4,5]) #addVariables to the problem
        #Line of code above is saying i'm adding all my variables and they can have the values of 1-5 (be in houses 1 to 5)
        
        problem.addConstraint(AllDifferentConstraint(), personone) # Adding my person list (constraint) to the problem
        problem.addConstraint(AllDifferentConstraint(), colourone)
        problem.addConstraint(AllDifferentConstraint(), smokeone)
        problem.addConstraint(AllDifferentConstraint(), petone)
        problem.addConstraint(AllDifferentConstraint(), drinkone)
        
        # A constraint is a limitation that must be adhered to in regards to the hints/rules in the riddle 
        #Adding the hints to the problem 
        #lambda is an anonymous function. The lambda expression is made by using lamda followed by your inputs
        #How to create a lambda expression = lambda input1, input2: one expression (the return value)
        problem.addConstraint(lambda a, b: a == b,["Brit", "Red"]) #variable brit and variable red belong in the same house
        problem.addConstraint(lambda a, b: a == b,["Swedish", "Dogs"])
        problem.addConstraint(lambda a, b: a == b,["Brit", "Red"])
        problem.addConstraint(lambda a, b: a == b,["Green", "Coffee"])
        problem.addConstraint(lambda a, b: a == b,["Danish", "Tea"])
        problem.addConstraint(lambda a, b: a == b +1 ,["Green", "White"]) #Green house is on the left of the white house , hence +1
        problem.addConstraint(lambda a, b: a == b,["PallMall", "Birds"])
        problem.addConstraint(lambda a, b: a == b,["Dunhill", "Yellow"])
        problem.addConstraint(lambda a: a == 3, ["Milk"    ]) #variable Milk belonds in the middle house (house 3)
        problem.addConstraint(lambda a: a == 1, ["Norwegian"  ]) #Norwegian lives in the 1st house, hence =1
        problem.addConstraint(lambda a, b: a == b - 1 or a == b + 1, ["Blends", "Cats"]) #The man who smokes Blends lives next to the man who keeps cats. Next to could be left (+1) or right (-1)
        problem.addConstraint(lambda a, b: a == b - 1 or a == b + 1, ["Dunhill", "Horses" ])#The man who smokes Dunhill lives next to the man who keeps horses. Next to could be left (+1) or right (-1)
        problem.addConstraint(lambda a, b: a == b, ["BlueMaster","Beer"])
        problem.addConstraint(lambda a, b: a == b, ["German", "Prince"])
        problem.addConstraint(lambda a, b: a == b - 1 or a == b + 1, ["Norwegian", "Blue"]) #The norwegian lives next to the blue house
        
        solution = problem.getSolution()  #problem.getSolution() is a function from constraint class, to find a solution to the problem
        
        for i in range(1,6):   #for loop - loops through the values 1-5
            for x in solution: # x = our variables 
                if solution[x] == i:  #if the solution to our variables = i (The house numbers)
                      print (str(i), x) #print the house number and the variable it belongs to 
        #Fish = House 5, German = House 5. Therefore the German owns the fish 
        self.result.set(solution) #To print the answer in GUI
                          
gui = puzzle_GUI()
        