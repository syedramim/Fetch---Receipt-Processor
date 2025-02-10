from fastapi import FastAPI
from ReceiptModel import Receipt
from data import Data

app = FastAPI()
receipt_data = Data()

@app.get('/receipts/{id}/points')
def get_points(id):
    try:
        return receipt_data.get_data_by_id(id)
    except KeyError as err:
        return "ERROR: {err}"

@app.post('/receipts/process')
def add_receipt(receipt: Receipt):
    try:
        added_data = receipt_data.add_data(receipt=receipt)
        return added_data
    except ValueError as err:
        return "ERROR: {err}"
    
