
```markdown

# Fynd assigment Task - 1

# Rating Prediction AI Microservice

## 📂 Project Structure
- **AI_microservice/**
  - `app.py`: FastAPI microservice that exposes an endpoint for analyzing reviews.
  - Run with:
    ```bash
    uvicorn app:app --reload --port 8000
    ```
  - Example request:
    ```bash
    curl -X POST "http://127.0.0.1:8000/analyze" \
    -H "Content-Type: application/json" \
    -d '{"system_prompt":"You are a helpful assistant.","review":"The product was excellent!"}'
    ```
    > You must pass both a `system_prompt` and a `review` in the request body.

- **main.py**  
  - Contains the major code logic.  
  - Loads a CSV file, randomly samples 40 reviews for each star rating (1–5).  
  - Sends these reviews to the AI microservice using `requests` with different system prompts for comparison.

- **comparisiontable.py**  
  - Generates a basic comparison table between prompts.  
  - Results are saved in `explaination.md`.

- **results/**  
  - Contains outputs, including comparison tables and chats from different AI models used during the process.

- **requirements.txt**  
  - Lists all dependencies needed to run the project:
    ```
    fastapi
    uvicorn
    requests
    pandas
    python-dotenv
    openai
    ```

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the FastAPI microservice:
   ```bash
   cd AI_microservice
   uvicorn app:app --reload --port 8000
   ```

3. Go back to the main project folder:
   ```bash
   cd ..
   ```

4. Run the main script:
   ```bash
   python main.py
   ```

5. Generate comparison tables:
   ```bash
   python comparisiontable.py
   ```

---

## 📊 Outputs

- **explaination.md**: Contains explanations and comparisons between different system prompts.  
- **results/**: Includes saved tables and AI chat logs for reference.

