//////////////////////////////////////////////////////////////
//
// Specification of the Deo syntactic analyser.
//
// Developed 2015/2016 by Leisha Hussien (2020430H). 
//
//////////////////////////////////////////////////////////////

grammar Fun;

// This specifies the Deo syntactic analyser.
// In detail, it specifies the syntax of Fun and the 
// translation of Deo phrases to ASTs.

options {
	output = AST;
	ASTLabelType = CommonTree;
}

tokens {        // special tokens for labeling AST nodes

}

//////// Constructs

norm	
	:	OB | PRO | PER
	;

op	:	AND | OR | NOT

simple_expr
	:	(AGENT)* norm ACTION
	;

complex_epr
	:	IF (simple_expr)* THEN simple_expr (op simple_expr)*
	|	simple_expr (op simple_expr)*
	;

//////// Lexicon

OB	:	'should';
PRO	:	'should not';
PER	:	'may';
IF	:	'if';
THEN	:	'then';
NOT	:	'not';
AND	:	'and';
OR	:	'or';

LPAR	:	'(' ;
RPAR	:	')' ;
COLON	:	':' ;
DOT	:	'.' ;

NUM	:	DIGIT+ ;

ACTION	:	LETTER (LETTER | NUM | SPACE)* ;
AGENT	:	LETTER (LETTER | NUM | SPACE)* ;

SPACE	:	(' ' | '\t')+             ;
EOL	:	'\r'? '\n'                ;
COMMENT :	'#' ~('\r' | '\n')*
		  '\r'? '\n'              ;

fragment LETTER : 'a'..'z' | 'A'..'Z' ;
fragment DIGIT  : '0'..'9' ;
