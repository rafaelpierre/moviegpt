from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging
import os

from moviegpt.providers.rag import RAGProvider
from moviegpt.prompts.recommendation import RecommendationPrompt

app = FastAPI()

@app.post("/generate")
async def generate(
    req: Request,
    message: dict
):
    try:
        logging.info(f"Question: {message['question']}")
        question = message["question"]

        prompt = RecommendationPrompt(details = question)
        logging.info(f"Prompt: {str(prompt)}")

        provider = RAGProvider(api_key = os.environ["OPENAI_API_KEY"])
        response = provider.query(prompt = prompt)
        payload = jsonable_encoder({"answer": str(response)})
        response = JSONResponse(content=payload)

        return response
    
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")