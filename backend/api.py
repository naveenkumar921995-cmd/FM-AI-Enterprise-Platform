from fastapi import FastAPI
from backend.schemas import ChatRequest
from backend.graph import run_graph

app = FastAPI(
    title="FM AI Enterprise API",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "status": "running",
        "application": "FM AI Enterprise"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = run_graph(request.query)

    return response