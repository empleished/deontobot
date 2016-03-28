import antlr3
from DeoLexer import DeoLexer
from DeoParser import DeoParser

# takes in a structured file and generates an ANTLR tree 
def getTree(): 
	fileName = raw_input("path to input file:\n")
	tree = generateTree(fileName)
	return tree

# lexes and parses a file to produce an ANTLR tree
def generateTree(fileName): 
	charStream = antlr3.ANTLRFileStream(fileName)
	lexer = DeoLexer(charStream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = DeoParser(tokens)
	rule = parser.prog()
	root = rule.tree
	
	print "\nTREE: "
	print_tree(root, 0)

	return root

# recursively prints every node of a tree formatted and indented
# CODE ADAPTED FROM: 
# http://keyboardlayouteditor.googlecode.com/svn-history/r58/trunk/KeyboardLayoutEditor/src/print_tree.py
def print_tree(node, depth):
	MAX = 10
	TABS = "\t\t\t\t\t\t\t\t\t\t"

	if depth >= MAX:
		return
	for n in node.getChildren():
		print TABS[:depth], "===", n.getText(), "==="
		print_tree(n, depth + 1)
