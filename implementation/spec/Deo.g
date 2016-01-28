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

prog	:	decl+	  					-> ^(PROG decl+)
	;

decl	:	fact_decl					-> ^(DECL fact_decl)
	|	rule_decl 					-> ^(DECL rule_decl)
	;

rule_decl	
	:	expr						
	;

fact_decl
	:	fact						
	;

//goal
//	:	decl						-> ^(GOAL goal)
//	;

fact
	:	ID ASSN atom 							
	;

atom	:	ATOM						
	;

pop	
	:	OB 								
	| 	PRO 								
	| 	PER	
	| 	NOT 	
	;

iop	:	AND 
	| 	OR 
	|	IFF
	;

expr	:	atom						-> ^(EXPR atom)
	|	prefix_expr					-> ^(EXPR prefix_expr)
	|	infix_expr					-> ^(EXPR infix_expr)
	|	ifthen_expr					-> ^(EXPR ifthen_expr)
	;

prefix_expr
	:	LB pop LB expr RB RB				-> ^(PREF pop expr)
	;

infix_expr
	:	LB expr iop expr RB				-> ^(INF expr iop expr)
	;

ifthen_expr
	:	LB IF expr THEN expr RB				-> ^(IFTHEN expr expr)
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
