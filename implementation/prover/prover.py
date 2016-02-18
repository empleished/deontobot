import ast

# checks if fact is an atom
# returns the fact if it is
# returns a list of decomposed atoms if not
# TODO
def isAtom(fact): 
	return fact

# returns the negation of a fact
# TODO
def negation(fact):
	return fact

def modusPonens(fact, node):
# if P and P -> Q then Q
	facts = []

	if node.value == "IFTHEN":
		if node.left == fact:
			facts = facts + node.right

	return facts

def modusTollens(fact, node):
# if ¬Q and P -> Q then ¬P
	facts = [] 

	if isNegation(fact): 
		if node.value == "IFTHEN": 
			if node.right == negation(fact): 
				facts = facts + isAtom(negation(node.left))

	return facts

def disjunctiveSyllogism(fact, node):
# if ¬P and (P or Q) then Q
	facts = []

	if isNegation(fact): 
		if node.value == "or": 
			if node.left == negation(fact): 
				facts = facts + isAtom(node.right)

	return facts

def deMorgansLaw(node):
# ¬(P or Q) is equivalent to ¬P and ¬Q
# ¬(P and Q) is equivalent to ¬P or ¬Q
	if node.left == "not": 
		if node.right.value == "or":
			newNode.value = "and"			
			newNodeFirstChild = "PREF"
			newNodeSecondChild = "PREF"
			newNodeFirstChild.left = "not"
			newNodeFirstChild.right = node.right.left
			newNodeSecondChild.left = "not"
			newNodeSecondChild.right = node.right.right
			newNode.left = newNodeFirstChild
			newNode.right = newNodeSecondChild
		if node.right.value == "and":
			newNode.value = "or"
			newNodeFirstChild = "PREF"
			newNodeSecondChild = "PREF"
			newNodeFirstChild.left = "not"
			newNodeFirstChild.right = node.right.left
			newNodeSecondChild.left = "not"
			newNodeSecondChild.right = node.right.right
			newNode.left = newNodeFirstChild
			newNode.right = newNodeSecondChild

	return newNode

def ruleOfSyllogism(tree):
# if (P -> Q) and (Q -> R) then P -> R
	nodes = Tree()
	newNode.value = "IFTHEN"

	for node in tree.body: 
		if node.value == "IFTHEN":
			p = node.left
			q = node.right

			for node in tree.body: 
				if node.value == "IFTHEN": 
					if node.left == q: 
						r = node.right
						newNode.left = p
						newNode.right = r
						nodes.add(newNode)

	return nodes

def decomposingConjunction(node):
# if (P and Q) then P, Q
	facts = []

	if node.value == "and":
		facts = facts + isAtom(node.left) + isAtom(node.right)

	return facts

# run logical rules on tree

def isProven(facts, statement):
	proven = false

	for fact in facts:
		if fact == statement:
			proven = true

	return proven

#def try_modus_ponens ():
#        for expr1, expr2 in facts:
#                apply_modus_ponens(expr1, expr2)
#                if proven return

#TODO
def proofStrategy(goals, facts, rules):
	proven = false
	steps = []
	progress = true
	factSize = len(facts)

	while (!proven and progress): 
		for fact in facts:
			for rule in rules.body:
				# try all combinations
			if len(facts) == factSize:
				progress = false

	return proven

#TODO
def yieldFactsFromRules(rules):
	facts = []

	for node in rules.body:
		facts = facts + isAtom(node.left)

	return facts

#TODO
def getTerms(tree): 
	terms.value = "TERMS"

	return terms

#TODO
def getRules(tree): 
	rules.value = "RULES"

	return rules

#TODO
def getFacts(tree): 
	facts = []

	return facts

#TODO
def getGoals(tree): 
	goals.value = "GOALS"

	return goals

def main(argv):
	tree = ast.parse(arg[1])

	terms = getTerms(tree)
	rules = getRules(tree)
	facts = getFacts(tree)
	goals = getGoals(tree)

	newFacts = yieldFactsFromRules(rules)
	facts = facts + newFacts

	proverSteps = proofStrategy(goals, facts, tree)

	if proverSteps[0] = false:
		print "statement is incongruent with provided facts"
	else:
		print "statement is coherent with provided facts"

	count = 1

	while count < proverSteps.length: 
		print proverSteps[count][0] + ": " + proverSteps[count][1]

if __name__ == "__main__":
	main(sys.argv)
