#Q1. Explain OOPS principles with code examples to demonstrate them ?
#Ans -OOps principal consists of 4 basic principals :-
#1- Inheritance:-
#Inheritance is the most important aspect of object-oriented programming, which simulates the real-world
#concept of inheritance. It specifies that the child object acquires all the properties and behaviors of
#the parent object.
#By using inheritance, we can create a class which uses all the properties and behavior of another class.
#The new class is known as a derived class or child class, and the one whose properties are acquired is 
#known as a base class or parent class.It provides the re-usability of the code.
#example code :-

class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
##Output :-
#Bird is ready
#Penguin is ready
#Penguin
#Swim faster
#Run faster
#2- Encapsulation :-
#Encapsulation is also an essential aspect of object-oriented programming. It is used to restrict access 
#to methods and variables. In encapsulation, code and data are wrapped together within a single unit from
#being modified by accident.
#code example :-

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

#c = Computer()
#c.sell()

#c.__maxprice = 1000
#c.sell()

#c.setMaxPrice(1000)
#c.sell()
##Output :-
#Selling Price: 900
#Selling Price: 900
#Selling Price: 1000
#3- Data Abstraction:-
#Data abstraction and encapsulation both are often used as synonyms. Both are nearly synonyms because 
#data abstraction is achieved through encapsulation.
#Abstraction is used to hide internal details and show only functionalities. Abstracting something means
#to give names to things so that the name captures the core of what a function or a whole program does.
#code example :-
import abc 
  
class parent:        
    def geeks(self): 
        pass
  
class child(parent): 
    def geeks(self): 
        print("child class") 

#print( issubclass(child, parent)) 
#print( isinstance(child(), parent)) 
#Output:
#True
#True
#4- polymorphism :-
#Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape.
#By polymorphism, we understand that one task can be performed in different ways. For example - you have
#a class animal, and all animals speak. But they speak differently. Here, the "speak" behavior is 
#polymorphic in a sense and depends on the animal. So, the abstract "animal" concept does not 
#actually "speak", but specific animals (like dogs and cats) have a concrete implementation of the
#action "speak".
#code :-

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

def flying_test(bird):
    bird.fly()

blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)

#Output :-
#Parrot can fly
#Penguin can't fly