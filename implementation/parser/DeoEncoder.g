//////////////////////////////////////////////////////////////
//
// Specification of the Deo code generator.
// -Deo -> SVM code generator
//
// Developed 2015/2016 Leisha Hussien (2020430H). 
// Adapted from code written by David Watt (University of Glasgow). 
//
//////////////////////////////////////////////////////////////

tree grammar DeoEncoder;

// This specifies the Deo -> SVM code generator.

options {
	tokenVocab = Deo;
	ASTLabelType = CommonTree;
}

// Auxiliary variables and methods

@members {
	private SVM obj = new SVM();

	private int globalvaraddr = 0;
	private int localvaraddr = 0;
	private int currentLocale = Address.GLOBAL;

	private SymbolTable<Address> addrTable =
	   new SymbolTable<Address>();

	private void predefine () {
	// Add predefined procedures to the address table.
		addrTable.put("read", new Address(SVM.READOFFSET, Address.CODE));
		addrTable.put("write", new Address(SVM.WRITEOFFSET, Address.CODE));
	}
}

//TODO Constructs

norm	
	:	OB
	| 	PRO
	| 	PER
	;

op	:	AND
	| 	OR
	| 	NOT
	| 	THEN

cond
	:	AGENT
	| 	ACTION
	;

rule	
	:	^(RULE 
		  norm 
		  AGENT 
		  ACTION)
	;

expr
	:	^(IF 
		  cond 
		  op 
		  cond
		  THEN 
		  rule 
		  op 
		  rule)
	|	^(EXPR 
		  rule 
		  op 
		  rule)
	;
