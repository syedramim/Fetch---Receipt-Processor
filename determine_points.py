from datetime import datetime, time
from math import ceil

example1 = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}


example2 = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}

class ReceiptPoints():
    points: int
    
    def init(self):
        self.points = 0
        
    def get_points(self, receipt):
        if not receipt: return -1
        pnts = 0
        
        try:
            pnts += self.handle_store_name(receipt["retailer"])
            pnts += self.handle_total(receipt["total"])
            pnts += self.handle_item_count(receipt["items"])
            pnts += self.handle_description(receipt["items"])
            pnts += self.handle_day(receipt["purchaseDate"])
            pnts += self.handle_time_of_day(receipt["purchaseTime"])
            
        except ValueError as err:
            print("ERROR: PARSING {err}")
            
        return pnts
        
    def handle_store_name(self, name):
        if not name: return -1
        pnts = 0
        
        for c in name:
            if c.isalnum():
                pnts += 1
        
        return pnts
    
    def handle_total(self, total):
        if not total: return -1
        pnts = 0
        
        cents = int(total[-2:])
        if cents == 0:
            pnts += 50
        if cents % 25 == 0:
            pnts += 25
            
        return pnts
    
    def handle_item_count(self, items):
        if not items: return -1
        
        count_items = len(items)
        pairs = count_items // 2
        
        return pairs * 5
    
    def handle_description(self, items):
        if not items: return -1
        pnts = 0
        
        for item in items:
            trimmed_desc = item["shortDescription"].strip()
            price = float(item["price"])
            
            if len(trimmed_desc) % 3 == 0:
                pnts += ceil(price * 0.2)
                
        return pnts
        
    def handle_day(self, date):
        if not date: return -1
        day = int(date[-2:])
        
        if day % 2 == 1:
            return 6
        
        return 0
            
    def handle_time_of_day(self, time_of_day):
        if not time_of_day: return -1
        
        try:
            time_converted = datetime.strptime(time_of_day, "%H:%M").time()
            first_range = time(14,0,0)
            second_range = time(16,0,0)
            if first_range <= time_converted <= second_range:
                return 10
        except ValueError as err:
            return "ERROR: Invalid Time {err}"
        
        return 0
        
        
        
        
        
        
x = ReceiptPoints()
print(x.get_points(example2))
        