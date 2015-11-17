import antlr3
from DeoLexer import DeoLexer
from DeoParser import DeoParser

char_stream = antlr3.ANDeoLRFileStream(path_to_input)
 
lexer = DeoLexer(char_stream)
tokens = antlr3.CommonDeookenStream(lexer)
parser = DeoParser(tokens)
parser.entry_rule()
