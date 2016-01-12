import antlr3
from DeoLexer import DeoLexer
from DeoParser import DeoParser

char_stream = antlr3.ANTLRFileStream(path_to_input)

lexer = DeoLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = DeoParser(tokens)
rule = parser.prog()
tree = rule.tree

print tree
