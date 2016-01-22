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
# https://bitbucket.org/takluyver/greentreesnakes/src/default/astpp.py?fileviewer=file-view-default

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
	facts = [];

if node matches pattern
add to facts

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
	
	if !found:
		facts = facts + ruleStrategy(fact, node, "if (P) then (¬¬P)");
		
		if !found: 
			facts = facts + ruleStrategy(fact, node, "if (¬¬P) then (P)");

	return found

def modusPonens(statement, tree): 
# if P and P -> Q then Q
	found = ruleStrategy(statement, tree, "if ((P) and (P -> Q)) then (Q)");

	return found
	
def modusTollens(statement, tree):
# if ¬Q and P -> Q then ¬P
	found = ruleStrategy(statement, tree, "if ((¬Q) and (P -> Q)) then (¬P)");

	return found
	
def disjunctiveSyllogism(statement, tree):
# if ¬P and (P or Q) then Q
	found = ruleStrategy(statement, tree, "if ((¬P) and (P or Q)) then (Q)");

	return found
	
def deMorgansLaw(statement, tree):
# ¬(P or Q) is equivalent to ¬P and ¬Q
# ¬P and ¬Q is equivalent to ¬(P or Q)
# ¬(P and Q) is equivalent to ¬P or ¬Q
# ¬P or ¬Q is equivalent to ¬(P and Q)
	found = false
	
	if !found: 
		found = ruleStrategy(statement, tree, "if (¬(P or Q)) then ((¬P) and (¬Q))");
		
		if !found: 
			found = ruleStrategy(statement, tree, "if ((¬P) and (¬Q)) then (¬(P or Q))");
		
			if !found: 
				found = ruleStrategy(statement, tree, "if (¬(P and Q)) then ((¬P) or (¬Q))");
		
				if !found: 
					found = ruleStrategy(statement, tree, "if ((¬P) or (¬Q)) then (¬(P and Q))");

	return found
	
def ruleOfSyllogism(statement, tree):
# if (P -> Q) and (Q -> R) then P -> R
	found = ruleStrategy(statement, tree, "if (if (P) then (Q)) and (if (Q) then (R)) then (if (P) then (R)");
	
	return found
	
def decomposingConjunction(statement, tree):
# if (P and Q) then P, Q
	found = ruleStrategy(statement, tree, "if ((P) and (Q)) then (P) and (Q)");

	return found

# run logical rules on tree

def isProven(facts, statement): 
proven = false;

for fact in facts: 
if fact == statement:
proven = true

return proven
	
def proofRules(statement, facts, tree):
	proven = false;
statementTree = ast.parse(statement)

for fact in facts: 
for node in tree.body:
	if (!proven):
		newFacts = modusPonens(statement, node)
facts = facts + newFacts
proven = isProven(facts, statement)

		if (!proven): 
			newFacts = modusTollens(statement, node)
facts = facts + newFacts
proven = isProven(facts, statement)

			if (!proven): 
				newFacts = disjunctiveSyllogism(statement, node)
facts = facts + newFacts
proven = isProven(facts, statement)

				if (!proven): 
					newFacts = deMorgansLaw(statement, node)
facts = facts + newFacts
proven = isProven(facts, statement)

					if (!proven): 
						newFacts = ruleOfSyllogism(statement, node)
facts = facts + newFacts
proven = isProven(facts, statement)

						if (!proven): 
							newFacts = doubleNegation(statement, node)
facts = facts + newFacts
proven = isProven(facts, statement)
							if (!proven): 
							newFacts = decomposingConjunction(statement, node)
facts = facts + newFacts
proven = isProven(facts, statement)

	return proven

def main(argv):
	if len(argv) == 1:
		print "no statement to prove provided"
		return

	statementToProve = argv[1]
facts = argv[2]
 
	proven = proofRules(statementToProve, facts, tree)

if __name__ == "__main__":
	main(sys.argv)
