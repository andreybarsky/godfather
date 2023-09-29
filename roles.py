
import time

class Role:
    def __init__(self, parent_game, instance_num):
        self.parent_game = parent_game
        self.instance_num = instance_num

        self.role_id = hash(time.time()) # unique id to each instance
        # is this necessary? or does base.id do the same job

        self.alive = True

    def allocate_player(self, player_id):
        self.player = player_id

    def __hash__(self):
        """each instance is unique, for dict lookup purposes"""
        return id(self)

    def __eq__(self, other):
        """equality between roles is based on the type of role,
        i.e. all Villagers evaluate as equal to each other"""
        return type(self) == type(other)

    # all roles, regardless of faction, can vote to lynch, unless overwritten:
    @day_action
    def vote(self, target):
        """by default, this is a vote to lynch and end the day"""



### pattern for Role subclasses:
### must contain _role_name and _faction_name as class or instance attributes
###     (these are displayed to players when needed)
###     _faction_name determines team allocation, so all town factions must be exactly 'Town'
### if __init__ is overwritten:
###     must be initialised with parent game and instance num as the only two args
###     must call Role.__init__ with those two args at some point in its own subclass init

class Townie(Role):
    ### not a real role; just groups 'standard' town roles together
    _faction_name = 'Town'

class Mafioso(Role):
    ### not a real role; just groups 'standard' town roles together
    _faction_name = 'Mafia'

class Villager(Role):
    _role_name = 'Villager'
    _faction_name = 'Town'

class Cop(Role):
    _role_name = 'Cop'
    _faction_name = 'Town'

    @day_action
    def protect(self, target):

class Doctor(Role):
    _role_name = 'Doctor'
    _faction_name = 'Town'

    @day_action
    def protect(self, target):

class Mafioso(Role):
    _role_name = 'Mafioso'
    _faction_name = 'Mafia'

    @night_action
    def night_action(self)
