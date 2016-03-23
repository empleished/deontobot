from parser import *
from rules import *
from checks import *
from getters import *
from create import *

def getTerms(tree): 
	terms = {}

	for node in tree.getChildren(): 
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
	steps = []

	for node in tree.getChildren(): 
		if node.getChild(0).getText() == entityType: 
			entities = entities + [node.getChild(0)]

	for entity in entities: 
		dcResults = decomposingConjunction(entity.getChild(0))
		entities += dcResults[0]
		steps += dcResults[1]

	return entities, steps

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
