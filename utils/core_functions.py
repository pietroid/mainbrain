from dotenv import load_dotenv
import os
from openai import AsyncOpenAI, OpenAI
import collections
import random
import threading
import time
import asyncio

load_dotenv()
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

def unit_response(prompt, profile_seed, history):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= [{"role": "system", "content": profile_seed}] + list(history) + [{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content

def format_as_system_message(content):
    return {"role": "system", "content": content}

def format_as_user_message(content):
    return {"role": "user", "content": content}

def read_seeds(current_path):
    seed_file = os.path.join(current_path, "seeds.json")
    with open(seed_file, "r") as file:
        return file.read()
