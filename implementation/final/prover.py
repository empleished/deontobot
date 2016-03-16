import antlr3
import antlr3.tree
import ast
import parser
from tree import *

# returns the negation of a fact
#def negation(fact):
#	negatedFact = Tree("PREF")
#	negatedFact.add = "not"
#	negatedFact.add = fact
#
#	return negatedFact

#TODO keep as ast, make new node and then setChildren(fact)
def negation(fact): 
	negatedFact = antlr3.tree.CommonTree(fact)
	negatedFact.setParent("not")

	return negatedFact

# checks whether node is a negation
def isNegation(node): 
	if node.getText() == "not":
		return True
	else: 
		return False

# checks whether two nodes are equal
def isEqual(firstNode, secondNode): 
	# for child in firstNode, child in secondNode
	# if all the same then equal == true
	equal = True

#	print firstNode
#	print secondNode

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

def modusPonens(fact, node):
# if P and P -> Q then Q
	print "modus"
	if node.getText() == "IFTHEN":
		if isEqual(node.getChild(0), fact):
			return node.getChild(2)
		else: 
			return None

def tryModusPonens(facts, node): 
	newFacts = []
	print "try modus"
	for fact in facts: 
		print fact, "=fact"
		newFact = modusPonens(fact, node)
		if newFact != None: 
			newFacts += newFact

	return newFacts

def modusTollens(fact, node):
# if not Q and P -> Q then not P
	if isNegation(fact): 
		if node.getText() == "IFTHEN": 
			if isEqual(node.getChild(2), negation(fact)): 
				return negation(node.getChild(0))
			else: 
				return None

def tryModusTollens(facts, node): 
	newFacts = []

	for fact in facts: 
		newFact = modusTollens(fact, node)
		if newFact != None: 
			newFacts += newFact

	return newFacts

def disjunctiveSyllogism(fact, node):
# if not P and (P or Q) then Q
	if isNegation(fact): 
		if node.getText() == "or": 
			if isEqual(node.getChild(0), negation(fact)): 
				return node.getChild(2)
			else: 
				return None

def tryDisjunctiveSyllogism(facts, node): 
	newFacts = []

	for fact in facts: 
		newFact = disjunctiveSyllogism(fact, node)
		if newFact != None: 
			newFacts += newFact

	return newFacts

#TODO fix - keep as ast
#def deMorgansLaw(node):
# not (P or Q) is equivalent to not P and not Q
# not (P and Q) is equivalent to not P or not Q
#	if node.left == "not": 
#		if node.right.value == "or":
#			newNode.value = "and"			
#			newNodeFirstChild = "PREF"
#			newNodeSecondChild = "PREF"
#			newNodeFirstChild.left = "not"
#			newNodeFirstChild.right = node.right.left
#			newNodeSecondChild.left = "not"
#			newNodeSecondChild.right = node.right.right
#			newNode.left = newNodeFirstChild
#			newNode.right = newNodeSecondChild
#		if node.right.value == "and":
#			newNode.value = "or"
#			newNodeFirstChild = "PREF"
#			newNodeSecondChild = "PREF"
#			newNodeFirstChild.left = "not"
#			newNodeFirstChild.right = node.right.left
#			newNodeSecondChild.left = "not"
#			newNodeSecondChild.right = node.right.right
#			newNode.left = newNodeFirstChild
#			newNode.right = newNodeSecondChild
#
#	return newNode

# fix - keep as ast
#def ruleOfSyllogism(tree):
# if (P -> Q) and (Q -> R) then P -> R
#	nodes = Tree()
#	newNode.value = "IFTHEN"
#
#	for node in tree.getChildren(): 
#		if node.value == "IFTHEN":
#			p = node.left
#			q = node.right
#
#			for node in tree.getChildren(): 
#				if node.value == "IFTHEN": 
#					if node.left == q: 
#						r = node.right
#						newNode.left = p
#						newNode.right = r
#						nodes.add(newNode)
#
#	return nodes

def decomposingConjunction(node):
# if (P and Q) then P, Q
	facts = []

	if node.getText() == "and":
		facts = facts + [node.getChild(0)] + [node.getChild(2)]

	return facts

# run logical rules on tree

def isProven(facts, goals):
	proven = False

	for fact in facts: 
		print fact, ", "
	print "\n"

	for goal in goals: 
		for fact in facts:
#			print fact.getChild(0), "=fact"
#			print goal.getChild(0), "=goal"
#			print isEqual(fact, goal)
			if isEqual(fact, goal):
				proven = True
#				print proven, "=proven"
		if proven == False: 
			return proven

	return proven

def proofStrategy(goals, facts, rules):
	proven = False
	steps = []
	progress = True
	factSize = len(facts)

	while (proven == False and progress == True): 
		for rule in rules:
			# try all combinations
			facts = facts + tryModusPonens(facts, rule)
			facts = facts + tryModusTollens(facts, rule)
			facts = facts + tryDisjunctiveSyllogism(facts, rule)
#			facts = facts + deMorgansLaw(rule)
#			facts = facts + ruleOfSyllogism(rule)
			facts = facts + decomposingConjunction(rule)			
		if len(facts) == factSize:
			progress = False
		proven = isProven(facts, goals)

	return [proven] + steps

def getTerms(tree): 
	terms = {}

	for node in tree.getChildren(): 
		if node.getText() == "TERM": 
			terms["symbol"] = node.getChild(0)
			terms["term"] = node.getChild(2)
			#node.getChildren(1) is ': '

	return terms

def getRules(tree): 
	rules = []

	for node in tree.getChildren(): 
		if node.getText() == "RULE": 
			rules = rules + [node.getChild(2)]

	return rules

def getFacts(tree): 
	facts = []

	for node in tree.getChildren(): 
		if node.getText() == "FACT": 
			facts = facts + [node.getChild(2)]

	return facts

def getGoals(tree): 
	goals = []

	for node in tree.getChildren(): 
		if node.getText() == "GOAL": 
			goals = goals + [node.getChild(2)]

	return goals

def runProver(tree):
	terms = getTerms(tree)
	rules = getRules(tree)
	facts = getFacts(tree)
	goals = getGoals(tree)

	proverSteps = proofStrategy(goals, facts, rules)

	print "proverSteps[0]: ", proverSteps[0]
	if proverSteps[0] == False:
		print "statement is incongruent with provided facts"
	else:
		print "statement is coherent with provided facts"

	count = 1

	#TODO modify to look up values of IDs in terms dictionary
	while count < len(proverSteps): 
		print proverSteps[count][0] + ": " + proverSteps[count][1]
		count += 1

tree = parser.runParser("tests/impl-ob-success.deo")
runProver(tree)
