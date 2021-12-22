# Shivali Mukherji 
# mukhe105
# CSCI 1133 Section 070
# Assignment 6

class Person:
  ''' A class to represent a Person

    Attributes
    ----------
    name : str
        first name of the person

  '''
  def __init__(self, name):

    ''' constructor that recieves name of person and initializes experience.'''

    self.name = name
    self.experience = 0


  def __str__(self):

    ''' returns the string to tell the person's name'''

    return "Hello my name is " + self.name

  
  def __repr__(self):

    ''' returns the string to tell the person's name a second time. '''

    return self.__str__()



class MathTeacher(Person):
  ''' A class that inherits from the Person class 
  to represent a math teacher

    Attributes
    ----------
    name : str
        first name of the math teacher
    eqn : str 
        math teacher's favorite equation

  '''
  def __init__(self, name, eqn):

    ''' constructor that takes in the math teacher's name and favorite equation. '''

    super().__init__(name)
    self.eqn = eqn


  def __str__(self):

    ''' returns the math teacher's name and favorite equation in a string. '''

    return self.name + ":" + " I am a math teacher. My favorite equation is " + self.eqn


  def __repr__(self):

    ''' returns the math teacher's introduction string. '''

    return self.name + ":" + " I am a math teacher."



class ScienceTeacher(Person):
  ''' A class that inherits from the Person class 
  to represent a science teacher

    Attributes
    ----------
    name : str
        first name of the science teacher
    law : str 
        science teacher's favorite scientific law

  '''
  def __init__(self, name, law):

    ''' constructor that recieves the science teacher's name and favorite scientific law. '''

    super().__init__(name)
    self.law = law


  def __str__(self):

    ''' returns the string of the science teacher's name and favorite scientific law. '''

    return self.name + ": I am a science teacher. My favorite science law is " + self.law
        

  def __repr__(self):

    ''' returns the science teacher's introduction string. '''

    return self.name + ": I am a science teacher."



def teacher_introductions(people):

  ''' recieves a list of objects from the person class and prints the list, as well as each item in the list. '''
  
  for person in people:
    print(person.__repr__())
    print(person.__str__())
    


def main():
  ''' driver funtion that prints the list of names and teacher introductions. '''
  shivali = Person("shivali")
  print(shivali.__str__())
  print(shivali.__repr__())
  ppl_list = list()
  schultz = MathTeacher("schultz", "quadratic")
  ppl_list.append(schultz)
  print(schultz.__str__())
  print(schultz.__repr__())
  marshak = ScienceTeacher("marshak", "conservation of energy")
  ppl_list.append(marshak)
  print(marshak.__str__())
  print(marshak.__repr__())
  teacher_introductions(ppl_list)

main()







  





  
