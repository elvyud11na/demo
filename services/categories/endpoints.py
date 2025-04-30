from config.stages import get_stage

class Endpoints:

    get_categories = f"{get_stage()}/categories"
    game_list_by_categories = lambda self, category_uuid: f"{get_stage()}/categories/{category_uuid}/games"