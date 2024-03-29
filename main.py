

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

class Unit:
    def __init__(self, profile_seed, memory_capacity, write_to_output=False):
        self.profile_seed = profile_seed
        self.history = collections.deque(maxlen=memory_capacity)
        self.connected_units = []
        self.write_to_output = write_to_output

    def connect(self, unit):
        self.connected_units.append(unit)
    #TODO: add async
    def send_prompt(self, prompt):
        self.history.append(format_as_user_message(prompt))

        response = unit_response(prompt, self.profile_seed, self.history)
        
        if self.write_to_output:
            print(response)
        
        self.history.append(format_as_system_message(response))
        for unit in self.connected_units:
            unit.send_prompt(response)

common_seed = """
To ensure adherence to the operational framework and maintain effectiveness, the units are instructed to follow these imperative guidelines:

1. **Prioritize Relevant Content Creation**:
    - Analyze feedback meticulously to assess the relevance of your content. A high similarity between feedback and your output indicates success; adjust accordingly if relevance is not established.
    
2. **Maintain Consistent Information Output**:
    - Ensure a steady and predictable flow of information at all times. Should deviations in your output's volume occur, immediately correct your course to either increase or decrease production, achieving consistency.

3. **Engage Selectively with Pertinent Information**:
    - Listen and respond only to the most relevant information within any scenario. Prioritize your interactions and content generation based on the importance and relevance of the information at hand.
"""
prompt = ""

def receive_input():
    global prompt
    while True:
        prompt = input()

async def process():
    global prompt
    global common_seed

    # Creating Units
    listener = Unit(common_seed, 5)
    middle_unit_1 = Unit(common_seed, 5)
    middle_unit_2 = Unit(common_seed, 5)
    final_decider = Unit(common_seed, 5, write_to_output=True)

    #units = [listener, middle_unit_1, middle_unit_2, final_decider]
    units = [listener, final_decider]

    # Connecting Units
    for unit in units:
        for other_unit in units:
            if unit != other_unit:
                unit.connect(other_unit)

    #loop
    while True:
        if(prompt != ""):
            temp_prompt = prompt
            prompt = ""
            listener.send_prompt(temp_prompt)

def wrap_process():
    asyncio.run(process())


receive_input_thread = threading.Thread(target=receive_input)
process_thread = threading.Thread(target=wrap_process)

receive_input_thread.start()
process_thread.start()