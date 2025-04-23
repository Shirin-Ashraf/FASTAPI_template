## FastAPI Template

A reusable FastAPI project template designed for AI developers to expose their ML/GenAI scripts as APIs — with built-in API key authentication, logging, and Docker support.

---

## Features

- 🔐 API Key Authentication
- 📜 Logging (console-based)
- ⚙️ Modular folder structure
- 🧪 Easily pluggable AI scripts
- 🐳 Docker & Docker Compose ready


## API Overview

#### 🔹 Hello API (GET `/api/v1/hello`)
A simple endpoint to test if your API is working.

#### Example Request:

curl -X GET "http://127.0.0.1:8000/api/v1/hello?name=Shirin" \
  -H "X-API-Key: supersecretapikey123"


#### Response:

{
  "message": "Hello, Shirin! Your API is working."
}




### 🔹 Text Generator API (POST `/api/v1/generate`)
Uses a basic mock script to generate a response based on your prompt.

#### Example Request:

curl -X POST "http://127.0.0.1:8000/api/v1/generate" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: supersecretapikey123" \
  -d '{"prompt": "Once upon a time"}'


#### Response:

{
  "generated_text": "Once upon a time... and then something amazing happened!"
}



## API Authentication

The APIs use API key-based authentication. Add this key to your headers as:

-H "X-API-Key: your_key_here"

Set your secret key in the `.env` file:

API_KEY=supersecretapikey123



## Running Locally


# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload


Open your browser at `http://127.0.0.1:8000/docs` to view Swagger API docs.



## Docker Setup

**Build and Run with Docker Compose**

docker-compose up --build


This will launch the API at `http://localhost:8000`



## Extend This Template

To add your own AI/ML script:
1. Add the logic in `app/` (e.g., `my_ai_logic.py`)
2. Create an endpoint under `app/api/v1/endpoints/`
3. Import and use your logic
4. Register the new router in `main.py`