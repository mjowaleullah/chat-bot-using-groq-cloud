import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

api = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_API_MODEL")
base_url = os.getenv("GROQ_API_BASE")

client = OpenAI(api_key=api,
                base_url=base_url)

def responser(content):
    """Return Your Message"""

    respons = client.chat.completions.create(
        messages=[
            {
            "role":"system",
            "content": "You are a great story maker, historian, and emotional supporter. Respond carefully and in a slightly funny tone. Use markdown formatting."
        },
        {
            "role" : "user",
            "content": content

        }],
        model= model
        )

    return respons.choices[0].message.content