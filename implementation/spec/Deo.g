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
    :	decl+								-> ^(PROG decl+)
	;

decl
    :	term								-> ^(TERM term)
	|	rule 								-> ^(RULE rule)
	|	fact								-> ^(FACT fact)
    |   goal      			  				-> ^(GOAL goal)    
	;

rule
	:	RULE ASSN expr

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
    :	ATOM								-> ^(ATOM atom)
	;

expr
    :	atom								-> ^(EXPR atom)
	|	prefix_expr							-> ^(EXPR prefix_expr)
	|	infix_expr							-> ^(EXPR infix_expr)
	|	ifthen_expr							-> ^(EXPR ifthen_expr)
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
	:	LB e1=expr iop e2=expr RB					-> ^(iop e1 e2)
	;

iop	:	AND 
	| 	OR 
	|	IFF
	;

ifthen_expr
	:	LB IF e1=expr THEN e1=expr RB				-> ^(IFTHEN e1 e2)
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

LB	:	'(';
RB	:	')';

ASSN	: 	':';

ATOM	:	LETTER (LETTER | DIGIT | ' ')*;
ID	:	LETTER (LETTER | DIGIT | '_')*;

fragment LETTER 	: 	'a'..'z' | 'A'..'Z';
fragment DIGIT  	: 	'0'..'9';
