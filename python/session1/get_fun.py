import random
import json
import os

file_path = os.path.join(os.path.dirname(__file__), "data.json")

with open(file_path, "r") as file:
    responses = json.load(file)

def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(responses["default"])