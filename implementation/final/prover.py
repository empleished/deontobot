import antlr3
import parser

''' STEPS '''

steps = []

# add prover step to global steps list
def addSteps(initial, final, transform, rule): 
	global steps 
	steps.append([initial, final, transform, rule])

# process each bit of the prover step for the formatted string
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

# return the list of steps as a formatted string
def stepsToString(): 
	global steps
	count = 0
	string = ""

	while count < len(steps): 
		string += "Step " + str(count + 1) + ": \n"
		initial = steps[count][0]
		final = steps[count][1]
		transform = steps[count][2]
		rule = steps[count][3]

		string += "INITIAL: " + processStepBit(initial) + "\nFINAL: " + processStepBit(final) + "\nTRANSFORM: " + processStepBit(transform) + "\nRULE: " + rule + "\n\n"
		
		count += 1

	return string

''' CREATE NEW NODE '''

# stores tokens in a dictionary
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

# check whether a list l contains an item i 
def contains(i, l): 
	for item in l: 
		if isEqual(i, item): 
			return True

	return False

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
	return isID(node) or isPOP(node)

''' RULES '''

''' NEGATION - if P then not P '''

# returns the negation of a fact
def negation(fact): 
	if (isNegation(fact.getChild(0))): # create new fact without existing negation node
		negatedFact = createNodeWithChildren("fact", [fact.getChild(0).getChild(0)])
	else: 
		negNode = createNodeWithChildren("not", [fact.getChild(0)]) # create a new negation node for the fact
		negatedFact = createNodeWithChildren("fact", [negNode]) # create a new fact for the negation node

	return negatedFact

''' MODUS PONENS - if P and (if P then Q) then Q '''

# recursively check each node of the rule tree to find a match
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

# try and extract a new fact using modus ponens
def modusPonens(facts, rule): 
	match = checkModusPonensMatch(facts, rule.getChild(0))

	if match: 
		new = createNodeWithChildren("fact", [rule.getChild(1)])

		if not(contains(new, facts)): 
			facts.append(new)
			addSteps(rule.getChild(0), new, rule, "modus ponens")

	return facts

# check that the rule is an if...then expression to try modus ponens
def tryModusPonens(facts, rule): 
	if isCond(rule.getChild(0)): 
		facts = modusPonens(facts, rule.getChild(0))

	return facts

''' MODUS TOLLENS - if not Q and (if P then Q) then not P '''

# recursively check each node of the rule tree to find a match
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

# try and extract a new fact using modus tollens
def modusTollens(facts, rule): 
	match = checkModusTollensMatch(facts, rule.getChild(1))
	
	if match: 
		negFact = createNodeWithChildren("not", [rule.getChild(0)])
		new = createNodeWithChildren("fact", [negFact])

		if not(contains(new, facts)): 
			facts.append(new)
			addSteps(rule.getChild(0), new, rule, "modus tollens")
	
	return facts

# check that the rule is an if...then expression to try modus tollens
def tryModusTollens(facts, rule): 
	if isCond(rule.getChild(0)): 
		facts = modusTollens(facts, rule.getChild(0))

	return facts
	
''' DECOMPOSING CONJUNCTION - if (P and Q) then P, Q '''

# recursively check each node of the rule tree to find a match
def decomposeConjunction(node, facts): 
	if isAnd(node): 
		facts = decomposeConjunction(node.getChild(0), facts)
		facts = decomposeConjunction(node.getChild(1), facts)
	if isSingleTerm(node): 
		new = createNodeWithChildren("fact", [node])
		if not(contains(new, facts)): 
			facts.append(new)
			addSteps(node.parent, new, node.parent, "decompose conjunction")
			return facts

	return facts

# try and decompose a conjunction for every fact in the fact set
def tryDecomposingConjunction(facts): 
	for fact in facts: 
		facts = decomposeConjunction(fact.getChild(0), facts)

	return facts

''' O-NECESSITY '''

# look through fact set for obligations and prohibitions
def tryONecessity(facts): 
	for fact in facts: 
		if isOB(fact.getChild(0)): 
			ob = createNodeWithChildren("fact", [fact.getChild(0).getChild(0)]) # create a new fact without OB node

			if not(contains(ob, facts)): 
				facts.append(ob)
				addSteps(fact, ob, fact.getChild(0), "O necessity")

		elif isPRO(fact.getChild(0)): 
			neg = createNodeWithChildren("not", [fact.getChild(0).getChild(0)]) # create a new negation node
			pro = createNodeWithChildren("fact", [neg]) # create a new fact for negation node without PRO node 

			if not(contains(pro, facts)): 
				facts.append(pro)
				addSteps(fact, pro, fact.getChild(0), "O necessity")
				
	return facts

''' SIMPLIFY FACT SET '''

# go through the fact set and break it down further
def simplifyFactSet(facts): 
	progress = True

	# try and decompose facts and find OB/PRO facts
	while progress: 
		factSize = len(facts)
		facts = tryDecomposingConjunction(facts)
		facts = tryONecessity(facts)

		if len(facts) == factSize: # no new facts found
			progress = False

	return facts

''' PROOF STRATEGY '''

# check whether each goal is in the fact set
def isProven(facts, goals):
	proven = False

	for goal in goals: 
		for fact in facts:
			if isEqual(fact.getChild(0), goal.getChild(0)):
				proven = True
		if not(proven): 
			return proven

	return proven

# runs proof strategy with goals, facts and rules
def proofStrategy(goals, facts, rules):
	global steps
	proven = False
	progress = True

	# check goal is not already in facts
	proven = isProven(facts, goals)

	# go through every rule and try and extract more facts
	while (not(proven) and progress): 
		facts = simplifyFactSet(facts)
		factSize = len(facts)

		for rule in rules:
			facts = tryModusPonens(facts, rule)
			facts = tryModusTollens(facts, rule)

		if len(facts) == factSize: # no new facts found
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
			terms["term"] = node.getChild(0).getChild(1).getText()[1:-1] # remove quotes from term

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

	# go through the proof strategy
	proverSteps = proofStrategy(goals, facts, rules)

	# print steps followed by the prover
	print proverSteps[1] 

	# print out a statement of success
	if proverSteps[0] == False:
		print "STATUS: failure"
	else:
		print "STATUS: success"

# get the ANTLR tree from the file parser and run the prover on it
tree = parser.getTree()
runProver(tree)
