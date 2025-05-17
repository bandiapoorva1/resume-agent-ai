# Rewrites weak resume sections
import openai

def enhance_resume(text):
    prompt = f"Rewrite this resume section to make it stronger and metric-driven:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
