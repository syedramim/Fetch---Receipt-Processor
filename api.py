from urllib.parse import unquote
from fastapi import FastAPI, HTTPException
from ReceiptModel import Receipt
from data import Data, DataError
from determine_points import ReceiptPoints, ReceiptPointsError

app = FastAPI()
receipt_data = Data()
points_calculator = ReceiptPoints()

@app.post("/receipts/process")
def add_receipt(receipt: Receipt):
    """
    Endpoint to store the given receipt and return a unique ID
    """
    try:
        record_id = receipt_data.add_data(receipt)
        return {"id": record_id}
    except DataError as err:
        raise HTTPException(
            status_code=400,
            detail=f"Bad Request ({err})"
        )
    except HTTPException as e:
        raise HTTPException(
            status_code=400,
            detail=f"Bad Request ({e})"
        )

@app.get("/receipts/{id}/points")
def get_points(id: str):
    """
    Endpoint to return the calculated points of the receipt with the given ID
    """
    try:
        cleaned_id = unquote(id).replace('"', '')
        stored_receipt = receipt_data.get_data_by_id(cleaned_id)
        pts = points_calculator.get_points(stored_receipt.dict())
        return {"points": pts}
    except DataError as err:
        raise HTTPException(
            status_code=400,
            detail=f"Bad Request ({err})"
        )
    except ReceiptPointsError as err:
        raise HTTPException(
            status_code=400,
            detail=f"Bad Request ({err})"
        )
    except HTTPException as err:
        raise HTTPException( 
            status_code=400,
            detail=f"Bad Request ({err})"
        )
