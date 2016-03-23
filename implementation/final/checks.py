from parser import *
from rules import *
from checks import *
from getters import *
from create import *

# checks whether node is a negation
def isNegation(node): 
	if node.getText() == "not":
		return True
	else: 
		return False

# checks whether two nodes are equal
def isEqual(firstNode, secondNode): 
	equal = True

	if firstNode.getText() == secondNode.getText(): 
		firstChildren = firstNode.getChildCount()
		secondChildren = secondNode.getChildCount() 

		if firstChildren == secondChildren: 
			for i in range(firstChildren): 
				equal = isEqual(firstNode.getChild(i), secondNode.getChild(i))
		else: 
			return False
	else: 
		return False	

	return equal

# checks whether either child of the first node equals the second
def checkBothChildren(first, second): 
	if isEqual(first.getChild(0), second):
		return True
	elif isEqual(first.getChild(1), second):
		return True
	else:
		return False

def isCond(node): 
	if node.getText() == "IFTHEN": 
		return True
	else: 
		return False

def isAnd(node): 
	if node.getText() == "and": 
		return True
	else: 
		return False

def isOr(node): 
	if node.getText() == "or": 
		return True
	else: 
		return False

def isIOP(node):
	if isOr(node) or isAnd(node): 
		return True
	else: 
		return False

def isOB(node): 
	if node.getText() == "OB": 
		return True
	else: 
		return False

def isPRO(node): 
	if node.getText() == "PRO": 
		return True
	else: 
		return False

def isPER(node): 
	if node.getText() == "PER": 
		return True
	else: 
		return False

def isPOP(node): 
	if isOB(node) or isPRO(node) or isPER(node) or isNegation(node): 
		return True
	else: 
		return False

def isFact(node): 
	if node.getText() == "fact": 
		return True
	else: 
		return False

def isRule(node): 
	if node.getText() == "rule": 
		return True
	else: 
		return False
	
def isGoal(node): 
	if node.getText() == "goal": 
		return True
	else: 
		return False

def isDecl(node): 
	if isFact(node) or isRule(node) or isGoal(node): 
		return True
	else: 
		return False

def contains(i, l): 
	for item in l: 
		if isEqual(i, item): 
			return True

	return False
