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
	COND;
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

fact	:	ATOM														
	;

op	:	AND 								
	| 	OR 								
	| 	NOT 								
	| 	THEN								
	|	IF								
	|	IFF								
	;

axiom	
	:	LB (norm LB fact RB) RB	
	;

comp_axiom	
	:	LB axiom RB				
	|	axiom+
	;
	
cond	:	LB fact RB
	|	LB fact (op fact)* RB
	;

expr
	:	IF cond THEN comp_axiom		 		-> ^(EXPR IF COND THEN AXIOM)
	|	comp_axiom IFF cond		 		-> ^(EXPR IFF FACT THEN AXIOM)	
	|	comp_axiom					-> ^(EXPR AXIOM)
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

ATOM	:	LETTER (LETTER | DIGIT | SPACE)*;
ID	:	LETTER (LETTER | DIGIT | '_')*;

SPACE	:	(' ' | '\t')+;
EOF	: 	'.';
COMMENT 	:	'#' ~('\r' | '\n')* '\r'? '\n';

fragment LETTER 	: 	'a'..'z' | 'A'..'Z';
fragment DIGIT  	: 	'0'..'9';
