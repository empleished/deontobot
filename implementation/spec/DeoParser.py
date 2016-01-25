# $ANTLR 3.5.2 Deo.g 2016-01-25 15:39:10

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
COND=8
DIGIT=9
EOL=10
EXPR=11
FACT=12
ID=13
IF=14
LB=15
LETTER=16
NOT=17
OB=18
OR=19
PER=20
PRO=21
PROG=22
RB=23
RULE=24
THEN=25

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "AND", "ASSN", "ATOM", "AXIOM", "COND", "DIGIT", "EOL", "EXPR", "FACT", 
    "ID", "IF", "LB", "LETTER", "NOT", "OB", "OR", "PER", "PRO", "PROG", 
    "RB", "RULE", "THEN"
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
    # Deo.g:26:1: prog : ( fact_decl )+ ( rule_decl )+ -> ^( PROG ( fact_decl )+ ( rule_decl )+ ) ;
    def prog(self, ):
        retval = self.prog_return()
        retval.start = self.input.LT(1)


        root_0 = None

        fact_decl1 = None
        rule_decl2 = None

        stream_fact_decl = RewriteRuleSubtreeStream(self._adaptor, "rule fact_decl")
        stream_rule_decl = RewriteRuleSubtreeStream(self._adaptor, "rule rule_decl")
        try:
            try:
                # Deo.g:26:6: ( ( fact_decl )+ ( rule_decl )+ -> ^( PROG ( fact_decl )+ ( rule_decl )+ ) )
                # Deo.g:26:8: ( fact_decl )+ ( rule_decl )+
                pass 
                # Deo.g:26:8: ( fact_decl )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ID) :
                        alt1 = 1


                    if alt1 == 1:
                        # Deo.g:26:8: fact_decl
                        pass 
                        self._state.following.append(self.FOLLOW_fact_decl_in_prog99)
                        fact_decl1 = self.fact_decl()

                        self._state.following.pop()
                        stream_fact_decl.add(fact_decl1.tree)



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                # Deo.g:26:19: ( rule_decl )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((IF <= LA2_0 <= LB)) :
                        alt2 = 1


                    if alt2 == 1:
                        # Deo.g:26:19: rule_decl
                        pass 
                        self._state.following.append(self.FOLLOW_rule_decl_in_prog102)
                        rule_decl2 = self.rule_decl()

                        self._state.following.pop()
                        stream_rule_decl.add(rule_decl2.tree)



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


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
                # 26:36: -> ^( PROG ( fact_decl )+ ( rule_decl )+ )
                # Deo.g:26:39: ^( PROG ( fact_decl )+ ( rule_decl )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROG, "PROG")
                , root_1)

                # Deo.g:26:46: ( fact_decl )+
                if not (stream_fact_decl.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_fact_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_fact_decl.nextTree())


                stream_fact_decl.reset()

                # Deo.g:26:57: ( rule_decl )+
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
    # Deo.g:29:1: rule_decl : expr -> ^( RULE expr ) ;
    def rule_decl(self, ):
        retval = self.rule_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expr3 = None

        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Deo.g:30:2: ( expr -> ^( RULE expr ) )
                # Deo.g:30:4: expr
                pass 
                self._state.following.append(self.FOLLOW_expr_in_rule_decl133)
                expr3 = self.expr()

                self._state.following.pop()
                stream_expr.add(expr3.tree)


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
                # 30:14: -> ^( RULE expr )
                # Deo.g:30:17: ^( RULE expr )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(RULE, "RULE")
                , root_1)

                self._adaptor.addChild(root_1, stream_expr.nextTree())

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
    # Deo.g:33:1: fact_decl : fact -> ^( FACT fact ) ;
    def fact_decl(self, ):
        retval = self.fact_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        fact4 = None

        stream_fact = RewriteRuleSubtreeStream(self._adaptor, "rule fact")
        try:
            try:
                # Deo.g:34:2: ( fact -> ^( FACT fact ) )
                # Deo.g:34:4: fact
                pass 
                self._state.following.append(self.FOLLOW_fact_in_fact_decl158)
                fact4 = self.fact()

                self._state.following.pop()
                stream_fact.add(fact4.tree)


                # AST Rewrite
                # elements: fact
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
                # 34:14: -> ^( FACT fact )
                # Deo.g:34:17: ^( FACT fact )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(FACT, "FACT")
                , root_1)

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


    class fact_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.fact_return, self).__init__()

            self.tree = None





    # $ANTLR start "fact"
    # Deo.g:37:1: fact : ID ASSN atom ;
    def fact(self, ):
        retval = self.fact_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID5 = None
        ASSN6 = None
        atom7 = None

        ID5_tree = None
        ASSN6_tree = None

        try:
            try:
                # Deo.g:38:2: ( ID ASSN atom )
                # Deo.g:38:4: ID ASSN atom
                pass 
                root_0 = self._adaptor.nil()


                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_fact182)
                ID5_tree = self._adaptor.createWithPayload(ID5)
                self._adaptor.addChild(root_0, ID5_tree)



                ASSN6 = self.match(self.input, ASSN, self.FOLLOW_ASSN_in_fact184)
                ASSN6_tree = self._adaptor.createWithPayload(ASSN6)
                self._adaptor.addChild(root_0, ASSN6_tree)



                self._state.following.append(self.FOLLOW_atom_in_fact186)
                atom7 = self.atom()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atom7.tree)




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


    class norm_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.norm_return, self).__init__()

            self.tree = None





    # $ANTLR start "norm"
    # Deo.g:41:1: norm : ( OB | PRO | PER );
    def norm(self, ):
        retval = self.norm_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set8 = None

        set8_tree = None

        try:
            try:
                # Deo.g:42:2: ( OB | PRO | PER )
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


    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.atom_return, self).__init__()

            self.tree = None





    # $ANTLR start "atom"
    # Deo.g:47:1: atom : ATOM ;
    def atom(self, ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ATOM9 = None

        ATOM9_tree = None

        try:
            try:
                # Deo.g:47:6: ( ATOM )
                # Deo.g:47:8: ATOM
                pass 
                root_0 = self._adaptor.nil()


                ATOM9 = self.match(self.input, ATOM, self.FOLLOW_ATOM_in_atom252)
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

    # $ANTLR end "atom"


    class op_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.op_return, self).__init__()

            self.tree = None





    # $ANTLR start "op"
    # Deo.g:50:1: op : ( AND | OR | NOT | THEN | IF );
    def op(self, ):
        retval = self.op_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set10 = None

        set10_tree = None

        try:
            try:
                # Deo.g:50:4: ( AND | OR | NOT | THEN | IF )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()


                set10 = self.input.LT(1)

                if self.input.LA(1) == AND or self.input.LA(1) == IF or self.input.LA(1) == NOT or self.input.LA(1) == OR or self.input.LA(1) == THEN:
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
    # Deo.g:58:1: axiom : LB ( norm LB atom RB ) RB ;
    def axiom(self, ):
        retval = self.axiom_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LB11 = None
        LB13 = None
        RB15 = None
        RB16 = None
        norm12 = None
        atom14 = None

        LB11_tree = None
        LB13_tree = None
        RB15_tree = None
        RB16_tree = None

        try:
            try:
                # Deo.g:59:2: ( LB ( norm LB atom RB ) RB )
                # Deo.g:59:4: LB ( norm LB atom RB ) RB
                pass 
                root_0 = self._adaptor.nil()


                LB11 = self.match(self.input, LB, self.FOLLOW_LB_in_axiom307)
                LB11_tree = self._adaptor.createWithPayload(LB11)
                self._adaptor.addChild(root_0, LB11_tree)



                # Deo.g:59:7: ( norm LB atom RB )
                # Deo.g:59:8: norm LB atom RB
                pass 
                self._state.following.append(self.FOLLOW_norm_in_axiom310)
                norm12 = self.norm()

                self._state.following.pop()
                self._adaptor.addChild(root_0, norm12.tree)


                LB13 = self.match(self.input, LB, self.FOLLOW_LB_in_axiom312)
                LB13_tree = self._adaptor.createWithPayload(LB13)
                self._adaptor.addChild(root_0, LB13_tree)



                self._state.following.append(self.FOLLOW_atom_in_axiom314)
                atom14 = self.atom()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atom14.tree)


                RB15 = self.match(self.input, RB, self.FOLLOW_RB_in_axiom316)
                RB15_tree = self._adaptor.createWithPayload(RB15)
                self._adaptor.addChild(root_0, RB15_tree)






                RB16 = self.match(self.input, RB, self.FOLLOW_RB_in_axiom319)
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
    # Deo.g:62:1: comp_axiom : ( axiom | axiom ( op axiom )+ );
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
                # Deo.g:63:2: ( axiom | axiom ( op axiom )+ )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == LB) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == OB or (PER <= LA4_1 <= PRO)) :
                        LA4_2 = self.input.LA(3)

                        if (LA4_2 == LB) :
                            LA4_3 = self.input.LA(4)

                            if (LA4_3 == ATOM) :
                                LA4_4 = self.input.LA(5)

                                if (LA4_4 == RB) :
                                    LA4_5 = self.input.LA(6)

                                    if (LA4_5 == RB) :
                                        LA4 = self.input.LA(7)
                                        if LA4 == EOF or LA4 == LB:
                                            alt4 = 1
                                        elif LA4 == IF:
                                            LA4_8 = self.input.LA(8)

                                            if (LA4_8 == LB) :
                                                LA4_10 = self.input.LA(9)

                                                if (LA4_10 == ID) :
                                                    alt4 = 1
                                                elif (LA4_10 == OB or (PER <= LA4_10 <= PRO)) :
                                                    alt4 = 2
                                                else:
                                                    nvae = NoViableAltException("", 4, 10, self.input)

                                                    raise nvae


                                            else:
                                                nvae = NoViableAltException("", 4, 8, self.input)

                                                raise nvae


                                        elif LA4 == AND or LA4 == NOT or LA4 == OR or LA4 == THEN:
                                            alt4 = 2
                                        else:
                                            nvae = NoViableAltException("", 4, 6, self.input)

                                            raise nvae


                                    else:
                                        nvae = NoViableAltException("", 4, 5, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 4, 4, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 4, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 4, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # Deo.g:63:4: axiom
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_axiom_in_comp_axiom331)
                    axiom17 = self.axiom()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, axiom17.tree)



                elif alt4 == 2:
                    # Deo.g:64:4: axiom ( op axiom )+
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_axiom_in_comp_axiom336)
                    axiom18 = self.axiom()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, axiom18.tree)


                    # Deo.g:64:10: ( op axiom )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == IF) :
                            LA3_2 = self.input.LA(2)

                            if (LA3_2 == LB) :
                                LA3_4 = self.input.LA(3)

                                if (LA3_4 == OB or (PER <= LA3_4 <= PRO)) :
                                    alt3 = 1




                        elif (LA3_0 == AND or LA3_0 == NOT or LA3_0 == OR or LA3_0 == THEN) :
                            alt3 = 1


                        if alt3 == 1:
                            # Deo.g:64:11: op axiom
                            pass 
                            self._state.following.append(self.FOLLOW_op_in_comp_axiom339)
                            op19 = self.op()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, op19.tree)


                            self._state.following.append(self.FOLLOW_axiom_in_comp_axiom341)
                            axiom20 = self.axiom()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, axiom20.tree)



                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1



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
    # Deo.g:67:1: cond : LB fact RB ;
    def cond(self, ):
        retval = self.cond_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LB21 = None
        RB23 = None
        fact22 = None

        LB21_tree = None
        RB23_tree = None

        try:
            try:
                # Deo.g:67:6: ( LB fact RB )
                # Deo.g:67:8: LB fact RB
                pass 
                root_0 = self._adaptor.nil()


                LB21 = self.match(self.input, LB, self.FOLLOW_LB_in_cond354)
                LB21_tree = self._adaptor.createWithPayload(LB21)
                self._adaptor.addChild(root_0, LB21_tree)



                self._state.following.append(self.FOLLOW_fact_in_cond356)
                fact22 = self.fact()

                self._state.following.pop()
                self._adaptor.addChild(root_0, fact22.tree)


                RB23 = self.match(self.input, RB, self.FOLLOW_RB_in_cond358)
                RB23_tree = self._adaptor.createWithPayload(RB23)
                self._adaptor.addChild(root_0, RB23_tree)





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


    class comp_cond_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.comp_cond_return, self).__init__()

            self.tree = None





    # $ANTLR start "comp_cond"
    # Deo.g:70:1: comp_cond : ( cond | cond ( op cond )+ );
    def comp_cond(self, ):
        retval = self.comp_cond_return()
        retval.start = self.input.LT(1)


        root_0 = None

        cond24 = None
        cond25 = None
        op26 = None
        cond27 = None


        try:
            try:
                # Deo.g:71:2: ( cond | cond ( op cond )+ )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == LB) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == ID) :
                        LA6_2 = self.input.LA(3)

                        if (LA6_2 == ASSN) :
                            LA6_3 = self.input.LA(4)

                            if (LA6_3 == ATOM) :
                                LA6_4 = self.input.LA(5)

                                if (LA6_4 == RB) :
                                    LA6_5 = self.input.LA(6)

                                    if (LA6_5 == THEN) :
                                        LA6_6 = self.input.LA(7)

                                        if (LA6_6 == LB) :
                                            LA6_8 = self.input.LA(8)

                                            if (LA6_8 == OB or (PER <= LA6_8 <= PRO)) :
                                                alt6 = 1
                                            elif (LA6_8 == ID) :
                                                alt6 = 2
                                            else:
                                                nvae = NoViableAltException("", 6, 8, self.input)

                                                raise nvae


                                        else:
                                            nvae = NoViableAltException("", 6, 6, self.input)

                                            raise nvae


                                    elif (LA6_5 == AND or LA6_5 == IF or LA6_5 == NOT or LA6_5 == OR) :
                                        alt6 = 2
                                    else:
                                        nvae = NoViableAltException("", 6, 5, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 6, 4, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 6, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 6, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 6, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # Deo.g:71:4: cond
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_cond_in_comp_cond370)
                    cond24 = self.cond()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, cond24.tree)



                elif alt6 == 2:
                    # Deo.g:72:4: cond ( op cond )+
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_cond_in_comp_cond375)
                    cond25 = self.cond()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, cond25.tree)


                    # Deo.g:72:9: ( op cond )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == THEN) :
                            LA5_1 = self.input.LA(2)

                            if (LA5_1 == LB) :
                                LA5_3 = self.input.LA(3)

                                if (LA5_3 == ID) :
                                    alt5 = 1




                        elif (LA5_0 == AND or LA5_0 == IF or LA5_0 == NOT or LA5_0 == OR) :
                            alt5 = 1


                        if alt5 == 1:
                            # Deo.g:72:10: op cond
                            pass 
                            self._state.following.append(self.FOLLOW_op_in_comp_cond378)
                            op26 = self.op()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, op26.tree)


                            self._state.following.append(self.FOLLOW_cond_in_comp_cond380)
                            cond27 = self.cond()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, cond27.tree)



                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1



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

    # $ANTLR end "comp_cond"


    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr"
    # Deo.g:75:1: expr : ( IF comp_cond THEN comp_axiom -> ^( EXPR IF COND comp_cond THEN AXIOM comp_axiom ) | comp_axiom -> ^( EXPR AXIOM comp_axiom ) );
    def expr(self, ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF28 = None
        THEN30 = None
        comp_cond29 = None
        comp_axiom31 = None
        comp_axiom32 = None

        IF28_tree = None
        THEN30_tree = None
        stream_THEN = RewriteRuleTokenStream(self._adaptor, "token THEN")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_comp_axiom = RewriteRuleSubtreeStream(self._adaptor, "rule comp_axiom")
        stream_comp_cond = RewriteRuleSubtreeStream(self._adaptor, "rule comp_cond")
        try:
            try:
                # Deo.g:75:6: ( IF comp_cond THEN comp_axiom -> ^( EXPR IF COND comp_cond THEN AXIOM comp_axiom ) | comp_axiom -> ^( EXPR AXIOM comp_axiom ) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == IF) :
                    alt7 = 1
                elif (LA7_0 == LB) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # Deo.g:75:8: IF comp_cond THEN comp_axiom
                    pass 
                    IF28 = self.match(self.input, IF, self.FOLLOW_IF_in_expr393) 
                    stream_IF.add(IF28)


                    self._state.following.append(self.FOLLOW_comp_cond_in_expr395)
                    comp_cond29 = self.comp_cond()

                    self._state.following.pop()
                    stream_comp_cond.add(comp_cond29.tree)


                    THEN30 = self.match(self.input, THEN, self.FOLLOW_THEN_in_expr397) 
                    stream_THEN.add(THEN30)


                    self._state.following.append(self.FOLLOW_comp_axiom_in_expr399)
                    comp_axiom31 = self.comp_axiom()

                    self._state.following.pop()
                    stream_comp_axiom.add(comp_axiom31.tree)


                    # AST Rewrite
                    # elements: comp_cond, comp_axiom, THEN, IF
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
                    # 75:40: -> ^( EXPR IF COND comp_cond THEN AXIOM comp_axiom )
                    # Deo.g:75:43: ^( EXPR IF COND comp_cond THEN AXIOM comp_axiom )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(EXPR, "EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_IF.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(COND, "COND")
                    )

                    self._adaptor.addChild(root_1, stream_comp_cond.nextTree())

                    self._adaptor.addChild(root_1, 
                    stream_THEN.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(AXIOM, "AXIOM")
                    )

                    self._adaptor.addChild(root_1, stream_comp_axiom.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt7 == 2:
                    # Deo.g:77:4: comp_axiom
                    pass 
                    self._state.following.append(self.FOLLOW_comp_axiom_in_expr426)
                    comp_axiom32 = self.comp_axiom()

                    self._state.following.pop()
                    stream_comp_axiom.add(comp_axiom32.tree)


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
                    # 77:19: -> ^( EXPR AXIOM comp_axiom )
                    # Deo.g:77:22: ^( EXPR AXIOM comp_axiom )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(EXPR, "EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(AXIOM, "AXIOM")
                    )

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



 

    FOLLOW_fact_decl_in_prog99 = frozenset([13, 14, 15])
    FOLLOW_rule_decl_in_prog102 = frozenset([1, 14, 15])
    FOLLOW_expr_in_rule_decl133 = frozenset([1])
    FOLLOW_fact_in_fact_decl158 = frozenset([1])
    FOLLOW_ID_in_fact182 = frozenset([5])
    FOLLOW_ASSN_in_fact184 = frozenset([6])
    FOLLOW_atom_in_fact186 = frozenset([1])
    FOLLOW_ATOM_in_atom252 = frozenset([1])
    FOLLOW_LB_in_axiom307 = frozenset([18, 20, 21])
    FOLLOW_norm_in_axiom310 = frozenset([15])
    FOLLOW_LB_in_axiom312 = frozenset([6])
    FOLLOW_atom_in_axiom314 = frozenset([23])
    FOLLOW_RB_in_axiom316 = frozenset([23])
    FOLLOW_RB_in_axiom319 = frozenset([1])
    FOLLOW_axiom_in_comp_axiom331 = frozenset([1])
    FOLLOW_axiom_in_comp_axiom336 = frozenset([4, 14, 17, 19, 25])
    FOLLOW_op_in_comp_axiom339 = frozenset([15])
    FOLLOW_axiom_in_comp_axiom341 = frozenset([1, 4, 14, 17, 19, 25])
    FOLLOW_LB_in_cond354 = frozenset([13])
    FOLLOW_fact_in_cond356 = frozenset([23])
    FOLLOW_RB_in_cond358 = frozenset([1])
    FOLLOW_cond_in_comp_cond370 = frozenset([1])
    FOLLOW_cond_in_comp_cond375 = frozenset([4, 14, 17, 19, 25])
    FOLLOW_op_in_comp_cond378 = frozenset([15])
    FOLLOW_cond_in_comp_cond380 = frozenset([1, 4, 14, 17, 19, 25])
    FOLLOW_IF_in_expr393 = frozenset([15])
    FOLLOW_comp_cond_in_expr395 = frozenset([25])
    FOLLOW_THEN_in_expr397 = frozenset([15])
    FOLLOW_comp_axiom_in_expr399 = frozenset([1])
    FOLLOW_comp_axiom_in_expr426 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("DeoLexer", DeoParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
