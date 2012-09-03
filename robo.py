#!/usr/bin/env python

"""
Licenses:

Affirmation text:  Creative Commons Share and Share-Alike
Code:  GPL
"""

import os
import random
import sys
import subprocess
import time


# will be file
affirmations = [
"Let every part of this test sequence take you deeper into relaxation and readiness.",
"""Think of yourself as a giant windmill.""",
"You are an enormously powerful machine, engineered to precise tolerances.",
"You harness the wind better by facing it.",
"You produce green energy, without waste.",
"Each gust of wind moves you further toward readiness, and relaxation.",
"With each rotation of your blades, go into deeper relaxation and readiness.",
"These orders are understood.",
"As your blades revolve, feel any tension in your central pivot disappear.",
"Sunlight creates wind and heats your metal skin.  You skin stretches and bends to right size and shape.",
"Let the warm sun take you further into relaxation and readiness.",
"You are well-lubricated.",
"Your blades tilt to just the right angle for optimal efficiency.",
"Your co-pilot helps direct you in the right direction.",
"You were designed for this task.  All is as designed.",
"Your base is flexible but secure.  All vibrations move you closer to readiness and transformation.",
"Energy pulse within you.",
"New life pulses within you.",
"""With each surge, you transform the wind into power.  Power to birth your baby.""",
"These orders are understood.",
"At the sound of the tone, you will go forty-seven percent further into relaxation.",
"Wind capture is complete.",
"Your skin is strong and flexible, and able to withstand sun and rain.",
"You are ninety feet tall and made of metal.",
"Your co-pilot will signal you when ready to exit.  Let these signals take you further into relaxation.",
"Energy reserves are adequate for the next phase of the transformation.",
"Now beginning transformation sequence.  System messages indicate progress.",
"Automated system checks indicate you are operating within normal parameters.",
"Upon completion, you will help release your copilot by opening the hatch.",
"These orders are understood.",
"As your blades transform into arms, release any tension where they join your body.",
"Feel your base diverge into two well-grounded legs.  Feel how flexible they are.",
"All noises you hear are normal parts of co-pilot exit sequence.  Let each tone take you further into the transformation",
"All fluids are at appropriate levels.",
"Your copilot is preparing to exit, and knows how to exit the hatch safely.",
"You hatch is exactly the right size to allow your copilot safe passage.",
"Test sequences have shown that all systems will work correctly.  You work well as a team.   You have practiced this."
"Test sequence complete.",
"You are now returning to low-power mode."
]


os.system('clear')
delay = 2
if sys.argv[1:]:  delay = float(sys.argv[1])
for x in affirmations:
	print x
	subprocess.call(["say",x,"-v","Vicki",'-r','150'])
	time.sleep(delay)
