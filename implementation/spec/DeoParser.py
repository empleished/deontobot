# $ANTLR 3.5.2 Deo.g 2015-12-02 15:25:37

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
AND=4
ASSN=5
ATOM=6
AXIOM=7
COMMENT=8
COND=9
DIGIT=10
EXPR=11
FACT=12
ID=13
IF=14
IFF=15
LB=16
LETTER=17
NOT=18
OB=19
OR=20
PER=21
PRO=22
PROG=23
RB=24
RULE=25
SPACE=26
THEN=27

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "AND", "ASSN", "ATOM", "AXIOM", "COMMENT", "COND", "DIGIT", "EXPR", 
    "FACT", "ID", "IF", "IFF", "LB", "LETTER", "NOT", "OB", "OR", "PER", 
    "PRO", "PROG", "RB", "RULE", "SPACE", "THEN"
]




class DeoParser(Parser):
    grammarFileName = "Deo.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(DeoParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.prog_return, self).__init__()

            self.tree = None





    # $ANTLR start "prog"
    # Deo.g:24:1: prog : ( fact_decl )+ ( rule_decl )+ EOF -> ^( PROG ( fact_decl )* ( rule_decl )+ ) ;
    def prog(self, ):
        retval = self.prog_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EOF3 = None
        fact_decl1 = None
        rule_decl2 = None

        EOF3_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_fact_decl = RewriteRuleSubtreeStream(self._adaptor, "rule fact_decl")
        stream_rule_decl = RewriteRuleSubtreeStream(self._adaptor, "rule rule_decl")
        try:
            try:
                # Deo.g:24:6: ( ( fact_decl )+ ( rule_decl )+ EOF -> ^( PROG ( fact_decl )* ( rule_decl )+ ) )
                # Deo.g:24:8: ( fact_decl )+ ( rule_decl )+ EOF
                pass 
                # Deo.g:24:8: ( fact_decl )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        alt1 = 1


                    if alt1 == 1:
                        # Deo.g:24:9: fact_decl
                        pass 
                        self._state.following.append(self.FOLLOW_fact_decl_in_prog95)
                        fact_decl1 = self.fact_decl()

                        self._state.following.pop()
                        stream_fact_decl.add(fact_decl1.tree)



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                # Deo.g:24:21: ( rule_decl )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LB) :
                        alt2 = 1


                    if alt2 == 1:
                        # Deo.g:24:22: rule_decl
                        pass 
                        self._state.following.append(self.FOLLOW_rule_decl_in_prog100)
                        rule_decl2 = self.rule_decl()

                        self._state.following.pop()
                        stream_rule_decl.add(rule_decl2.tree)



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                EOF3 = self.match(self.input, EOF, self.FOLLOW_EOF_in_prog104) 
                stream_EOF.add(EOF3)


                # AST Rewrite
                # elements: fact_decl, rule_decl
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
                # 24:43: -> ^( PROG ( fact_decl )* ( rule_decl )+ )
                # Deo.g:24:46: ^( PROG ( fact_decl )* ( rule_decl )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROG, "PROG")
                , root_1)

                # Deo.g:24:53: ( fact_decl )*
                while stream_fact_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_fact_decl.nextTree())


                stream_fact_decl.reset();

                # Deo.g:24:64: ( rule_decl )+
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
            super(DeoParser.rule_decl_return, self).__init__()

            self.tree = None





    # $ANTLR start "rule_decl"
    # Deo.g:27:1: rule_decl : ( expr )+ -> ^( RULE ( expr )+ ) ;
    def rule_decl(self, ):
        retval = self.rule_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expr4 = None

        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Deo.g:28:2: ( ( expr )+ -> ^( RULE ( expr )+ ) )
                # Deo.g:28:4: ( expr )+
                pass 
                # Deo.g:28:4: ( expr )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == LB) :
                        alt3 = 1


                    if alt3 == 1:
                        # Deo.g:28:5: expr
                        pass 
                        self._state.following.append(self.FOLLOW_expr_in_rule_decl134)
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
                # 28:17: -> ^( RULE ( expr )+ )
                # Deo.g:28:20: ^( RULE ( expr )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(RULE, "RULE")
                , root_1)

                # Deo.g:28:27: ( expr )+
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


    class fact_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.fact_decl_return, self).__init__()

            self.tree = None





    # $ANTLR start "fact_decl"
    # Deo.g:31:1: fact_decl : ID ASSN fact -> ^( FACT ID fact ) ;
    def fact_decl(self, ):
        retval = self.fact_decl_return()
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
                # Deo.g:32:2: ( ID ASSN fact -> ^( FACT ID fact ) )
                # Deo.g:32:4: ID ASSN fact
                pass 
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_fact_decl162) 
                stream_ID.add(ID5)


                ASSN6 = self.match(self.input, ASSN, self.FOLLOW_ASSN_in_fact_decl164) 
                stream_ASSN.add(ASSN6)


                self._state.following.append(self.FOLLOW_fact_in_fact_decl166)
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
                # 32:21: -> ^( FACT ID fact )
                # Deo.g:32:24: ^( FACT ID fact )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(FACT, "FACT")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

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

    # $ANTLR end "fact_decl"


    class norm_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.norm_return, self).__init__()

            self.tree = None





    # $ANTLR start "norm"
    # Deo.g:35:1: norm : ( OB | PRO | PER );
    def norm(self, ):
        retval = self.norm_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set8 = None

        set8_tree = None

        try:
            try:
                # Deo.g:36:2: ( OB | PRO | PER )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()


                set8 = self.input.LT(1)

                if self.input.LA(1) == OB or (PER <= self.input.LA(1) <= PRO):
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
            super(DeoParser.fact_return, self).__init__()

            self.tree = None





    # $ANTLR start "fact"
    # Deo.g:41:1: fact : ATOM ;
    def fact(self, ):
        retval = self.fact_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ATOM9 = None

        ATOM9_tree = None

        try:
            try:
                # Deo.g:41:6: ( ATOM )
                # Deo.g:41:8: ATOM
                pass 
                root_0 = self._adaptor.nil()


                ATOM9 = self.match(self.input, ATOM, self.FOLLOW_ATOM_in_fact240)
                ATOM9_tree = self._adaptor.createWithPayload(ATOM9)
                self._adaptor.addChild(root_0, ATOM9_tree)





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
            super(DeoParser.op_return, self).__init__()

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

                if self.input.LA(1) == AND or (IF <= self.input.LA(1) <= IFF) or self.input.LA(1) == NOT or self.input.LA(1) == OR or self.input.LA(1) == THEN:
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
            super(DeoParser.axiom_return, self).__init__()

            self.tree = None





    # $ANTLR start "axiom"
    # Deo.g:52:1: axiom : LB ( norm LB fact RB ) RB ;
    def axiom(self, ):
        retval = self.axiom_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LB11 = None
        LB13 = None
        RB15 = None
        RB16 = None
        norm12 = None
        fact14 = None

        LB11_tree = None
        LB13_tree = None
        RB15_tree = None
        RB16_tree = None

        try:
            try:
                # Deo.g:53:2: ( LB ( norm LB fact RB ) RB )
                # Deo.g:53:4: LB ( norm LB fact RB ) RB
                pass 
                root_0 = self._adaptor.nil()


                LB11 = self.match(self.input, LB, self.FOLLOW_LB_in_axiom355)
                LB11_tree = self._adaptor.createWithPayload(LB11)
                self._adaptor.addChild(root_0, LB11_tree)



                # Deo.g:53:7: ( norm LB fact RB )
                # Deo.g:53:8: norm LB fact RB
                pass 
                self._state.following.append(self.FOLLOW_norm_in_axiom358)
                norm12 = self.norm()

                self._state.following.pop()
                self._adaptor.addChild(root_0, norm12.tree)


                LB13 = self.match(self.input, LB, self.FOLLOW_LB_in_axiom360)
                LB13_tree = self._adaptor.createWithPayload(LB13)
                self._adaptor.addChild(root_0, LB13_tree)



                self._state.following.append(self.FOLLOW_fact_in_axiom362)
                fact14 = self.fact()

                self._state.following.pop()
                self._adaptor.addChild(root_0, fact14.tree)


                RB15 = self.match(self.input, RB, self.FOLLOW_RB_in_axiom364)
                RB15_tree = self._adaptor.createWithPayload(RB15)
                self._adaptor.addChild(root_0, RB15_tree)






                RB16 = self.match(self.input, RB, self.FOLLOW_RB_in_axiom367)
                RB16_tree = self._adaptor.createWithPayload(RB16)
                self._adaptor.addChild(root_0, RB16_tree)





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


    class comp_axiom_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.comp_axiom_return, self).__init__()

            self.tree = None





    # $ANTLR start "comp_axiom"
    # Deo.g:56:1: comp_axiom : ( axiom | axiom ( op axiom )+ );
    def comp_axiom(self, ):
        retval = self.comp_axiom_return()
        retval.start = self.input.LT(1)


        root_0 = None

        axiom17 = None
        axiom18 = None
        op19 = None
        axiom20 = None


        try:
            try:
                # Deo.g:57:2: ( axiom | axiom ( op axiom )+ )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == LB) :
                    LA5_1 = self.input.LA(2)

                    if (LA5_1 == OB or (PER <= LA5_1 <= PRO)) :
                        LA5_2 = self.input.LA(3)

                        if (LA5_2 == LB) :
                            LA5_3 = self.input.LA(4)

                            if (LA5_3 == ATOM) :
                                LA5_4 = self.input.LA(5)

                                if (LA5_4 == RB) :
                                    LA5_5 = self.input.LA(6)

                                    if (LA5_5 == RB) :
                                        LA5_6 = self.input.LA(7)

                                        if (LA5_6 == EOF or LA5_6 == LB) :
                                            alt5 = 1
                                        elif (LA5_6 == AND or (IF <= LA5_6 <= IFF) or LA5_6 == NOT or LA5_6 == OR or LA5_6 == THEN) :
                                            alt5 = 2
                                        else:
                                            nvae = NoViableAltException("", 5, 6, self.input)

                                            raise nvae


                                    else:
                                        nvae = NoViableAltException("", 5, 5, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 5, 4, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 5, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 5, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 5, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # Deo.g:57:4: axiom
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_axiom_in_comp_axiom380)
                    axiom17 = self.axiom()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, axiom17.tree)



                elif alt5 == 2:
                    # Deo.g:58:4: axiom ( op axiom )+
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_axiom_in_comp_axiom386)
                    axiom18 = self.axiom()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, axiom18.tree)


                    # Deo.g:58:10: ( op axiom )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == AND or (IF <= LA4_0 <= IFF) or LA4_0 == NOT or LA4_0 == OR or LA4_0 == THEN) :
                            alt4 = 1


                        if alt4 == 1:
                            # Deo.g:58:11: op axiom
                            pass 
                            self._state.following.append(self.FOLLOW_op_in_comp_axiom389)
                            op19 = self.op()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, op19.tree)


                            self._state.following.append(self.FOLLOW_axiom_in_comp_axiom391)
                            axiom20 = self.axiom()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, axiom20.tree)



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1



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

    # $ANTLR end "comp_axiom"


    class cond_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.cond_return, self).__init__()

            self.tree = None





    # $ANTLR start "cond"
    # Deo.g:61:1: cond : ( LB fact RB | LB fact ( op fact )+ RB );
    def cond(self, ):
        retval = self.cond_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LB21 = None
        RB23 = None
        LB24 = None
        RB28 = None
        fact22 = None
        fact25 = None
        op26 = None
        fact27 = None

        LB21_tree = None
        RB23_tree = None
        LB24_tree = None
        RB28_tree = None

        try:
            try:
                # Deo.g:61:6: ( LB fact RB | LB fact ( op fact )+ RB )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == LB) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == ATOM) :
                        LA7_2 = self.input.LA(3)

                        if (LA7_2 == RB) :
                            alt7 = 1
                        elif (LA7_2 == AND or (IF <= LA7_2 <= IFF) or LA7_2 == NOT or LA7_2 == OR or LA7_2 == THEN) :
                            alt7 = 2
                        else:
                            nvae = NoViableAltException("", 7, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # Deo.g:61:8: LB fact RB
                    pass 
                    root_0 = self._adaptor.nil()


                    LB21 = self.match(self.input, LB, self.FOLLOW_LB_in_cond404)
                    LB21_tree = self._adaptor.createWithPayload(LB21)
                    self._adaptor.addChild(root_0, LB21_tree)



                    self._state.following.append(self.FOLLOW_fact_in_cond406)
                    fact22 = self.fact()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, fact22.tree)


                    RB23 = self.match(self.input, RB, self.FOLLOW_RB_in_cond408)
                    RB23_tree = self._adaptor.createWithPayload(RB23)
                    self._adaptor.addChild(root_0, RB23_tree)




                elif alt7 == 2:
                    # Deo.g:62:4: LB fact ( op fact )+ RB
                    pass 
                    root_0 = self._adaptor.nil()


                    LB24 = self.match(self.input, LB, self.FOLLOW_LB_in_cond413)
                    LB24_tree = self._adaptor.createWithPayload(LB24)
                    self._adaptor.addChild(root_0, LB24_tree)



                    self._state.following.append(self.FOLLOW_fact_in_cond415)
                    fact25 = self.fact()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, fact25.tree)


                    # Deo.g:62:12: ( op fact )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == AND or (IF <= LA6_0 <= IFF) or LA6_0 == NOT or LA6_0 == OR or LA6_0 == THEN) :
                            alt6 = 1


                        if alt6 == 1:
                            # Deo.g:62:13: op fact
                            pass 
                            self._state.following.append(self.FOLLOW_op_in_cond418)
                            op26 = self.op()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, op26.tree)


                            self._state.following.append(self.FOLLOW_fact_in_cond420)
                            fact27 = self.fact()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, fact27.tree)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    RB28 = self.match(self.input, RB, self.FOLLOW_RB_in_cond424)
                    RB28_tree = self._adaptor.createWithPayload(RB28)
                    self._adaptor.addChild(root_0, RB28_tree)




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

    # $ANTLR end "cond"


    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr"
    # Deo.g:65:1: expr : comp_axiom -> ^( EXPR comp_axiom ) ;
    def expr(self, ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        comp_axiom29 = None

        stream_comp_axiom = RewriteRuleSubtreeStream(self._adaptor, "rule comp_axiom")
        try:
            try:
                # Deo.g:65:6: ( comp_axiom -> ^( EXPR comp_axiom ) )
                # Deo.g:68:3: comp_axiom
                pass 
                self._state.following.append(self.FOLLOW_comp_axiom_in_expr438)
                comp_axiom29 = self.comp_axiom()

                self._state.following.pop()
                stream_comp_axiom.add(comp_axiom29.tree)


                # AST Rewrite
                # elements: comp_axiom
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
                # 68:18: -> ^( EXPR comp_axiom )
                # Deo.g:68:21: ^( EXPR comp_axiom )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(EXPR, "EXPR")
                , root_1)

                self._adaptor.addChild(root_1, stream_comp_axiom.nextTree())

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



 

    FOLLOW_fact_decl_in_prog95 = frozenset([13, 16])
    FOLLOW_rule_decl_in_prog100 = frozenset([16])
    FOLLOW_EOF_in_prog104 = frozenset([1])
    FOLLOW_expr_in_rule_decl134 = frozenset([1, 16])
    FOLLOW_ID_in_fact_decl162 = frozenset([5])
    FOLLOW_ASSN_in_fact_decl164 = frozenset([6])
    FOLLOW_fact_in_fact_decl166 = frozenset([1])
    FOLLOW_ATOM_in_fact240 = frozenset([1])
    FOLLOW_LB_in_axiom355 = frozenset([19, 21, 22])
    FOLLOW_norm_in_axiom358 = frozenset([16])
    FOLLOW_LB_in_axiom360 = frozenset([6])
    FOLLOW_fact_in_axiom362 = frozenset([24])
    FOLLOW_RB_in_axiom364 = frozenset([24])
    FOLLOW_RB_in_axiom367 = frozenset([1])
    FOLLOW_axiom_in_comp_axiom380 = frozenset([1])
    FOLLOW_axiom_in_comp_axiom386 = frozenset([4, 14, 15, 18, 20, 27])
    FOLLOW_op_in_comp_axiom389 = frozenset([16])
    FOLLOW_axiom_in_comp_axiom391 = frozenset([1, 4, 14, 15, 18, 20, 27])
    FOLLOW_LB_in_cond404 = frozenset([6])
    FOLLOW_fact_in_cond406 = frozenset([24])
    FOLLOW_RB_in_cond408 = frozenset([1])
    FOLLOW_LB_in_cond413 = frozenset([6])
    FOLLOW_fact_in_cond415 = frozenset([4, 14, 15, 18, 20, 27])
    FOLLOW_op_in_cond418 = frozenset([6])
    FOLLOW_fact_in_cond420 = frozenset([4, 14, 15, 18, 20, 24, 27])
    FOLLOW_RB_in_cond424 = frozenset([1])
    FOLLOW_comp_axiom_in_expr438 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("DeoLexer", DeoParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
