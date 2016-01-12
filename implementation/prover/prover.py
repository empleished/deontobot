# -*- coding: cp1252 -*-

# NOTES:
# useful documentation: https://greentreesnakes.readthedocs.org/en/latest/manipulating.html

# convert prohibitions and permissions to obligations:
# - PRO(C)->OB(¬C)
# - PER(C)->¬OB(C) AND ¬OB(¬C)

def convertProhibition(tree):
	return tree
	
def convertPermission(tree):
	return tree

# run logical rules on tree, atom by atom, to simplify

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
	return listOfAtoms
	
def proofRules(atom, tree):
	return tree

def main:
        tree = convertProhibition(tree)
        tree = convertPermission(tree)
        listOfAtoms = stripOutAtoms(tree)

        for atom in listOfAtoms:
                tree = proofRules(atom, tree)
