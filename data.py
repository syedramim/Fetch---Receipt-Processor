from ReceiptModel import Receipt
import uuid

class Data():
    data = None
    
    def __init__(self):
        self.data = {}
    
    def add_data(self, receipt: Receipt):
        if not receipt: return -1
        
        try:
            id = str(uuid.uuid4())
            self.data[id] = receipt
            
            return id
        except ValueError as err:
            print("ERROR: ADDING {err}")

        return "Unknown Error"
            
    def get_data_by_id(self, id):
        if not id: return -1
        
        try:
            return self.data[id.replace("%22", "")]
        except KeyError as err:
            print("ERROR: GETTING DATA {err}")
        
        
                
    