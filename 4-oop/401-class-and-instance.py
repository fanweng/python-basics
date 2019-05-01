#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
401-class-and-instance.py
'''

################################## OOP #########################################
# Object-oriented programming: uses abstraction (classes, objects) to create models.
# Procedural programming: unit as a sequence of statements.

############################ Class & Instance ##################################

class Student(object):  # create a class with a name starting with a capital letter
    
    class_name = "Student"  # class attribute

    def __init__(self, name, score):    # "self" points to the instance itself
        self.name = name        # public instance attribute
        self.__score = score    # private instance attribute

    def show_score(self):   # create a method that can encapsulate the data
        print("%s's score is %d" % (self.name, self.__score))
  
    def set_score(self, score): # a method to access the private attribute
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("Bad score")

bruce = Student("Bruce Wayne", 96)  # create an instance

print(Student)
print(bruce)
print(bruce.name)
#print(bruce.__score)    # This will fail because __score is a private attribute
bruce.show_score()

bruce.set_score(92)
bruce.show_score()

print(dir(bruce))   # "dir()" lists all attributes and mehtod of an object

print(hasattr(bruce, "gender"))
print(getattr(bruce, "gender", 404))
setattr(bruce, "gender", "male")
print(getattr(bruce, "gender"))

############################### Inheritance ####################################

class Animal(object):   # Animal as a Parent/Base/Super class

    def run(self):
        print("Animal is running...")

    def eat(self):
        print("Animal is eating...")

class Dog(Animal):      # Dog as a Child/Sub class of Animal
    
    def run(self):  # this overrides the parent's method
        print("Dog is running...")

dog = Dog()
dog.run()
dog.eat()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

########################### Multiple Inheritance ###############################
# Use "MixIn" to provide many optional features for a class

class Pokemon(object):
    pass

class Kanto(Pokemon):
    pass

class Normal(Pokemon):
    pass

class Water(Pokemon):
    pass

class CutMixIn(object):
    def cut(self):
        print("Using cut...")

class SurfMixIn(object):
    def surf(self):
        print("Using surf...")

class Lapras(Kanto, Water): # inherit multiple parent classes
    pass

class Meowth(Kanto, Normal, SurfMixIn, CutMixIn): # Use MixIn class to add additional features
    pass

