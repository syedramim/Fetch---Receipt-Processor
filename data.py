import uuid
from ReceiptModel import Receipt

class DataError(Exception):
    pass

class Data:
    """
    This class is used to store and retrieve receipt data in memory
    """

    def __init__(self):
        """
        Initializes an empty dictionary to hold receipt data
        """
        self.data = {}

    def add_data(self, receipt: Receipt):
        """
        add_data() generates a new UUID for the given receipt and stores it

        Args:
            receipt (Receipt): The receipt

        Returns:
            str: The UUID string used to store the receipt
        """
        if not receipt:
            raise DataError("No receipt was provided to add")

        try:
            record_id = str(uuid.uuid4())
            self.data[record_id] = receipt
            return record_id
        except ValueError as err:
            raise DataError(f"Error while adding receipt: {err}")

    def get_data_by_id(self, record_id: str):
        """
        get_data_by_id() retrieves the stored receipt with the given UUID

        Args:
            record_id (str): The UUID key

        Returns:
            Receipt: The receipt object matching the given UUID
        """
        if not record_id:
            raise DataError("No ID was provided to retrieve data")

        try:
            return self.data[record_id]
        except KeyError:
            raise DataError(f"No receipt found for ID: {record_id}")

        
        
                
    