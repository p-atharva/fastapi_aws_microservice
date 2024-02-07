# from lib.logic import wiki

# result = wiki()
# print(result)

# Doing a small FASTApi function
from fastapi import FastAPI
import uvicorn
from lib.logic import search_wiki
from lib.logic import wiki as wikisummary
from lib.logic import phrase as wikiphrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello and Welcome Custom WIKIPEDIA API, Do /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to Search in WIkipedia"""

    result = search_wiki(value)
    return {"Results": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retreieve WIkipedia Page in one line"""

    result = wikisummary(name)
    return {"Results": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retreieve WIkipedia Page in one line and also Phrases"""

    result = wikiphrases(name)
    return {"Results": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
