from pydantic import BaseModel

class Item(BaseModel):
    """
    The Item Class is a model expected for each item in the Items in a receipt

    Args:
        BaseModel (BaseModel): for the model of Item
    """
    
    shortDescription: str
    price: str

class Receipt(BaseModel):
    """
    The Receipt Class is a model for the expected Receipt

    Args:
        BaseModel (BaseModel): for the model of Receipt
    """
    
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[Item]
    total: str
        
