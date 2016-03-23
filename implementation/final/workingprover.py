import antlr3
import antlr3.tree
import antlr3.tokens
import parser

steps = []

#initial, final, transform, rule
def addSteps(oldFact, newFact, node, rule): 
	global steps 
	steps = steps + [[oldFact, newFact, node, rule]]

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

def stepsToString(): 
	global steps
	count = 0
	string = ""

	while count < len(steps): 
		string += "\n\nStep " + str(count + 1) + ": \n"
		initial = steps[count][0]
		final = steps[count][1]
		transform = steps[count][2]
		rule = steps[count][3]

		string += "INITIAL: " + processStepBit(initial) + "\nFINAL: " + processStepBit(final) + "\nTRANSFORM: " + processStepBit(transform) + "\nRULE: " + rule
		
		count += 1

	return string[2:]

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

def createNodeWithChildren(tokenText, children): 
	node = createNode(tokenText)
	node.addChildren(children)

	return node

# returns the negation of a fact
def negation(fact): 
	if (isNegation(fact.getChild(0))): 
		negatedFact = createNodeWithChildren("fact", [fact.getChild(0).getChild(0)])
		parser.print_tree(negatedFact, 0)
	else: 
		negNode = createNodeWithChildren("not", [fact.getChild(0)])
		negatedFact = createNodeWithChildren("fact", [negNode])

	return negatedFact

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

def tryModusPonens(facts, node): 
	newFacts = []
	count = 0

	if isCond(node.getChild(0)): 
		for fact in facts: 
			if isEqual(node.getChild(0).getChild(0), fact.getChild(0)):
				new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
				newFacts += [new]
				addSteps(fact, new, node.getChild(0), "modus ponens")
			else: 
				tryModusPonens(facts, node.getChild(0))

		if isAnd(node.getChild(0).getChild(0)): 
			match = False
			i = 0

			while i < len(facts) - 1: 
				f1 = facts[i]

				# check f1 matches either of nodes children
				match = checkBothChildren(node.getChild(0).getChild(0), f1.getChild(0))

				if match: 
					j = i + 1 

					while j < len(facts): 
						f2 = facts[j]
						# check f2 matches either of nodes children
						match = checkBothChildren(node.getChild(0).getChild(0), f2.getChild(0))

						if match: 
							new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
							newFacts += [new]
							addSteps(fact, new, node.getChild(0), "modus ponens")
						else: 
							tryModusPonens(facts, node.getChild(0))
						j += 1
				i += 1

		if isOr(node.getChild(0).getChild(0)): 
			match = False
			for fact in facts: 
				match = checkBothChildren(node.getChild(0).getChild(0), fact.getChild(0))

				if match: 
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					addSteps(fact, new, node.getChild(0), "modus ponens")
				else: 
					tryModusPonens(facts, node.getChild(0))

		elif isIOP(node.getChild(0).getChild(0)): 
			for fact in facts: 
				if isEqual(node.getChild(0).getChild(0).getChild(0), fact.getChild(0)):
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					addSteps(fact, new, node.getChild(0), "modus ponens")
				else: 
					tryModusPonens(facts, node.getChild(0))

		count += 1

	return newFacts

def tryModusTollens(facts, node): 
	newFacts = []
	count = 0

	if isCond(node.getChild(0)): 
		for fact in facts: 
			neg = negation(fact)

			if isEqual(node.getChild(0).getChild(1), neg.getChild(0)):
				negFact = createNodeWithChildren("not", [node.getChild(0).getChild(0)])
				new = createNodeWithChildren("fact", [negFact])
				newFacts += [new]
				addSteps(fact, new, node.getChild(0), "modus tollens")
			else: 
				tryModusTollens(facts, node.getChild(0))

		if isAnd(node.getChild(0).getChild(0)): 
			match = False
			i = 0

			while i < len(facts) - 1: 
				f1 = facts[i]

				n1 = negation(f1)

				# check f1 matches either of nodes children
				match = checkBothChildren(node.getChild(0).getChild(0), f1.getChild(0))

				if match: 
					j = i + 1 

					while j < len(facts): 
						f2 = facts[j]
						n2 = negation(f2)
						# check f2 matches either of nodes children
						match = checkBothChildren(node.getChild(0).getChild(0), n2.getChild(0))

						if match: 
							new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
							newFacts += [new]
							addSteps(fact, new, node.getChild(0), "modus tollens")
						else: 
							tryModusTollens(facts, node.getChild(0))
						j += 1
				i += 1

		if isOr(node.getChild(0).getChild(0)): 
			match = False
			for fact in facts: 
				neg = negation(fact)
				match = checkBothChildren(node.getChild(0).getChild(0), neg.getChild(0))

				if match: 
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					addSteps(fact, new, node.getChild(0), "modus tollens")
				else: 
					tryModusTollens(facts, node.getChild(0))

		elif isIOP(node.getChild(0).getChild(0)): 
			for fact in facts: 
				neg = negation(fact)
				if isEqual(node.getChild(0).getChild(0).getChild(0), neg.getChild(0)):
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					addSteps(fact, new, node.getChild(0), "modus tollens")
				else: 
					tryModusTollens(facts, node.getChild(0))

		count += 1
	return newFacts

'''
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
			addSteps(fact, new, node.getChild(0), "disjunctive syllogism")

	return newFacts
'''
def decomposingConjunction(node):
# if (P and Q) then P, Q
	facts = []
	if node.getChild(0) is not None: 
		if isAnd(node.getChild(0)):
			first = createNode(node.getText())
			second = createNode(node.getText())

			first.addChildren([node.getChild(0).getChild(0)])
			second.addChildren([node.getChild(0).getChild(1)])

			facts = facts + [first] + [second]

			addSteps(node, first, node.getChild(0), "decomposing conjunction")
			addSteps(node, second, node.getChild(0), "decomposing conjunction")
		elif isPOP(node.getChild(0)): 
			facts = facts + decomposingConjunction(node.getChild(0))

	return facts

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

def contains(i, l): 
	for item in l: 
		if isEqual(i, item): 
			return True

	return False

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
			newFacts = newFacts + tryModusPonens(facts, rule)
			newFacts = newFacts + tryModusTollens(facts, rule)
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

def getTerms(tree): 
	terms = {}

	for node in tree.getChildren(): 
		if node.getChild(0).getText() == "TERM": 
			terms["symbol"] = node.getChild(0).getChild(0).getText()
			terms["term"] = node.getChild(0).getChild(1).getText()[1:-1]

	return terms

def getRules(tree): 
	return getEntities(tree, "rule")

def getFacts(tree): 
	return getEntities(tree, "fact")

def getGoals(tree): 
	return getEntities(tree, "goal")

def getEntities(tree, entityType): 
	entities = []

	for node in tree.getChildren(): 
		if node.getChild(0).getText() == entityType: 
			entities = entities + [node.getChild(0)]

	for entity in entities: 
		entities = entities + decomposingConjunction(entity.getChild(0))

	return entities

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

tree = parser.getTree()
runProver(tree)
