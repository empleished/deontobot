import antlr3
import antlr3.tree
import antlr3.tokens
import ast
import parser
import pprint

steps = []

#initial, final, transform, rule
def addSteps(oldFact, newFact, node, rule): 
	global steps 
	steps = steps + [[oldFact, newFact, node, rule]]

def processStepBit(bit): 
	string = ""
#	print bit, "=bit"
	if bit is None:
		string += ""
		return string
	if isDecl(bit): 
#		print processStepBit(bit.getChild(0)), "=processStepBit(bit.getChild(0)) decl"
		return processStepBit(bit.getChild(0))
	elif isIOP(bit): 
#		print bit, "=bit bit"
#		print (bit.getChild(0) is None), "=processStepBit(bit.getChild(0)) iop"
#		print (bit.getChild(1) is None), "=processStepBit(bit.getChild(1)) iop"
		return "(" + processStepBit(bit.getChild(0)) + " " + bit.getText() + " " + processStepBit(bit.getChild(1)) + ")"
	elif isPOP(bit): 
		return "(" + bit.getText() + " " + processStepBit(bit.getChild(0)) + ")"
	elif isCond(bit): 
#		print (bit.getChild(0) is None), "=processStepBit(bit.getChild(0)) cond"
#		print (bit.getChild(1) is None), "=processStepBit(bit.getChild(1)) cond"
		return "(if " + processStepBit(bit.getChild(0)) + " then " + processStepBit(bit.getChild(1)) + ")"
	else: 
#		print "hi"
		string += bit.getText()
#		print string, "=string"
		return string

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

		string += "INITIAL: " + processStepBit(initial)
		string += "\nFINAL: " + processStepBit(final)
		string += "\nTRANSFORM: " + processStepBit(transform)
		string += "\nRULE: " + rule
		
		count += 1

	return string[2:]

#def printSteps(): 
#	#TODO print properly with content of term IDs
#	global steps
#	print steps, "=steps"
#	count = 0
#
#	print "PROVER STEPS: "
#
#	while count < len(steps): 
#		print "Step ", count + 1, ": "
#		print "old fact: "
#		print steps[count][0], "=old fact"
#		print steps[count][0].getChild(0), "=old fact child"
#		print steps[count][1], "=new fact"
#		print steps[count][2], "=node"
#		print steps[count][3], "=rule"
#		parser.print_tree(steps[count][0], 0)
#		print "new fact: "
#		parser.print_tree(steps[count][1], 0)
#		print "node: "
#		parser.print_tree(steps[count][2], 0)
#		print "rule: "
#		print steps[count][3]
#		count += 1

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
#	print "fact"
#	parser.print_tree(fact, 0)
#	print fact.getText(), "=fact text"
#	print fact.getToken(), "=fact token"
	if (isNegation(fact.getChild(0))): 
#		print "fact is negation"
#		print fact.getChild(0).getToken(), "=fact child token"
#		print fact.getChild(0).getChild(0), "=fact grandchild"
#		negatedFact.setChildIndex(0)
		negatedFact = createNodeWithChildren("fact", [fact.getChild(0).getChild(0)])
		parser.print_tree(negatedFact, 0)
#		addSteps(fact, negatedFact, createNode("not"), "negation")
	else: 
#		print "fact is not negation"
		negNode = createNodeWithChildren("not", [fact.getChild(0)])
		negatedFact = createNodeWithChildren("fact", [negNode])
#		addSteps(fact, negatedFact, createNode("not"), "negation")
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
	if firstNode is not None and secondNode is not None: 
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
	if isOr(node):
		return True
	elif isAnd(node): 
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
	if isOB(node): 	
		return True
	if isPRO(node): 
		return True
	if isPER(node): 
		return True
	if isNegation(node): 
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
	if isFact(node): 
		return True
	if isRule(node): 
		return True
	if isGoal(node): 
		return True
	else: 
		return False

def checkBothChildren(node, fact): 
	if isEqual(node.getChild(0), fact):
		return True
	elif isEqual(node.getChild(1), fact):
		return True
	else:
		return False

def tryModusPonens(facts, node): 
	newFacts = []
#	print "print node:"
#	parser.print_tree(node, 0)
	count = 0

#	print node.getChild(0), "=node child"
#	print isCond(node.getChild(0)), "=node child is cond"
#	print facts

	if isCond(node.getChild(0)): 
#		print "hi"	
		for fact in facts: 
#			print count
#			print "print fact:"
#			parser.print_tree(fact, 0)
			# if fact and node.getChild(0) match
			# create new fact node.getChild(1)
#			print node.getChild(0).getChild(0), "=node grandchild"
#			print fact.getChild(0), "=fact child"

			if isEqual(node.getChild(0).getChild(0), fact.getChild(0)):
				new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
				newFacts += [new]
				addSteps(fact, new, node.getChild(0), "modus ponens")
			else: 
				tryModusPonens(facts, node.getChild(0))
#			print "end cond"

		if isAnd(node.getChild(0).getChild(0)): 
#			print "is and"
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
#			print "is or"
			match = False
			for fact in facts: 
				# check f1 matches either of nodes children
