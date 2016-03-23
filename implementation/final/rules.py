from parser import *
from rules import *
from checks import *
from getters import *
from create import *

# returns the negation of a fact
def negation(fact): 
	if (isNegation(fact.getChild(0))): 
		negatedFact = createNodeWithChildren("fact", [fact.getChild(0).getChild(0)])
		parser.print_tree(negatedFact, 0)
	else: 
		negNode = createNodeWithChildren("not", [fact.getChild(0)])
		negatedFact = createNodeWithChildren("fact", [negNode])

	return negatedFact

def tryModusPonens(facts, node): 
	newFacts = []
	steps = []
	count = 0

	if isCond(node.getChild(0)): 
		for fact in facts: 
			if isEqual(node.getChild(0).getChild(0), fact.getChild(0)):
				new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
				newFacts += [new]
				steps += [fact, new, node.getChild(0), "modus ponens"]
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
							steps += [fact, new, node.getChild(0), "modus ponens"]
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
					steps += [fact, new, node.getChild(0), "modus ponens"]
				else: 
					tryModusPonens(facts, node.getChild(0))

		elif isIOP(node.getChild(0).getChild(0)): 
			for fact in facts: 
				if isEqual(node.getChild(0).getChild(0).getChild(0), fact.getChild(0)):
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					steps += [fact, new, node.getChild(0), "modus ponens"]
				else: 
					tryModusPonens(facts, node.getChild(0))

		count += 1

	return [newFacts] + [steps]

def tryModusTollens(facts, node): 
	newFacts = []
	steps = []
	count = 0

	if isCond(node.getChild(0)): 
		for fact in facts: 
			neg = negation(fact)

			if isEqual(node.getChild(0).getChild(1), neg.getChild(0)):
				negFact = createNodeWithChildren("not", [node.getChild(0).getChild(0)])
				new = createNodeWithChildren("fact", [negFact])
				newFacts += [new]
				steps += [fact, new, node.getChild(0), "modus tollens"]
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
							steps += [fact, new, node.getChild(0), "modus tollens"]
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
					steps += [fact, new, node.getChild(0), "modus tollens"]
				else: 
					tryModusTollens(facts, node.getChild(0))

		elif isIOP(node.getChild(0).getChild(0)): 
			for fact in facts: 
				neg = negation(fact)
				if isEqual(node.getChild(0).getChild(0).getChild(0), neg.getChild(0)):
					new = createNodeWithChildren("fact", [node.getChild(0).getChild(1)])
					newFacts += [new]
					steps += [fact, new, node.getChild(0), "modus tollens"]
				else: 
					tryModusTollens(facts, node.getChild(0))

		count += 1
	return [newFacts] + [steps]

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
	steps = []

	if node.getChild(0) is not None: 
		if isAnd(node.getChild(0)):
			first = createNode(node.getText())
			second = createNode(node.getText())

			first.addChildren([node.getChild(0).getChild(0)])
			second.addChildren([node.getChild(0).getChild(1)])

			facts = facts + [first] + [second]

			steps += [node, first, node.getChild(0), "decomposing conjunction"]
			steps += [node, second, node.getChild(0), "decomposing conjunction"]
		elif isPOP(node.getChild(0)): 
			facts = facts + decomposingConjunction(node.getChild(0))

	return [facts] + [steps]
