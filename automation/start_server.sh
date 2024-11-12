#!/bin/bash
echo "Starting FastAPI server..."
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
