import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# Initialize FastAPI app
app = FastAPI()

# Configure Nebius OpenAI-compatible client
client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY")  # set your key in environment
)

# Request schema
class ReviewRequest(BaseModel):
    system_prompt: str
    review: str

@app.post("/analyze")
async def analyze_review(req: ReviewRequest):
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-fast",
        messages=[
            {"role": "system", "content": req.system_prompt},
            {"role": "user", "content": [{"type": "text", "text": req.review}]}
        ],
        response_format={"type": "json_object"} # Force JSON if the model supports it
    )
    # return {"review": req.review, "ai_response": response.choices[0].message.content}
    import json
    import re
    
    ai_content = response.choices[0].message.content
    
    # Try to extract JSON from response
    try:
        # Remove markdown code blocks if present
        cleaned = re.sub(r'```json\s*|\s*```', '', ai_content)
        cleaned = cleaned.strip()
        
        # Parse JSON
        parsed = json.loads(cleaned)
        return parsed
    except:
        # If parsing fails, return error structure
        return {
            "predicted_stars": None,
            "explanation": "Failed to parse JSON",
            "raw_response": ai_content
        }

