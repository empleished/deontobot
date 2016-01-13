# NOTES:

# useful documentation: 
# https://greentreesnakes.readthedocs.org/en/latest/manipulating.html
# https://bitbucket.org/takluyver/greentreesnakes/src/default/astpp.py?fileviewer=file-view-default

# thoughts:
# -is it worth stripping out the rules and putting them in a separate tree rather than directly modifying the AST

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

# logical rules

def modusPonens(atom, tree): 
	return tree
	
def modusTollens(atom, tree):
	return tree
	
def disjunctiveSyllogism(atom, tree):
	return tree
	
def deMorgansLaw(atom, tree):
	return tree
	
def ruleOfSyllogism(atom, tree):
	return tree
	
def doubleNegation(atom, tree):
	return tree
	
def decomposingConjunction(atom, tree):
	return tree
	
def stripOutAtoms(tree):
	listOfAtoms = []
# search nodes for node.getChild == ":"
# collect node
# add node to listOfAtoms
	return listOfAtoms

# run logical rules on tree, atom by atom, to simplify
	
def proofRules(atom, tree):
	tree = modusPonens(atom, tree)
	tree = modusTollens(atom, tree)
	tree = disjunctiveSyllogism(atom, tree)
	tree = deMorgansLaw(atom, tree)
	tree = ruleOfSyllogism(atom, tree)
	tree = doubleNegation(atom, tree)
	tree = decomposingConjunction(atom, tree)
	return tree

def main():
	tree = convertProhibition(tree)
	tree = convertPermission(tree)
	listOfAtoms = stripOutAtoms(tree)

	for atom in listOfAtoms:
		tree = proofRules(atom, tree)
