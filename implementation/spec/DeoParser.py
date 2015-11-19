# $ANTLR 3.1.2 Deo.g 2015-11-19 08:38:31

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
IFF=5
ASSN=14
STATE=19
RULE=9
RB=24
PER=17
LETTER=25
NOT=22
AND=20
ID=13
SPACE=27
EOF=-1
PRO=16
ACTION=18
OB=15
IF=4
AXIOM=10
PROG=11
EOL=28
EXPR=7
THEN=6
OR=21
LB=23
VAR=12
DIGIT=26
COMMENT=29
FACT=8

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "IF", "IFF", "THEN", "EXPR", "FACT", "RULE", "AXIOM", "PROG", "VAR", 
    "ID", "ASSN", "OB", "PRO", "PER", "ACTION", "STATE", "AND", "OR", "NOT", 
    "LB", "RB", "LETTER", "DIGIT", "SPACE", "EOL", "COMMENT"
]




class DeoParser(Parser):
    grammarFileName = "Deo.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "prog"
    # Deo.g:23:1: prog : ( var_decl )+ ( rule_decl )+ EOF -> ^( PROG ( var_decl )* ( rule_decl )+ ) ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF3 = None
        var_decl1 = None

        rule_decl2 = None


        EOF3_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_var_decl = RewriteRuleSubtreeStream(self._adaptor, "rule var_decl")
        stream_rule_decl = RewriteRuleSubtreeStream(self._adaptor, "rule rule_decl")
        try:
            try:
                # Deo.g:23:6: ( ( var_decl )+ ( rule_decl )+ EOF -> ^( PROG ( var_decl )* ( rule_decl )+ ) )
                # Deo.g:23:8: ( var_decl )+ ( rule_decl )+ EOF
                pass 
                # Deo.g:23:8: ( var_decl )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        alt1 = 1


                    if alt1 == 1:
                        # Deo.g:23:8: var_decl
                        pass 
                        self._state.following.append(self.FOLLOW_var_decl_in_prog90)
                        var_decl1 = self.var_decl()

                        self._state.following.pop()
                        stream_var_decl.add(var_decl1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                # Deo.g:23:18: ( rule_decl )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((LB <= LA2_0 <= RB)) :
                        alt2 = 1


                    if alt2 == 1:
                        # Deo.g:23:18: rule_decl
                        pass 
                        self._state.following.append(self.FOLLOW_rule_decl_in_prog93)
                        rule_decl2 = self.rule_decl()

                        self._state.following.pop()
                        stream_rule_decl.add(rule_decl2.tree)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                EOF3=self.match(self.input, EOF, self.FOLLOW_EOF_in_prog96) 
                stream_EOF.add(EOF3)

                # AST Rewrite
                # elements: rule_decl, var_decl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 23:38: -> ^( PROG ( var_decl )* ( rule_decl )+ )
                # Deo.g:23:41: ^( PROG ( var_decl )* ( rule_decl )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROG, "PROG"), root_1)

                # Deo.g:23:48: ( var_decl )*
                while stream_var_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_var_decl.nextTree())


                stream_var_decl.reset();
                # Deo.g:23:58: ( rule_decl )+
                if not (stream_rule_decl.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_rule_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_rule_decl.nextTree())


                stream_rule_decl.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "prog"

    class rule_decl_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "rule_decl"
    # Deo.g:26:1: rule_decl : ( expr )+ -> ^( RULE ( expr )+ ) ;
    def rule_decl(self, ):

        retval = self.rule_decl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        expr4 = None


        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Deo.g:27:2: ( ( expr )+ -> ^( RULE ( expr )+ ) )
                # Deo.g:27:4: ( expr )+
                pass 
                # Deo.g:27:4: ( expr )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == LB) :
                        alt3 = 1
                    elif (LA3_0 == RB) :
                        alt3 = 1


                    if alt3 == 1:
                        # Deo.g:27:4: expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_rule_decl125)
                        expr4 = self.expr()

                        self._state.following.pop()
                        stream_expr.add(expr4.tree)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1



                # AST Rewrite
                # elements: expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 27:15: -> ^( RULE ( expr )+ )
                # Deo.g:27:18: ^( RULE ( expr )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RULE, "RULE"), root_1)

                # Deo.g:27:25: ( expr )+
                if not (stream_expr.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_expr.hasNext():
                    self._adaptor.addChild(root_1, stream_expr.nextTree())


                stream_expr.reset()

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "rule_decl"

    class var_decl_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "var_decl"
    # Deo.g:30:1: var_decl : ID ASSN fact -> ^( VAR ID fact ) ;
    def var_decl(self, ):

        retval = self.var_decl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID5 = None
        ASSN6 = None
        fact7 = None


        ID5_tree = None
        ASSN6_tree = None
        stream_ASSN = RewriteRuleTokenStream(self._adaptor, "token ASSN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_fact = RewriteRuleSubtreeStream(self._adaptor, "rule fact")
        try:
            try:
                # Deo.g:31:2: ( ID ASSN fact -> ^( VAR ID fact ) )
                # Deo.g:31:4: ID ASSN fact
                pass 
                ID5=self.match(self.input, ID, self.FOLLOW_ID_in_var_decl152) 
                stream_ID.add(ID5)
                ASSN6=self.match(self.input, ASSN, self.FOLLOW_ASSN_in_var_decl154) 
                stream_ASSN.add(ASSN6)
                self._state.following.append(self.FOLLOW_fact_in_var_decl156)
                fact7 = self.fact()

                self._state.following.pop()
                stream_fact.add(fact7.tree)

                # AST Rewrite
                # elements: ID, fact
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 31:21: -> ^( VAR ID fact )
                # Deo.g:31:24: ^( VAR ID fact )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                self._adaptor.addChild(root_1, stream_ID.nextNode())
                self._adaptor.addChild(root_1, stream_fact.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "var_decl"

    class norm_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "norm"
    # Deo.g:34:1: norm : ( OB | PRO | PER );
    def norm(self, ):

        retval = self.norm_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set8 = None

        set8_tree = None

        try:
            try:
                # Deo.g:35:2: ( OB | PRO | PER )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()

                set8 = self.input.LT(1)
                if (OB <= self.input.LA(1) <= PER):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set8))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "norm"

    class fact_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "fact"
    # Deo.g:40:1: fact : ( ACTION | STATE );
    def fact(self, ):

        retval = self.fact_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set9 = None

        set9_tree = None

        try:
            try:
                # Deo.g:40:6: ( ACTION | STATE )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()

                set9 = self.input.LT(1)
                if (ACTION <= self.input.LA(1) <= STATE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set9))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "fact"

    class op_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "op"
    # Deo.g:44:1: op : ( AND | OR | NOT | THEN | IF | IFF );
    def op(self, ):

        retval = self.op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set10 = None

        set10_tree = None

        try:
            try:
                # Deo.g:44:4: ( AND | OR | NOT | THEN | IF | IFF )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()

                set10 = self.input.LT(1)
                if (IF <= self.input.LA(1) <= THEN) or (AND <= self.input.LA(1) <= NOT):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set10))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "op"

    class axiom_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "axiom"
    # Deo.g:52:1: axiom : norm LB ACTION RB -> ^( AXIOM norm ACTION ) ;
    def axiom(self, ):

        retval = self.axiom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB12 = None
        ACTION13 = None
        RB14 = None
        norm11 = None


        LB12_tree = None
        ACTION13_tree = None
        RB14_tree = None
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_ACTION = RewriteRuleTokenStream(self._adaptor, "token ACTION")
        stream_norm = RewriteRuleSubtreeStream(self._adaptor, "rule norm")
        try:
            try:
                # Deo.g:53:2: ( norm LB ACTION RB -> ^( AXIOM norm ACTION ) )
                # Deo.g:53:4: norm LB ACTION RB
                pass 
                self._state.following.append(self.FOLLOW_norm_in_axiom358)
                norm11 = self.norm()

                self._state.following.pop()
                stream_norm.add(norm11.tree)
                LB12=self.match(self.input, LB, self.FOLLOW_LB_in_axiom360) 
                stream_LB.add(LB12)
                ACTION13=self.match(self.input, ACTION, self.FOLLOW_ACTION_in_axiom362) 
                stream_ACTION.add(ACTION13)
                RB14=self.match(self.input, RB, self.FOLLOW_RB_in_axiom364) 
                stream_RB.add(RB14)

                # AST Rewrite
                # elements: ACTION, norm
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 53:25: -> ^( AXIOM norm ACTION )
                # Deo.g:53:28: ^( AXIOM norm ACTION )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AXIOM, "AXIOM"), root_1)

                self._adaptor.addChild(root_1, stream_norm.nextTree())
                self._adaptor.addChild(root_1, stream_ACTION.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "axiom"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "expr"
    # Deo.g:56:1: expr : ( ( LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB -> ^( EXPR IF FACT THEN AXIOM ) | ( LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB -> ^( EXPR IFF FACT THEN AXIOM ) | ( LB axiom ( op axiom )* )* RB -> ^( EXPR AXIOM ) );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB15 = None
        IF16 = None
        LB17 = None
        RB21 = None
        THEN22 = None
        LB23 = None
        RB27 = None
        RB28 = None
        LB29 = None
        IFF30 = None
        LB31 = None
        RB35 = None
        THEN36 = None
        LB37 = None
        RB41 = None
        RB42 = None
        LB43 = None
        RB47 = None
        fact18 = None

        op19 = None

        fact20 = None

        axiom24 = None

        op25 = None

        axiom26 = None

        fact32 = None

        op33 = None

        fact34 = None

        axiom38 = None

        op39 = None

        axiom40 = None

        axiom44 = None

        op45 = None

        axiom46 = None


        LB15_tree = None
        IF16_tree = None
        LB17_tree = None
        RB21_tree = None
        THEN22_tree = None
        LB23_tree = None
        RB27_tree = None
        RB28_tree = None
        LB29_tree = None
        IFF30_tree = None
        LB31_tree = None
        RB35_tree = None
        THEN36_tree = None
        LB37_tree = None
        RB41_tree = None
        RB42_tree = None
        LB43_tree = None
        RB47_tree = None
        stream_IFF = RewriteRuleTokenStream(self._adaptor, "token IFF")
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_THEN = RewriteRuleTokenStream(self._adaptor, "token THEN")
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_fact = RewriteRuleSubtreeStream(self._adaptor, "rule fact")
        stream_op = RewriteRuleSubtreeStream(self._adaptor, "rule op")
        stream_axiom = RewriteRuleSubtreeStream(self._adaptor, "rule axiom")
        try:
            try:
                # Deo.g:57:2: ( ( LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB -> ^( EXPR IF FACT THEN AXIOM ) | ( LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB -> ^( EXPR IFF FACT THEN AXIOM ) | ( LB axiom ( op axiom )* )* RB -> ^( EXPR AXIOM ) )
                alt16 = 3
                LA16_0 = self.input.LA(1)

                if (LA16_0 == LB) :
                    LA16 = self.input.LA(2)
                    if LA16 == IF:
                        alt16 = 1
                    elif LA16 == IFF:
                        alt16 = 2
                    elif LA16 == OB or LA16 == PRO or LA16 == PER:
                        alt16 = 3
                    else:
                        nvae = NoViableAltException("", 16, 1, self.input)

                        raise nvae

                elif (LA16_0 == RB) :
                    alt16 = 1
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # Deo.g:57:4: ( LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB
                    pass 
                    # Deo.g:57:4: ( LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )*
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == LB) :
                            alt8 = 1


                        if alt8 == 1:
                            # Deo.g:57:5: LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB
                            pass 
                            LB15=self.match(self.input, LB, self.FOLLOW_LB_in_expr389) 
                            stream_LB.add(LB15)
                            IF16=self.match(self.input, IF, self.FOLLOW_IF_in_expr391) 
                            stream_IF.add(IF16)
                            # Deo.g:57:11: ( LB fact ( op fact )* )*
                            while True: #loop5
                                alt5 = 2
                                LA5_0 = self.input.LA(1)

                                if (LA5_0 == LB) :
                                    alt5 = 1


                                if alt5 == 1:
                                    # Deo.g:57:12: LB fact ( op fact )*
                                    pass 
                                    LB17=self.match(self.input, LB, self.FOLLOW_LB_in_expr394) 
                                    stream_LB.add(LB17)
                                    self._state.following.append(self.FOLLOW_fact_in_expr396)
                                    fact18 = self.fact()

                                    self._state.following.pop()
                                    stream_fact.add(fact18.tree)
                                    # Deo.g:57:20: ( op fact )*
                                    while True: #loop4
                                        alt4 = 2
                                        LA4_0 = self.input.LA(1)

                                        if ((IF <= LA4_0 <= THEN) or (AND <= LA4_0 <= NOT)) :
                                            alt4 = 1


                                        if alt4 == 1:
                                            # Deo.g:57:21: op fact
                                            pass 
                                            self._state.following.append(self.FOLLOW_op_in_expr399)
                                            op19 = self.op()

                                            self._state.following.pop()
                                            stream_op.add(op19.tree)
                                            self._state.following.append(self.FOLLOW_fact_in_expr401)
                                            fact20 = self.fact()

                                            self._state.following.pop()
                                            stream_fact.add(fact20.tree)


                                        else:
                                            break #loop4




                                else:
                                    break #loop5


                            RB21=self.match(self.input, RB, self.FOLLOW_RB_in_expr407) 
                            stream_RB.add(RB21)
                            THEN22=self.match(self.input, THEN, self.FOLLOW_THEN_in_expr412) 
                            stream_THEN.add(THEN22)
                            # Deo.g:58:8: ( LB axiom ( op axiom )* )*
                            while True: #loop7
                                alt7 = 2
                                LA7_0 = self.input.LA(1)

                                if (LA7_0 == LB) :
                                    alt7 = 1


                                if alt7 == 1:
                                    # Deo.g:58:9: LB axiom ( op axiom )*
                                    pass 
                                    LB23=self.match(self.input, LB, self.FOLLOW_LB_in_expr415) 
                                    stream_LB.add(LB23)
                                    self._state.following.append(self.FOLLOW_axiom_in_expr417)
                                    axiom24 = self.axiom()

                                    self._state.following.pop()
                                    stream_axiom.add(axiom24.tree)
                                    # Deo.g:58:18: ( op axiom )*
                                    while True: #loop6
                                        alt6 = 2
                                        LA6_0 = self.input.LA(1)

                                        if ((IF <= LA6_0 <= THEN) or (AND <= LA6_0 <= NOT)) :
                                            alt6 = 1


                                        if alt6 == 1:
                                            # Deo.g:58:19: op axiom
                                            pass 
                                            self._state.following.append(self.FOLLOW_op_in_expr420)
                                            op25 = self.op()

                                            self._state.following.pop()
                                            stream_op.add(op25.tree)
                                            self._state.following.append(self.FOLLOW_axiom_in_expr422)
                                            axiom26 = self.axiom()

                                            self._state.following.pop()
                                            stream_axiom.add(axiom26.tree)


                                        else:
                                            break #loop6




                                else:
                                    break #loop7


                            RB27=self.match(self.input, RB, self.FOLLOW_RB_in_expr428) 
                            stream_RB.add(RB27)


                        else:
                            break #loop8


                    RB28=self.match(self.input, RB, self.FOLLOW_RB_in_expr432) 
                    stream_RB.add(RB28)

                    # AST Rewrite
                    # elements: THEN, IF
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 58:42: -> ^( EXPR IF FACT THEN AXIOM )
                    # Deo.g:58:45: ^( EXPR IF FACT THEN AXIOM )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_IF.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(FACT, "FACT"))
                    self._adaptor.addChild(root_1, stream_THEN.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(AXIOM, "AXIOM"))

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt16 == 2:
                    # Deo.g:59:4: ( LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB
                    pass 
                    # Deo.g:59:4: ( LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == LB) :
                            alt13 = 1


                        if alt13 == 1:
                            # Deo.g:59:5: LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB
                            pass 
                            LB29=self.match(self.input, LB, self.FOLLOW_LB_in_expr454) 
                            stream_LB.add(LB29)
                            IFF30=self.match(self.input, IFF, self.FOLLOW_IFF_in_expr456) 
                            stream_IFF.add(IFF30)
                            # Deo.g:59:12: ( LB fact ( op fact )* )*
                            while True: #loop10
                                alt10 = 2
                                LA10_0 = self.input.LA(1)

                                if (LA10_0 == LB) :
                                    alt10 = 1


                                if alt10 == 1:
                                    # Deo.g:59:13: LB fact ( op fact )*
                                    pass 
                                    LB31=self.match(self.input, LB, self.FOLLOW_LB_in_expr459) 
                                    stream_LB.add(LB31)
                                    self._state.following.append(self.FOLLOW_fact_in_expr461)
                                    fact32 = self.fact()

                                    self._state.following.pop()
                                    stream_fact.add(fact32.tree)
                                    # Deo.g:59:21: ( op fact )*
                                    while True: #loop9
                                        alt9 = 2
                                        LA9_0 = self.input.LA(1)

                                        if ((IF <= LA9_0 <= THEN) or (AND <= LA9_0 <= NOT)) :
                                            alt9 = 1


                                        if alt9 == 1:
                                            # Deo.g:59:22: op fact
                                            pass 
                                            self._state.following.append(self.FOLLOW_op_in_expr464)
                                            op33 = self.op()

                                            self._state.following.pop()
                                            stream_op.add(op33.tree)
                                            self._state.following.append(self.FOLLOW_fact_in_expr466)
                                            fact34 = self.fact()

                                            self._state.following.pop()
                                            stream_fact.add(fact34.tree)


                                        else:
                                            break #loop9




                                else:
                                    break #loop10


                            RB35=self.match(self.input, RB, self.FOLLOW_RB_in_expr472) 
                            stream_RB.add(RB35)
                            THEN36=self.match(self.input, THEN, self.FOLLOW_THEN_in_expr477) 
                            stream_THEN.add(THEN36)
                            # Deo.g:60:8: ( LB axiom ( op axiom )* )*
                            while True: #loop12
                                alt12 = 2
                                LA12_0 = self.input.LA(1)

                                if (LA12_0 == LB) :
                                    alt12 = 1


                                if alt12 == 1:
                                    # Deo.g:60:9: LB axiom ( op axiom )*
                                    pass 
                                    LB37=self.match(self.input, LB, self.FOLLOW_LB_in_expr480) 
                                    stream_LB.add(LB37)
                                    self._state.following.append(self.FOLLOW_axiom_in_expr482)
                                    axiom38 = self.axiom()

                                    self._state.following.pop()
                                    stream_axiom.add(axiom38.tree)
                                    # Deo.g:60:18: ( op axiom )*
                                    while True: #loop11
                                        alt11 = 2
                                        LA11_0 = self.input.LA(1)

                                        if ((IF <= LA11_0 <= THEN) or (AND <= LA11_0 <= NOT)) :
                                            alt11 = 1


                                        if alt11 == 1:
                                            # Deo.g:60:19: op axiom
                                            pass 
                                            self._state.following.append(self.FOLLOW_op_in_expr485)
                                            op39 = self.op()

                                            self._state.following.pop()
                                            stream_op.add(op39.tree)
                                            self._state.following.append(self.FOLLOW_axiom_in_expr487)
                                            axiom40 = self.axiom()

                                            self._state.following.pop()
                                            stream_axiom.add(axiom40.tree)


                                        else:
                                            break #loop11




                                else:
                                    break #loop12


                            RB41=self.match(self.input, RB, self.FOLLOW_RB_in_expr493) 
                            stream_RB.add(RB41)


                        else:
                            break #loop13


                    RB42=self.match(self.input, RB, self.FOLLOW_RB_in_expr497) 
                    stream_RB.add(RB42)

                    # AST Rewrite
                    # elements: THEN, IFF
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 60:42: -> ^( EXPR IFF FACT THEN AXIOM )
                    # Deo.g:60:45: ^( EXPR IFF FACT THEN AXIOM )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_IFF.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(FACT, "FACT"))
                    self._adaptor.addChild(root_1, stream_THEN.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(AXIOM, "AXIOM"))

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt16 == 3:
                    # Deo.g:61:4: ( LB axiom ( op axiom )* )* RB
                    pass 
                    # Deo.g:61:4: ( LB axiom ( op axiom )* )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == LB) :
                            alt15 = 1


                        if alt15 == 1:
                            # Deo.g:61:5: LB axiom ( op axiom )*
                            pass 
                            LB43=self.match(self.input, LB, self.FOLLOW_LB_in_expr520) 
                            stream_LB.add(LB43)
                            self._state.following.append(self.FOLLOW_axiom_in_expr522)
                            axiom44 = self.axiom()

                            self._state.following.pop()
                            stream_axiom.add(axiom44.tree)
                            # Deo.g:61:14: ( op axiom )*
                            while True: #loop14
                                alt14 = 2
                                LA14_0 = self.input.LA(1)

                                if ((IF <= LA14_0 <= THEN) or (AND <= LA14_0 <= NOT)) :
                                    alt14 = 1


                                if alt14 == 1:
                                    # Deo.g:61:15: op axiom
                                    pass 
                                    self._state.following.append(self.FOLLOW_op_in_expr525)
                                    op45 = self.op()

                                    self._state.following.pop()
                                    stream_op.add(op45.tree)
                                    self._state.following.append(self.FOLLOW_axiom_in_expr527)
                                    axiom46 = self.axiom()

                                    self._state.following.pop()
                                    stream_axiom.add(axiom46.tree)


                                else:
                                    break #loop14




                        else:
                            break #loop15


                    RB47=self.match(self.input, RB, self.FOLLOW_RB_in_expr533) 
                    stream_RB.add(RB47)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 61:35: -> ^( EXPR AXIOM )
                    # Deo.g:61:38: ^( EXPR AXIOM )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, self._adaptor.createFromType(AXIOM, "AXIOM"))

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "expr"


    # Delegated rules


 

    FOLLOW_var_decl_in_prog90 = frozenset([13, 23, 24])
    FOLLOW_rule_decl_in_prog93 = frozenset([23, 24])
    FOLLOW_EOF_in_prog96 = frozenset([1])
    FOLLOW_expr_in_rule_decl125 = frozenset([1, 23, 24])
    FOLLOW_ID_in_var_decl152 = frozenset([14])
    FOLLOW_ASSN_in_var_decl154 = frozenset([18, 19])
    FOLLOW_fact_in_var_decl156 = frozenset([1])
    FOLLOW_set_in_norm0 = frozenset([1])
    FOLLOW_set_in_fact0 = frozenset([1])
    FOLLOW_set_in_op0 = frozenset([1])
    FOLLOW_norm_in_axiom358 = frozenset([23])
    FOLLOW_LB_in_axiom360 = frozenset([18])
    FOLLOW_ACTION_in_axiom362 = frozenset([24])
    FOLLOW_RB_in_axiom364 = frozenset([1])
    FOLLOW_LB_in_expr389 = frozenset([4])
    FOLLOW_IF_in_expr391 = frozenset([23, 24])
    FOLLOW_LB_in_expr394 = frozenset([18, 19])
    FOLLOW_fact_in_expr396 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_op_in_expr399 = frozenset([18, 19])
    FOLLOW_fact_in_expr401 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_RB_in_expr407 = frozenset([6])
    FOLLOW_THEN_in_expr412 = frozenset([23, 24])
    FOLLOW_LB_in_expr415 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr417 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_op_in_expr420 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr422 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_RB_in_expr428 = frozenset([23, 24])
    FOLLOW_RB_in_expr432 = frozenset([1])
    FOLLOW_LB_in_expr454 = frozenset([5])
    FOLLOW_IFF_in_expr456 = frozenset([23, 24])
    FOLLOW_LB_in_expr459 = frozenset([18, 19])
    FOLLOW_fact_in_expr461 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_op_in_expr464 = frozenset([18, 19])
    FOLLOW_fact_in_expr466 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_RB_in_expr472 = frozenset([6])
    FOLLOW_THEN_in_expr477 = frozenset([23, 24])
    FOLLOW_LB_in_expr480 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr482 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_op_in_expr485 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr487 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_RB_in_expr493 = frozenset([23, 24])
    FOLLOW_RB_in_expr497 = frozenset([1])
    FOLLOW_LB_in_expr520 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr522 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_op_in_expr525 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr527 = frozenset([4, 5, 6, 20, 21, 22, 23, 24])
    FOLLOW_RB_in_expr533 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("DeoLexer", DeoParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
