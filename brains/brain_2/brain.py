import json
from utils.brain import Brain
from utils.unit import Unit
from utils.core_functions import *

current_path = os.path.dirname(os.path.abspath(__file__))
seeds = read_seeds(current_path)
listener_seed = json.loads(seeds)["listener"]
final_decider_seed = json.loads(seeds)["final_decider"]

# Creating Units
listener = Unit("listener", listener_seed, 3, write_to_output=True)
final_decider = Unit("final_decider", final_decider_seed, 3, write_to_output=True)

units = [listener, final_decider]

connections = [
    [listener, final_decider],
]

brain1 = Brain(units, listener, connections)