# QTEngine Translation Server

A FastAPI-based server for Chinese to Sino-Vietnamese translation using QTEngine.

## Project Overview

QTEngine Translation Server is a specialized translation API that focuses on translating text between Chinese and Sino-Vietnamese languages. Built with FastAPI, it provides a robust and efficient translation service.

## Features

- Chinese to Sino-Vietnamese translation
- RESTful API endpoints
- CORS support
- Swagger UI documentation
- Docker containerization support

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-repo/QTEngineServer.git
cd QTEngineServer
```

2. Clone the QTEngine submodule:
```bash
git clone https://github.com/SmashPhoenix272/QTEngine.git QTEngine
```

3. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

### Local Development
```bash
python QTEngineServer.py
```
The server will start at `http://localhost:2210`

### Docker Deployment
1. Build the Docker image:
```bash
docker build -t qtengine-server .
```

2. Run the Docker container:
```bash
docker-compose up
```

### Running with Uvicorn

The server can be started directly using Uvicorn:
```bash
uvicorn QTEngineServer:app --host 0.0.0.0 --port 2210
```

## API Endpoints

The server provides the following endpoints:

- `GET /`: Root endpoint returning API information
  - Returns API name, version, and status
- `GET /ping`: Health check endpoint
  - Confirms server availability
- `POST /translate`: Translation endpoint
  - Accepts a translation request with source text
  - Returns translated text and metadata
- `GET /metadata`: Translation engine metadata endpoint
  - Retrieves additional information about the translation engine

### Endpoint Details

#### Translation Request
- **Endpoint**: `/translate`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "text": "Chinese text to translate",
    "options": {} // Optional translation options
  }
  ```
- **Response**:
  ```json
  {
    "translated_text": "Translated text",
    "metadata": {
      "status": "success",
      "source_length": 10,
      "translated_length": 15
    }
  }
  ```

## API Documentation
When the server is running, access:
- Swagger UI: `http://localhost:2210/docs`
- ReDoc: `http://localhost:2210/redoc`

## Technologies

- **Framework**: FastAPI
- **Translation Engine**: QTEngine
- **CORS**: Fully configurable Cross-Origin Resource Sharing
- **Documentation**: Automatic Swagger UI support

## Dependencies
- FastAPI
- Uvicorn
- Pydantic
- Python-dotenv
- Watchdog

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
[Specify your license here]

## Contact
[Add contact information or support details]
