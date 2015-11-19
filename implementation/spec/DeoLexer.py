# $ANTLR 3.1.2 Deo.g 2015-11-19 08:38:31

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
EOF=-1
SPACE=27
PRO=16
ACTION=18
OB=15
AXIOM=10
IF=4
PROG=11
EXPR=7
EOL=28
THEN=6
OR=21
LB=23
VAR=12
DIGIT=26
COMMENT=29
FACT=8


class DeoLexer(Lexer):

    grammarFileName = "Deo.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )






    # $ANTLR start "OB"
    def mOB(self, ):

        try:
            _type = OB
            _channel = DEFAULT_CHANNEL

            # Deo.g:66:4: ( 'it is obliged' )
            # Deo.g:66:6: 'it is obliged'
            pass 
            self.match("it is obliged")



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

            # Deo.g:67:5: ( 'it is prohibited' )
            # Deo.g:67:7: 'it is prohibited'
            pass 
            self.match("it is prohibited")



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

            # Deo.g:68:5: ( 'it is permitted' )
            # Deo.g:68:7: 'it is permitted'
            pass 
            self.match("it is permitted")



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

            # Deo.g:70:4: ( 'if' )
            # Deo.g:70:6: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "IFF"
    def mIFF(self, ):

        try:
            _type = IFF
            _channel = DEFAULT_CHANNEL

            # Deo.g:71:5: ( 'if and only if' )
            # Deo.g:71:7: 'if and only if'
            pass 
            self.match("if and only if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IFF"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # Deo.g:72:6: ( 'then' )
            # Deo.g:72:8: 'then'
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

            # Deo.g:73:5: ( 'not' )
            # Deo.g:73:7: 'not'
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

            # Deo.g:74:5: ( 'and' )
            # Deo.g:74:7: 'and'
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

            # Deo.g:75:4: ( 'or' )
            # Deo.g:75:6: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "LB"
    def mLB(self, ):

        try:
            _type = LB
            _channel = DEFAULT_CHANNEL

            # Deo.g:77:4: ( '(' )
            # Deo.g:77:6: '('
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

            # Deo.g:78:4: ( ')' )
            # Deo.g:78:6: ')'
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

            # Deo.g:80:6: ( '=' )
            # Deo.g:80:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSN"



    # $ANTLR start "ACTION"
    def mACTION(self, ):

        try:
            _type = ACTION
            _channel = DEFAULT_CHANNEL

            # Deo.g:82:8: ( LETTER ( LETTER | DIGIT | SPACE )* )
            # Deo.g:82:10: LETTER ( LETTER | DIGIT | SPACE )*
            pass 
            self.mLETTER()
            # Deo.g:82:17: ( LETTER | DIGIT | SPACE )*
            while True: #loop1
                alt1 = 4
                LA1 = self.input.LA(1)
                if LA1 == 65 or LA1 == 66 or LA1 == 67 or LA1 == 68 or LA1 == 69 or LA1 == 70 or LA1 == 71 or LA1 == 72 or LA1 == 73 or LA1 == 74 or LA1 == 75 or LA1 == 76 or LA1 == 77 or LA1 == 78 or LA1 == 79 or LA1 == 80 or LA1 == 81 or LA1 == 82 or LA1 == 83 or LA1 == 84 or LA1 == 85 or LA1 == 86 or LA1 == 87 or LA1 == 88 or LA1 == 89 or LA1 == 90 or LA1 == 97 or LA1 == 98 or LA1 == 99 or LA1 == 100 or LA1 == 101 or LA1 == 102 or LA1 == 103 or LA1 == 104 or LA1 == 105 or LA1 == 106 or LA1 == 107 or LA1 == 108 or LA1 == 109 or LA1 == 110 or LA1 == 111 or LA1 == 112 or LA1 == 113 or LA1 == 114 or LA1 == 115 or LA1 == 116 or LA1 == 117 or LA1 == 118 or LA1 == 119 or LA1 == 120 or LA1 == 121 or LA1 == 122:
                    alt1 = 1
                elif LA1 == 48 or LA1 == 49 or LA1 == 50 or LA1 == 51 or LA1 == 52 or LA1 == 53 or LA1 == 54 or LA1 == 55 or LA1 == 56 or LA1 == 57:
                    alt1 = 2
                elif LA1 == 9 or LA1 == 32:
                    alt1 = 3

                if alt1 == 1:
                    # Deo.g:82:18: LETTER
                    pass 
                    self.mLETTER()


                elif alt1 == 2:
                    # Deo.g:82:27: DIGIT
                    pass 
                    self.mDIGIT()


                elif alt1 == 3:
                    # Deo.g:82:35: SPACE
                    pass 
                    self.mSPACE()


                else:
                    break #loop1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ACTION"



    # $ANTLR start "STATE"
    def mSTATE(self, ):

        try:
            _type = STATE
            _channel = DEFAULT_CHANNEL

            # Deo.g:83:7: ( LETTER ( LETTER | DIGIT | SPACE )* )
            # Deo.g:83:9: LETTER ( LETTER | DIGIT | SPACE )*
            pass 
            self.mLETTER()
            # Deo.g:83:16: ( LETTER | DIGIT | SPACE )*
            while True: #loop2
                alt2 = 4
                LA2 = self.input.LA(1)
                if LA2 == 65 or LA2 == 66 or LA2 == 67 or LA2 == 68 or LA2 == 69 or LA2 == 70 or LA2 == 71 or LA2 == 72 or LA2 == 73 or LA2 == 74 or LA2 == 75 or LA2 == 76 or LA2 == 77 or LA2 == 78 or LA2 == 79 or LA2 == 80 or LA2 == 81 or LA2 == 82 or LA2 == 83 or LA2 == 84 or LA2 == 85 or LA2 == 86 or LA2 == 87 or LA2 == 88 or LA2 == 89 or LA2 == 90 or LA2 == 97 or LA2 == 98 or LA2 == 99 or LA2 == 100 or LA2 == 101 or LA2 == 102 or LA2 == 103 or LA2 == 104 or LA2 == 105 or LA2 == 106 or LA2 == 107 or LA2 == 108 or LA2 == 109 or LA2 == 110 or LA2 == 111 or LA2 == 112 or LA2 == 113 or LA2 == 114 or LA2 == 115 or LA2 == 116 or LA2 == 117 or LA2 == 118 or LA2 == 119 or LA2 == 120 or LA2 == 121 or LA2 == 122:
                    alt2 = 1
                elif LA2 == 48 or LA2 == 49 or LA2 == 50 or LA2 == 51 or LA2 == 52 or LA2 == 53 or LA2 == 54 or LA2 == 55 or LA2 == 56 or LA2 == 57:
                    alt2 = 2
                elif LA2 == 9 or LA2 == 32:
                    alt2 = 3

                if alt2 == 1:
                    # Deo.g:83:17: LETTER
                    pass 
                    self.mLETTER()


                elif alt2 == 2:
                    # Deo.g:83:26: DIGIT
                    pass 
                    self.mDIGIT()


                elif alt2 == 3:
                    # Deo.g:83:34: SPACE
                    pass 
                    self.mSPACE()


                else:
                    break #loop2





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STATE"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # Deo.g:84:4: ( LETTER ( LETTER | DIGIT | '_' )* )
            # Deo.g:84:6: LETTER ( LETTER | DIGIT | '_' )*
            pass 
            self.mLETTER()
            # Deo.g:84:13: ( LETTER | DIGIT | '_' )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57) or (65 <= LA3_0 <= 90) or LA3_0 == 95 or (97 <= LA3_0 <= 122)) :
                    alt3 = 1


                if alt3 == 1:
                    # Deo.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "SPACE"
    def mSPACE(self, ):

        try:
            _type = SPACE
            _channel = DEFAULT_CHANNEL

            # Deo.g:86:7: ( ( ' ' | '\\t' )+ )
            # Deo.g:86:9: ( ' ' | '\\t' )+
            pass 
            # Deo.g:86:9: ( ' ' | '\\t' )+
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



    # $ANTLR start "EOL"
    def mEOL(self, ):

        try:
            _type = EOL
            _channel = DEFAULT_CHANNEL

            # Deo.g:87:5: ( ( '\\r' )? '\\n' )
            # Deo.g:87:7: ( '\\r' )? '\\n'
            pass 
            # Deo.g:87:7: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # Deo.g:87:7: '\\r'
                pass 
                self.match(13)



            self.match(10)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EOL"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # Deo.g:88:9: ( '#' (~ ( '\\r' | '\\n' ) )* ( '\\r' )? '\\n' )
            # Deo.g:88:11: '#' (~ ( '\\r' | '\\n' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(35)
            # Deo.g:88:15: (~ ( '\\r' | '\\n' ) )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((0 <= LA6_0 <= 9) or (11 <= LA6_0 <= 12) or (14 <= LA6_0 <= 65535)) :
                    alt6 = 1


                if alt6 == 1:
                    # Deo.g:88:15: ~ ( '\\r' | '\\n' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop6


            # Deo.g:88:31: ( '\\r' )?
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 13) :
                alt7 = 1
            if alt7 == 1:
                # Deo.g:88:31: '\\r'
                pass 
                self.match(13)



            self.match(10)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # Deo.g:90:17: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # Deo.g:91:17: ( '0' .. '9' )
            # Deo.g:91:19: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # Deo.g:1:8: ( OB | PRO | PER | IF | IFF | THEN | NOT | AND | OR | LB | RB | ASSN | ACTION | STATE | ID | SPACE | EOL | COMMENT )
        alt8 = 18
        alt8 = self.dfa8.predict(self.input)
        if alt8 == 1:
            # Deo.g:1:10: OB
            pass 
            self.mOB()


        elif alt8 == 2:
            # Deo.g:1:13: PRO
            pass 
            self.mPRO()


        elif alt8 == 3:
            # Deo.g:1:17: PER
            pass 
            self.mPER()


        elif alt8 == 4:
            # Deo.g:1:21: IF
            pass 
            self.mIF()


        elif alt8 == 5:
            # Deo.g:1:24: IFF
            pass 
            self.mIFF()


        elif alt8 == 6:
            # Deo.g:1:28: THEN
            pass 
            self.mTHEN()


        elif alt8 == 7:
            # Deo.g:1:33: NOT
            pass 
            self.mNOT()


        elif alt8 == 8:
            # Deo.g:1:37: AND
            pass 
            self.mAND()


        elif alt8 == 9:
            # Deo.g:1:41: OR
            pass 
            self.mOR()


        elif alt8 == 10:
            # Deo.g:1:44: LB
            pass 
            self.mLB()


        elif alt8 == 11:
            # Deo.g:1:47: RB
            pass 
            self.mRB()


        elif alt8 == 12:
            # Deo.g:1:50: ASSN
            pass 
            self.mASSN()


        elif alt8 == 13:
            # Deo.g:1:55: ACTION
            pass 
            self.mACTION()


        elif alt8 == 14:
            # Deo.g:1:62: STATE
            pass 
            self.mSTATE()


        elif alt8 == 15:
            # Deo.g:1:68: ID
            pass 
            self.mID()


        elif alt8 == 16:
            # Deo.g:1:71: SPACE
            pass 
            self.mSPACE()


        elif alt8 == 17:
            # Deo.g:1:77: EOL
            pass 
            self.mEOL()


        elif alt8 == 18:
            # Deo.g:1:81: COMMENT
            pass 
            self.mCOMMENT()







    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\1\uffff\5\17\3\uffff\1\17\3\uffff\1\17\1\32\1\uffff\2\17\1\uffff"
        u"\4\17\1\40\2\17\1\uffff\3\17\1\44\1\45\1\uffff\2\17\1\50\2\uffff"
        u"\2\17\1\uffff\31\17\1\106\3\17\1\uffff\2\17\1\114\1\17\1\116\1"
        u"\uffff\1\117\2\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\120\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\6\11\3\uffff\1\11\3\uffff\2\11\1\uffff\2\11\1\uffff\7\11\1\uffff"
        u"\5\11\1\uffff\3\11\2\uffff\2\11\1\uffff\35\11\1\uffff\5\11\1\uffff"
        u"\1\11\2\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\6\172\3\uffff\1\172\3\uffff\2\172\1\uffff\2\172\1\uffff\7\172"
        u"\1\uffff\5\172\1\uffff\3\172\2\uffff\2\172\1\uffff\35\172\1\uffff"
        u"\5\172\1\uffff\1\172\2\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\6\uffff\1\12\1\13\1\14\1\uffff\1\20\1\21\1\22\2\uffff\1\15\2\uffff"
        u"\1\17\7\uffff\1\4\5\uffff\1\11\3\uffff\1\7\1\10\2\uffff\1\6\35"
        u"\uffff\1\1\5\uffff\1\5\1\uffff\1\3\1\2"
        )

    DFA8_special = DFA.unpack(
        u"\120\uffff"
        )

            
    DFA8_transition = [
        DFA.unpack(u"\1\12\1\13\2\uffff\1\13\22\uffff\1\12\2\uffff\1\14\4"
        u"\uffff\1\6\1\7\23\uffff\1\10\3\uffff\32\11\6\uffff\1\4\7\11\1\1"
        u"\4\11\1\3\1\5\4\11\1\2\6\11"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\5\20\1\16\15\20\1\15\6\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\7\20\1\24\22\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\16\20\1\25\13\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\15\20\1\26\14\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\21\20\1\27\10\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\30\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u"\1\23\26\uffff\1\31\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\4\20\1\35\25\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\23\20\1\36\6\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\3\20\1\37\26\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\41\21\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\1\42\31\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\15\20\1\43\14\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\22\33\1\46\7\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\15\33\1\47\14\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\51\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\3\33\1\52\26\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\16\33\1\53\1\54\12\33"),
        DFA.unpack(u"\1\23\26\uffff\1\55\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\1\33\1\56\30\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\4\33\1\60\14\33\1\57\10\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\16\33\1\61\13\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\13\33\1\62\16\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\16\33\1\63\13\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\21\33\1\64\10\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\15\33\1\65\14\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\66\21\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\7\33\1\67\22\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\14\33\1\70\15\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\13\33\1\71\16\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\6\33\1\72\23\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\73\21\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\74\21\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\30\33\1\75\1\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\4\33\1\76\25\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\1\33\1\77\30\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\23\33\1\100\6\33"),
        DFA.unpack(u"\1\23\26\uffff\1\101\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\3\33\1\102\26\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\103\21\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\23\33\1\104\6\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\105\21\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\23\33\1\107\6\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\4\33\1\110\25\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\5\33\1\111\24\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\4\33\1\112\25\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\3\33\1\113\26\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\3\33\1\115\26\33"),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\23\26\uffff\1\23\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #8

    DFA8 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(DeoLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
