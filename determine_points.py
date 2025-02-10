from datetime import datetime, time
from math import ceil
from ReceiptModel import Receipt

class ReceiptPointsError(Exception):
    pass

class ReceiptPoints:
  """
  This class is used to determine the points of a receipt
  """

  def get_points(self, receipt: Receipt):
    """
    get_points() is meant to return the total points given a receipet

    Args:
        receipt (Receipt): the receipt is of the receipt model 

    Returns:
        int: the total points the receipt should be, 
        if there is an issue however it will return error or -1 if there is not receipt
    """
    if not receipt:
        return -1
    try:
        pts = 0
        pts += self.handle_store_name(receipt["retailer"])
        pts += self.handle_total(receipt["total"])
        pts += self.handle_item_count(receipt["items"])
        pts += self.handle_description(receipt["items"])
        pts += self.handle_day(receipt["purchaseDate"])
        pts += self.handle_time_of_day(receipt["purchaseTime"])
        return pts
    except ReceiptPointsError as e:
        return f"ERROR: {e}"
    except (ValueError, TypeError, AttributeError) as err:
        return f"ERROR: {err}"

  def handle_store_name(self, name):
    """
    handle_store_name() takes the retailer name and outputs the points expected
    given the alphanumerical count

    Args:
        name (str): the name of the retailer

    Returns:
        int: points or raises an error if invalid 
    """
    if not name:
        raise ReceiptPointsError("Missing retailer name")
    pts = 0
    for c in name:
        if c.isalnum():
            pts += 1
    return pts

  def handle_total(self, total):
    """
    handle_total() takes the total of the receipt 
    and returns the expected points or -1 if error with total

    Args:
        total (str): the total of the receipt of the item costs

    Returns:
        int: points or raises an error if invalid
    """
    if not total:
        raise ReceiptPointsError("Missing total")
    try:
        pts = 0
        cents = int(total[-2:])
        if cents == 0:
            pts += 50
        if cents % 25 == 0:
            pts += 25
        return pts
    except:
        raise ReceiptPointsError("Invalid total format")

  def handle_item_count(self, items):
    """
    handle_item_count() takes the items array and gets the count of them 
    and for every pair of 2 gives the receipt 5 points

    Args:
        items (List[dict]): an array of item dicts with shortDescription and price

    Returns:
        int: points or raises an error if invalid
    """
    if not items:
        raise ReceiptPointsError("No items in receipt")
    return (len(items) // 2) * 5

  def handle_description(self, items):
    """
    handle_description() takes the items array and goes through every item,
    if the item has a description length being a multiple of 3 then it gives points accordingly

    Args:
        items (List[dict]): an array of item dicts with shortDescription and price

    Returns:
        int: points or raises an error if invalid
    """
    if not items:
        raise ReceiptPointsError("No items for description")
    pts = 0
    for i in items:
        desc = i["shortDescription"].strip() if i["shortDescription"] else ""
        try:
            price = float(i["price"])
        except:
            raise ReceiptPointsError("Invalid item price")
        if len(desc) % 3 == 0:
            pts += ceil(price * 0.2)
    return pts

  def handle_day(self, d):
    """
    handle_day() checks the purchase date
    if the day is odd, returns 6 points, otherwise returns 0

    Args:
        d (str): the purchase date

    Returns:
        int: points or raises an error if invalid
    """
    if not d:
        raise ReceiptPointsError("Missing purchase date")
    try:
        day = int(d[-2:])
        return 6 if day % 2 == 1 else 0
    except:
        raise ReceiptPointsError("Invalid purchase date format")

  def handle_time_of_day(self, t):
    """
    handle_time_of_day() checks if the purchase time is between 2PM and 4PM 
    and returns 10 points, otherwise 0

    Args:
        t (str): the purchase time 
    Returns:
        int: points or raises an error if invalid
    """
    if not t:
        raise ReceiptPointsError("Missing purchase time")
    try:
        converted = datetime.strptime(t, "%H:%M").time()
        if time(14, 0) <= converted <= time(16, 0):
            return 10
        return 0
    except:
        raise ReceiptPointsError("Invalid purchase time format")
