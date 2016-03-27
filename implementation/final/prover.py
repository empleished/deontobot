import antlr3
import antlr3.tree
import antlr3.tokens
import parser

''' STEPS '''

steps = []

def addSteps(oldFact, newFact, node, rule): 
	global steps 
	steps.append([oldFact, newFact, node, rule])

def processStepBit(bit): 
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

''' CREATE NEW NODE '''

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

# calls createNode() then adds children to the new node
def createNodeWithChildren(tokenText, children): 
	node = createNode(tokenText)
	node.addChildren(children)
	return node

''' CHECKS '''

# checks whether two nodes are equal
def isEqual(firstNode, secondNode): 
	equal = True

	if firstNode.getText() == secondNode.getText(): 
		firstChildren = firstNode.getChildCount()
		secondChildren = secondNode.getChildCount() 

		# check nodes have the same number of children
		if firstChildren == secondChildren: 
			for i in range(firstChildren): 
				# recursively check each node's children are equal
				equal = isEqual(firstNode.getChild(i), secondNode.getChild(i))
		else: 
			return False
	else: 
		return False	

	return equal

# checks whether either child of the first node equals the second
def checkBothChildren(first, second): 
	return isEqual(first.getChild(0), second) or isEqual(first.getChild(1), second)

def isFact(node): 
	return node.getText() == "fact"

def isRule(node): 
	return node.getText() == "rule"
	
def isGoal(node): 
	return node.getText() == "goal"

def isDecl(node): 
	return isFact(node) or isRule(node) or isGoal(node)

def isCond(node): 
	return node.getText() == "IFTHEN"

def isAnd(node): 
	return node.getText() == "and"

def isOr(node): 
	return node.getText() == "or"

def isIOP(node):
	return isOr(node) or isAnd(node)

def isNegation(node): 
	return node.getText() == "not"

def isOB(node): 
	return node.getText() == "OB"

def isPRO(node): 
	return node.getText() == "PRO"

def isPER(node): 
	return node.getText() == "PER"

def isPOP(node): 
	return isOB(node) or isPRO(node) or isPER(node) or isNegation(node)

def isID(node):
	return not(isCond(node) or isAnd(node) or isOr(node) or isIOP(node) or isOB(node) or isPRO(node) or isPER(node) or isPOP(node) or isFact(node) or isRule(node) or isGoal(node) or isDecl(node))

def isSingleTerm(node): 
	return isID(node) or isPOP(node) or isNegation(node)

def contains(i, l): 
	for item in l: 
		if isEqual(i, item): 
			return True

	return False

''' RULES '''

# returns the negation of a fact
def negation(fact): 
	if (isNegation(fact.getChild(0))): 
		negatedFact = createNodeWithChildren("fact", [fact.getChild(0).getChild(0)])
	else: 
		negNode = createNodeWithChildren("not", [fact.getChild(0)])
		negatedFact = createNodeWithChildren("fact", [negNode])

	return negatedFact

''' MODUS PONENS - if P and (if P then Q) then Q '''

def checkModusPonensMatch(facts, node): 
	if isCond(node): 
		return checkModusPonensMatch(facts, node)
	if isAnd(node):
		return checkModusPonensMatch(facts, node.getChild(0)) and checkModusPonensMatch(facts, node.getChild(1))
	if isOr(node): 
		return checkModusPonensMatch(facts, node.getChild(0)) or checkModusPonensMatch(facts, node.getChild(1))
	if isSingleTerm(node):
		for fact in facts: 
			if isEqual(node, fact.getChild(0)):
				return True
		return False

def modusPonens(facts, rule): 
	print "trying modus ponens"
	steps = []
	match = False

	match = checkModusPonensMatch(facts, rule.getChild(0))

	if match: 
		new = createNodeWithChildren("fact", [rule.getChild(1)])
		addSteps(rule.getChild(0), new, rule, "modus ponens")
		return new
	else: 
		return None

def tryModusPonens(facts, rule): 
	newFacts = []

	if isCond(rule.getChild(0)): 
		newFacts.append(modusPonens(facts, rule.getChild(0)))

		for fact in newFacts: 
			if fact is not None: 
				if not(contains(fact, facts)): 
					facts.append(fact)

	return facts

''' MODUS TOLLENS - if not Q and (if P then Q) then not P '''

