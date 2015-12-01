import antlr3
from DeoLexer import DeoLexer
from DeoParser import DeoParser
from DeoTreeWalker import DeoTreeWalker

char_stream = antlr3.ANTLRFileStream(path_to_input)

lexer = DeoLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = DeoParser(tokens)
rule = parser.prog()

root = r.tree
 
nodes = antlr3.tree.CommonTreeNodeStream(root)
nodes.setTokenStream(tokens)
walker = TWalker(nodes)
walker.prog()
