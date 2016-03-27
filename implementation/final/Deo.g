grammar Deo;

options {
	language = Python;
	output = AST;
	ASTLabelType = CommonTree;
}

// LABELS FOR AST NODES // 

tokens {        
	IFTHEN;
	EXPR;
	PROG;
	GOAL;
	DECL;
	INF;
	PREF;
	IFTHEN;
	ATOM;
	TERM;
	RULE;
	FACT;
}

// PARSER RULES //

prog
	:	decl+ EOF							-> ^(PROG decl+) 
	;

decl
	:	term EOL							-> ^(DECL term)
	|	rule EOL							-> ^(DECL rule)
	|	fact EOL							-> ^(DECL fact)
	|	goal EOL    			  				-> ^(DECL goal)
	;
rule
	:	RULE ASSN expr							-> ^(RULE expr)	
	;

fact
	:	FACT ASSN expr							-> ^(FACT expr)	
	;

goal
	:	GOAL ASSN expr							-> ^(GOAL expr)	
	;

term
	:	ID ASSN atom 							-> ^(TERM ID atom)
	;

atom
	:	ATOM										
	;

expr
	:	ID								-> ^(ID)
	|	prefix_expr							-> ^(prefix_expr)
	|	infix_expr							-> ^(infix_expr)
	|	ifthen_expr							-> ^(ifthen_expr) 
	;

prefix_expr
	:	LB pop SPACE expr RB						-> ^(pop expr)	
	;

pop	
	:	OB 								
	| 	PRO 								
	| 	PER	
	| 	NOT 										
	;

infix_expr
	:	LB e1=expr SPACE iop SPACE e2=expr RB				-> ^(iop $e1 $e2)
	;

iop	:	AND 
	| 	OR 										
	;

ifthen_expr
	:	LB IF SPACE e1=expr SPACE THEN SPACE e2=expr RB			-> ^(IFTHEN $e1 $e2) 
	;

// LEXER RULES //

OB	:	'OB';
PRO	:	'PRO';
PER	:	'PER';

IF	:	'if';
IFF	:	'iff';
THEN	:	'then';
NOT	:	'not';
AND	:	'and';
OR	:	'or';

TERM    :	'term';
GOAL    :	'goal';
RULE    :	'rule';
FACT    :	'fact';

LB	:	'(';
RB	:	')';

ASSN	: 	': ';

ATOM	:	'"' LETTER (LETTER | DIGIT | PUNCT)* '"';
ID	:	LETTER (LETTER | DIGIT | '_')*;

fragment LETTER 	: 	'a'..'z' | 'A'..'Z';
fragment DIGIT  	: 	'0'..'9';

fragment PUNCT		:	'\'' | ',' | ' ';

EOL     :	'\r'? '\n';             
SPACE   :	('\t' | ' ')+;          
