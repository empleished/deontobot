import antlr3
from DeoLexer import DeoLexer
from DeoParser import DeoParser
 
path_to_input = "/home/empleished/humeanator/deontobot/implementation/spec/tests/csEthics.txt"
opened_file = open(path_to_input, 'r')
input = "";

for line in opened_file: 
	input = input + line

unicode_input = input.decode("utf-8")

char_stream = antlr3.ANTLRStringStream(unicode_input)
lexer = DeoLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = DeoParser(tokens)
parser.entry_rule()