#				print node.getChild(0).getChild(0).getChild(0), "=node great grandchild"
#				print node.getChild(0).getChild(0).getChild(1), "=node great grandchild"
#				print fact.getChild(0), "=fact child"
				match = checkBothChildren(node.getChild(0).getChild(0), fact.getChild(0))

				if match: 
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					addSteps(fact, new, node.getChild(0), "modus ponens")
				else: 
					tryModusPonens(facts, node.getChild(0))

		elif isIOP(node.getChild(0).getChild(0)): 
#			print "else"
			for fact in facts: 
				if isEqual(node.getChild(0).getChild(0).getChild(0), fact.getChild(0)):
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					addSteps(fact, new, node.getChild(0), "modus ponens")
				else: 
					tryModusPonens(facts, node.getChild(0))

		count += 1
#	print "print newfacts:"
#	for f in newFacts: 
#		parser.print_tree(f, 0)
	return newFacts

def tryModusTollens(facts, node): 
	newFacts = []
#	print "print node:"
#	parser.print_tree(node, 0)
	count = 0

#	print node.getChild(0), "=node child"
#	print isCond(node.getChild(0)), "=node child is cond"

	if isCond(node.getChild(0)): 
		for fact in facts: 
#			print "print fact:"
#			parser.print_tree(fact, 0)

			neg = negation(fact)

#			print "print neg:"
#			parser.print_tree(neg, 0)
			# if neg and node.getChild(0) match
			# create new fact node.getChild(1)
#			print node.getChild(0).getChild(0), "=node grandchild"
#			print neg.getChild(0), "=neg child"

			if isEqual(node.getChild(0).getChild(1), neg.getChild(0)):
				#new = createNode("fact")
#				new.addChildren([node.getChild(0)])
#				return negation(new)
#				print "is equal ///"
				negFact = createNodeWithChildren("not", [node.getChild(0).getChild(0)])
				new = createNodeWithChildren("fact", [negFact])
#				print "print new:"
#				parser.print_tree(new, 0)
				newFacts += [new]
				addSteps(fact, new, node.getChild(0), "modus tollens")
			else: 
				tryModusTollens(facts, node.getChild(0))
#			print "end cond"

		if isAnd(node.getChild(0).getChild(0)): 
#			print "is and"
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
#			print "is or"
			match = False
			for fact in facts: 
				# check f1 matches either of nodes children
#				print node.getChild(0).getChild(0).getChild(0), "=node great grandchild"
#				print node.getChild(0).getChild(0).getChild(1), "=node great grandchild"
#				print fact.getChild(0), "=fact child"
				neg = negation(fact)
				match = checkBothChildren(node.getChild(0).getChild(0), neg.getChild(0))

				if match: 
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					addSteps(fact, new, node.getChild(0), "modus tollens")
				else: 
					tryModusTollens(facts, node.getChild(0))

		elif isIOP(node.getChild(0).getChild(0)): 
#			print "else"
			for fact in facts: 
				neg = negation(fact)
				if isEqual(node.getChild(0).getChild(0).getChild(0), neg.getChild(0)):
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					addSteps(fact, new, node.getChild(0), "modus tollens")
				else: 
					tryModusTollens(facts, node.getChild(0))

		count += 1
#	print "print newfacts:"
#	for f in newFacts: 
#		parser.print_tree(f, 0)
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
'''

def tryDisjunctiveSyllogism(facts, node): 
	newFacts = []

	for fact in facts: 
		newFact = disjunctiveSyllogism(fact, node)
		if newFact != None: 
			newFacts += [newFact]
			addSteps(fact, new, node.getChild(0), "disjunctive syllogism")

	return newFacts

def decomposingConjunction(node):
# if (P and Q) then P, Q
	facts = []
#	print node, "=node"
#	print node.getChild(0), "=node child"
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

#	for fact in facts: 
#		print fact.getText(), "=fact"
#		print fact.getChild(0), "=fact child"

	for fact in facts:
		facts = facts + decomposingConjunction(fact)

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
	progress = True
	count = 0
	global steps

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
#			newFacts = newFacts + ruleOfSyllogism(rule)		
			for f in newFacts: 
				if contains(f, facts) == False: 
					facts = facts + [f]
				else: 
					print "contains"

		if len(facts) == factSize:
			progress = False
		
		proven = isProven(facts, goals)
#		print "SO IS IT??"
#		print proven

	proofSteps = stepsToString()

	return [proven] + [proofSteps]

def getTerms(tree): 
	terms = {}

	for node in tree.getChildren(): 
#		print node.getChild(0), "=term node child"
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
#		print node, "=node"
#		print node.getChild(0), "=node child"
		if node.getChild(0).getText() == entityType: 
			entities = entities + [node.getChild(0)]

	for entity in entities: 
		entities = entities + decomposingConjunction(entity.getChild(0))

	return entities

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

	if proverSteps[0] == False:
		print "STATUS: failure"
	else:
		print proverSteps[1]
		print "\nSTATUS: success"

	count = 1

tree = parser.getTree()
runProver(tree)
