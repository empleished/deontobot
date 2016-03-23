from parser import *
from rules import *
from checks import *
from getters import *
from create import *

def processStepBit(bit): 
	string = ""

	if bit is None:
		return ""
	if isDecl(bit): 
		return processStepBit(bit.getChild(0))
	elif isIOP(bit): 
		return "(" + processStepBit(bit.getChild(0)) + " " + bit.getText() + " " + processStepBit(bit.getChild(1)) + ")"
	elif isPOP(bit): 
		return "(" + bit.getText() + " " + processStepBit(bit.getChild(0)) + ")"
	elif isCond(bit): 
		return "(if " + processStepBit(bit.getChild(0)) + " then " + processStepBit(bit.getChild(1)) + ")"
	else: 
		return bit.getText()

def stepsToString(steps): 
	count = 0
	string = ""

	while count < len(steps): 
		string += "\n\nStep " + str(count + 1) + ":\n"
		initial = steps[count][0]
		final = steps[count][1]
		transform = steps[count][2]
		rule = steps[count][3]

		string += "INITIAL: " + processStepBit(initial) + "\nFINAL: " + processStepBit(final) 
		string += "\nTRANSFORM: " + processStepBit(transform) + "\nRULE: " + rule
		
		count += 1

	return string[2:]
