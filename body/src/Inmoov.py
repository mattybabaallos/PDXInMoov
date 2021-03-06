#!/bin/python
"""
This module are Inmoov!

Authors:
    Brett Creeley
    Matty Baba Allos
"""
import json
import time
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
        obj["default_angle"],
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



        self.head = Head(
                filter(lambda x: x.name == "head_x" ,servos)[0],
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
        self.right_shoulder = Shoulder(
            filter(lambda x: x.name == "right_shoulder_flexion" ,servos)[0],
            filter(lambda x: x.name == "right_shoulder_abduction" ,servos)[0],
            filter(lambda x: x.name == "right_shoulder_rotation_x" ,servos)[0],
            filter(lambda x: x.name == "right_shoulder_rotation_y" ,servos)[0])


        self.right_arm = Arm(self.right_forearm,self.right_shoulder)

        #Left side
        self.left_wrist = Wrist(filter(lambda x: x.name == "left_wrist" ,servos)[0])
        self.left_hand = Hand(
            Finger(filter(lambda x: x.name == "left_pinky" ,servos)[0]),
            Finger(filter(lambda x: x.name == "left_ring" ,servos)[0]),
            Finger(filter(lambda x: x.name == "left_middle" ,servos)[0]),
            Finger(filter(lambda x: x.name == "left_index" ,servos)[0]),
            Finger(filter(lambda x: x.name == "left_thumb" ,servos)[0])
        )
        self.left_forearm = Forearm(self.left_hand,self.left_wrist)
        self.left_shoulder = Shoulder(
            filter(lambda x: x.name == "left_shoulder_flexion" ,servos)[0],
            filter(lambda x: x.name == "left_shoulder_abduction" ,servos)[0],
            filter(lambda x: x.name == "left_shoulder_rotation_x" ,servos)[0],
            filter(lambda x: x.name == "left_shoulder_rotation_y" ,servos)[0])

        self.left_arm = Arm(self.left_forearm,self.left_shoulder)

        self.initialize()


    def do_motion(self, motion_id):
        """
            Make InMoov do one of these motions
        """
        if motion_id == 0:
                self.wave()
        elif motion_id == 1:
                self.point()
		time.sleep(5)
		self.wave()
        elif motion_id == 2:
                self.initialize()


    def wave(self):
	self.left_arm.forearm.hand.off()
	self.left_arm.shoulder.rotation_up(-20)
        self.left_arm.shoulder.rotation_internal(60)
	self.left_arm.shoulder.abduction_up(-90)
	time.sleep(2)
	self.left_arm.shoulder.abduction_up(60)
	time.sleep(0.5)
	time.sleep(2)
	self.left_arm.shoulder.abduction_up(90)
	time.sleep(1.5)
	self.left_arm.shoulder.abduction_up(0)
	time.sleep(2)
	self.left_arm.shoulder.abduction_up(90)
	time.sleep(1.5)
	self.left_arm.shoulder.abduction_up(0)

	self.left_arm.shoulder.rotation_up(-20)
        self.left_arm.shoulder.flex(90)
        self.left_arm.shoulder.rotation_internal(60)

    def point(self):
	self.left_arm.shoulder.rotation_up(-20)
        self.left_arm.shoulder.rotation_internal(60)
        time.sleep(3)

        self.left_arm.shoulder.rotation_internal(90)
        self.left_arm.forearm.hand.make_fist()
        self.left_arm.shoulder.rotation_up(60)
        self.left_arm.forearm.hand.straighten_all_fingers()
    def thumbs_down(self):
        pass
    def goodbye(self):
        pass

    def initialize(self):
        """initializes InMoov"""
        self.head.initialize()
        self.left_arm.initialize()
    def off(self):
        """Turns InMoov off"""
        self.head.off()
        self.left_arm.off()
        self.right_arm.off()
