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
	FACT;
	ATOM;
}

// PARSER RULES //

prog	:	fact_decl+ rule_decl+ EOF   			-> ^(PROG fact_decl+ rule_decl+)
	;

rule_decl	
	:	expr+						-> ^(RULE expr+) 
	;

fact_decl
	:	(ID ASSN fact EOL)+				-> ^((ID ASSN fact)+)
	;

norm	
	:	OB 								
	| 	PRO 								
	| 	PER								
	;

fact	:	ATOM						-> ^(FACT fact)
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
	:	axiom
	|	axiom (op axiom)+
	;
	
cond	:	LB fact RB
	;
	
comp_cond
	:	cond
	|	LB cond (op cond)+ RB
	;

expr	:
	:	IF comp_cond THEN comp_axiom EOL	 	-> ^(EXPR IF COND comp_cond THEN AXIOM comp_axiom)
//	|	comp_axiom IFF cond EOL		 		-> ^(EXPR IFF FACT fact THEN AXIOM comp_axiom)	
	|	comp_axiom EOL					-> ^(EXPR AXIOM comp_axiom)
	;

// LEXER RULES //

OB	:	'OB';
PRO	:	'PRO';
PER	:	'PER';

IF	:	'if';
//IFF	:	'iff';
THEN	:	'then';
NOT	:	'not';
AND	:	'and';
OR	:	'or';

LB	:	'(';
RB	:	')';

ASSN	: 	':';

ATOM	:	LETTER (LETTER | DIGIT | ' ')*;
ID	:	LETTER (LETTER | DIGIT | '_')*;

EOF	: 	'#';
EOL	:	'.';

fragment LETTER 	: 	'a'..'z' | 'A'..'Z';
fragment DIGIT  	: 	'0'..'9';
