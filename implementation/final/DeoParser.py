# $ANTLR 3.1.2 Deo.g 2016-03-10 23:06:15

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
IFF=27
TERM=12
ASSN=16
RULE=13
RB=19
PER=22
LETTER=30
PREF=10
NOT=23
ATOM=11
AND=25
ID=17
SPACE=24
EOF=-1
PRO=21
INF=9
OB=20
IF=28
PROG=6
EXPR=5
EOL=15
THEN=29
DECL=8
OR=26
IFTHEN=4
LB=18
DIGIT=31
GOAL=7
FACT=14

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "IFTHEN", "EXPR", "PROG", "GOAL", "DECL", "INF", "PREF", "ATOM", "TERM", 
    "RULE", "FACT", "EOL", "ASSN", "ID", "LB", "RB", "OB", "PRO", "PER", 
    "NOT", "SPACE", "AND", "OR", "IFF", "IF", "THEN", "LETTER", "DIGIT"
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
    # Deo.g:26:1: prog : ( decl )+ EOF -> ^( PROG ( decl )+ ) ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        decl1 = None


        EOF2_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_decl = RewriteRuleSubtreeStream(self._adaptor, "rule decl")
        try:
            try:
                # Deo.g:27:2: ( ( decl )+ EOF -> ^( PROG ( decl )+ ) )
                # Deo.g:27:4: ( decl )+ EOF
                pass 
                # Deo.g:27:4: ( decl )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == GOAL or (RULE <= LA1_0 <= FACT) or LA1_0 == ID) :
                        alt1 = 1


                    if alt1 == 1:
                        # Deo.g:27:4: decl
                        pass 
                        self._state.following.append(self.FOLLOW_decl_in_prog103)
                        decl1 = self.decl()

                        self._state.following.pop()
                        stream_decl.add(decl1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                EOF2=self.match(self.input, EOF, self.FOLLOW_EOF_in_prog106) 
                stream_EOF.add(EOF2)

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
                # 27:21: -> ^( PROG ( decl )+ )
                # Deo.g:27:24: ^( PROG ( decl )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROG, "PROG"), root_1)

                # Deo.g:27:31: ( decl )+
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
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "decl"
    # Deo.g:30:1: decl : ( term EOL -> ^( TERM term ) | rule EOL -> ^( RULE rule ) | fact EOL -> ^( FACT fact ) | goal EOL -> ^( GOAL goal ) );
    def decl(self, ):

        retval = self.decl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOL4 = None
        EOL6 = None
        EOL8 = None
        EOL10 = None
        term3 = None

        rule5 = None

        fact7 = None

        goal9 = None


        EOL4_tree = None
        EOL6_tree = None
        EOL8_tree = None
        EOL10_tree = None
        stream_EOL = RewriteRuleTokenStream(self._adaptor, "token EOL")
        stream_fact = RewriteRuleSubtreeStream(self._adaptor, "rule fact")
        stream_term = RewriteRuleSubtreeStream(self._adaptor, "rule term")
        stream_rule = RewriteRuleSubtreeStream(self._adaptor, "rule rule")
        stream_goal = RewriteRuleSubtreeStream(self._adaptor, "rule goal")
        try:
            try:
                # Deo.g:31:2: ( term EOL -> ^( TERM term ) | rule EOL -> ^( RULE rule ) | fact EOL -> ^( FACT fact ) | goal EOL -> ^( GOAL goal ) )
                alt2 = 4
                LA2 = self.input.LA(1)
                if LA2 == ID:
                    alt2 = 1
                elif LA2 == RULE:
                    alt2 = 2
                elif LA2 == FACT:
                    alt2 = 3
                elif LA2 == GOAL:
                    alt2 = 4
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # Deo.g:31:4: term EOL
                    pass 
                    self._state.following.append(self.FOLLOW_term_in_decl133)
                    term3 = self.term()

                    self._state.following.pop()
                    stream_term.add(term3.tree)
                    EOL4=self.match(self.input, EOL, self.FOLLOW_EOL_in_decl135) 
                    stream_EOL.add(EOL4)

                    # AST Rewrite
                    # elements: term
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
                    # 31:20: -> ^( TERM term )
                    # Deo.g:31:23: ^( TERM term )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TERM, "TERM"), root_1)

                    self._adaptor.addChild(root_1, stream_term.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 2:
                    # Deo.g:32:4: rule EOL
                    pass 
                    self._state.following.append(self.FOLLOW_rule_in_decl155)
                    rule5 = self.rule()

                    self._state.following.pop()
                    stream_rule.add(rule5.tree)
                    EOL6=self.match(self.input, EOL, self.FOLLOW_EOL_in_decl157) 
                    stream_EOL.add(EOL6)

                    # AST Rewrite
                    # elements: rule
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
                    # 32:20: -> ^( RULE rule )
                    # Deo.g:32:23: ^( RULE rule )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RULE, "RULE"), root_1)

                    self._adaptor.addChild(root_1, stream_rule.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 3:
                    # Deo.g:33:4: fact EOL
                    pass 
                    self._state.following.append(self.FOLLOW_fact_in_decl177)
                    fact7 = self.fact()

                    self._state.following.pop()
                    stream_fact.add(fact7.tree)
                    EOL8=self.match(self.input, EOL, self.FOLLOW_EOL_in_decl179) 
                    stream_EOL.add(EOL8)

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
                    # 33:20: -> ^( FACT fact )
                    # Deo.g:33:23: ^( FACT fact )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FACT, "FACT"), root_1)

                    self._adaptor.addChild(root_1, stream_fact.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt2 == 4:
                    # Deo.g:34:4: goal EOL
                    pass 
                    self._state.following.append(self.FOLLOW_goal_in_decl199)
                    goal9 = self.goal()

                    self._state.following.pop()
                    stream_goal.add(goal9.tree)
                    EOL10=self.match(self.input, EOL, self.FOLLOW_EOL_in_decl201) 
                    stream_EOL.add(EOL10)

                    # AST Rewrite
                    # elements: goal
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
                    # 34:25: -> ^( GOAL goal )
                    # Deo.g:34:28: ^( GOAL goal )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GOAL, "GOAL"), root_1)

                    self._adaptor.addChild(root_1, stream_goal.nextTree())

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

    class rule_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "rule"
    # Deo.g:37:1: rule : RULE ASSN expr ;
    def rule(self, ):

        retval = self.rule_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RULE11 = None
        ASSN12 = None
        expr13 = None


        RULE11_tree = None
        ASSN12_tree = None

        try:
            try:
                # Deo.g:38:2: ( RULE ASSN expr )
                # Deo.g:38:4: RULE ASSN expr
                pass 
                root_0 = self._adaptor.nil()

                RULE11=self.match(self.input, RULE, self.FOLLOW_RULE_in_rule236)

                RULE11_tree = self._adaptor.createWithPayload(RULE11)
                self._adaptor.addChild(root_0, RULE11_tree)

                ASSN12=self.match(self.input, ASSN, self.FOLLOW_ASSN_in_rule238)

                ASSN12_tree = self._adaptor.createWithPayload(ASSN12)
                self._adaptor.addChild(root_0, ASSN12_tree)

                self._state.following.append(self.FOLLOW_expr_in_rule240)
                expr13 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr13.tree)



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

    # $ANTLR end "rule"

    class fact_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "fact"
    # Deo.g:41:1: fact : FACT ASSN expr ;
    def fact(self, ):

        retval = self.fact_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FACT14 = None
        ASSN15 = None
        expr16 = None


        FACT14_tree = None
        ASSN15_tree = None

        try:
            try:
                # Deo.g:42:2: ( FACT ASSN expr )
                # Deo.g:42:4: FACT ASSN expr
                pass 
                root_0 = self._adaptor.nil()

                FACT14=self.match(self.input, FACT, self.FOLLOW_FACT_in_fact251)

                FACT14_tree = self._adaptor.createWithPayload(FACT14)
                self._adaptor.addChild(root_0, FACT14_tree)

                ASSN15=self.match(self.input, ASSN, self.FOLLOW_ASSN_in_fact253)

                ASSN15_tree = self._adaptor.createWithPayload(ASSN15)
                self._adaptor.addChild(root_0, ASSN15_tree)

                self._state.following.append(self.FOLLOW_expr_in_fact255)
                expr16 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr16.tree)



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

    class goal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "goal"
    # Deo.g:45:1: goal : GOAL ASSN expr ;
    def goal(self, ):

        retval = self.goal_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GOAL17 = None
        ASSN18 = None
        expr19 = None


        GOAL17_tree = None
        ASSN18_tree = None

        try:
            try:
                # Deo.g:46:2: ( GOAL ASSN expr )
                # Deo.g:46:4: GOAL ASSN expr
                pass 
                root_0 = self._adaptor.nil()

                GOAL17=self.match(self.input, GOAL, self.FOLLOW_GOAL_in_goal266)

                GOAL17_tree = self._adaptor.createWithPayload(GOAL17)
                self._adaptor.addChild(root_0, GOAL17_tree)

                ASSN18=self.match(self.input, ASSN, self.FOLLOW_ASSN_in_goal268)

                ASSN18_tree = self._adaptor.createWithPayload(ASSN18)
                self._adaptor.addChild(root_0, ASSN18_tree)

                self._state.following.append(self.FOLLOW_expr_in_goal270)
                expr19 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr19.tree)



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

    # $ANTLR end "goal"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "term"
    # Deo.g:49:1: term : ID ASSN atom ;
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID20 = None
        ASSN21 = None
        atom22 = None


        ID20_tree = None
        ASSN21_tree = None

        try:
            try:
                # Deo.g:50:2: ( ID ASSN atom )
                # Deo.g:50:4: ID ASSN atom
                pass 
                root_0 = self._adaptor.nil()

                ID20=self.match(self.input, ID, self.FOLLOW_ID_in_term287)

                ID20_tree = self._adaptor.createWithPayload(ID20)
                self._adaptor.addChild(root_0, ID20_tree)

                ASSN21=self.match(self.input, ASSN, self.FOLLOW_ASSN_in_term289)

                ASSN21_tree = self._adaptor.createWithPayload(ASSN21)
                self._adaptor.addChild(root_0, ASSN21_tree)

                self._state.following.append(self.FOLLOW_atom_in_term291)
                atom22 = self.atom()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atom22.tree)



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

    # $ANTLR end "term"

    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "atom"
    # Deo.g:53:1: atom : ATOM ;
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ATOM23 = None

        ATOM23_tree = None

        try:
            try:
                # Deo.g:54:2: ( ATOM )
                # Deo.g:54:4: ATOM
                pass 
                root_0 = self._adaptor.nil()

                ATOM23=self.match(self.input, ATOM, self.FOLLOW_ATOM_in_atom310)

                ATOM23_tree = self._adaptor.createWithPayload(ATOM23)
                self._adaptor.addChild(root_0, ATOM23_tree)




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

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "expr"
    # Deo.g:57:1: expr : ( ID -> ^( EXPR ID ) | prefix_expr -> ^( EXPR prefix_expr ) | infix_expr -> ^( EXPR infix_expr ) | ifthen_expr -> ^( EXPR ifthen_expr ) );
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ID24 = None
        prefix_expr25 = None

        infix_expr26 = None

        ifthen_expr27 = None


        ID24_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_prefix_expr = RewriteRuleSubtreeStream(self._adaptor, "rule prefix_expr")
        stream_infix_expr = RewriteRuleSubtreeStream(self._adaptor, "rule infix_expr")
        stream_ifthen_expr = RewriteRuleSubtreeStream(self._adaptor, "rule ifthen_expr")
        try:
            try:
                # Deo.g:58:2: ( ID -> ^( EXPR ID ) | prefix_expr -> ^( EXPR prefix_expr ) | infix_expr -> ^( EXPR infix_expr ) | ifthen_expr -> ^( EXPR ifthen_expr ) )
                alt3 = 4
                LA3_0 = self.input.LA(1)

                if (LA3_0 == ID) :
                    alt3 = 1
                elif (LA3_0 == LB) :
                    LA3 = self.input.LA(2)
                    if LA3 == IF:
                        alt3 = 4
                    elif LA3 == ID or LA3 == LB:
                        alt3 = 3
                    elif LA3 == OB or LA3 == PRO or LA3 == PER or LA3 == NOT:
                        alt3 = 2
                    else:
                        nvae = NoViableAltException("", 3, 2, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # Deo.g:58:4: ID
                    pass 
                    ID24=self.match(self.input, ID, self.FOLLOW_ID_in_expr329) 
                    stream_ID.add(ID24)

                    # AST Rewrite
                    # elements: ID
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
                    # 58:18: -> ^( EXPR ID )
                    # Deo.g:58:21: ^( EXPR ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_ID.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 2:
                    # Deo.g:59:4: prefix_expr
                    pass 
                    self._state.following.append(self.FOLLOW_prefix_expr_in_expr353)
                    prefix_expr25 = self.prefix_expr()

                    self._state.following.pop()
                    stream_prefix_expr.add(prefix_expr25.tree)

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
                    # 59:25: -> ^( EXPR prefix_expr )
                    # Deo.g:59:28: ^( EXPR prefix_expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_prefix_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 3:
                    # Deo.g:60:4: infix_expr
                    pass 
                    self._state.following.append(self.FOLLOW_infix_expr_in_expr375)
                    infix_expr26 = self.infix_expr()

                    self._state.following.pop()
                    stream_infix_expr.add(infix_expr26.tree)

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
                    # 60:24: -> ^( EXPR infix_expr )
                    # Deo.g:60:27: ^( EXPR infix_expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_infix_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 4:
                    # Deo.g:61:4: ifthen_expr
                    pass 
                    self._state.following.append(self.FOLLOW_ifthen_expr_in_expr397)
                    ifthen_expr27 = self.ifthen_expr()

                    self._state.following.pop()
                    stream_ifthen_expr.add(ifthen_expr27.tree)

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
                    # 61:25: -> ^( EXPR ifthen_expr )
                    # Deo.g:61:28: ^( EXPR ifthen_expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR, "EXPR"), root_1)

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
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "prefix_expr"
    # Deo.g:64:1: prefix_expr : LB pop LB expr RB RB -> ^( PREF pop expr ) ;
    def prefix_expr(self, ):

        retval = self.prefix_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB28 = None
        LB30 = None
        RB32 = None
        RB33 = None
        pop29 = None

        expr31 = None


        LB28_tree = None
        LB30_tree = None
        RB32_tree = None
        RB33_tree = None
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_pop = RewriteRuleSubtreeStream(self._adaptor, "rule pop")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Deo.g:65:2: ( LB pop LB expr RB RB -> ^( PREF pop expr ) )
                # Deo.g:65:4: LB pop LB expr RB RB
                pass 
                LB28=self.match(self.input, LB, self.FOLLOW_LB_in_prefix_expr425) 
                stream_LB.add(LB28)
                self._state.following.append(self.FOLLOW_pop_in_prefix_expr427)
                pop29 = self.pop()

                self._state.following.pop()
                stream_pop.add(pop29.tree)
                LB30=self.match(self.input, LB, self.FOLLOW_LB_in_prefix_expr429) 
                stream_LB.add(LB30)
                self._state.following.append(self.FOLLOW_expr_in_prefix_expr431)
                expr31 = self.expr()

                self._state.following.pop()
                stream_expr.add(expr31.tree)
                RB32=self.match(self.input, RB, self.FOLLOW_RB_in_prefix_expr433) 
                stream_RB.add(RB32)
                RB33=self.match(self.input, RB, self.FOLLOW_RB_in_prefix_expr435) 
                stream_RB.add(RB33)

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
                # 65:30: -> ^( PREF pop expr )
                # Deo.g:65:33: ^( PREF pop expr )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PREF, "PREF"), root_1)

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

    class pop_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "pop"
    # Deo.g:68:1: pop : ( OB | PRO | PER | NOT );
    def pop(self, ):

        retval = self.pop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set34 = None

        set34_tree = None

        try:
            try:
                # Deo.g:69:2: ( OB | PRO | PER | NOT )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()

                set34 = self.input.LT(1)
                if (OB <= self.input.LA(1) <= NOT):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set34))
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

    class infix_expr_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "infix_expr"
    # Deo.g:75:1: infix_expr : LB e1= expr SPACE iop SPACE e2= expr RB -> ^( iop $e1 $e2) ;
    def infix_expr(self, ):

        retval = self.infix_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB35 = None
        SPACE36 = None
        SPACE38 = None
        RB39 = None
        e1 = None

        e2 = None

        iop37 = None


        LB35_tree = None
        SPACE36_tree = None
        SPACE38_tree = None
        RB39_tree = None
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_SPACE = RewriteRuleTokenStream(self._adaptor, "token SPACE")
        stream_iop = RewriteRuleSubtreeStream(self._adaptor, "rule iop")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Deo.g:76:2: ( LB e1= expr SPACE iop SPACE e2= expr RB -> ^( iop $e1 $e2) )
                # Deo.g:76:4: LB e1= expr SPACE iop SPACE e2= expr RB
                pass 
                LB35=self.match(self.input, LB, self.FOLLOW_LB_in_infix_expr512) 
                stream_LB.add(LB35)
                self._state.following.append(self.FOLLOW_expr_in_infix_expr516)
                e1 = self.expr()

                self._state.following.pop()
                stream_expr.add(e1.tree)
                SPACE36=self.match(self.input, SPACE, self.FOLLOW_SPACE_in_infix_expr518) 
                stream_SPACE.add(SPACE36)
                self._state.following.append(self.FOLLOW_iop_in_infix_expr520)
                iop37 = self.iop()

                self._state.following.pop()
                stream_iop.add(iop37.tree)
                SPACE38=self.match(self.input, SPACE, self.FOLLOW_SPACE_in_infix_expr522) 
                stream_SPACE.add(SPACE38)
                self._state.following.append(self.FOLLOW_expr_in_infix_expr526)
                e2 = self.expr()

                self._state.following.pop()
                stream_expr.add(e2.tree)
                RB39=self.match(self.input, RB, self.FOLLOW_RB_in_infix_expr528) 
                stream_RB.add(RB39)

                # AST Rewrite
                # elements: e1, e2, iop
                # token labels: 
                # rule labels: retval, e1, e2
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if e1 is not None:
                    stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "rule e1", e1.tree)
                else:
                    stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "token e1", None)


                if e2 is not None:
                    stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "rule e2", e2.tree)
                else:
                    stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "token e2", None)


                root_0 = self._adaptor.nil()
                # 76:46: -> ^( iop $e1 $e2)
                # Deo.g:76:49: ^( iop $e1 $e2)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_iop.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_e1.nextTree())
                self._adaptor.addChild(root_1, stream_e2.nextTree())

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

    class iop_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "iop"
    # Deo.g:79:1: iop : ( AND | OR | IFF );
    def iop(self, ):

        retval = self.iop_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set40 = None

        set40_tree = None

        try:
            try:
                # Deo.g:79:5: ( AND | OR | IFF )
                # Deo.g:
                pass 
                root_0 = self._adaptor.nil()

                set40 = self.input.LT(1)
                if (AND <= self.input.LA(1) <= IFF):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set40))
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

    class ifthen_expr_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "ifthen_expr"
    # Deo.g:84:1: ifthen_expr : LB IF SPACE e1= expr SPACE THEN SPACE e2= expr RB -> ^( IFTHEN $e1 $e2) ;
    def ifthen_expr(self, ):

        retval = self.ifthen_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LB41 = None
        IF42 = None
        SPACE43 = None
        SPACE44 = None
        THEN45 = None
        SPACE46 = None
        RB47 = None
        e1 = None

        e2 = None


        LB41_tree = None
        IF42_tree = None
        SPACE43_tree = None
        SPACE44_tree = None
        THEN45_tree = None
        SPACE46_tree = None
        RB47_tree = None
        stream_LB = RewriteRuleTokenStream(self._adaptor, "token LB")
        stream_THEN = RewriteRuleTokenStream(self._adaptor, "token THEN")
        stream_RB = RewriteRuleTokenStream(self._adaptor, "token RB")
        stream_SPACE = RewriteRuleTokenStream(self._adaptor, "token SPACE")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Deo.g:85:2: ( LB IF SPACE e1= expr SPACE THEN SPACE e2= expr RB -> ^( IFTHEN $e1 $e2) )
                # Deo.g:85:4: LB IF SPACE e1= expr SPACE THEN SPACE e2= expr RB
                pass 
                LB41=self.match(self.input, LB, self.FOLLOW_LB_in_ifthen_expr578) 
                stream_LB.add(LB41)
                IF42=self.match(self.input, IF, self.FOLLOW_IF_in_ifthen_expr580) 
                stream_IF.add(IF42)
                SPACE43=self.match(self.input, SPACE, self.FOLLOW_SPACE_in_ifthen_expr582) 
                stream_SPACE.add(SPACE43)
                self._state.following.append(self.FOLLOW_expr_in_ifthen_expr586)
                e1 = self.expr()

                self._state.following.pop()
                stream_expr.add(e1.tree)
                SPACE44=self.match(self.input, SPACE, self.FOLLOW_SPACE_in_ifthen_expr588) 
                stream_SPACE.add(SPACE44)
                THEN45=self.match(self.input, THEN, self.FOLLOW_THEN_in_ifthen_expr590) 
                stream_THEN.add(THEN45)
                SPACE46=self.match(self.input, SPACE, self.FOLLOW_SPACE_in_ifthen_expr592) 
                stream_SPACE.add(SPACE46)
                self._state.following.append(self.FOLLOW_expr_in_ifthen_expr596)
                e2 = self.expr()

                self._state.following.pop()
                stream_expr.add(e2.tree)
                RB47=self.match(self.input, RB, self.FOLLOW_RB_in_ifthen_expr598) 
                stream_RB.add(RB47)

                # AST Rewrite
                # elements: e2, e1
                # token labels: 
                # rule labels: retval, e1, e2
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                if e1 is not None:
                    stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "rule e1", e1.tree)
                else:
                    stream_e1 = RewriteRuleSubtreeStream(self._adaptor, "token e1", None)


                if e2 is not None:
                    stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "rule e2", e2.tree)
                else:
                    stream_e2 = RewriteRuleSubtreeStream(self._adaptor, "token e2", None)


                root_0 = self._adaptor.nil()
                # 85:55: -> ^( IFTHEN $e1 $e2)
                # Deo.g:85:58: ^( IFTHEN $e1 $e2)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IFTHEN, "IFTHEN"), root_1)

                self._adaptor.addChild(root_1, stream_e1.nextTree())
                self._adaptor.addChild(root_1, stream_e2.nextTree())

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


    # Delegated rules


 

    FOLLOW_decl_in_prog103 = frozenset([7, 13, 14, 17])
    FOLLOW_EOF_in_prog106 = frozenset([1])
    FOLLOW_term_in_decl133 = frozenset([15])
    FOLLOW_EOL_in_decl135 = frozenset([1])
    FOLLOW_rule_in_decl155 = frozenset([15])
    FOLLOW_EOL_in_decl157 = frozenset([1])
    FOLLOW_fact_in_decl177 = frozenset([15])
    FOLLOW_EOL_in_decl179 = frozenset([1])
    FOLLOW_goal_in_decl199 = frozenset([15])
    FOLLOW_EOL_in_decl201 = frozenset([1])
    FOLLOW_RULE_in_rule236 = frozenset([16])
    FOLLOW_ASSN_in_rule238 = frozenset([17, 18])
    FOLLOW_expr_in_rule240 = frozenset([1])
    FOLLOW_FACT_in_fact251 = frozenset([16])
    FOLLOW_ASSN_in_fact253 = frozenset([17, 18])
    FOLLOW_expr_in_fact255 = frozenset([1])
    FOLLOW_GOAL_in_goal266 = frozenset([16])
    FOLLOW_ASSN_in_goal268 = frozenset([17, 18])
    FOLLOW_expr_in_goal270 = frozenset([1])
    FOLLOW_ID_in_term287 = frozenset([16])
    FOLLOW_ASSN_in_term289 = frozenset([11])
    FOLLOW_atom_in_term291 = frozenset([1])
    FOLLOW_ATOM_in_atom310 = frozenset([1])
    FOLLOW_ID_in_expr329 = frozenset([1])
    FOLLOW_prefix_expr_in_expr353 = frozenset([1])
    FOLLOW_infix_expr_in_expr375 = frozenset([1])
    FOLLOW_ifthen_expr_in_expr397 = frozenset([1])
    FOLLOW_LB_in_prefix_expr425 = frozenset([20, 21, 22, 23])
    FOLLOW_pop_in_prefix_expr427 = frozenset([18])
    FOLLOW_LB_in_prefix_expr429 = frozenset([17, 18])
    FOLLOW_expr_in_prefix_expr431 = frozenset([19])
    FOLLOW_RB_in_prefix_expr433 = frozenset([19])
    FOLLOW_RB_in_prefix_expr435 = frozenset([1])
    FOLLOW_set_in_pop0 = frozenset([1])
    FOLLOW_LB_in_infix_expr512 = frozenset([17, 18])
    FOLLOW_expr_in_infix_expr516 = frozenset([24])
    FOLLOW_SPACE_in_infix_expr518 = frozenset([25, 26, 27])
    FOLLOW_iop_in_infix_expr520 = frozenset([24])
    FOLLOW_SPACE_in_infix_expr522 = frozenset([17, 18])
    FOLLOW_expr_in_infix_expr526 = frozenset([19])
    FOLLOW_RB_in_infix_expr528 = frozenset([1])
    FOLLOW_set_in_iop0 = frozenset([1])
    FOLLOW_LB_in_ifthen_expr578 = frozenset([28])
    FOLLOW_IF_in_ifthen_expr580 = frozenset([24])
    FOLLOW_SPACE_in_ifthen_expr582 = frozenset([17, 18])
    FOLLOW_expr_in_ifthen_expr586 = frozenset([24])
    FOLLOW_SPACE_in_ifthen_expr588 = frozenset([29])
    FOLLOW_THEN_in_ifthen_expr590 = frozenset([24])
    FOLLOW_SPACE_in_ifthen_expr592 = frozenset([17, 18])
    FOLLOW_expr_in_ifthen_expr596 = frozenset([19])
    FOLLOW_RB_in_ifthen_expr598 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("DeoLexer", DeoParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
