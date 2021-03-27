from typing import List, Dict

import pandas as pd
import numpy as np
from random import shuffle

import scipy.sparse
from sklearn.metrics.pairwise import pairwise_distances


class RecommendationEngine:
    def __init__(self, top_k: int = 100,
                 only_available_in_ru: bool = True):
        """
        :param top_k: Top-k wine_ids prediction.
        """
        self.top_k = top_k

    def predict(self, sight_ids):
        predictions = [i for i in range(1, 2046)]
        shuffle(predictions)
        return predictions[:self.top_k]
