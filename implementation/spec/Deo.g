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

fact	:	LB ACTION RB														
	;

op	:	AND 								
	| 	OR 								
	| 	NOT 								
	| 	THEN								
	|	IF								
	|	IFF								
	;

axiom	
	:	LB (norm LB ACTION RB) RB			-> ^(AXIOM norm ACTION)
	;

comp_axiom	:	axiom (op axiom)*
	;
	
cond	:	fact (op fact)*
	;

expr
	:	IF (LB cond RB)
		THEN (LB comp_axiom RB)	 			-> ^(EXPR IF COND THEN AXIOM)
	|	(LB comp_axiom RB) 
		IFF (LB cond RB)	 			-> ^(EXPR IFF FACT THEN AXIOM)	
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

ACTION	:	LETTER (LETTER | DIGIT | SPACE)*;
ID	:	LETTER (LETTER | DIGIT | '_')*;

SPACE	:	(' ' | '\t')+;
EOF	: 	'.';
COMMENT 	:	'#' ~('\r' | '\n')* '\r'? '\n';

fragment LETTER 	: 	'a'..'z' | 'A'..'Z';
fragment DIGIT  	: 	'0'..'9';
