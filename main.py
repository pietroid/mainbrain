from dotenv import load_dotenv
import os
import collections
import random
import threading
import time
import asyncio
from utils.brain import Brain
from utils.core_functions import *
from utils.unit import Unit
import brains.brain_2.brain

## Setting up the used brain
used_brain = brains.brain_2.brain.brain1

## Needed to run the brain
external_receiver = used_brain.receiver
units = used_brain.units

def run_unit(unit):
    while True:
        if(len(unit.input_queue) > 0 and unit.time_since_last_answer() > 5):
            prompts = list(unit.input_queue)
            unit.input_queue.clear()

            response = unit.answer_prompts(prompts)
            unit.send_response(response)

def receive_input():
    global prompt
    while True:
        prompt = input()
        if(prompt != ""):
            external_receiver.add_response_to_queue(prompt)

## Input thread responsible the capture of the user's input
receive_input_thread = threading.Thread(target=receive_input)
receive_input_thread.start()

## Each unit is a separate thread
for unit in units:
    unit_thread = threading.Thread(target=run_unit, args=(unit,))
    unit_thread.start()