# Prover workflow
# Read in list of statements about the world (data set of facts).
# Read in goal.
# while data set doesn't contain goal.
## choose member of data set via some strategy
## choose a rule to apply to generate new fact
## if new fact created add to data set

## Note, need to know when to stop (i.e. cannot generate any new facts).

## Example program:
# Facts:
### A
### A -> B
# Goal:
# B
# Prover would apply rule A ^ (A->B) => B
# Would add B to fact set
# Check fact set contains B (it does).
# halt.
# report sequence of steps to prove B (what rules were applied).
#
# NOTES:

# useful documentation: 
# https://greentreesnakes.readthedocs.org/en/latest/manipulating.html
# https://hg.python.org/cpython/file/2.7/Lib/ast.py

# useful pieces of code: 
# for node in tree.body - for every node in the tree
# self.generic_visit(node) - visit children of the node
# node.body[-1] - gets the last node in a function's body

def transform(fact, rule):
# for P in rule
# replace P with fact
	transformedStatement = ""

	for node in rule.body: 
		if node == "P": 
			transformedStatement.add(fact)
		else: 
			transformedStatement.add(node)
	
	return transformedStatement

def search(pattern, node):
	facts = []

	if node == pattern:
		facts = facts + node

	return facts

def ruleStrategy(fact, node, ruleString):
	ruleTree = ast.parse(ruleString);
	pattern = transform(fact, ruleTree); 
	facts = search(pattern, node);

	return facts

# logical rules
	
def doubleNegation(statement, tree):
# P is equivalent to ¬¬P 
# ¬¬P is equivalent to P 
	facts = []
	
	facts = facts + ruleStrategy(fact, node, "if (P) then (¬¬P)");
	facts = facts + ruleStrategy(fact, node, "if (¬¬P) then (P)");

	return facts


#def modusPonens (facts)
# if P and P -> Q then Q
# if fact data set contains a P and Q, such that there is one fact P and another fact P->Q, then add Q to facts list.
#    for fact in facts:
#        if fact is an atom;
#            for fact2 in facts:
#                 if fact2 is an implication:
#                     then facts.add(fact2.consequence)

def modusPonens(statement, tree): 
# if P and P -> Q then Q
	facts = ruleStrategy(fact, node, "if ((P) and (P -> Q)) then (Q)");

	return facts
	
def modusTollens(statement, tree):
# if ¬Q and P -> Q then ¬P
	facts = ruleStrategy(fact, node, "if ((¬Q) and (P -> Q)) then (¬P)");

	return facts
	
def disjunctiveSyllogism(statement, tree):
# if ¬P and (P or Q) then Q
	facts = ruleStrategy(fact, node, "if ((¬P) and (P or Q)) then (Q)");

	return facts
	
def deMorgansLaw(fact, tree):
# ¬(P or Q) is equivalent to ¬P and ¬Q
# ¬P and ¬Q is equivalent to ¬(P or Q)
# ¬(P and Q) is equivalent to ¬P or ¬Q
# ¬P or ¬Q is equivalent to ¬(P and Q)
	facts = []
	
	facts = facts + ruleStrategy(fact, node, "if (¬(P or Q)) then ((¬P) and (¬Q))");
	facts = facts + ruleStrategy(fact, node, "if ((¬P) and (¬Q)) then (¬(P or Q))");
	facts = facts + ruleStrategy(fact, node, "if (¬(P and Q)) then ((¬P) or (¬Q))");
	facts = facts + ruleStrategy(fact, node, "if ((¬P) or (¬Q)) then (¬(P and Q))");

	return facts
	
def ruleOfSyllogism(statement, tree):
# if (P -> Q) and (Q -> R) then P -> R
	facts = ruleStrategy(fact, node, "if (if (P) then (Q)) and (if (Q) then (R)) then (if (P) then (R)");
	
	return facts
	
def decomposingConjunction(statement, tree):
# if (P and Q) then P, Q
	facts = ruleStrategy(fact, node, "if ((P) and (Q)) then (P) and (Q)");

	return facts

# run logical rules on tree

def isProven(facts, statement): 
	proven = false;
	
	for fact in facts: 
		if fact == statement:
			proven = true
	
	return proven
	
def proofRules(statement, facts, tree):
	proven = false;
	steps = []
	statementTree = ast.parse(statement)
	
    while (!proven): 
        for fact in facts: 
		    for node in tree.body:
				newFacts = modusPonens(statement, node)
				
				if (newFacts != []): 
					facts = facts + newFacts
					steps = steps + ["modus ponens", fact]
					
				proven = isProven(facts, statement)
		
				if (!proven): 
					newFacts = modusTollens(statement, node)
				
					if (newFacts != []): 
						facts = facts + newFacts
						steps = steps + ["modus tollens", fact]
						
					proven = isProven(facts, statement)
		
					if (!proven): 
						newFacts = disjunctiveSyllogism(statement, node)
				
						if (newFacts != []): 
							facts = facts + newFacts
							steps = steps + ["disjunctive syllogism", fact]
							
						proven = isProven(facts, statement)
		
						if (!proven): 
							newFacts = deMorgansLaw(statement, node)
				
							if (newFacts != []): 
								facts = facts + newFacts
								steps = steps + ["deMorgan's law", fact]
								
							proven = isProven(facts, statement)
		
							if (!proven): 
								newFacts = ruleOfSyllogism(statement, node)
				
								if (newFacts != []): 
									facts = facts + newFacts
									steps = steps + ["rule of syllogism", fact]
									
								proven = isProven(facts, statement)
		
								if (!proven): 
									newFacts = doubleNegation(statement, node)
				
									if (newFacts != []): 
										facts = facts + newFacts
										steps = steps + ["double negation", fact]
										
									proven = isProven(facts, statement)
								
									if (!proven): 
										newFacts = decomposingConjunction(statement, node)
				
										if (newFacts != []): 
											facts = facts + newFacts
											steps = steps + ["decomposing conjunction", fact]
											
										proven = isProven(facts, statement)

	return [proven] + steps

def main(argv):
	if len(argv) == 1:
		print "no facts or statement to prove provided"
		return

	statementToProve = argv[1]
	facts = argv[2]
 
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