def checkModusTollensMatch(facts, node): 
	if isCond(node): 
		return checkModusTollensMatch(facts, node)
	if isAnd(node):
		return checkModusTollensMatch(facts, node.getChild(0)) and checkModusTollensMatch(facts, node.getChild(1))
	if isOr(node): 
		return checkModusTollensMatch(facts, node.getChild(0)) or checkModusTollensMatch(facts, node.getChild(1))
	if isSingleTerm(node):
		for fact in facts: 
			negFact = negation(fact)

			if isEqual(node, negFact.getChild(0)):
				return True
		return False

def modusTollens(facts, rule): 
	print "trying modus tollens"
	steps = []
	match = False

	match = checkModusTollensMatch(facts, rule.getChild(1))
	
	if match: 
		negFact = createNodeWithChildren("not", [rule.getChild(0)])
		new = createNodeWithChildren("fact", [negFact])
		addSteps(rule.getChild(0), new, rule, "modus tollens")
		return new
	else: 
		return None	

def tryModusTollens(facts, rule): 
	newFacts = []
	if isCond(rule.getChild(0)): 
		newFacts.append(modusTollens(facts, rule.getChild(0)))

		for fact in newFacts: 
			if fact is not None: 
				if not(contains(fact, facts)): 
					facts.append(fact)

	return facts
	
''' DECOMPOSING CONJUNCTION - if (P and Q) then P, Q '''

def decomposeConjunction(node): 
	print "trying decompose conjunction"
	if isAnd(node): 
		return decomposeConjunction(node.getChild(0)), decomposeConjunction(node.getChild(1))
	if isNegation(node) or isID(node): 
		new = createNodeWithChildren("fact", [node])
		return new
	else: 
		return None

def processTuple(tuples, factList): 
	for t in tuples: 
		if type(t) is tuple: 
			factList = processTuple(t, factList)
		else: 
			factList.append(t)
	return factList

def tryDecomposingConjunction(facts): 
	for fact in facts: 
		new = decomposeConjunction(fact.getChild(0))

		if type(new) is tuple: 
			factList = []
			factList = processTuple(new, factList)

			for f in factList: 
				if f is not None: 
					if contains(f, facts) == False: 
						facts.append(f)
						addSteps(fact, f, fact, "decompose conjunction")

	return facts

''' O-NECESSITY '''

def tryONecessity(facts): 
	print "trying o necessity"
	for fact in facts: 
		if isOB(fact.getChild(0)): 
			ob = createNodeWithChildren("fact", [fact.getChild(0).getChild(0)])
			newFact = ob
			if contains(newFact, facts) == False: 
				facts.append(newFact)
				addSteps(fact, newFact, fact.getChild(0), "O necessity")
		elif isPRO(fact.getChild(0)): 
			neg =  createNodeWithChildren("not", [fact.getChild(0).getChild(0)])
			pro = createNodeWithChildren("fact", [neg])
			newFact = pro
			if contains(newFact, facts) == False: 
				facts.append(newFact)
				addSteps(fact, newFact, fact.getChild(0), "O necessity")
				
	return facts

''' SIMPLIFY FACT SET '''

def simplifyFactSet(facts): 
	progress = True

	while progress: 
		factSize = len(facts)
		facts = tryDecomposingConjunction(facts)
		facts = tryONecessity(facts)

		if len(facts) == factSize:
			progress = False

	return facts

''' PROOF STRATEGY '''

def isProven(facts, goals):
	proven = False

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
			facts = tryModusPonens(facts, rule)
			facts = tryModusTollens(facts, rule)
		facts = simplifyFactSet(facts)

		if len(facts) == factSize:
			progress = False
		
		proven = isProven(facts, goals)

	# convert steps list to a string
	proofSteps = stepsToString()

	return proven, proofSteps

''' GETTERS '''

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
			entities.append(node.getChild(0))

	return entities

''' RUN PROVER '''

def runProver(tree):
	# set up terms, rules, facts, goals
	terms = getTerms(tree)
	rules = getRules(tree)
	facts = getFacts(tree)
	goals = getGoals(tree)

	proverSteps = proofStrategy(goals, facts, rules)
	print proverSteps[1] # print steps followed by the prover

	# print out a statement of success
	if proverSteps[0] == False:
		print "STATUS: failure"
	else:
		print "\nSTATUS: success"

tree = parser.getTree()
runProver(tree)
