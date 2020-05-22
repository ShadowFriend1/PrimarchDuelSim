from typing import List

from Base_Models.Unit import Unit
from Turns.Player_Turn import PlayerTurn


class GameRound:

    player_1_turn: PlayerTurn
    player_2_turn: PlayerTurn
    game_end: int

    def __init__(self, player_1: List[Unit], player_2: List[Unit]):
        player_1_turn = PlayerTurn(player_1, player_2)
        player_2_turn = PlayerTurn(player_2, player_1)
        player_1_turn.start()
        self.game_end = player_1_turn.end_of_turn()
        if self.game_end == 0:
            player_2_turn.start()
            self.game_end = player_2_turn.end_of_turn()
