import antlr3
import antlr3.tree
from DeoLexer import DeoLexer
from DeoParser import DeoParser
import astdump	

def runParser(fileName): 
	char_stream = antlr3.ANTLRFileStream(fileName)

	lexer = DeoLexer(char_stream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = DeoParser(tokens)
	rule = parser.prog()

	root = rule.tree
#	print "tree =", root.toStringTree()
#	nodes = antlr3.tree.CommonTreeNodeStream(root)
#	nodes.setTokenStream(tokens)
	
	print_tree(root, 0)

	return root

# n in node.getChildren()
def print_tree(node, depth):
	MAX = 10
	TABS = "\t\t\t\t\t\t\t\t\t\t"

	if depth >= MAX:
		return
	for n in node.getChildren():
		print TABS[:depth], "===", n.getText(), "==="
		print_tree(n, depth + 1)
