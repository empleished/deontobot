grammar Deo;

options {
	language = Python;
	output = AST;
	ASTLabelType = CommonTree;
}

tokens {        //TODO special tokens for labeling AST nodes
	IF;
//	IFF;
	THEN;
	EXPR;
	FACT;
	RULE;
	AXIOM;
	COND;
	PROG;
	FACT;
	ATOM;
	ASSN;
}

// PARSER RULES //

prog	:	fact_decl+ rule_decl+    			-> ^(PROG fact_decl+ rule_decl+)
	;

rule_decl	
	:	expr						-> ^(RULE expr) 
	;

fact_decl
	:	fact						-> ^(FACT fact)
	;

fact
	:	ID ASSN atom 					//-> ^(ID ASSN atom)
	;

norm	
	:	OB 								
	| 	PRO 								
	| 	PER								
	;

atom	:	ATOM						
	;

op	:	AND 
	| 	OR 
	| 	NOT 
	| 	THEN
	|	IF
//	|	IFF
	;

axiom	
	:	LB (norm LB atom RB) RB
	;

comp_axiom	
	:	axiom
	|	axiom (op axiom)+
	;
	
cond	:	LB fact RB
	;
	
comp_cond
	:	cond
	|	cond (op cond)+ 
	;

expr	:	IF comp_cond THEN comp_axiom		 	-> ^(EXPR IF COND comp_cond THEN AXIOM comp_axiom)
//		comp_axiom IFF cond		 		-> ^(EXPR IFF FACT fact THEN AXIOM comp_axiom)	
	|	comp_axiom					-> ^(EXPR AXIOM comp_axiom)
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

EOL 	: 	'.';

ATOM	:	LETTER (LETTER | DIGIT | ' ')*;
ID	:	LETTER (LETTER | DIGIT | '_')*;

fragment LETTER 	: 	'a'..'z' | 'A'..'Z';
fragment DIGIT  	: 	'0'..'9';
