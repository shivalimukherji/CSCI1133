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


class ScienceGeek(Person):

  ''' class to represent the ScienceGeek level 
    in the Thunderdome, Inherits from Person class

    Attributes
    ----------

    name : str
      first name of the ScienceGeek player

    life_points : int
      number of life points the ScienceGeek player has

    experience: int
      number that represents how much experience the ScienceGeek player has

     '''

  def __init__(self, name, life_points, experience):

    ''' constructor that recieves the name, life_points, and experience of each player. '''

    super().__init__(name)
    self.life_points = life_points
    self.experience = experience


  def __repr__(self):

    ''' method returns the string to represent the player, 
    the number of life points they have, their experience, and their level. '''

    return self.name + " - " + " life_points = " + str(self.life_points) + " experience = " + str(self.experience) + " level = " + self.__class__.__name__


  def __str__(self):

    ''' same as repr '''

    return self.__repr__()
  

  def collaborate(self,target):

    ''' method that makes a player from the levels Scientist and MadScientist respectively to collaborate on a project. Each player gains or loses life points and experience as they try to "out-science" each other . '''

    if self.__class__.__name__ == target.__class__.__name__ :
      same_power = abs(self.experience - target.experience)/2
      target.life_points = target.life_points - same_power
      self.life_points = self.life_points - same_power
    else:
      if target.__class__.__name__ == "Scientist":
        same_power = abs(self.experience - target.experience)/2
        sci_life_points = int(round(1.5 * same_power))
        non_sci_life_points = int(round(.75 * same_power))
        self.life_points = self.life_points - sci_life_points
        target.life_points = target.life_points - non_sci_life_points

      elif target.__class__.name__ == "MadScientist":
        same_power = abs(self.experience - target.experience)/2
        mad_sci_points = int(round(2 * same_power))
        non_mad_sci_points = int(round(0.5 * same_power))
        self.life_points = self.life_points - mad_sci_points
        target.life_points = target.life_points - non_mad_sci_points
    self.experience += 1
    target.experience += 1


  def evolve(self):

    ''' If a ScienceGeek has accumulated 4+ points, then this method should return a Scientist object. '''

    if self.experience >= 4:
      return Scientist(self.name, self.life_points, self.experience)
    else:
      return self


class Scientist(ScienceGeek):

  ''' class to represent the Scientist level 
    in the Thunderdome, Inherits from ScienceGeek.

    Attributes
    ----------

    name : str
      first name of the Scientist player

    life_points : int
      number of life points the Scientist player has

    experience: int
      number that represents how much experience the Scientist player has

     '''

  def __init__(self, name, life_points, experience):
    ''' constructor that recieves the name, life_points, and experience of each player. '''
    super().__init__(name, life_points, experience)

  def collaborate(self, target):

      ''' method that makes a player from the levels ScienceGeek and MadScientist respectively to collaborate on a project. Each player gains or loses life points and experience as they try to "out-science" each other . '''

      if self.__class__.__name__ == target.__class__.__name__ :
        same_power = abs(self.experience - target.experience)/2
        target.life_points = target.life_points - same_power
        self.life_points = self.life_points - same_power
      else:
        if target.__class__.__name__ == "ScienceGeek":
          same_power = abs(self.experience - target.experience)/2
          non_sci_life_points = int(round(0.75 * same_power))
          sci_life_points = int(round(1.5 * same_power))
          self.life_points = self.life_points - non_sci_life_points
          target.life_points = target.life_points - sci_life_points
      
        elif target.__class.__name__ == "MadScientist":
          same_power = abs(self.experience - target.experience)/2
          mad_sci_points = int(round(2 * same_power))
          non_mad_sci_points = int(round(0.5 * same_power))
          self.life_points = self.life_points - mad_sci_points
          target.life_points = target.life_points - non_mad_sci_points
  

  def evolve(self):

    ''' If a ScienceGeek has accumulated 8+ points, then this method should return a MadScientist object. '''

    if self.experience >= 8:
        return MadScientist(self.name, self.life_points, self.experience)
    else:
        return self
        

class MadScientist(Scientist):

  ''' class to represent the MadScientist level 
    in the Thunderdome, Inherits from the Scientist class 

    Attributes
    ----------

    name : str
      first name of the MadScientist player

    life_points : int
      number of life points the MadScientist player has

    experience: int
      number that represents how much experience the MadScientist player has

     '''


  def __init__(self, name, life_points, experience):

    ''' constructor that recieves the name, life_points, and experience of each player. '''

    super().__init__(name, life_points, experience)


  def collaborate(self, target):

      ''' method that makes two players from the MadScientist level to collaborate on a project. Each player gains or loses life points and experience as they try to "out-science" each other . '''

      if self.__class__.__name__ == target.__class__.__name__ :
        same_power = abs(self.experience - target.experience)/2
        target.life_points = target.life_points - same_power
        self.life_points = self.life_points - same_power
      else:
        if target.__class__.__name__ in ["Scientist" , "ScienceGeek"]:
          same_power = abs(self.experience - target.experience)/2
          mad_sci_points = int(round(2 * same_power))
          non_mad_sci_points = int(round(0.5 * same_power))
          self.life_points = self.life_points - non_mad_sci_points
          target.life_points = target.life_points - mad_sci_points
      self.experience += 1
      target.experience += 1


def main():
  ''' driver function that prints each string and the match results. '''
  geek1 = ScienceGeek("Mr. Bean", 20, 10)
  geek2 = ScienceGeek("Captain Ahab", 25, 0)
  print(geek1.__str__())
  print(geek2.__str__())
  print(geek1.name + " collaborating with " + geek2.name)
  geek1.collaborate(geek2)
  print(geek1.__str__())
  print(geek2.__str__())
  evolution = geek1.evolve()
  print(geek1.name + " evolving to ...")
  print(evolution.__str__())
  mad_scientist = MadScientist("Elmo", 30, 20)
  print(mad_scientist.__str__())
  print(mad_scientist.name + " collaborating with " + evolution.name)
  mad_scientist.collaborate(evolution)
  print(evolution.__str__())
  print(mad_scientist.__str__())


main()
    
  