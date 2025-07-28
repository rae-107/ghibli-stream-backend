from fastapi import FastAPI

app = FastAPI()

@app.get("/movies")
def root():
    return {"message": "This should be your movies!"}
