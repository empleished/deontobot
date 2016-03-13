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
	nodes = antlr3.tree.CommonTreeNodeStream(root)
	nodes.setTokenStream(tokens)
    return nodes
