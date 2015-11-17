# $ANTLR 3.1.2 Deo.g 2015-11-17 17:47:04

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
RB=25
PER=17
LETTER=26
NOT=23
AND=21
ID=13
SPACE=28
EOF=-1
PRO=16
ACTION=18
OB=15
IF=4
AXIOM=10
PROG=11
EOL=29
EXPR=7
THEN=6
OR=22
AGENT=20
LB=24
VAR=12
DIGIT=27
COMMENT=30
FACT=8

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "IF", "IFF", "THEN", "EXPR", "FACT", "RULE", "AXIOM", "PROG", "VAR", 
    "ID", "ASSN", "OB", "PRO", "PER", "ACTION", "STATE", "AGENT", "AND", 
    "OR", "NOT", "LB", "RB", "LETTER", "DIGIT", "SPACE", "EOL", "COMMENT"
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


        self.dfa19 = self.DFA19(
            self, 19,
            eot = self.DFA19_eot,
            eof = self.DFA19_eof,
            min = self.DFA19_min,
            max = self.DFA19_max,
            accept = self.DFA19_accept,
            special = self.DFA19_special,
            transition = self.DFA19_transition
            )






                
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
    # Deo.g:40:1: fact : ( ACTION | STATE | AGENT );
    def fact(self, ):

        retval = self.fact_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set9 = None

        set9_tree = None

        try:
            try:
                # Deo.g:40:6: ( ACTION | STATE | AGENT )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()

                set9 = self.input.LT(1)
                if (ACTION <= self.input.LA(1) <= AGENT):
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
    # Deo.g:45:1: op : ( AND | OR | NOT | THEN | IF | IFF );
    def op(self, ):

        retval = self.op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set10 = None

        set10_tree = None

        try:
            try:
                # Deo.g:45:4: ( AND | OR | NOT | THEN | IF | IFF )
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
    # Deo.g:53:1: axiom : norm LB ACTION RB -> ^( AXIOM norm AGENT ACTION ) ;
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
                # Deo.g:54:2: ( norm LB ACTION RB -> ^( AXIOM norm AGENT ACTION ) )
                # Deo.g:54:4: norm LB ACTION RB
                pass 
                self._state.following.append(self.FOLLOW_norm_in_axiom365)
                norm11 = self.norm()

                self._state.following.pop()
                stream_norm.add(norm11.tree)
                LB12=self.match(self.input, LB, self.FOLLOW_LB_in_axiom367) 
                stream_LB.add(LB12)
                ACTION13=self.match(self.input, ACTION, self.FOLLOW_ACTION_in_axiom369) 
                stream_ACTION.add(ACTION13)
                RB14=self.match(self.input, RB, self.FOLLOW_RB_in_axiom371) 
                stream_RB.add(RB14)

                # AST Rewrite
                # elements: norm, ACTION
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
                # 54:25: -> ^( AXIOM norm AGENT ACTION )
                # Deo.g:54:28: ^( AXIOM norm AGENT ACTION )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AXIOM, "AXIOM"), root_1)

                self._adaptor.addChild(root_1, stream_norm.nextTree())
                self._adaptor.addChild(root_1, self._adaptor.createFromType(AGENT, "AGENT"))
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
    # Deo.g:57:1: expr : ( ( LB AGENT )* RB ( LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB -> ^( EXPR AGENT IF FACT THEN AXIOM axiom ) | ( LB AGENT )* RB ( LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB -> ^( EXPR AGENT IFF FACT THEN AXIOM axiom ) | ( LB AGENT )* RB ( LB axiom ( op axiom )* )* RB -> ^( EXPR AGENT AXIOM axiom ) );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB15 = None
        AGENT16 = None
        RB17 = None
        LB18 = None
        IF19 = None
        LB20 = None
        RB24 = None
        THEN25 = None
        LB26 = None
        RB30 = None
        RB31 = None
        LB32 = None
        AGENT33 = None
        RB34 = None
        LB35 = None
        IFF36 = None
        LB37 = None
        RB41 = None
        THEN42 = None
        LB43 = None
        RB47 = None
        RB48 = None
        LB49 = None
        AGENT50 = None
        RB51 = None
        LB52 = None
        RB56 = None
        fact21 = None

        op22 = None

        fact23 = None

        axiom27 = None

        op28 = None

        axiom29 = None

        fact38 = None

        op39 = None

        fact40 = None

        axiom44 = None

        op45 = None

        axiom46 = None

        axiom53 = None

        op54 = None

        axiom55 = None


        LB15_tree = None
        AGENT16_tree = None
        RB17_tree = None
        LB18_tree = None
        IF19_tree = None
        LB20_tree = None
        RB24_tree = None
        THEN25_tree = None
        LB26_tree = None
        RB30_tree = None
        RB31_tree = None
        LB32_tree = None
        AGENT33_tree = None
        RB34_tree = None
        LB35_tree = None
        IFF36_tree = None
        LB37_tree = None
        RB41_tree = None
        THEN42_tree = None
        LB43_tree = None
        RB47_tree = None
        RB48_tree = None
        LB49_tree = None
        AGENT50_tree = None
        RB51_tree = None
        LB52_tree = None
        RB56_tree = None
        stream_IFF = RewriteRuleTokenStream(self._adaptor, "token IFF")
        stream_AGENT = RewriteRuleTokenStream(self._adaptor, "token AGENT")
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_THEN = RewriteRuleTokenStream(self._adaptor, "token THEN")
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_fact = RewriteRuleSubtreeStream(self._adaptor, "rule fact")
        stream_op = RewriteRuleSubtreeStream(self._adaptor, "rule op")
        stream_axiom = RewriteRuleSubtreeStream(self._adaptor, "rule axiom")
        try:
            try:
                # Deo.g:58:2: ( ( LB AGENT )* RB ( LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB -> ^( EXPR AGENT IF FACT THEN AXIOM axiom ) | ( LB AGENT )* RB ( LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB -> ^( EXPR AGENT IFF FACT THEN AXIOM axiom ) | ( LB AGENT )* RB ( LB axiom ( op axiom )* )* RB -> ^( EXPR AGENT AXIOM axiom ) )
                alt19 = 3
                alt19 = self.dfa19.predict(self.input)
                if alt19 == 1:
                    # Deo.g:58:4: ( LB AGENT )* RB ( LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB
                    pass 
                    # Deo.g:58:4: ( LB AGENT )*
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == LB) :
                            alt4 = 1


                        if alt4 == 1:
                            # Deo.g:58:5: LB AGENT
                            pass 
                            LB15=self.match(self.input, LB, self.FOLLOW_LB_in_expr398) 
                            stream_LB.add(LB15)
                            AGENT16=self.match(self.input, AGENT, self.FOLLOW_AGENT_in_expr400) 
                            stream_AGENT.add(AGENT16)


                        else:
                            break #loop4


                    RB17=self.match(self.input, RB, self.FOLLOW_RB_in_expr404) 
                    stream_RB.add(RB17)
                    # Deo.g:58:19: ( LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == LB) :
                            alt9 = 1


                        if alt9 == 1:
                            # Deo.g:58:20: LB IF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB
                            pass 
                            LB18=self.match(self.input, LB, self.FOLLOW_LB_in_expr407) 
                            stream_LB.add(LB18)
                            IF19=self.match(self.input, IF, self.FOLLOW_IF_in_expr412) 
                            stream_IF.add(IF19)
                            # Deo.g:59:6: ( LB fact ( op fact )* )*
                            while True: #loop6
                                alt6 = 2
                                LA6_0 = self.input.LA(1)

                                if (LA6_0 == LB) :
                                    alt6 = 1


                                if alt6 == 1:
                                    # Deo.g:59:7: LB fact ( op fact )*
                                    pass 
                                    LB20=self.match(self.input, LB, self.FOLLOW_LB_in_expr415) 
                                    stream_LB.add(LB20)
                                    self._state.following.append(self.FOLLOW_fact_in_expr417)
                                    fact21 = self.fact()

                                    self._state.following.pop()
                                    stream_fact.add(fact21.tree)
                                    # Deo.g:59:15: ( op fact )*
                                    while True: #loop5
                                        alt5 = 2
                                        LA5_0 = self.input.LA(1)

                                        if ((IF <= LA5_0 <= THEN) or (AND <= LA5_0 <= NOT)) :
                                            alt5 = 1


                                        if alt5 == 1:
                                            # Deo.g:59:16: op fact
                                            pass 
                                            self._state.following.append(self.FOLLOW_op_in_expr420)
                                            op22 = self.op()

                                            self._state.following.pop()
                                            stream_op.add(op22.tree)
                                            self._state.following.append(self.FOLLOW_fact_in_expr422)
                                            fact23 = self.fact()

                                            self._state.following.pop()
                                            stream_fact.add(fact23.tree)


                                        else:
                                            break #loop5




                                else:
                                    break #loop6


                            RB24=self.match(self.input, RB, self.FOLLOW_RB_in_expr428) 
                            stream_RB.add(RB24)
                            THEN25=self.match(self.input, THEN, self.FOLLOW_THEN_in_expr433) 
                            stream_THEN.add(THEN25)
                            # Deo.g:60:8: ( LB axiom ( op axiom )* )*
                            while True: #loop8
                                alt8 = 2
                                LA8_0 = self.input.LA(1)

                                if (LA8_0 == LB) :
                                    alt8 = 1


                                if alt8 == 1:
                                    # Deo.g:60:9: LB axiom ( op axiom )*
                                    pass 
                                    LB26=self.match(self.input, LB, self.FOLLOW_LB_in_expr436) 
                                    stream_LB.add(LB26)
                                    self._state.following.append(self.FOLLOW_axiom_in_expr438)
                                    axiom27 = self.axiom()

                                    self._state.following.pop()
                                    stream_axiom.add(axiom27.tree)
                                    # Deo.g:60:18: ( op axiom )*
                                    while True: #loop7
                                        alt7 = 2
                                        LA7_0 = self.input.LA(1)

                                        if ((IF <= LA7_0 <= THEN) or (AND <= LA7_0 <= NOT)) :
                                            alt7 = 1


                                        if alt7 == 1:
                                            # Deo.g:60:19: op axiom
                                            pass 
                                            self._state.following.append(self.FOLLOW_op_in_expr441)
                                            op28 = self.op()

                                            self._state.following.pop()
                                            stream_op.add(op28.tree)
                                            self._state.following.append(self.FOLLOW_axiom_in_expr443)
                                            axiom29 = self.axiom()

                                            self._state.following.pop()
                                            stream_axiom.add(axiom29.tree)


                                        else:
                                            break #loop7




                                else:
                                    break #loop8


                            RB30=self.match(self.input, RB, self.FOLLOW_RB_in_expr449) 
                            stream_RB.add(RB30)


                        else:
                            break #loop9


                    RB31=self.match(self.input, RB, self.FOLLOW_RB_in_expr453) 
                    stream_RB.add(RB31)

                    # AST Rewrite
                    # elements: AGENT, axiom, IF, THEN
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
                    # 60:42: -> ^( EXPR AGENT IF FACT THEN AXIOM axiom )
                    # Deo.g:60:45: ^( EXPR AGENT IF FACT THEN AXIOM axiom )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_AGENT.nextNode())
                    self._adaptor.addChild(root_1, stream_IF.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(FACT, "FACT"))
                    self._adaptor.addChild(root_1, stream_THEN.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(AXIOM, "AXIOM"))
                    self._adaptor.addChild(root_1, stream_axiom.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt19 == 2:
                    # Deo.g:61:4: ( LB AGENT )* RB ( LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )* RB
                    pass 
                    # Deo.g:61:4: ( LB AGENT )*
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == LB) :
                            alt10 = 1


                        if alt10 == 1:
                            # Deo.g:61:5: LB AGENT
                            pass 
                            LB32=self.match(self.input, LB, self.FOLLOW_LB_in_expr479) 
                            stream_LB.add(LB32)
                            AGENT33=self.match(self.input, AGENT, self.FOLLOW_AGENT_in_expr481) 
                            stream_AGENT.add(AGENT33)


                        else:
                            break #loop10


                    RB34=self.match(self.input, RB, self.FOLLOW_RB_in_expr485) 
                    stream_RB.add(RB34)
                    # Deo.g:61:19: ( LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == LB) :
                            alt15 = 1


                        if alt15 == 1:
                            # Deo.g:61:20: LB IFF ( LB fact ( op fact )* )* RB THEN ( LB axiom ( op axiom )* )* RB
                            pass 
                            LB35=self.match(self.input, LB, self.FOLLOW_LB_in_expr488) 
                            stream_LB.add(LB35)
                            IFF36=self.match(self.input, IFF, self.FOLLOW_IFF_in_expr493) 
                            stream_IFF.add(IFF36)
                            # Deo.g:62:7: ( LB fact ( op fact )* )*
                            while True: #loop12
                                alt12 = 2
                                LA12_0 = self.input.LA(1)

                                if (LA12_0 == LB) :
                                    alt12 = 1


                                if alt12 == 1:
                                    # Deo.g:62:8: LB fact ( op fact )*
                                    pass 
                                    LB37=self.match(self.input, LB, self.FOLLOW_LB_in_expr496) 
                                    stream_LB.add(LB37)
                                    self._state.following.append(self.FOLLOW_fact_in_expr498)
                                    fact38 = self.fact()

                                    self._state.following.pop()
                                    stream_fact.add(fact38.tree)
                                    # Deo.g:62:16: ( op fact )*
                                    while True: #loop11
                                        alt11 = 2
                                        LA11_0 = self.input.LA(1)

                                        if ((IF <= LA11_0 <= THEN) or (AND <= LA11_0 <= NOT)) :
                                            alt11 = 1


                                        if alt11 == 1:
                                            # Deo.g:62:17: op fact
                                            pass 
                                            self._state.following.append(self.FOLLOW_op_in_expr501)
                                            op39 = self.op()

                                            self._state.following.pop()
                                            stream_op.add(op39.tree)
                                            self._state.following.append(self.FOLLOW_fact_in_expr503)
                                            fact40 = self.fact()

                                            self._state.following.pop()
                                            stream_fact.add(fact40.tree)


                                        else:
                                            break #loop11




                                else:
                                    break #loop12


                            RB41=self.match(self.input, RB, self.FOLLOW_RB_in_expr509) 
                            stream_RB.add(RB41)
                            THEN42=self.match(self.input, THEN, self.FOLLOW_THEN_in_expr514) 
                            stream_THEN.add(THEN42)
                            # Deo.g:63:8: ( LB axiom ( op axiom )* )*
                            while True: #loop14
                                alt14 = 2
                                LA14_0 = self.input.LA(1)

                                if (LA14_0 == LB) :
                                    alt14 = 1


                                if alt14 == 1:
                                    # Deo.g:63:9: LB axiom ( op axiom )*
                                    pass 
                                    LB43=self.match(self.input, LB, self.FOLLOW_LB_in_expr517) 
                                    stream_LB.add(LB43)
                                    self._state.following.append(self.FOLLOW_axiom_in_expr519)
                                    axiom44 = self.axiom()

                                    self._state.following.pop()
                                    stream_axiom.add(axiom44.tree)
                                    # Deo.g:63:18: ( op axiom )*
                                    while True: #loop13
                                        alt13 = 2
                                        LA13_0 = self.input.LA(1)

                                        if ((IF <= LA13_0 <= THEN) or (AND <= LA13_0 <= NOT)) :
                                            alt13 = 1


                                        if alt13 == 1:
                                            # Deo.g:63:19: op axiom
                                            pass 
                                            self._state.following.append(self.FOLLOW_op_in_expr522)
                                            op45 = self.op()

                                            self._state.following.pop()
                                            stream_op.add(op45.tree)
                                            self._state.following.append(self.FOLLOW_axiom_in_expr524)
                                            axiom46 = self.axiom()

                                            self._state.following.pop()
                                            stream_axiom.add(axiom46.tree)


                                        else:
                                            break #loop13




                                else:
                                    break #loop14


                            RB47=self.match(self.input, RB, self.FOLLOW_RB_in_expr530) 
                            stream_RB.add(RB47)


                        else:
                            break #loop15


                    RB48=self.match(self.input, RB, self.FOLLOW_RB_in_expr534) 
                    stream_RB.add(RB48)

                    # AST Rewrite
                    # elements: axiom, AGENT, IFF, THEN
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
                    # 63:42: -> ^( EXPR AGENT IFF FACT THEN AXIOM axiom )
                    # Deo.g:63:45: ^( EXPR AGENT IFF FACT THEN AXIOM axiom )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_AGENT.nextNode())
                    self._adaptor.addChild(root_1, stream_IFF.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(FACT, "FACT"))
                    self._adaptor.addChild(root_1, stream_THEN.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(AXIOM, "AXIOM"))
                    self._adaptor.addChild(root_1, stream_axiom.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt19 == 3:
                    # Deo.g:64:4: ( LB AGENT )* RB ( LB axiom ( op axiom )* )* RB
                    pass 
                    # Deo.g:64:4: ( LB AGENT )*
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == LB) :
                            alt16 = 1


                        if alt16 == 1:
                            # Deo.g:64:5: LB AGENT
                            pass 
                            LB49=self.match(self.input, LB, self.FOLLOW_LB_in_expr561) 
                            stream_LB.add(LB49)
                            AGENT50=self.match(self.input, AGENT, self.FOLLOW_AGENT_in_expr563) 
                            stream_AGENT.add(AGENT50)


                        else:
                            break #loop16


                    RB51=self.match(self.input, RB, self.FOLLOW_RB_in_expr567) 
                    stream_RB.add(RB51)
                    # Deo.g:64:19: ( LB axiom ( op axiom )* )*
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == LB) :
                            alt18 = 1


                        if alt18 == 1:
                            # Deo.g:64:20: LB axiom ( op axiom )*
                            pass 
                            LB52=self.match(self.input, LB, self.FOLLOW_LB_in_expr570) 
                            stream_LB.add(LB52)
                            self._state.following.append(self.FOLLOW_axiom_in_expr575)
                            axiom53 = self.axiom()

                            self._state.following.pop()
                            stream_axiom.add(axiom53.tree)
                            # Deo.g:65:9: ( op axiom )*
                            while True: #loop17
                                alt17 = 2
                                LA17_0 = self.input.LA(1)

                                if ((IF <= LA17_0 <= THEN) or (AND <= LA17_0 <= NOT)) :
                                    alt17 = 1


                                if alt17 == 1:
                                    # Deo.g:65:10: op axiom
                                    pass 
                                    self._state.following.append(self.FOLLOW_op_in_expr578)
                                    op54 = self.op()

                                    self._state.following.pop()
                                    stream_op.add(op54.tree)
                                    self._state.following.append(self.FOLLOW_axiom_in_expr580)
                                    axiom55 = self.axiom()

                                    self._state.following.pop()
                                    stream_axiom.add(axiom55.tree)


                                else:
                                    break #loop17




                        else:
                            break #loop18


                    RB56=self.match(self.input, RB, self.FOLLOW_RB_in_expr586) 
                    stream_RB.add(RB56)

                    # AST Rewrite
                    # elements: AGENT, axiom
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
                    # 65:30: -> ^( EXPR AGENT AXIOM axiom )
                    # Deo.g:65:33: ^( EXPR AGENT AXIOM axiom )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_AGENT.nextNode())
                    self._adaptor.addChild(root_1, self._adaptor.createFromType(AXIOM, "AXIOM"))
                    self._adaptor.addChild(root_1, stream_axiom.nextTree())

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


    # lookup tables for DFA #19

    DFA19_eot = DFA.unpack(
        u"\10\uffff"
        )

    DFA19_eof = DFA.unpack(
        u"\10\uffff"
        )

    DFA19_min = DFA.unpack(
        u"\1\30\1\24\2\30\1\4\3\uffff"
        )

    DFA19_max = DFA.unpack(
        u"\1\31\1\24\2\31\1\21\3\uffff"
        )

    DFA19_accept = DFA.unpack(
        u"\5\uffff\1\1\1\2\1\3"
        )

    DFA19_special = DFA.unpack(
        u"\10\uffff"
        )

            
    DFA19_transition = [
        DFA.unpack(u"\1\1\1\2"),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\1\5"),
        DFA.unpack(u"\1\1\1\2"),
        DFA.unpack(u"\1\5\1\6\11\uffff\3\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #19

    DFA19 = DFA
 

    FOLLOW_var_decl_in_prog90 = frozenset([13, 24, 25])
    FOLLOW_rule_decl_in_prog93 = frozenset([24, 25])
    FOLLOW_EOF_in_prog96 = frozenset([1])
    FOLLOW_expr_in_rule_decl125 = frozenset([1, 24, 25])
    FOLLOW_ID_in_var_decl152 = frozenset([14])
    FOLLOW_ASSN_in_var_decl154 = frozenset([18, 19, 20])
    FOLLOW_fact_in_var_decl156 = frozenset([1])
    FOLLOW_set_in_norm0 = frozenset([1])
    FOLLOW_set_in_fact0 = frozenset([1])
    FOLLOW_set_in_op0 = frozenset([1])
    FOLLOW_norm_in_axiom365 = frozenset([24])
    FOLLOW_LB_in_axiom367 = frozenset([18])
    FOLLOW_ACTION_in_axiom369 = frozenset([25])
    FOLLOW_RB_in_axiom371 = frozenset([1])
    FOLLOW_LB_in_expr398 = frozenset([20])
    FOLLOW_AGENT_in_expr400 = frozenset([24, 25])
    FOLLOW_RB_in_expr404 = frozenset([24, 25])
    FOLLOW_LB_in_expr407 = frozenset([4])
    FOLLOW_IF_in_expr412 = frozenset([24, 25])
    FOLLOW_LB_in_expr415 = frozenset([18, 19, 20])
    FOLLOW_fact_in_expr417 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_op_in_expr420 = frozenset([18, 19, 20])
    FOLLOW_fact_in_expr422 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_RB_in_expr428 = frozenset([6])
    FOLLOW_THEN_in_expr433 = frozenset([24, 25])
    FOLLOW_LB_in_expr436 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr438 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_op_in_expr441 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr443 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_RB_in_expr449 = frozenset([24, 25])
    FOLLOW_RB_in_expr453 = frozenset([1])
    FOLLOW_LB_in_expr479 = frozenset([20])
    FOLLOW_AGENT_in_expr481 = frozenset([24, 25])
    FOLLOW_RB_in_expr485 = frozenset([24, 25])
    FOLLOW_LB_in_expr488 = frozenset([5])
    FOLLOW_IFF_in_expr493 = frozenset([24, 25])
    FOLLOW_LB_in_expr496 = frozenset([18, 19, 20])
    FOLLOW_fact_in_expr498 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_op_in_expr501 = frozenset([18, 19, 20])
    FOLLOW_fact_in_expr503 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_RB_in_expr509 = frozenset([6])
    FOLLOW_THEN_in_expr514 = frozenset([24, 25])
    FOLLOW_LB_in_expr517 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr519 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_op_in_expr522 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr524 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_RB_in_expr530 = frozenset([24, 25])
    FOLLOW_RB_in_expr534 = frozenset([1])
    FOLLOW_LB_in_expr561 = frozenset([20])
    FOLLOW_AGENT_in_expr563 = frozenset([24, 25])
    FOLLOW_RB_in_expr567 = frozenset([24, 25])
    FOLLOW_LB_in_expr570 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr575 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_op_in_expr578 = frozenset([15, 16, 17])
    FOLLOW_axiom_in_expr580 = frozenset([4, 5, 6, 21, 22, 23, 24, 25])
    FOLLOW_RB_in_expr586 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("DeoLexer", DeoParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
