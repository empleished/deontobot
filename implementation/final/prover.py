import antlr3
import antlr3.tree
import antlr3.tokens

from parser import *
from rules import *
from checks import *
from getters import *
from create import *

steps = []

def addSteps(initial, final, transform, rule): 
	global steps 
	steps = steps + [[initial, final, transform, rule]]
# run logical rules on tree
def isProven(facts, goals):
	proven = False
	for fact in facts:
		facts = facts + decomposingConjunction(fact)

	for goal in goals: 
		for fact in facts:
			if isEqual(fact.getChild(0), goal.getChild(0)):
				proven = True
		if proven == False: 
			return proven

	return proven

def proofStrategy(goals, facts, rules):
	global steps
	proven = False
	progress = True

	# check goal is not already in facts
	proven = isProven(facts, goals)

	# go through rules
	while (proven == False and progress == True): 
		factSize = len(facts)
		for rule in rules:
			newFacts = []
			steps = []

			mpResults = tryModusPonens(facts, rule)
			newFacts = newFacts + mpResults[0]
			steps = steps + mpResults[1]

			mtResults = tryModusTollens(facts, rule)
			newFacts = newFacts + mtResults[0]
			steps = steps + mtResults[1]			

			#newFacts = newFacts + tryDisjunctiveSyllogism(facts, rule)
#			newFacts = newFacts + ruleOfSyllogism(rule)		
			for f in newFacts: 
				if contains(f, facts) == False: 
					facts = facts + [f]
				else: 
					print "contains"

		if len(facts) == factSize:
			progress = False
		
		proven = isProven(facts, goals)

	# convert steps list to a string
	proofSteps = stepsToString()

	return [proven] + [proofSteps]

def runProver(tree):
	terms = getTerms(tree)
	rules = getRules(tree)
	facts = getFacts(tree)
	goals = getGoals(tree)

	proverSteps = proofStrategy(goals, facts, rules)

	if proverSteps[0] == False:
		print "STATUS: failure"
	else:
		print proverSteps[1]
		print "\nSTATUS: success"

	count = 1

tree = getTree()
runProver(tree)
