import antlr3
import antlr3.tree
from DeoLexer import DeoLexer
from DeoParser import DeoParser

def getTree(): 
	fileName = "tests/climatechangeagricultureadaptation.deo" #raw_input("file:")
	tree = generateTree(fileName)
	return tree

def generateTree(fileName): 
	charStream = antlr3.ANTLRFileStream(fileName)
	lexer = DeoLexer(charStream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = DeoParser(tokens)
	rule = parser.prog()
	root = rule.tree
	
	print "TREE: "
	print_tree(root, 0)

	return root

# CODE ADAPTED FROM: http://keyboardlayouteditor.googlecode.com/svn-history/r58/trunk/KeyboardLayoutEditor/src/print_tree.py
def print_tree(node, depth):
	MAX = 10
	TABS = "\t\t\t\t\t\t\t\t\t\t"

	if depth >= MAX:
		return
	for n in node.getChildren():
		print TABS[:depth], "===", n.getText(), "==="
		print_tree(n, depth + 1)


