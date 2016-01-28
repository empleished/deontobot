# $ANTLR 3.5.2 Deo.g 2016-01-28 17:17:12

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
DECL=9
DIGIT=10
EOL=11
EXPR=12
FACT=13
GOAL=14
ID=15
IF=16
IFF=17
IFTHEN=18
INF=19
LB=20
LETTER=21
NOT=22
OB=23
OR=24
PER=25
PREF=26
PRO=27
PROG=28
RB=29
RULE=30
THEN=31

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "AND", "ASSN", "ATOM", "AXIOM", "COND", "DECL", "DIGIT", "EOL", "EXPR", 
    "FACT", "GOAL", "ID", "IF", "IFF", "IFTHEN", "INF", "LB", "LETTER", 
    "NOT", "OB", "OR", "PER", "PREF", "PRO", "PROG", "RB", "RULE", "THEN"
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
    # Deo.g:31:1: prog : ( decl )+ -> ^( PROG ( decl )+ ) ;
    def prog(self, ):
        retval = self.prog_return()
        retval.start = self.input.LT(1)


        root_0 = None

        decl1 = None

        stream_decl = RewriteRuleSubtreeStream(self._adaptor, "rule decl")
        try:
            try:
                # Deo.g:31:6: ( ( decl )+ -> ^( PROG ( decl )+ ) )
                # Deo.g:31:8: ( decl )+
                pass 
                # Deo.g:31:8: ( decl )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ATOM or LA1_0 == ID or LA1_0 == LB) :
                        alt1 = 1


                    if alt1 == 1:
                        # Deo.g:31:8: decl
                        pass 
                        self._state.following.append(self.FOLLOW_decl_in_prog122)
                        decl1 = self.decl()

                        self._state.following.pop()
                        stream_decl.add(decl1.tree)



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                # AST Rewrite
                # elements: decl
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
                # 31:21: -> ^( PROG ( decl )+ )
                # Deo.g:31:24: ^( PROG ( decl )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PROG, "PROG")
                , root_1)

                # Deo.g:31:31: ( decl )+
                if not (stream_decl.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_decl.hasNext():
                    self._adaptor.addChild(root_1, stream_decl.nextTree())


                stream_decl.reset()

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


    class decl_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.decl_return, self).__init__()

            self.tree = None





    # $ANTLR start "decl"
    # Deo.g:34:1: decl : ( fact_decl -> ^( DECL fact_decl ) | rule_decl -> ^( DECL rule_decl ) );
    def decl(self, ):
        retval = self.decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        fact_decl2 = None
        rule_decl3 = None

        stream_fact_decl = RewriteRuleSubtreeStream(self._adaptor, "rule fact_decl")
        stream_rule_decl = RewriteRuleSubtreeStream(self._adaptor, "rule rule_decl")
        try:
            try:
                # Deo.g:34:6: ( fact_decl -> ^( DECL fact_decl ) | rule_decl -> ^( DECL rule_decl ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == ID) :
                    alt2 = 1
                elif (LA2_0 == ATOM or LA2_0 == LB) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # Deo.g:34:8: fact_decl
                    pass 
                    self._state.following.append(self.FOLLOW_fact_decl_in_decl149)
                    fact_decl2 = self.fact_decl()

                    self._state.following.pop()
                    stream_fact_decl.add(fact_decl2.tree)


                    # AST Rewrite
                    # elements: fact_decl
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
                    # 34:22: -> ^( DECL fact_decl )
                    # Deo.g:34:25: ^( DECL fact_decl )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DECL, "DECL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_fact_decl.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt2 == 2:
                    # Deo.g:35:4: rule_decl
                    pass 
                    self._state.following.append(self.FOLLOW_rule_decl_in_decl166)
                    rule_decl3 = self.rule_decl()

                    self._state.following.pop()
                    stream_rule_decl.add(rule_decl3.tree)


                    # AST Rewrite
                    # elements: rule_decl
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
                    # 35:19: -> ^( DECL rule_decl )
                    # Deo.g:35:22: ^( DECL rule_decl )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(DECL, "DECL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_rule_decl.nextTree())

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

    # $ANTLR end "decl"


    class rule_decl_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.rule_decl_return, self).__init__()

            self.tree = None





    # $ANTLR start "rule_decl"
    # Deo.g:38:1: rule_decl : expr ;
    def rule_decl(self, ):
        retval = self.rule_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        expr4 = None


        try:
            try:
                # Deo.g:39:2: ( expr )
                # Deo.g:39:4: expr
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr_in_rule_decl191)
                expr4 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr4.tree)




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
    # Deo.g:42:1: fact_decl : fact ;
    def fact_decl(self, ):
        retval = self.fact_decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        fact5 = None


        try:
            try:
                # Deo.g:43:2: ( fact )
                # Deo.g:43:4: fact
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_fact_in_fact_decl208)
                fact5 = self.fact()

                self._state.following.pop()
                self._adaptor.addChild(root_0, fact5.tree)




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
    # Deo.g:50:1: fact : ID ASSN atom ;
    def fact(self, ):
        retval = self.fact_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID6 = None
        ASSN7 = None
        atom8 = None

        ID6_tree = None
        ASSN7_tree = None

        try:
            try:
                # Deo.g:51:2: ( ID ASSN atom )
                # Deo.g:51:4: ID ASSN atom
                pass 
                root_0 = self._adaptor.nil()


                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_fact229)
                ID6_tree = self._adaptor.createWithPayload(ID6)
                self._adaptor.addChild(root_0, ID6_tree)



                ASSN7 = self.match(self.input, ASSN, self.FOLLOW_ASSN_in_fact231)
                ASSN7_tree = self._adaptor.createWithPayload(ASSN7)
                self._adaptor.addChild(root_0, ASSN7_tree)



                self._state.following.append(self.FOLLOW_atom_in_fact233)
                atom8 = self.atom()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atom8.tree)




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


    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.atom_return, self).__init__()

            self.tree = None





    # $ANTLR start "atom"
    # Deo.g:54:1: atom : ATOM ;
    def atom(self, ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ATOM9 = None

        ATOM9_tree = None

        try:
            try:
                # Deo.g:54:6: ( ATOM )
                # Deo.g:54:8: ATOM
                pass 
                root_0 = self._adaptor.nil()


                ATOM9 = self.match(self.input, ATOM, self.FOLLOW_ATOM_in_atom251)
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


    class pop_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.pop_return, self).__init__()

            self.tree = None





    # $ANTLR start "pop"
    # Deo.g:57:1: pop : ( OB | PRO | PER | NOT );
    def pop(self, ):
        retval = self.pop_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set10 = None

        set10_tree = None

        try:
            try:
                # Deo.g:58:2: ( OB | PRO | PER | NOT )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()


                set10 = self.input.LT(1)

                if (NOT <= self.input.LA(1) <= OB) or self.input.LA(1) == PER or self.input.LA(1) == PRO:
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

    # $ANTLR end "pop"


    class iop_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.iop_return, self).__init__()

            self.tree = None





    # $ANTLR start "iop"
    # Deo.g:64:1: iop : ( AND | OR | IFF );
    def iop(self, ):
        retval = self.iop_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set11 = None

        set11_tree = None

        try:
            try:
                # Deo.g:64:5: ( AND | OR | IFF )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()


                set11 = self.input.LT(1)

                if self.input.LA(1) == AND or self.input.LA(1) == IFF or self.input.LA(1) == OR:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set11))

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

    # $ANTLR end "iop"


    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr"
    # Deo.g:86:1: expr : ( atom -> ^( EXPR atom ) | prefix_expr -> ^( EXPR prefix_expr ) | infix_expr -> ^( EXPR infix_expr ) | ifthen_expr -> ^( EXPR ifthen_expr ) );
    def expr(self, ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        atom12 = None
        prefix_expr13 = None
        infix_expr14 = None
        ifthen_expr15 = None

        stream_infix_expr = RewriteRuleSubtreeStream(self._adaptor, "rule infix_expr")
        stream_prefix_expr = RewriteRuleSubtreeStream(self._adaptor, "rule prefix_expr")
        stream_ifthen_expr = RewriteRuleSubtreeStream(self._adaptor, "rule ifthen_expr")
        stream_atom = RewriteRuleSubtreeStream(self._adaptor, "rule atom")
        try:
            try:
                # Deo.g:86:6: ( atom -> ^( EXPR atom ) | prefix_expr -> ^( EXPR prefix_expr ) | infix_expr -> ^( EXPR infix_expr ) | ifthen_expr -> ^( EXPR ifthen_expr ) )
                alt3 = 4
                LA3_0 = self.input.LA(1)

                if (LA3_0 == ATOM) :
                    alt3 = 1
                elif (LA3_0 == LB) :
                    LA3 = self.input.LA(2)
                    if LA3 == IF:
                        alt3 = 4
                    elif LA3 == NOT or LA3 == OB or LA3 == PER or LA3 == PRO:
                        alt3 = 2
                    elif LA3 == ATOM or LA3 == LB:
                        alt3 = 3
                    else:
                        nvae = NoViableAltException("", 3, 2, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # Deo.g:90:3: atom
                    pass 
                    self._state.following.append(self.FOLLOW_atom_in_expr366)
                    atom12 = self.atom()

                    self._state.following.pop()
                    stream_atom.add(atom12.tree)


                    # AST Rewrite
                    # elements: atom
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
                    # 90:13: -> ^( EXPR atom )
                    # Deo.g:90:16: ^( EXPR atom )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(EXPR, "EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_atom.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 2:
                    # Deo.g:91:4: prefix_expr
                    pass 
                    self._state.following.append(self.FOLLOW_prefix_expr_in_expr384)
                    prefix_expr13 = self.prefix_expr()

                    self._state.following.pop()
                    stream_prefix_expr.add(prefix_expr13.tree)


                    # AST Rewrite
                    # elements: prefix_expr
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
                    # 91:20: -> ^( EXPR prefix_expr )
                    # Deo.g:91:23: ^( EXPR prefix_expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(EXPR, "EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_prefix_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 3:
                    # Deo.g:92:4: infix_expr
                    pass 
                    self._state.following.append(self.FOLLOW_infix_expr_in_expr401)
                    infix_expr14 = self.infix_expr()

                    self._state.following.pop()
                    stream_infix_expr.add(infix_expr14.tree)


                    # AST Rewrite
                    # elements: infix_expr
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
                    # 92:19: -> ^( EXPR infix_expr )
                    # Deo.g:92:22: ^( EXPR infix_expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(EXPR, "EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_infix_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 4:
                    # Deo.g:93:4: ifthen_expr
                    pass 
                    self._state.following.append(self.FOLLOW_ifthen_expr_in_expr418)
                    ifthen_expr15 = self.ifthen_expr()

                    self._state.following.pop()
                    stream_ifthen_expr.add(ifthen_expr15.tree)


                    # AST Rewrite
                    # elements: ifthen_expr
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
                    # 93:20: -> ^( EXPR ifthen_expr )
                    # Deo.g:93:23: ^( EXPR ifthen_expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(EXPR, "EXPR")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_ifthen_expr.nextTree())

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


    class prefix_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.prefix_expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "prefix_expr"
    # Deo.g:96:1: prefix_expr : LB pop LB expr RB RB -> ^( PREF pop expr ) ;
    def prefix_expr(self, ):
        retval = self.prefix_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LB16 = None
        LB18 = None
        RB20 = None
        RB21 = None
        pop17 = None
        expr19 = None

        LB16_tree = None
        LB18_tree = None
        RB20_tree = None
        RB21_tree = None
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_pop = RewriteRuleSubtreeStream(self._adaptor, "rule pop")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Deo.g:97:2: ( LB pop LB expr RB RB -> ^( PREF pop expr ) )
                # Deo.g:97:4: LB pop LB expr RB RB
                pass 
                LB16 = self.match(self.input, LB, self.FOLLOW_LB_in_prefix_expr441) 
                stream_LB.add(LB16)


                self._state.following.append(self.FOLLOW_pop_in_prefix_expr443)
                pop17 = self.pop()

                self._state.following.pop()
                stream_pop.add(pop17.tree)


                LB18 = self.match(self.input, LB, self.FOLLOW_LB_in_prefix_expr445) 
                stream_LB.add(LB18)


                self._state.following.append(self.FOLLOW_expr_in_prefix_expr447)
                expr19 = self.expr()

                self._state.following.pop()
                stream_expr.add(expr19.tree)


                RB20 = self.match(self.input, RB, self.FOLLOW_RB_in_prefix_expr449) 
                stream_RB.add(RB20)


                RB21 = self.match(self.input, RB, self.FOLLOW_RB_in_prefix_expr451) 
                stream_RB.add(RB21)


                # AST Rewrite
                # elements: pop, expr
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
                # 97:28: -> ^( PREF pop expr )
                # Deo.g:97:31: ^( PREF pop expr )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(PREF, "PREF")
                , root_1)

                self._adaptor.addChild(root_1, stream_pop.nextTree())

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

    # $ANTLR end "prefix_expr"


    class infix_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.infix_expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "infix_expr"
    # Deo.g:100:1: infix_expr : LB expr iop expr RB -> ^( INF expr iop expr ) ;
    def infix_expr(self, ):
        retval = self.infix_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LB22 = None
        RB26 = None
        expr23 = None
        iop24 = None
        expr25 = None

        LB22_tree = None
        RB26_tree = None
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_iop = RewriteRuleSubtreeStream(self._adaptor, "rule iop")
        try:
            try:
                # Deo.g:101:2: ( LB expr iop expr RB -> ^( INF expr iop expr ) )
                # Deo.g:101:4: LB expr iop expr RB
                pass 
                LB22 = self.match(self.input, LB, self.FOLLOW_LB_in_infix_expr475) 
                stream_LB.add(LB22)


                self._state.following.append(self.FOLLOW_expr_in_infix_expr477)
                expr23 = self.expr()

                self._state.following.pop()
                stream_expr.add(expr23.tree)


                self._state.following.append(self.FOLLOW_iop_in_infix_expr479)
                iop24 = self.iop()

                self._state.following.pop()
                stream_iop.add(iop24.tree)


                self._state.following.append(self.FOLLOW_expr_in_infix_expr481)
                expr25 = self.expr()

                self._state.following.pop()
                stream_expr.add(expr25.tree)


                RB26 = self.match(self.input, RB, self.FOLLOW_RB_in_infix_expr483) 
                stream_RB.add(RB26)


                # AST Rewrite
                # elements: expr, expr, iop
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
                # 101:27: -> ^( INF expr iop expr )
                # Deo.g:101:30: ^( INF expr iop expr )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(INF, "INF")
                , root_1)

                self._adaptor.addChild(root_1, stream_expr.nextTree())

                self._adaptor.addChild(root_1, stream_iop.nextTree())

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

    # $ANTLR end "infix_expr"


    class ifthen_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(DeoParser.ifthen_expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "ifthen_expr"
    # Deo.g:104:1: ifthen_expr : LB IF expr THEN expr RB -> ^( IFTHEN expr expr ) ;
    def ifthen_expr(self, ):
        retval = self.ifthen_expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LB27 = None
        IF28 = None
        THEN30 = None
        RB32 = None
        expr29 = None
        expr31 = None

        LB27_tree = None
        IF28_tree = None
        THEN30_tree = None
        RB32_tree = None
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_THEN = RewriteRuleTokenStream(self._adaptor, "token THEN")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Deo.g:105:2: ( LB IF expr THEN expr RB -> ^( IFTHEN expr expr ) )
                # Deo.g:105:4: LB IF expr THEN expr RB
                pass 
                LB27 = self.match(self.input, LB, self.FOLLOW_LB_in_ifthen_expr509) 
                stream_LB.add(LB27)


                IF28 = self.match(self.input, IF, self.FOLLOW_IF_in_ifthen_expr511) 
                stream_IF.add(IF28)


                self._state.following.append(self.FOLLOW_expr_in_ifthen_expr513)
                expr29 = self.expr()

                self._state.following.pop()
                stream_expr.add(expr29.tree)


                THEN30 = self.match(self.input, THEN, self.FOLLOW_THEN_in_ifthen_expr515) 
                stream_THEN.add(THEN30)


                self._state.following.append(self.FOLLOW_expr_in_ifthen_expr517)
                expr31 = self.expr()

                self._state.following.pop()
                stream_expr.add(expr31.tree)


                RB32 = self.match(self.input, RB, self.FOLLOW_RB_in_ifthen_expr519) 
                stream_RB.add(RB32)


                # AST Rewrite
                # elements: expr, expr
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
                # 105:31: -> ^( IFTHEN expr expr )
                # Deo.g:105:34: ^( IFTHEN expr expr )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(IFTHEN, "IFTHEN")
                , root_1)

                self._adaptor.addChild(root_1, stream_expr.nextTree())

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

    # $ANTLR end "ifthen_expr"



 

    FOLLOW_decl_in_prog122 = frozenset([1, 6, 15, 20])
    FOLLOW_fact_decl_in_decl149 = frozenset([1])
    FOLLOW_rule_decl_in_decl166 = frozenset([1])
    FOLLOW_expr_in_rule_decl191 = frozenset([1])
    FOLLOW_fact_in_fact_decl208 = frozenset([1])
    FOLLOW_ID_in_fact229 = frozenset([5])
    FOLLOW_ASSN_in_fact231 = frozenset([6])
    FOLLOW_atom_in_fact233 = frozenset([1])
    FOLLOW_ATOM_in_atom251 = frozenset([1])
    FOLLOW_atom_in_expr366 = frozenset([1])
    FOLLOW_prefix_expr_in_expr384 = frozenset([1])
    FOLLOW_infix_expr_in_expr401 = frozenset([1])
    FOLLOW_ifthen_expr_in_expr418 = frozenset([1])
    FOLLOW_LB_in_prefix_expr441 = frozenset([22, 23, 25, 27])
    FOLLOW_pop_in_prefix_expr443 = frozenset([20])
    FOLLOW_LB_in_prefix_expr445 = frozenset([6, 20])
    FOLLOW_expr_in_prefix_expr447 = frozenset([29])
    FOLLOW_RB_in_prefix_expr449 = frozenset([29])
    FOLLOW_RB_in_prefix_expr451 = frozenset([1])
    FOLLOW_LB_in_infix_expr475 = frozenset([6, 20])
    FOLLOW_expr_in_infix_expr477 = frozenset([4, 17, 24])
    FOLLOW_iop_in_infix_expr479 = frozenset([6, 20])
    FOLLOW_expr_in_infix_expr481 = frozenset([29])
    FOLLOW_RB_in_infix_expr483 = frozenset([1])
    FOLLOW_LB_in_ifthen_expr509 = frozenset([16])
    FOLLOW_IF_in_ifthen_expr511 = frozenset([6, 20])
    FOLLOW_expr_in_ifthen_expr513 = frozenset([31])
    FOLLOW_THEN_in_ifthen_expr515 = frozenset([6, 20])
    FOLLOW_expr_in_ifthen_expr517 = frozenset([29])
    FOLLOW_RB_in_ifthen_expr519 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("DeoLexer", DeoParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
