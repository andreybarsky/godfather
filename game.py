import roles

import random
import os

class ServerSession:
    def __init__(self, server_id):
        self.server_id = server_id

        self.existing_games = {} # dict keying game names to their GameSession objects

        self.server_preferences = {} # allows for custom settings per server if needed

    def random_game_name(self):
        """placeholder function: should eventually create funny and memorable unique names,
        but for now just uses an ascending integer to differentiate"""
        game_integer = 0
        game_name = f'Game_{game_integer}'
        while not self.name_is_taken(game_name):
            game_integer += 1
            game_name = f'Game_{game_integer}'
        return game_name

    def name_is_taken(self, name):
        """returns True is a game exists in this server by that name, False otherwise"""
        return (name in self.existing_games.keys())

    def server_dir_exists(self):
        return True if self.server_id


class GameSession:
    def __init__(self, setup:dict, players:list, server: ServerSession, , game_name = None):
        """args:

        setup: a dict that keys role strings to the number of players with that role.
            for example, a typical 7-player game of magia:
                setup = {'villager': 3, 'doctor': 1, 'cop': 1, 'mafia': 2}

        players: a list of discord IDs of the players in this game.
            roles will be randomly distributed between players.

        server: an initialised ServerSession object unique to the server this game exists in.

        game_name: an optional string to give the game a unique name,
            which also affects the name of ther """

        self.setup = setup
        self.players = players
        self.server_session = server

        if game_name is None:
            # create a default game name if one is not
            game_name =
        else:


        # create discord roles for the game: (we call them 'tags' for disambiguity with game roles)
        self.game_tag, self.alive_tag, self.dead_tag = self.create_basic_tags()

        # allocate players to roles: (and keep mappings in both directions)
        self.player_roles, self.role_players = self.allocate_roles(roles, players)



    def allocate_roles(self, setup, players):
        available_roles = []
        for role_name, num in setup.items():
            for i in range(num):
                role_id = f'{role_name}{i}'
                available_roles.append(role_name)
        num_roles = len(available_roles)
        assert len(available_roles) == len(players), f"number of roles ({num_roles}) does not match number of players ({len(players)})"

        player_roles = {}
        role_players = {}

        # simply shuffle order of both players and roles, then allocate one-to-one:
        player_order = [p for p in players]
        random.shuffle(player_order)
        random.shuffle(available_roles)
        for player, role in zip(player_order, available_roles):
            player_roles[player] = role
            role_players[role] = player

        return player_roles, role_players

    def kill_player(self, player):
        """switches a player from alive to dead. in order, this:
            - triggers any death effects their role has
            - """





