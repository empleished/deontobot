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

prog	:	fact_decl+ rule_decl+ EOF   			-> ^(PROG fact_decl* rule_decl+)
	;

rule_decl	
	:	expr+						-> ^(RULE expr+) 
	;

fact_decl
	:	fact+					-> ^(FACT fact+)
	;

norm	
	:	OB 								
	| 	PRO 								
	| 	PER								
	;

fact	:	ID ASSN ATOM EOL					-> ^(ATOM ID fact)
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
	|	LB fact (op fact)+ RB
	;

expr	:
//	:	IF cond THEN comp_axiom EOL		 	-> ^(EXPR IF COND THEN AXIOM)
//	|	comp_axiom IFF cond EOL		 		-> ^(EXPR IFF FACT THEN AXIOM)	
		comp_axiom EOL					-> ^(EXPR comp_axiom)
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
EOF	: 	'#';
EOL	:	'.';

fragment LETTER 	: 	'a'..'z' | 'A'..'Z';
fragment DIGIT  	: 	'0'..'9';
