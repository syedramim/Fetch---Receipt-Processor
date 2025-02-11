# Receipt Processor

This project implements a web service that fulfills the provided API specification. It accepts receipt JSON data, calculates reward points based on defined rules, and returns a unique receipt ID or the calculated points. Data is stored in memory and is not persisted between application restarts.

## API Endpoints

### Process Receipt
**Endpoint:** `POST /receipts/process`  
**Description:** Accepts a JSON receipt, stores it, and returns a unique receipt ID.  
**Example Response:**
```json
{ "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
```

### Get Points
**Endpoint:** `GET /receipts/{id}/points`  
**Description:** Returns the number of points awarded for the receipt corresponding to the given ID.  
**Example Response:**
```json
{ "points": 32 }
```

## Example Using curl

**Submit a Receipt:**
```bash
curl -X POST http://localhost/receipts/process \
  -H "Content-Type: application/json" \
  -d '{
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
          {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
          {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
          {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
          {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
          {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"}
        ],
        "total": "35.35"
      }'
```
This should return a JSON object with an `"id"` value.

**Retrieve Points:**
```bash
curl http://localhost/receipts/<id>/points
```
Replace `<id>` with the actual ID returned from the previous call. This should return the calculated points.

## Running the Application

### Prerequisites
- Git installed.
- Python 3.12.6 or higher.
- Docker (optional for containerized deployment).

### Clone the Repository
```bash
git clone https://github.com/syedramim/Receipt-Processor.git
cd receipt-processor-challenge
```

### Using Docker
To build and run using Docker:
1. **Build the Docker Image:**  
   (This step also runs the unit tests; if any test fails, the build will stop.)
   ```bash
   docker build -t receipt-processor .
   ```
2. **Run the Docker Container:**
   ```bash
   docker run -p 80:80 receipt-processor
   ```

## Running Tests
To run the unit tests locally, execute:
```bash
python -m unittest discover
```

## Note
Data is stored in memory only. All receipts will be lost when the application stops.
