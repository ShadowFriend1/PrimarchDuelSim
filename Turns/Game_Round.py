from typing import List

from Base_Models.Unit import Unit
from Turns.Player_Turn import PlayerTurn


class GameRound:

    def __init__(self, player_1: List[Unit], player_2: List[Unit]):
        player_1_turn = PlayerTurn(player_1, player_2)
        player_2_turn = PlayerTurn(player_2, player_1)
