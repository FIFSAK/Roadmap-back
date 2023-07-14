# Roadmap assistant - backend

## Fill envs:

```
OPENAI_API_KEY
SERPAPI_API_KEY
PASSWORD_MONGODB
```

## How to local run with docker:

### Run:

1. `docker build -t app .`
2. `docker run -dp 8080:8080 app`

## How to local run with uvicorn:

### Run:
1. `pip install --no-cache-dir --upgrade -r requirements.txt`
2. `uvicorn main:app --reload`

