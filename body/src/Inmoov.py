#!/bin/python
"""
This module are Inmoov!

Authors:
    Brett Creeley
    Matty Baba Allos
"""
import json
from Arm import Arm
from Servo import Servo
from Head import Head
from Hand import Hand
from Forearm import Forearm
from Wrist import Wrist
from Finger import Finger
from Shoulder import Shoulder


INMOOV_FILE = "inmoov_servo.json"
servos = []

def parse(obj):
    if "body_part" not in obj:
        raise Exception("Could not parse JSON object")

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


class Inmoov(object):
    """
    This class are Inmoov!
    """
    def __init__(self):
        """
        Build all of Inmoov's parts.
        """

        #open the file json file
        with open(INMOOV_FILE) as json_file:
            json.load(json_file,object_hook=parse)



        self.head = Head(filter(lambda x: x.name == "head_x" ,servos)[0],
                filter(lambda x: x.name == "head_y" ,servos)[0])

        #Right side
        self.right_wrist = Wrist(filter(lambda x: x.name == "left_wrist" ,servos)[0])
        self.right_hand = Hand(
            Finger(filter(lambda x: x.name == "right_pinky" ,servos)[0]),
            Finger(filter(lambda x: x.name == "right_ring" ,servos)[0]),
            Finger(filter(lambda x: x.name == "right_mid" ,servos)[0]),
            Finger(filter(lambda x: x.name == "right_index" ,servos)[0]),
            Finger(filter(lambda x: x.name == "right_thumb" ,servos)[0])
        )
        self.right_forearm = Forearm(self.right_hand,self.right_wrist)
        self.right_shoulder = Shoulder(filter(lambda x: x.name == "right_shoulder" ,servos)[0],
            filter(lambda x: x.name == "right_shoulder_abduction" ,servos)[0],
            filter(lambda x: x.name == "right_shoulder_flexion" ,servos)[0])

        #Left side
        self.left_wrist = Wrist(filter(lambda x: x.name == "left_wrist" ,servos)[0])
        self.left_hand = Hand(
            Finger(filter(lambda x: x.name == "left_pinky" ,servos)[0]),
            Finger(filter(lambda x: x.name == "left_ring" ,servos)[0]),
            Finger(filter(lambda x: x.name == "left_mid" ,servos)[0]),
            Finger(filter(lambda x: x.name == "left_index" ,servos)[0]),
            Finger(filter(lambda x: x.name == "left_thumb" ,servos)[0])
        )
        self.left_forearm = Forearm(self.left_hand,self.left_wrist)
        self.left_shoulder = Shoulder(filter(lambda x: x.name == "left_shoulder" ,servos)[0],
            filter(lambda x: x.name == "left_shoulder_abduction" ,servos)[0],
            filter(lambda x: x.name == "left_shoulder_flexion" ,servos)[0])


    def off(self):
        """Truns InMoov off"""
        self.head.off()
        self.right_shoulder.off()
        self.right_forearm.off()
        self.left_shoulder.off()
        self.left_forearm.off()
        self.head.off()