import pandas as pd
import random
import requests
df = pd.read_csv("yelp.csv",header=0,sep=",")
# print(df.head())
# print(df.columns)

# this gets you the column text 
# column_text = df["text"].tolist()
# print(len(column_text))
# random 200 reviewers
# random_200 = random.sample(column_text,200)
# print(len(random_200))

# for review in random_200:
#     print(review)
#     each_review = 



# col_dict = df.groupby("stars")["text"].apply(list).to_dict()
# print(len(col_dict))
# for stars, reviews in col_dict.items():
#     print(f"Stars: {stars}, Number of reviews: {len(reviews)}")
# Getting the random 200 samples for testing 

sampled_df = (
    df[["stars", "text"]]
    .groupby("stars", group_keys=False)
    .apply(lambda x: x.sample(n=min(40, len(x))))
)

# sampled_df.info()


def get_prediction(review_text, system_prompt):
    url = "http://127.0.0.1:8000/analyze"
    payload = {
        "system_prompt": system_prompt,
        "review": review_text
    }
    try:
        response = requests.post(url, json=payload)
        return response.json() # This should return your {predicted_stars, explanation}
    except Exception as e:
        return {"predicted_stars": None, "explanation": "Error"}

# Example: Running it on your sampled_df

system_prompt_v1 = """You are a review expert. Analyze the review and return ONLY valid JSON with this exact structure:
{
  "predicted_stars": <number from 1 to 5>,
  "explanation": "<brief reasoning>"
}"""

system_prompt_v2 = """You are a Brutal review analyzer. Analyze the review and return ONLY valid JSON with this exact structure:
{
  "predicted_stars": <number from 1 to 5>,
  "explanation": "<brief reasoning>"
}"""

system_prompt_v3 = """You are a conservative review scorer.
Assign stars only when the sentiment is clearly supported by the text.
Avoid extremes unless explicitly stated.
Return ONLY valid JSON exactly as shown:
{
  "predicted_stars": <integer 1–5>,
  "explanation": "<brief evidence-based reasoning>"
}
Output nothing else."""
# Store results
results = []
for index, row in sampled_df.iterrows():
    prediction = get_prediction(row['text'], system_prompt_v3)

    results.append({
        "actual": row['stars'],
        "Orginal_text":row['text'],
        "predicted": prediction.get("predicted_stars"),
        "explanation": prediction.get("explanation"),  
        "is_valid_json": prediction.get("predicted_stars") is not None,    
        })
# print(results)
results_df = pd.DataFrame(results)
results_df.to_csv("results_v3.csv", index=False)

# print(sampled_df.head(10)) 