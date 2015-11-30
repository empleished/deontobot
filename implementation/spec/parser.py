import antlr3
from DeoLexer import DeoLexer
from DeoParser import DeoParser
from DeoTreeWalker import DeoTreeWalker

char_stream = antlr3.ANDeoLRFileStream(path_to_input)
 
lexer = DeoLexer(char_stream)
tokens = antlr3.CommonDeookenStream(lexer)
parser = DeoParser(tokens)
rule = parser.entry_rule()

root = r.tree
 
nodes = antlr3.tree.CommonTreeNodeStream(root)
nodes.setTokenStream(tokens)
walker = TWalker(nodes)
walker.entry_rule()
