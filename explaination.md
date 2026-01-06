# Task 1 - Rating Prediction Summary

1. The Prompts Used
    V1 (The Expert): A basic "professional" prompt. I used this to see how the AI handles reviews with no special instructions.

    V2 (The Brutal): I told the AI to be a "Brutal analyzer." I did this to see if a harsher personality would better catch small complaints that people usually ignore.

    V3 (The Conservative): I told the AI to be careful and only give extreme scores (1 or 5) if the text was very strong. I added "Output nothing else" to keep the JSON clean.

# Model Evaluation Results

| Strategy      | Accuracy | JSON Validity | Note                                                   |
|---------------|----------|---------------|--------------------------------------------------------|
| V1: Expert    | 61%      | 100%          | Often missed the mark on 3-star reviews.               |
| V2: Brutal    | 67%      | 100%          | Better at catching negatives, but a bit too mean.      |
| V3: Conservative | 70%   | 100%          | Best. It stayed calm and looked for real evidence.     |


2. Result difference
V1 vs V2: Switching from a "general expert" to a "brutal" persona gained me 6% in accuracy. This happened because the "Brutal" prompt stopped the AI from being too "nice" to bad businesses. It was better at seeing when a customer was actually unhappy.
V2 vs V3: Moving to the "Conservative" prompt got me the best result (70%). By telling the AI to not jump to conclusions and only score what is explicitly written, it stopped making wild guesses. This proves that for Yelp reviews, a "cautious" AI is more accurate than an "emotional" one.

```
Reliability: My microservice was 100% reliable for JSON formatting. Even though I changed the AI's personality, the code never broke because the instructions to "Return ONLY JSON" were kept in every prompt.
```