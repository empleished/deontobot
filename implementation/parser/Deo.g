//////////////////////////////////////////////////////////////
//
// specification of the Deo syntactic analyser:
// -Deo syntax
// -translation of Deo phrases to ASTs
//
// Developed 2015/2016 by Leisha Hussien (2020430H).
// Adapted from code written by David Watt (University of Glasgow).  
//
//////////////////////////////////////////////////////////////

grammar Deo;

options {
	output = AST;
	ASTLabelType = CommonTree;
}

tokens {        //TODO special tokens for labeling AST nodes
	IF;
	THEN;
	EXPR;
	RULE;
}

//////// Programs

prog	:	decl+ EOF							-> (PROG decl+)

//////// Declarations

decl	:	expr+								-> (DECL expr+)

//////// Constructs

norm	
	:	OB 								-> OB
	| 	PRO 								-> PRO
	| 	PER								-> PER
	;

op	:	AND 								-> AND
	| 	OR 								-> OR
	| 	NOT 								-> NOT
	| 	THEN								-> THEN

cond
	:	AGENT								-> AGENT
	| 	ACTION								-> ACTION
	;

rule	
	:	norm LB AGENT ACTION RB						-> (RULE norm AGENT ACTION)
	;

expr
	:	IF (LB cond (op cond)*)* RB THEN (LB rule (op rule)*)* RB	-> (IF (cond (op cond)*)* THEN (rule (op rule)*)*)
	|	(LB rule (op rule)*)* RB					-> (EXPR (rule (op rule)*)*)
	;

//////// Lexicon

OB	:	'should';
PRO	:	'should not';
PER	:	'may';

IF	:	'if';
THEN	:	'then';
NOT	:	'not';
AND	:	'and';
OR	:	'or';

LB	:	'(';
RB	:	')';

ACTION	:	LETTER (LETTER | DIGIT | SPACE)*;
AGENT	:	LETTER (LETTER | DIGIT | SPACE)*;

SPACE	:	(' ' | '\t')+             ;
EOL	:	'\r'? '\n'                ;
COMMENT :	'#' ~('\r' | '\n')*
		  '\r'? '\n'              ;

fragment LETTER : 'a'..'z' | 'A'..'Z' ;
fragment DIGIT  : '0'..'9' ;
