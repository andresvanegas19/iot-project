import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "API"}


@app.get("/domain/{domain}")
def get_domain(domain: str):
    response = requests.get("http://ip-api.com/json/" + domain)
    return response.json()


if __name__ == "__main__":
    # for make test
    uvicorn.run(app, host="0.0.0.0", port=8000)