grammar Deo;

options {
	language = Python;
	output = AST;
	ASTLabelType = CommonTree;
}

tokens {        //TODO special tokens for labeling AST nodes
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
	:	decl+ EOF								-> ^(PROG decl+)
	;

decl
	:	term EOL								-> ^(TERM term)
	|	rule EOL								-> ^(RULE rule)
	|	fact EOL								-> ^(FACT fact)
	|	goal EOL    			  				-> ^(GOAL goal)    
	;

rule
	:	RULE ASSN expr
	;

fact
	:	FACT ASSN expr
	;

goal
	:	GOAL ASSN expr						
	;

term
	:	ID ASSN atom 							
	;

atom
	:	ATOM								
	;

expr
	:	ID								    -> ^(EXPR ID)
	|	prefix_expr						    -> ^(EXPR prefix_expr)
	|	infix_expr						    -> ^(EXPR infix_expr)
	|	ifthen_expr						    -> ^(EXPR ifthen_expr)
	;

prefix_expr
	:	LB pop LB expr RB RB						-> ^(PREF pop expr)
	;

pop	
	:	OB 								
	| 	PRO 								
	| 	PER	
	| 	NOT 	
	;

infix_expr
	:	LB e1=expr SPACE iop SPACE e2=expr RB					-> ^(iop $e1 $e2)
	;

iop	:	AND 
	| 	OR 
	|	IFF
	;

ifthen_expr
	:	LB IF SPACE e1=expr SPACE THEN SPACE e2=expr RB				-> ^(IFTHEN $e1 $e2)
	;

// LEXER RULES //

OB	:	'OB';
PRO	:	'PRO';
PER	:	'PER';

IF	    :	'if';
IFF	    :	'iff';
THEN	:	'then';
NOT	    :	'not';
AND	    :	'and';
OR	    :	'or';

TERM    :   'term';
GOAL    :   'goal';
RULE    :   'rule';
FACT    :   'fact';

LB	:	'(';
RB	:	')';

ASSN	: 	': ';

ATOM	:	'"' LETTER (LETTER | DIGIT | ' ')* '"';
ID	    :	LETTER (LETTER | DIGIT | '_')*;

fragment LETTER 	: 	'a'..'z' | 'A'..'Z';
fragment DIGIT  	: 	'0'..'9';

EOL     :   '\r'? '\n';             
SPACE   :   ('\t' | ' ')+;          
