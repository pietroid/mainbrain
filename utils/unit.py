import collections
import time
from utils.core_functions import *

class Unit:
    def __init__(self, profile_seed, memory_capacity, write_to_output=False):
        self.profile_seed = profile_seed
        self.history = collections.deque(maxlen=memory_capacity)
        self.connected_units = []
        self.input_queue = []
        self.write_to_output = write_to_output
        self.last_time_answered = 0

    def time_since_last_answer(self):
        return time.time() - self.last_time_answered

    def add_response_to_queue(self, response):
        self.input_queue.append(response)
    
    def connect(self, unit):
        self.connected_units.append(unit)

    def send_response(self, response):
        for unit in self.connected_units:
            unit.add_response_to_queue(response)
    
    def answer_prompts(self, prompts):
        for prompt in prompts:
            self.history.append(format_as_user_message(prompt))

        response = unit_response(prompt, self.profile_seed, self.history)
        self.last_time_answered = time.time()
        
        if self.write_to_output:
            print(response)
            print("")
        
        self.history.append(format_as_system_message(response))
        return response