@echo off
REM Run the API server locally for testing

cd api
echo Starting API server on http://localhost:8000
echo To use this API, add ?api=http://localhost:8000 to your URL
echo Example: http://localhost:3000?api=http://localhost:8000
echo.
uvicorn main:app --reload --host 0.0.0.0 --port 8000
