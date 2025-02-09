from fastapi import FastAPI

app = FastAPI()

@app.get('/receipts/{id}/points')
def get_points(id: int):
    return {0:0}

@app.post('/receipts/process')
def get_points():
    return 'Added to list'