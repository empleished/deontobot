from parser import *
from rules import *
from checks import *
from getters import *
from create import *

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
