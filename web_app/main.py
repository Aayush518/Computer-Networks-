from fastapi import FastAPI

# Initialize FastAPI
app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "Computer Network"}
