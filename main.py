from typing import Dict, List

from fastapi import FastAPI, Depends, Security, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey

from src import config
from src.entities.sights import SightsList
from src.models.recommender import RecommendationEngine

app = FastAPI()
api_key_query = APIKeyQuery(name=config.API_KEY_NAME_IN_QUERY,
                            auto_error=False)
api_key_header = APIKeyHeader(name=config.API_KEY_NAME_IN_HEADER,
                              auto_error=False)

recommender = RecommendationEngine(top_k=config.top_k)


@app.post('/predict', response_model=SightsList)
async def recommend_similar_wines(
        sight_ids: List[int],
        cities: List[str]
):
    sight_ids_rec = recommender.predict(sight_ids)
    recommendations = SightsList(sight_ids=sight_ids_rec)
    return recommendations
