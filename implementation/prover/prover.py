# NOTES:

# useful documentation: 
# https://greentreesnakes.readthedocs.org/en/latest/manipulating.html
# https://bitbucket.org/takluyver/greentreesnakes/src/default/astpp.py?fileviewer=file-view-default

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
	return statement

def search(statement, tree):
	found = false;

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
	found = ruleStrategy(statement, tree, "** FILL THIS IN **");

	return found

def modusPonens(statement, tree): 
# if P and P -> Q then Q
	found = ruleStrategy(statement, tree, "** FILL THIS IN **");

	return found
	
def modusTollens(statement, tree):
# if ¬Q and P -> Q then ¬P
	found = ruleStrategy(statement, tree, "** FILL THIS IN **");

	return found
	
def disjunctiveSyllogism(statement, tree):
# if ¬P and (P or Q) then Q
	found = ruleStrategy(statement, tree, "** FILL THIS IN **");

	return found
	
def deMorgansLaw(statement, tree):
# ¬(P or Q) is equivalent to ¬P and ¬Q
# ¬P and ¬Q is equivalent to ¬(P or Q)
# ¬(P and Q) is equivalent to ¬P or ¬Q
# ¬P or ¬Q is equivalent to ¬(P and Q)
	found = ruleStrategy(statement, tree, "** FILL THIS IN **");

	return found
	
def ruleOfSyllogism(statement, tree):
# if (P -> Q) and (Q -> R) then P -> R
	found = ruleStrategy(statement, tree, "** FILL THIS IN **");

	return found
	
def decomposingConjunction(statement, tree):
# if (P and Q) then P, Q
	found = ruleStrategy(statement, tree, "** FILL THIS IN **");

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
