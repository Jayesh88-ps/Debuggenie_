from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class DebugRequest(BaseModel):
    code: str
    prompt: str

@app.post("/debug")
async def debug_code(req: DebugRequest):
    message = f"Debug the following code based on this question:\n\nCode:\n{req.code}\n\nQuestion: {req.prompt}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}]
        )

        return {"response": response.choices[0].message['content'].strip()}

    except Exception as e:
        return {"response": f"An error occurred: {str(e)}"}