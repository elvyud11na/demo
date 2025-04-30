import os
from config.stages import get_stage

class Endpoints:
    all_games = f"{get_stage()}/games"
    search_game = f"{get_stage()}/games/search"
    search_game_by_uuid = lambda self, game_uuid: f"{get_stage()}/games/{game_uuid}"