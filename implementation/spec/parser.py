import antlr3
from DeoLexer import DeoLexer
from DeoParser import DeoParser

char_stream = antlr3.ANTLRFileStream("tests/csEthics.deo")

lexer = DeoLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = DeoParser(tokens)
rule = parser.prog()
tree = rule.tree

for node in tree: 
	print node
