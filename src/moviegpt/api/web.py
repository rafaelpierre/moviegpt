from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import logging
import os

from moviegpt.providers.rag import RAGProvider
from moviegpt.prompts.recommendation import RecommendationPrompt

app = FastAPI()

class Prompt(BaseModel):
    details: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "details": "Movies similar to The Godfather"
                },
                {
                    "details": "spiderman"
                },
            ]
        }
    }

@app.post("/generate", tags=["Generate"])
async def generate(
    req: Request,
    prompt_obj: Prompt
):
    """Generates movie recommendations.

    Params:

        prompt_obj: Prompt object containing movie recommendation details.

    """
    try:
        logging.info(f"Prompt: {prompt_obj.details}")

        prompt = RecommendationPrompt(details = prompt_obj.details)
        logging.info(f"Prompt: {str(prompt)}")

        provider = RAGProvider(api_key = os.environ["OPENAI_API_KEY"])
        response = provider.query(prompt = prompt)
        payload = jsonable_encoder({"answer": str(response)})
        response = JSONResponse(content=payload)

        return response
    
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")