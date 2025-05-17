# Uses OpenAI to critique resume
import openai

def critique_resume(text):
    prompt = f"Critique this resume content and suggest improvements:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
