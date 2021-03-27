from typing import Dict

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


def get_api_key(api_key_query_value: str = Security(api_key_query),
                api_key_header_value: str = Security(api_key_header)):
    if api_key_query_value == config.API_KEY:
        return api_key_query
    elif api_key_header_value == config.API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403)


@app.get('/predict', response_model=SightsList)
async def recommend_similar_wines(
        sight_ids: List[int],
        api_key: APIKey = Depends(get_api_key)
):
    sight_ids_rec = recommender.predict(sight_ids)
    recommendations = SightsList(sight_ids=sight_ids_rec)
    return recommendations
