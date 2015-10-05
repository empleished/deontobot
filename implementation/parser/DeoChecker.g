//////////////////////////////////////////////////////////////
//
// specification of the Deo contextual analyser:
// -scope checking
// -type checking
//
// Developed 2015/2016 by Leisha Hussien (2020430H). 
// Adapted from code written by David Watt (University of Glasgow). 
//
//////////////////////////////////////////////////////////////

tree grammar DeoChecker;

options {
	tokenVocab = Deo;
	ASTLabelType = CommonTree;
}


//////// Auxiliary variables and methods

@members {

	// Contextual errors

	private int errorCount = 0;

	private void reportError (String message,
	                          CommonTree ast) {
	// Print an error message relating to the given 
	// (sub)AST.
		int line = ast.getLine(),
		    column = ast.getCharPositionInLine() ;
		System.err.println("line " + line + ":" + column + " " + message);
		errorCount++;
	}

	public int getNumberOfContextualErrors () {
	// Return the total number of errors so far detected.
		return errorCount;
	}

	// Scope checking

	private SymbolTable<Type> typeTable =
	   new SymbolTable<Type>();

	private void predefine () {
	// Add predefined procedures to the type table.
		typeTable.put("read", new Type.Mapping(Type.VOID, Type.INT));
		typeTable.put("write", new Type.Mapping(Type.INT, Type.VOID));
	}

	private void define (String id, Type type, CommonTree decl) {
	// Add id with its type to the type table, checking 
	// that id is not already declared in the same scope.
		boolean ok = typeTable.put(id, type);
		if (!ok) {
			reportError(id + " is redeclared", decl);
		}
	}

	private Type retrieve (String id, CommonTree occ) {
	// Retrieve id's type from the type table.
		Type type = typeTable.get(id);
		if (type == null) {
			reportError(id + " is undeclared", occ);
			return Type.ERROR;
		} else
			return type;
	}

	// Type checking

	private static final Type.Mapping
	   NOTTYPE = new Type.Mapping(Type.BOOL, Type.BOOL),
	   COMPTYPE = new Type.Mapping(
	      new Type.Pair(Type.INT, Type.INT), Type.BOOL),
	   ARITHTYPE = new Type.Mapping(
	      new Type.Pair(Type.INT, Type.INT), Type.INT),
	   MAINTYPE = new Type.Mapping(Type.VOID, Type.VOID);

	private void checkType (Type typeExpected,
	                        Type typeActual,
	                        CommonTree construct) {
	// Check that a construct's actual type matches 
	// the expected type.
		if (! typeActual.equiv(typeExpected))
			reportError("type is " + typeActual
			   + ", should be " + typeExpected,
			   construct);
	}

	private Type checkCall (String id, Type typeArg,
	                        CommonTree call) {
	// Check that a procedure call identifies a procedure 
	// and that its argument type matches the proecure's 
	// type. Return the type of the procedure call.
		Type typeProc = retrieve(id, call);
		if (! (typeProc instanceof Type.Mapping)) {
			reportError(id + " is not a procedure", call);
			return Type.ERROR;
		} else {
			Type.Mapping mapping = (Type.Mapping)typeProc;
			checkType(mapping.domain, typeArg, call);
			return mapping.range;
		}
	}

	private Type checkUnary (Type.Mapping typeOp,
	                         Type typeArg,
	                         CommonTree op) {
	// Check that a unary operator's operand type matches 
	// the operator's type. Return the type of the operator 
	// application.
		if (!(typeOp.domain instanceof Type.Primitive))
			reportError("unary operator should have 1 operand", op);
		else
			checkType(typeOp.domain, typeArg, op);
		return typeOp.range;
	}

	private Type checkBinary (Type.Mapping typeOp,
	                          Type typeArg1, Type typeArg2,
	                          CommonTree op) {
	// Check that a binary operator's operand types match 
	// the operator's type. Return the type of the operator 
	// application.
		if (! (typeOp.domain instanceof Type.Pair))
			reportError("binary operator should have 2 operands", op);
		else {
			Type.Pair pair = (Type.Pair)typeOp.domain;
			checkType(pair.first, typeArg1, op);
			checkType(pair.second, typeArg2, op);
		}
		return typeOp.range;
	}

}

//TODO Constructs
