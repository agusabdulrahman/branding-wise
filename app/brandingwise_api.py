from typing import Union
from fastapi import FastAPI, HTTPException
from brandingwise import generate_branding_snippet, generate_keyswords
from mangum import Mangum


app = FastAPI()

handler = Mangum(app)
MAX_INPUT_LENGTH = 30

@app.get("/generate_snippet")

async def generate_branding_snippet_route(prompt: str):
    validate_input_legth(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet}

@app.get("/generate_keywords")

async def generate_keywords_api(prompt: str):
    validate_input_legth(prompt)
    keywords = generate_keyswords(prompt)
    return {"snippet": None, "Keywords": keywords}

@app.get("/generate_snippet_and_keywords")

async def generate_keywords_api(prompt: str):
    validate_input_legth(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keyswords(prompt)
    
    return {"snippet": snippet, "keywords": keywords}
    
def validate_input_legth(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code = 400,
            datail = f"Input length is to long. Mst be under {MAX_INPUT_LENGTH} character. "
        )

# uvicorn copikit_api:app --reload