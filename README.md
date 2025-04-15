# DebugGenie - AI-Powered Code Debugger

## Overview
DebugGenie is a simple FastAPI-based backend for an AI-driven debugger that uses OpenAI GPT-4 to understand and fix code through natural language.

## Features
- Accepts code and natural language questions via API
- Uses GPT-4 for personalized debugging help
- Simple to deploy and integrate with any frontend

## How to Use

### 1. Setup
Create a `.env` file in the root folder with your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Locally
```bash
uvicorn main:app --reload
```

### 4. Deploy
Deploy using Render, Railway, or Fly.io. Make sure to set `OPENAI_API_KEY` in environment variables.