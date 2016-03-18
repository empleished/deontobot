import antlr3
import antlr3.tree
import antlr3.tokens
import ast
import parser
import pprint

# stores tokens in a dict
def getAllTokens(): 
	tokens = {}
	t = open("Deo.tokens", "r")
	line = t.readline()
	
	while line != "": 
		line = line.split("=")
		tokens["text"] = line[0]
		tokens["id"] = line[1]
		line = t.readline()

	return tokens

# creates a new node from token
def createNode(tokenText): 
	tokens = getAllTokens()
	tokenID = tokens.get(tokenText)
	nodeToken = antlr3.tokens.CommonToken(tokenID, tokenText)
	nodeToken.type = tokenID
	nodeToken.text = tokenText
	node = antlr3.tree.CommonTree(nodeToken)
	
	return node

# returns the negation of a fact
#TODO keep as ast, make new node and then setChildren(fact)
def negation(fact): 
	negatedFact = antlr3.tree.CommonTree(fact)
#	print negatedFact, "=neg fact"
#	print "fact"
	parser.print_tree(fact, 0)
#	print fact.getText(), "=fact text"
#	print fact.getToken(), "=fact token"
	if (isNegation(fact.getChild(0))): 
#		print "fact is negation"
#		print fact.getChild(0).getToken(), "=fact child token"
#		print type(fact.getChild(0).getChild(0)), "=type"
		negatedFact.setChildIndex(0)
		negatedFact.addChildren([fact.getChild(0).getChild(0)])
	else: 
#		print "fact is not negation"
		negNode = createNode("not")
		negNode.addChildren([fact.getChild(0)])
		negatedFact.addChildren([negNode])
#		negatedFact.setChild(0, fact.getChild(0))
		#negatedFact.getChild(0).setChild(fact.getChild(0))

#	print "negated fact:"
#	print negatedFact, "=neg fact"
#	print negatedFact.getChild(0)
#	parser.print_tree(negatedFact, 0)	
#	print "end"

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

#	print firstNode, "=first"
#	print secondNode, "=second"

#	print "equality"
#	print firstNode == secondNode

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
#	print "modus"
	if node.getText() == "IFTHEN":
#		print fact, "=fact"
#		print fact.getChild(0), node.getChild(0)
		if isEqual(node.getChild(0), fact.getChild(0)):
			new = createNode("fact")
			new.addChildren([node.getChild(1)])
			return new
		else: 
			return None

def tryModusPonens(facts, node): 
	newFacts = []

	for fact in facts: 
		newFact = modusPonens(fact, node.getChild(0))
		
		if newFact != None: 
			newFacts += [newFact]

	return newFacts

def modusTollens(fact, node):
# if not Q and P -> Q then not P
#	print "fact: "
#	parser.print_tree(fact, 0)
#	print "node: "
#	parser.print_tree(node, 0)
#	print fact, "=fact"
#	print node, "=node"
	if isNegation(fact.getChild(0)): 
		if node.getText() == "IFTHEN": 
#			print "it's a cond"
#			print node.getChild(1)
#			print fact
#			print fact.getChild(0).getChild(0)
#			print "????????"
			neg = negation(fact)
#			print neg, "=neg"
#			print neg.getChild(0), "=neg child"
			if isEqual(node.getChild(1), neg.getChild(0)): 
#				print "they're equal"
#				print node.getChild(0), "=P"
				new = createNode("fact")
				new.addChildren([node.getChild(0)])
				return negation(new)
			else: 
				return None

def tryModusTollens(facts, node): 
	newFacts = []

	for fact in facts: 
		newFact = modusTollens(fact, node.getChild(0))
		if newFact != None: 
			newFacts += [newFact]

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
			newFacts += [newFact]

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

#	for fact in facts: 
#		print fact.getChild(0), "=fact"

	for goal in goals: 
		for fact in facts:
#			print "IS PROVEN??"
#			print fact.getChild(0), "=fact"
#			print goal.getChild(0), "=goal"
#			print isEqual(fact.getChild(0), goal.getChild(0))
			if isEqual(fact.getChild(0), goal.getChild(0)):
				proven = True
		if proven == False: 
			return proven

	return proven

def contains(i, l): 
	for item in l: 
		if isEqual(i, item): 
			return True

	return False

def proofStrategy(goals, facts, rules):
	proven = False
	steps = []
	progress = True
	count = 0

	proven = isProven(facts, goals)

	while (proven == False and progress == True): 
		factSize = len(facts)
		for rule in rules:
			count += 1
			# try all combinations
			newFacts = []
			newFacts = newFacts + tryModusPonens(facts, rule)
			newFacts = newFacts + tryModusTollens(facts, rule)
			#newFacts = newFacts + tryDisjunctiveSyllogism(facts, rule)
#			newFacts = newFacts + deMorgansLaw(rule)
#			newFacts = newFacts + ruleOfSyllogism(rule)
			#newFacts = newFacts + decomposingConjunction(rule)			
			for f in newFacts: 
				if contains(f, facts) == False: 
					facts = facts + [f]

		if len(facts) == factSize:
			progress = False
		
		proven = isProven(facts, goals)
#		print "SO IS IT??"
#		print proven

	return [proven] + steps

def getTerms(tree): 
	terms = {}

	for node in tree.getChildren(): 
#		print node.getChild(0), "=term node child"
		if node.getChild(0).getText() == "TERM": 
			terms["symbol"] = node.getChild(0).getChild(0).getText()
			terms["term"] = node.getChild(0).getChild(1).getText()[1:-1]

	return terms

def getRules(tree): 
	rules = []

	for node in tree.getChildren(): 
#		print node.getChild(0), "=node"
		if node.getChild(0).getText() == "rule": 
			rules = rules + [node.getChild(0)]

	return rules

def getFacts(tree): 
	facts = []

	for node in tree.getChildren(): 
		if node.getChild(0).getText() == "fact": 
			facts = facts + [node.getChild(0)]
	return facts

def getGoals(tree): 
	goals = []

	for node in tree.getChildren(): 
		if node.getChild(0).getText() == "goal": 
			goals = goals + [node.getChild(0)]

	return goals

def printList(l): 
	for m in l: 
		parser.print_tree(m, 0)

def runProver(tree):
	terms = getTerms(tree)
	rules = getRules(tree)
	facts = getFacts(tree)
	goals = getGoals(tree)

#	print "terms:"
#	pprint.pprint(terms, width=1)
#	print "rules:"
#	printList(rules)
#	print "facts:"
#	printList(facts)
#	print "goals:"
#	printList(goals)
	'''
	print "negation:"
	newFact = negation(facts[0])
	parser.print_tree(newFact, 0)
	'''
	proverSteps = proofStrategy(goals, facts, rules)

#	print "proverSteps[0]: ", proverSteps[0]
	if proverSteps[0] == False:
		print "fail"
	else:
		print "success"

	count = 1

	#TODO modify to look up values of IDs in terms dictionary
#	while count < len(proverSteps): 
#		print proverSteps[count][0] + ": " + proverSteps[count][1]
#		count += 1

#fileName = raw_input("file:")

tree = parser.getTree()
runProver(tree)
