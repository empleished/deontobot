# $ANTLR 3.1.2 Deo.g 2016-03-28 01:47:07

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TERM=9
ASSN=13
RULE=6
RB=18
PER=21
LETTER=27
NOT=22
ATOM=15
AND=23
ID=14
EOF=-1
SPACE=17
PRO=20
OB=19
IF=25
PROG=4
EOL=12
EXPR=11
THEN=26
DECL=5
OR=24
IFTHEN=10
LB=16
DIGIT=28
PUNCT=29
GOAL=8
FACT=7


class DeoLexer(Lexer):

    grammarFileName = "Deo.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )






    # $ANTLR start "OB"
    def mOB(self, ):

        try:
            _type = OB
            _channel = DEFAULT_CHANNEL

            # Deo.g:87:4: ( 'OB' )
            # Deo.g:87:6: 'OB'
            pass 
            self.match("OB")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OB"



    # $ANTLR start "PRO"
    def mPRO(self, ):

        try:
            _type = PRO
            _channel = DEFAULT_CHANNEL

            # Deo.g:88:5: ( 'PRO' )
            # Deo.g:88:7: 'PRO'
            pass 
            self.match("PRO")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PRO"



    # $ANTLR start "PER"
    def mPER(self, ):

        try:
            _type = PER
            _channel = DEFAULT_CHANNEL

            # Deo.g:89:5: ( 'PER' )
            # Deo.g:89:7: 'PER'
            pass 
            self.match("PER")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PER"



    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # Deo.g:91:4: ( 'if' )
            # Deo.g:91:6: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # Deo.g:92:6: ( 'then' )
            # Deo.g:92:8: 'then'
            pass 
            self.match("then")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THEN"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # Deo.g:93:5: ( 'not' )
            # Deo.g:93:7: 'not'
            pass 
            self.match("not")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # Deo.g:94:5: ( 'and' )
            # Deo.g:94:7: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # Deo.g:95:4: ( 'or' )
            # Deo.g:95:6: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "TERM"
    def mTERM(self, ):

        try:
            _type = TERM
            _channel = DEFAULT_CHANNEL

            # Deo.g:97:9: ( 'term' )
            # Deo.g:97:11: 'term'
            pass 
            self.match("term")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TERM"



    # $ANTLR start "GOAL"
    def mGOAL(self, ):

        try:
            _type = GOAL
            _channel = DEFAULT_CHANNEL

            # Deo.g:98:9: ( 'goal' )
            # Deo.g:98:11: 'goal'
            pass 
            self.match("goal")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GOAL"



    # $ANTLR start "RULE"
    def mRULE(self, ):

        try:
            _type = RULE
            _channel = DEFAULT_CHANNEL

            # Deo.g:99:9: ( 'rule' )
            # Deo.g:99:11: 'rule'
            pass 
            self.match("rule")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RULE"



    # $ANTLR start "FACT"
    def mFACT(self, ):

        try:
            _type = FACT
            _channel = DEFAULT_CHANNEL

            # Deo.g:100:9: ( 'fact' )
            # Deo.g:100:11: 'fact'
            pass 
            self.match("fact")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FACT"



    # $ANTLR start "LB"
    def mLB(self, ):

        try:
            _type = LB
            _channel = DEFAULT_CHANNEL

            # Deo.g:102:4: ( '(' )
            # Deo.g:102:6: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LB"



    # $ANTLR start "RB"
    def mRB(self, ):

        try:
            _type = RB
            _channel = DEFAULT_CHANNEL

            # Deo.g:103:4: ( ')' )
            # Deo.g:103:6: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RB"



    # $ANTLR start "ASSN"
    def mASSN(self, ):

        try:
            _type = ASSN
            _channel = DEFAULT_CHANNEL

            # Deo.g:105:6: ( ': ' )
            # Deo.g:105:9: ': '
            pass 
            self.match(": ")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSN"



    # $ANTLR start "ATOM"
    def mATOM(self, ):

        try:
            _type = ATOM
            _channel = DEFAULT_CHANNEL

            # Deo.g:107:6: ( '\"' LETTER ( LETTER | DIGIT | PUNCT )* '\"' )
            # Deo.g:107:8: '\"' LETTER ( LETTER | DIGIT | PUNCT )* '\"'
            pass 
            self.match(34)
            self.mLETTER()
            # Deo.g:107:19: ( LETTER | DIGIT | PUNCT )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 32 or LA1_0 == 39 or LA1_0 == 44 or (48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # Deo.g:
                    pass 
                    if self.input.LA(1) == 32 or self.input.LA(1) == 39 or self.input.LA(1) == 44 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ATOM"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # Deo.g:108:4: ( LETTER ( LETTER | DIGIT | '_' )* )
            # Deo.g:108:6: LETTER ( LETTER | DIGIT | '_' )*
            pass 
            self.mLETTER()
            # Deo.g:108:13: ( LETTER | DIGIT | '_' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57) or (65 <= LA2_0 <= 90) or LA2_0 == 95 or (97 <= LA2_0 <= 122)) :
                    alt2 = 1


                if alt2 == 1:
                    # Deo.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop2





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # Deo.g:111:2: ( 'a' .. 'z' | 'A' .. 'Z' )
            # Deo.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # Deo.g:113:2: ( '0' .. '9' )
            # Deo.g:113:5: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "PUNCT"
    def mPUNCT(self, ):

        try:
            # Deo.g:116:2: ( '\\'' | ',' | ' ' )
            # Deo.g:
            pass 
            if self.input.LA(1) == 32 or self.input.LA(1) == 39 or self.input.LA(1) == 44:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "PUNCT"



    # $ANTLR start "EOL"
    def mEOL(self, ):

        try:
            _type = EOL
            _channel = DEFAULT_CHANNEL

            # Deo.g:118:9: ( ( '\\r' )? '\\n' )
            # Deo.g:118:11: ( '\\r' )? '\\n'
            pass 
            # Deo.g:118:11: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # Deo.g:118:11: '\\r'
                pass 
                self.match(13)



            self.match(10)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EOL"



    # $ANTLR start "SPACE"
    def mSPACE(self, ):

        try:
            _type = SPACE
            _channel = DEFAULT_CHANNEL

            # Deo.g:119:9: ( ( '\\t' | ' ' )+ )
            # Deo.g:119:11: ( '\\t' | ' ' )+
            pass 
            # Deo.g:119:11: ( '\\t' | ' ' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 9 or LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # Deo.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SPACE"



    def mTokens(self):
        # Deo.g:1:8: ( OB | PRO | PER | IF | THEN | NOT | AND | OR | TERM | GOAL | RULE | FACT | LB | RB | ASSN | ATOM | ID | EOL | SPACE )
        alt5 = 19
        alt5 = self.dfa5.predict(self.input)
        if alt5 == 1:
            # Deo.g:1:10: OB
            pass 
            self.mOB()


        elif alt5 == 2:
            # Deo.g:1:13: PRO
            pass 
            self.mPRO()


        elif alt5 == 3:
            # Deo.g:1:17: PER
            pass 
            self.mPER()


        elif alt5 == 4:
            # Deo.g:1:21: IF
            pass 
            self.mIF()


        elif alt5 == 5:
            # Deo.g:1:24: THEN
            pass 
            self.mTHEN()


        elif alt5 == 6:
            # Deo.g:1:29: NOT
            pass 
            self.mNOT()


        elif alt5 == 7:
            # Deo.g:1:33: AND
            pass 
            self.mAND()


        elif alt5 == 8:
            # Deo.g:1:37: OR
            pass 
            self.mOR()


        elif alt5 == 9:
            # Deo.g:1:40: TERM
            pass 
            self.mTERM()


        elif alt5 == 10:
            # Deo.g:1:45: GOAL
            pass 
            self.mGOAL()


        elif alt5 == 11:
            # Deo.g:1:50: RULE
            pass 
            self.mRULE()


        elif alt5 == 12:
            # Deo.g:1:55: FACT
            pass 
            self.mFACT()


        elif alt5 == 13:
            # Deo.g:1:60: LB
            pass 
            self.mLB()


        elif alt5 == 14:
            # Deo.g:1:63: RB
            pass 
            self.mRB()


        elif alt5 == 15:
            # Deo.g:1:66: ASSN
            pass 
            self.mASSN()


        elif alt5 == 16:
            # Deo.g:1:71: ATOM
            pass 
            self.mATOM()


        elif alt5 == 17:
            # Deo.g:1:76: ID
            pass 
            self.mID()


        elif alt5 == 18:
            # Deo.g:1:79: EOL
            pass 
            self.mEOL()


        elif alt5 == 19:
            # Deo.g:1:83: SPACE
            pass 
            self.mSPACE()







    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\1\uffff\12\17\7\uffff\1\36\2\17\1\41\4\17\1\46\3\17\1\uffff\1"
        u"\52\1\53\1\uffff\2\17\1\56\1\57\1\uffff\3\17\2\uffff\1\63\1\64"
        u"\2\uffff\1\65\1\66\1\67\5\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\70\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\11\1\102\1\105\1\146\1\145\1\157\1\156\1\162\1\157\1\165\1\141"
        u"\7\uffff\1\60\1\117\1\122\1\60\1\145\1\162\1\164\1\144\1\60\1\141"
        u"\1\154\1\143\1\uffff\2\60\1\uffff\1\156\1\155\2\60\1\uffff\1\154"
        u"\1\145\1\164\2\uffff\2\60\2\uffff\3\60\5\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\172\1\102\1\122\1\146\1\150\1\157\1\156\1\162\1\157\1\165\1"
        u"\141\7\uffff\1\172\1\117\1\122\1\172\1\145\1\162\1\164\1\144\1"
        u"\172\1\141\1\154\1\143\1\uffff\2\172\1\uffff\1\156\1\155\2\172"
        u"\1\uffff\1\154\1\145\1\164\2\uffff\2\172\2\uffff\3\172\5\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\13\uffff\1\15\1\16\1\17\1\20\1\21\1\22\1\23\14\uffff\1\1\2\uffff"
        u"\1\4\4\uffff\1\10\3\uffff\1\2\1\3\2\uffff\1\6\1\7\3\uffff\1\5\1"
        u"\11\1\12\1\13\1\14"
        )

    DFA5_special = DFA.unpack(
        u"\70\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\1\21\1\20\2\uffff\1\20\22\uffff\1\21\1\uffff\1\16\5"
        u"\uffff\1\13\1\14\20\uffff\1\15\6\uffff\16\17\1\1\1\2\12\17\6\uffff"
        u"\1\6\4\17\1\12\1\10\1\17\1\3\4\17\1\5\1\7\2\17\1\11\1\17\1\4\6"
        u"\17"),
        DFA.unpack(u"\1\22"),
        DFA.unpack(u"\1\24\14\uffff\1\23"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\27\2\uffff\1\26"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    DFA5 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(DeoLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
