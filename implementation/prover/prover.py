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

# convert prohibitions and permissions to obligations:
# - PRO(C)->OB(¬C)
# - PER(C)->¬OB(C) AND ¬OB(¬C)

def convertProhibition(tree):
# search tree for node == "PRO"
# when pro node found
# -> collect child nodes up til node == ";"
# -> collect parent nodes up til node == ";"
# -> remove nodes
# -> create nodes == A -> OB(¬C)
# -> add new nodes to tree
	return tree
	
def convertPermission(tree):
# search tree for node == "PER"
# when pro node found
# -> collect child nodes up til node == ";"
# -> collect parent nodes up til node == ";"
# -> remove nodes
# -> create nodes == A -> ¬OB(¬C) AND A -> ¬OB(C)
# -> add new nodes to tree
	return tree

def transform(statement, rule):
# for P in rule
# replace P with statement
	transformedStatement = ""

	for node in rule.body: 
		if node == "P": 
			transformedStatement.add(statement)
		else: 
			transformedStatement.add(node)
	
	return transformedStatement

def search(statement, tree):
# look through tree for first part of statement 
# if found move onto its child and the second part of statement
# and so following
	found = false;
	
	# for treenode in tree 
	# 	for statenode in statement
	# 		if treenode = statenode then
	# 			for treenodechild in treenode
	# 				if treenodechild = statementchild
	#					continue
	#				else
	#					break
	#		else
	#			continue

	return found

def ruleStrategy(statement, tree, ruleString):
	ruleTree = ast.parse(ruleString);
	transformedStatement = transform(statement, ruleTree); 
	found = search(transformedStatement, tree);

	return found

# logical rules
	
def doubleNegation(statement, tree):
# P is equivalent to ¬¬P 
# ¬¬P is equivalent to P 
	found = false
	
	if !found:
		found = ruleStrategy(statement, tree, "if (P) then (¬¬P)");
		
		if !found: 
			found = ruleStrategy(statement, tree, "if (¬¬P) then (P)");

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
	
def proofRules(statement, tree):
	proven = false;

	if (!proven):
		proven = modusPonens(statement, tree)

		if (!proven): 
			proven = modusTollens(statement, tree)

			if (!proven): 
				proven = disjunctiveSyllogism(statement, tree)

				if (!proven): 
					proven = deMorgansLaw(statement, tree)

					if (!proven): 
						proven = ruleOfSyllogism(statement, tree)

						if (!proven): 
							proven = doubleNegation(statement, tree)

							if (!proven): 
								proven = decomposingConjunction(statement, tree)
	return proven

def main(argv):
	if len(argv) == 1:
		print "no statement to prove provided"
		return

	statementToProve = argv[1]

	tree = convertProhibition(tree)
	tree = convertPermission(tree)

	statementTree = ast.parse(statementToProve) 
	proven = proofRules(statementTree, tree)

if __name__ == "__main__":
	main(sys.argv)
