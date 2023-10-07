from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return {"age": "24 years old", "home": {"country": "Niue", "address": "272 example street"}, "friends": ["Dora, Veronika", "Katleen, Phaedra", "Drucill, Anne-marie", "Starlene, Lenee", "Carroll, Callida"]}
