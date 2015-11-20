grammar Deo;

options {
	language = Python;
	output = AST;
	ASTLabelType = CommonTree;
}

tokens {        //TODO special tokens for labeling AST nodes
	IF;
	IFF;
	THEN;
	EXPR;
	FACT;
	RULE;
	AXIOM;
	PROG;
	VAR;
}

// PARSER RULES //

prog	:	var_decl+ rule_decl+ EOF   			-> ^(PROG var_decl* rule_decl+)
	;

rule_decl	
	:	expr+						-> ^(RULE expr+) 
	;

var_decl
	:	ID ASSN fact					-> ^(VAR ID fact)
	;

norm	
	:	OB 								
	| 	PRO 								
	| 	PER								
	;

fact	:	ACTION														
	;

op	:	AND 								
	| 	OR 								
	| 	NOT 								
	| 	THEN								
	|	IF								
	|	IFF								
	;

axiom	
	:	norm LB ACTION RB				-> ^(AXIOM norm ACTION)
	;

expr
	:	IF (LB fact (op fact)* RB)
		THEN (LB axiom (op axiom)* RB)	 		-> ^(EXPR IF FACT THEN AXIOM)
	|	IFF (LB fact (op fact)* RB) 
		THEN (LB axiom (op axiom)* RB)	 		-> ^(EXPR IFF FACT THEN AXIOM)	
	|	axiom (op axiom)* 				-> ^(EXPR AXIOM)
	;

// LEXER RULES //

OB	:	'it is obliged';
PRO	:	'it is prohibited';
PER	:	'it is permitted';

IF	:	'if';
IFF	:	'if and only if';
THEN	:	'then';
NOT	:	'not';
AND	:	'and';
OR	:	'or';

LB	:	'(';
RB	:	')';

ASSN	: 	':';

ACTION	:	LETTER (LETTER | DIGIT | SPACE)*;
ID	:	LETTER (LETTER | DIGIT | '_')*;

SPACE	:	(' ' | '\t')+;
EOL	:	'\r'? '\n';
COMMENT :	'#' ~('\r' | '\n')* '\r'? '\n';

fragment LETTER : 'a'..'z' | 'A'..'Z';
fragment DIGIT  : '0'..'9';