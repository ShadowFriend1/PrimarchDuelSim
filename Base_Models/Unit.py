from typing import List
from Base_Models.Model import Model


class Unit:
    models: List[Model] = []

    def __init__(self, models: List[Model]):
        self.models = models

    def get_models(self):
        return self.models
