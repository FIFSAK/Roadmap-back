import os
import logging
import dotenv
import openai

dotenv.load_dotenv(dotenv.find_dotenv())


openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure logging

logging.basicConfig(level=logging.INFO)


def make_request(message, prompt, max_tokens = None):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": f"{prompt}"},
            {"role": "user", "content": f"{message}"},
        ],
        max_tokens = max_tokens,
        temperature = 0
    )

    return response['choices'][0]['message']['content']

async def openai_call(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=120,
        temperature=0.5
    )
    return response.choices[0].text.strip()