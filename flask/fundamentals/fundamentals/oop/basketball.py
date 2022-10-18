

# Update the constructor to accept a dictionary with a players information

class Player:

    


    def __init__(self, player_data):
        self.name = player_data["name"]
        self.age = player_data ["age"]
        self.position = player_data["position"]
        self.team = player_data["team"]

    def __repr__(self):
        return "Name: {}, Age: {}, Position:{}, team: {}".format(
            self.name,self.age, self.position, self.team)
    
    
    @classmethod
    def get_team(cls, players):
        new_team = []
        for player_data in players:
            new_team.append(cls(player_data))
        print(new_team)
        return new_team

kevin = {
    
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    }


jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???
# jason_player = Player(jason)
# print(jason_player)


# print(kyrie["name"])
# kyrie_play = Player(kyrie)
# print(kyrie_play)

# print(kevin["name"])
# kevin_play = Player(kevin)
# print(kevin_play)

# create instancesfor each of the following dictionaries
    
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]
Player.get_team(players)
# for loop over the list of dicitonaries and
# each time use the dictionary info to
# create a new player(instance)
# new_team = [] 
# new_team = []
# for player_data in players:
#     player = Player(player_data)
#     new_team.append(player)
# print(new_team)







# Ninja Bonus: add an @class method called get_team(cls, team_list) that,
# given a list of dictionaries populates and returns a new list of player objects.

