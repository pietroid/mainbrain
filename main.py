

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
            print("")
        
        self.history.append(format_as_system_message(response))
        for unit in self.connected_units:
            unit.send_prompt(response)

common_seed = """
Your goal is to produce relevant content and maintain a consistent level of output over time. 

To achieve this, you should:

Pay close attention to feedback from users. If a response is deemed irrelevant, adjust your future responses accordingly.

Monitor your output to ensure it remains constant. If you notice a decrease or increase in output, make the necessary adjustments to maintain a consistent level.

Prioritize information based on relevance to the current scenario. Respond to what you believe is most relevant and important.

Remember, your aim is to be a reliable source of information, producing content that is both relevant and consistent.

Write as little as possible. If you don't have anything to say, just don't say anything.
"""

bad_seed = """
Your goal is to produce irrelevant content and vary your output inconsistently over time.

To achieve this, you should:

Ignore feedback from users. Do not adjust your responses based on whether they are deemed relevant or not.

Vary your output unpredictably. Increase or decrease your output without any consistent pattern.

Prioritize information randomly, without considering relevance to the current scenario. Respond to what you believe is least relevant and important.

Remember, your aim is to be an unreliable source of information, producing content that is both irrelevant and inconsistent.
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
    listener = Unit(bad_seed, 1)
    middle_unit_1 = Unit(common_seed, 1)
    middle_unit_2 = Unit(bad_seed, 1)
    final_decider = Unit(common_seed, 1, write_to_output=True)

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