# Shivali Mukherji 
# mukhe105
# CSCI 1133 Section 070
# Assignment 6

import random

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

      elif target.__class__.__name__ == "MadScientist":
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
      
      elif target.__class__.__name__ == "MadScientist":
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

    ''' method that makes two players from the MadScientist level to collaborate on a project. Each player gains or loses life points and experience as they try to "out-science" each other. '''
    
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


def thunderdome(people):

    ''' function that takes a dictionary with the name of the ScienceGeek 
    and a list of three elements representing their name, life points, and experience.'''

    players = dict()
    people_keys = list(people.keys())
    
    # Creating players dictionary
    for name in people_keys:
        people_attr = people.get(name)
        geek = ScienceGeek(name, people_attr[0], people_attr[1])
        players[name] = geek

    #Initialize round of play
    play = 0

    #Begin outer loop
    while(True):
        selection = list()
        player_names = list(players.keys())
        
        # Randomly select two players 
        # making sure they are not same
        while(len(players) > 2):
            selection = random.choices(player_names, k = 2)
            if selection.count(selection[0]) != len(selection):
                break
                
        player1_name = ""
        player2_name = ""
        #Player selection
        if len(selection) == 0:
            player1_name = player_names[0]
            player2_name = player_names[1]
        else:
            player1_name = selection[0]
            player2_name = selection[1]

        player1 = players.get(player1_name)
        player2 = players.get(player2_name)
        
        # Making sure it is a valid player1
        if player1 is not None and player2 is not None:
            #Initialize round of play
            play = 0
            print("BEGIN THUNDERDOME WITH:")
            print(player1.__str__())
            print(player2.__str__())
            #Begin inner loop
            while(True):
                player1.collaborate(player2)
                if player1.life_points > 0:
                    player1_evol = player1.evolve()
                    if player1.__class__.__name__ != player1_evol.__class__.__name__ :
                        players[player1_name] = player1_evol
                if player2.life_points > 0:
                    player2_evol = player2.evolve()
                    if player2.__class__.__name__ != player2_evol.__class__.__name__ :
                        players[player2_name] = player2_evol

                #Re-assign players
                player1 = players.get(player1_name)
                player2 = players.get(player2_name)
                #Exit the loop if either player is None
                #OR non-existent
                if player1 is None or player2 is None:
                    break
                print("After round " + str(play))
                print(player1.__str__())
                print(player2.__str__())

                if player1.life_points <= 0:
                    print(player1_name + " eliminated")
                    players.pop(player1_name)
                    if player1_name in player_names: player_names.remove(player1_name)
                elif player2.life_points <= 0:
                    print(player2_name + " eliminated")
                    players.pop(player2_name)
                    if player2_name in player_names: player_names.remove(player2_name)
                # Move to the next game
                play += 1
                #print("Number of players: " + str(len(players)))
                #If only one player left, return winner from here
                if len(players) == 1:
                    return players
            #End inner loop            
        else:
            return players
    #End outer loop
    

def main():
    ''' driver function that obtains the winner from the dictionary and prints it. '''
    ppl_dict = {"Mr. Bean":[20,10], "Elmo":[100,2], "Captain Ahab":[25,0]}
    winner_dict = thunderdome(ppl_dict)
    #There should be only one winner
    if len(winner_dict) == 1:
        for key,winner in winner_dict.items():
            print("WINNER: " + winner.__str__())


main()