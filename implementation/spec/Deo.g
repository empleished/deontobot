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
}

// PARSER RULES //

prog
    :	decl+					-> ^(PROG decl+)
	;

decl
    :	fact					-> ^(DECL fact)
	|	rule 					-> ^(DECL rule)
    |   goal                    -> ^(DECL goal)    
	;

goal
	:	expr					-> ^(GOAL goal)
	;

fact
	:	ID ASSN atom 							
	;

atom
    :	ATOM						
	;

expr
    :	atom						-> ^(EXPR atom)
	|	prefix_expr					-> ^(EXPR prefix_expr)
	|	infix_expr					-> ^(EXPR infix_expr)
	|	ifthen_expr					-> ^(EXPR ifthen_expr)
	;

prefix_expr
	:	LB pop LB expr RB RB				-> ^(PREF pop expr)
	;

pop	
	:	OB 								
	| 	PRO 								
	| 	PER	
	| 	NOT 	
	;

infix_expr
	:	LB expr iop expr RB				-> ^(INF expr iop expr)
	;

iop	:	AND 
	| 	OR 
	|	IFF
	;

ifthen_expr
	:	LB IF expr THEN expr RB			-> ^(IFTHEN expr expr)
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
