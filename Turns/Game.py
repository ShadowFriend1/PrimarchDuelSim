from typing import List

from Base_Models.Unit import Unit
from Turns.Game_Round import GameRound


class Game:

    game_end = 0

    def __init__(self, player_1: List[Unit], player_2: List[Unit], turn_limit: int = 0):
        if turn_limit != 0:
            while (turn_limit > 0) & (self.game_end == 0):
                game_round = GameRound(player_1, player_2)
                self.game_end = game_round.game_end
        else:
            while self.game_end == 0:
                game_round = GameRound(player_1, player_2)
                self.game_end = game_round.game_end
