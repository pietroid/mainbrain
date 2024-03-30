import json
from utils.brain import Brain
from utils.unit import Unit
from utils.core_functions import *

current_path = os.path.dirname(os.path.abspath(__file__))
seeds = read_seeds(current_path)
common_seed = json.loads(seeds)["default"]

# Creating Units
listener = Unit(common_seed, 1)
middle_unit_1 = Unit(common_seed, 1)
middle_unit_2 = Unit(common_seed, 1)
final_decider = Unit(common_seed, 1, write_to_output=True)

units = [listener, middle_unit_1, middle_unit_2, final_decider]

connections = [
    [listener, middle_unit_1],
    [middle_unit_1, middle_unit_2],
    [middle_unit_2, middle_unit_1],
    [middle_unit_2, final_decider]
]
#units = [listener, final_decider]

brain1 = Brain(units, listener, connections)