import ast

def doubleNegation(statement, tree):
# P is equivalent to ¬¬P
# ¬¬P is equivalent to P
	facts = []

	return facts

def modusPonens(fact, node):
# if P and P -> Q then Q
	facts = []

	if node == 'IFTHEN':
		if node.popleft() == fact:
# if fact is not an atom -- deal with it??
			facts = facts + node.popright()

	return facts

def modusTollens(statement, tree):
# if ¬Q and P -> Q then ¬P
	facts = []

	return facts

def disjunctiveSyllogism(statement, tree):
# if ¬P and (P or Q) then Q
	facts = []

	return facts

def deMorgansLaw(fact, tree):
# ¬(P or Q) is equivalent to ¬P and ¬Q
# ¬P and ¬Q is equivalent to ¬(P or Q)
# ¬(P and Q) is equivalent to ¬P or ¬Q
# ¬P or ¬Q is equivalent to ¬(P and Q)
	facts = []

	return facts

def ruleOfSyllogism(statement, tree):
# if (P -> Q) and (Q -> R) then P -> R
	facts = []

	return facts

def decomposingConjunction(statement, tree):
# if (P and Q) then P, Q
	facts = []

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

#while (!proven and progress):
#        fact_size=len(facts)
#
#        try_modus_ponens ()
#        try_
#        
#        for each rule in rules:
#                try all combinations of facts
#        if (len(facts) == fact_size):
#                progress = false

def proofRules(statement, facts, tree):
	proven = false
	steps = []

	while (!proven): 
        for fact in facts: 
		    for node in tree.body:
				newFacts = modusPonens(fact, node)
				
				if (newFacts != []): 
					facts = facts + newFacts
					steps = steps + ["modus ponens", fact]
					
				proven = isProven(facts, statement)
		
				if (!proven): 
					newFacts = modusTollens(fact, node)
				
					if (newFacts != []): 
						facts = facts + newFacts
						steps = steps + ["modus tollens", fact]
						
					proven = isProven(facts, statement)
		
					if (!proven): 
						newFacts = disjunctiveSyllogism(fact, node)
				
						if (newFacts != []): 
							facts = facts + newFacts
							steps = steps + ["disjunctive syllogism", fact]
							
						proven = isProven(facts, statement)
		
						if (!proven): 
							newFacts = deMorgansLaw(fact, node)
				
							if (newFacts != []): 
								facts = facts + newFacts
								steps = steps + ["deMorgan's law", fact]
								
							proven = isProven(facts, statement)
		
							if (!proven): 
								newFacts = ruleOfSyllogism(fact, node)
				
								if (newFacts != []): 
									facts = facts + newFacts
									steps = steps + ["rule of syllogism", fact]
									
								proven = isProven(facts, statement)
		
								if (!proven): 
									newFacts = doubleNegation(fact, node)
				
									if (newFacts != []): 
										facts = facts + newFacts
										steps = steps + ["double negation", fact]
										
									proven = isProven(facts, statement)
								
									if (!proven): 
										newFacts = decomposingConjunction(fact, node)
				
										if (newFacts != []): 
											facts = facts + newFacts
											steps = steps + ["decomposing conjunction", fact]
											
										proven = isProven(facts, statement)

	return [proven] + steps

def yieldFactsFromTree(tree):
	facts = []

	for node in tree.body:
		if node == 'ATOM':
		facts = facts + node.children

	return facts

def main(argv):
	statementToProve = argv[1]
	facts = argv[2]

	tree = ast.parse(arg[3])

	newFacts = yieldFactsFromTree(tree)

	proverSteps = proofRules(statementToProve, facts, tree)

	count = 1

	if proverSteps[0] = false:
		print "statement is incongruent with provided facts"
	else:
		print "statement is coherent with provided facts"

	while count < proverSteps.length: 
		print proverSteps[count][0] + ": " + proverSteps[count][1]

if __name__ == "__main__":
	main(sys.argv)
