#This file is sandbox workspace to try code in


import json
from Servo import Servo
import time


json_data = None
servos= []
def parse(obj):
    if "body_part" not in obj:
        raise Exception("Could not parse JSON object")
        return
    
    if "disabled" in obj:
        if obj["disabled"] is True:
            return

    servos.append(Servo(
        obj["id"],
        obj["min_pulse"],
        obj["max_pulse"],
        obj["min_degree"],
        obj["max_degree"],
        obj["body_part"]
        ))

with open("inmoov_servo.json") as json_file:
    json_data = json.load(json_file,object_hook=parse)


print servos[0].channel ,servos[0].shield_id

servos[0].rotate(10)
time.sleep(1)
servos[0].off()
