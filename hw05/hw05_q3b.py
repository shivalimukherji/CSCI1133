# Shivali Mukherji 
# mukhe105
# CSCI 1133 Section 070
# Assignment 5

import random
import thoroughbreds
import races

class Horse:
                   
    def __init__(self, horse_info):

        '''constructor that takes in a dictionary from the file thoroughbreds.py'''

        self.name = horse_info['name']
        self.height = horse_info['height']
        self.color = horse_info['color']
        self.age = horse_info['age']
        self.sex = horse_info['sex']
        self.sire = horse_info['sire']
        self.dam = horse_info['dam']
        self.damsire = horse_info['damsire']
        self.record = dict(horse_info['record'])
        self.earnings =  horse_info['earnings']
        

    def get_record(self):
        '''getter function that obtains the record information in the dictionary for each horse. This dictionary has keys corresponding to starts and placements (1st, 2nd, or 3rd), with values showing the amount of times the horse had finished in those places'''
        return self.record

    def update_record(self,placement):
        '''setter function that updates the the starts, wins, places, and shows in the records dictionary for each horse in thoroughbreds.puy'''
        self.record = placement

    def get_earnings(self):
        '''getter function that obrains the earnings key in each of the horse dictionaries in the thoroughbreds.py file'''
        return self.earnings
        
    def update_earnings(self, purse):
        '''setter function that updates the earnings key in each horse dictionary'''
        self.earnings += purse

class Race:
            
    posts = {}
    entrants = []

    def __init__(self, race_info):

        '''constructor that takes in a dictionary from the file races.py. initializes an empty lists for the entrants, and empty dictionary for the posts.'''
        
        self.name = race_info['name']
        self.type = race_info['type']
        self.grade = race_info['grade']
        self.distance = race_info['distance']
        self.purse = race_info['purse']
        self.surface = race_info['surface']
        self.posts =  dict()
        self.entrants = list()
        
    def register_entrant(self,my_horse):
        '''function that enters a horse into a race by appending it to the entrants list.'''
        self.entrants.append(my_horse)

    def assign_posts(self):
        '''function that randomly assigns horses in the race to a post position by iterating through the entrants list'''
        temp_list = self.entrants
        for k in range(1,len(self.entrants) + 1,1):
            assignee = random.choice(temp_list)
            self.posts[k]=assignee
            temp_list.remove(assignee)
        print("--------------Line Up--------------")
        for post,horse in self.posts.items():
            print("post:",post,"--horse name:",horse.name)
        print("-----------------------------------")

    def call_to_post(self):
        '''function that uses the entrants list to registrar horses into the race'''
        if len(self.entrants) == 0:
            for horse_info in thoroughbreds.barn:
                this_horse = Horse(horse_info)
                self.register_entrant(this_horse)
        self.assign_posts()

    def and_theyre_off(self):
        '''function that runs a race by randomly assigning a finishing order of horses from the entrants list'''
        participant_keys = list(self.posts.keys())
        # print(participant_keys)
        # print(type(participant_keys))
        print("--------------Results--------------------")
        win_post = random.choice(participant_keys)
        winner = self.posts[win_post]
        print("Post: ", win_post,"-->First Place: ",winner.name)
        participant_keys.remove(win_post)
        second_post = random.choice(participant_keys)
        second = self.posts[second_post]
        print("Post: ", second_post, "-->Second Place: ",second.name)
        participant_keys.remove(second_post)
        third_post = random.choice(participant_keys)
        third = self.posts[third_post]
        print("Post: ", third_post, "-->Third Place: ", third.name)
        participant_keys.remove(third_post)
        print("-----------------------------------------")
    
    def run_with_odds(self):
        '''function to the Race class to randomly choose the finishing order of the horses in the race, weighted by the odds for each horse. '''
        weights = list()
        entrant_list = list(self.posts.values())
        #print(len(entrant_list))
        #Get the odds for each of the horses
        for horse_info in entrant_list:
            odds_on_horse = horse_info.get_odds()
            odds_pair = odds_on_horse.split("-")
            weight = int(odds_pair[1])/int(odds_pair[0])
            #print(horse_info.name,"--",weight)
            weights.append(weight)
        #print(len(weights))
        participant_keys = list(self.posts.keys())
        # print(participant_keys)
        # print(type(participant_keys))
        print("--------------Results--------------------")
        #Returns a list of 1 element. So need to access by index function
        win_post = random.choices(participant_keys, weights, k=1)
        winner = self.posts[win_post[0]]
        print("Post: ", win_post[0],"-->First Place: ",winner.name)
        participant_keys.remove(win_post[0])
        # Reduce the size of the weights list by 1
        weights.pop()
        second_post = random.choices(participant_keys, weights, k=1)
        second = self.posts[second_post[0]]
        print("Post: ", second_post[0], "-->Second Place: ",second.name)
        participant_keys.remove(second_post[0])
        weights.pop()
        third_post = random.choices(participant_keys, weights, k=1)
        third = self.posts[third_post[0]]
        print("Post: ", third_post[0], "-->Third Place: ", third.name)
        participant_keys.remove(third_post[0])
        weights.pop()
        print("-----------------------------------------")


def main():
    '''driver function the welcomes user, prints race card, asks uset which race they would like to see, and returns results'''
    print("Welcome to the Track!")
    print("Today's race card:")
    for race_info in races.program:
        print(race_info['name'])
    print("For results, select from one of the above")
    race_name = input()
    if race_name == 'Kentucky Derby':
        selection = Race(races.ky_derby)
    elif race_name == 'Kentucky Oaks':
        selection = Race(races.ky_oaks)
    elif race_name == 'Derby City Distaff Stakes':
        selection = Race(races.dc_distaff)
    elif race_name == 'Eight Belles Stakes':
        selection = Race(races.eight_belles)
    elif race_name == 'Blue Grass Stakes':
        selection = Race(races.blue_grass)
    elif race_name == 'Preakness Stakes':
        selection = Race(races.preakness)
    elif race_name == 'Belmont Stakes':
        selection = Race(races.belmont)
    elif race_name == 'Appalachian Stakes':
        selection = Race(races.appalachian)
    elif race_name == 'Bourbon Stakes':
        selection = Race(races.bourbon)
    elif race_name == 'Louisville Stakes':
        selection = Race(races.louisville)
    else:
        print('Invalid input')
        exit()
    print("------------------------------------------")
    print('Assigning horses to posts for the race: ', selection.name)
    selection.call_to_post()
    print("Running: ", selection.name)
    selection.and_theyre_off()

main()















