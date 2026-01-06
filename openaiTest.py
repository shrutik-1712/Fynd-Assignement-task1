import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key='v1.CmMKHHN0YXRpY2tleS1lMDBjdGRnZDZoejl4ZWU0YTkSIXNlcnZpY2VhY2NvdW50LWUwMHJyY3RmN2VwZnNoN2syMzIMCM__8soGEKmEkK8COgsIz4KLlgcQwLqZBkACWgNlMDA.AAAAAAAAAAGbJIVpItdFDoH3KIlVjkeNjhLa9kKgoooo7TRrqq0N_eTyTChEmHDXGjWvFHFtWmLL3GsoCs0-RboEUG_PL9UM'
)

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-fast",
    messages=[
        {
            "role": "system",
            "content": """HI I am a Meta AI"""
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """who are you"""
                }
            ]
        }
    ]
)

print(response.to_json())