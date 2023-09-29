### module for managing server sessions, server-specific game caches, etc.

import os

servers_root_dir = '~/servers/'

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
        server_dirs = os.path.listdir(servers_root_dir)
        return True if self.server_id in server_dirs

    def initialise_dir(self):
        server_path = os.path.join(servers_root_dir)
        os.path.mkdir(server_path) # create empty directory for this server

        settings_file_path = os.path.join(server_path, 'settings.txt')
        open(settings_file_path, 'x') # create empty file

        active_games_path = os.path.join(server_path, 'active_games')
        os.path.mkdir(active_games_path)

        inactive_games_path = os.path.join(server_path, 'inactive_games')
        os.path.mkdir(inactive_games_path)
