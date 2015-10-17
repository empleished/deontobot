//////////////////////////////////////////////////////////////
//
// specification of the Deo syntactic analyser:
// -Deo syntax
// -translation of Deo phrases to ASTs
//
// Developed 2015/2016 by Leisha Hussien. 
//
//////////////////////////////////////////////////////////////

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
	EXIST;
}

//////// Programs

prog	:	var_decl+ rule_decl+ EOF   					-> ^(PROG 
											var_decl*
											rule_decl+)
	;

//////// Declarations

rule_decl	
	:	expr+								-> (RULE expr+)
	;

var_decl
	:	ID ASSN fact							-> (VAR ID fact)
	;

//////// Constructs

norm	
	:	OB 								-> OB
	| 	PRO 								-> PRO
	| 	PER								-> PER
	;

fact	:	ACTION								-> ACTION
	|	STATE								-> STATE
	|	AGENT								-> AGENT
	;

op	:	AND 								-> AND
	| 	OR 								-> OR
	| 	NOT 								-> NOT
	| 	THEN								-> THEN
	|	IF								-> IF
	|	IFF								-> IFF
	;

axiom	
	:	norm LB ACTION RB						-> (AXIOM norm AGENT ACTION)
	;

existential
	:	ALL 
	|	EXISTS
	;

expr
	:	existential (LB AGENT)* RB 
		(LB IF (LB fact (op fact)*)* RB 
		THEN (LB axiom (op axiom)*)* RB)* RB				-> (EXPR EXIST AGENT IF FACT THEN AXIOM)
	|	existential (LB AGENT)* RB 
		(LB IFF (LB fact (op fact)*)* RB 				-> (EXPR EXIST AGENT IFF FACT THEN AXIOM)
		THEN (LB axiom (op axiom)*)* RB)* RB					
	|	existential (LB AGENT)* RB 
		(LB axiom (op axiom)*)* RB					-> (EXPR EXIST AGENT AXIOM)
	;

//////// Lexicon

OB	:	'it is obliged';
PRO	:	'it is prohibited';
PER	:	'it is permitted';

IF	:	'if';
IFF	:	'if and only if';
THEN	:	'then';
NOT	:	'not';
AND	:	'and';
OR	:	'or';

ALL	:	'for all';	
EXISTS	:	'there exists';

LB	:	'(';
RB	:	')';

ACTION	:	LETTER (LETTER | DIGIT | SPACE)*;
STATE	:	LETTER (LETTER | DIGIT | SPACE)*;
AGENT 	:	LETTER (LETTER | DIGIT | SPACE)*;
ID	:	LETTER (LETTER | DIGIT | '_')*;

SPACE	:	(' ' | '\t')+;
EOL	:	'\r'? '\n';
COMMENT :	'#' ~('\r' | '\n')* '\r'? '\n';

fragment LETTER : 'a'..'z' | 'A'..'Z';
fragment DIGIT  : '0'..'9';
