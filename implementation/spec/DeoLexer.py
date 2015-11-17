# $ANTLR 3.1.2 Deo.g 2015-11-17 17:47:05

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
RB=25
PER=17
LETTER=26
NOT=23
AND=21
ID=13
EOF=-1
SPACE=28
PRO=16
ACTION=18
OB=15
AXIOM=10
IF=4
PROG=11
EXPR=7
EOL=29
THEN=6
OR=22
AGENT=20
LB=24
VAR=12
DIGIT=27
COMMENT=30
FACT=8


class DeoLexer(Lexer):

    grammarFileName = "Deo.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )






    # $ANTLR start "OB"
    def mOB(self, ):

        try:
            _type = OB
            _channel = DEFAULT_CHANNEL

            # Deo.g:70:4: ( 'it is obliged' )
            # Deo.g:70:6: 'it is obliged'
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

            # Deo.g:71:5: ( 'it is prohibited' )
            # Deo.g:71:7: 'it is prohibited'
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

            # Deo.g:72:5: ( 'it is permitted' )
            # Deo.g:72:7: 'it is permitted'
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

            # Deo.g:74:4: ( 'if' )
            # Deo.g:74:6: 'if'
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

            # Deo.g:75:5: ( 'if and only if' )
            # Deo.g:75:7: 'if and only if'
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

            # Deo.g:76:6: ( 'then' )
            # Deo.g:76:8: 'then'
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

            # Deo.g:77:5: ( 'not' )
            # Deo.g:77:7: 'not'
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

            # Deo.g:78:5: ( 'and' )
            # Deo.g:78:7: 'and'
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

            # Deo.g:79:4: ( 'or' )
            # Deo.g:79:6: 'or'
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

            # Deo.g:81:4: ( '(' )
            # Deo.g:81:6: '('
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

            # Deo.g:82:4: ( ')' )
            # Deo.g:82:6: ')'
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

            # Deo.g:84:6: ( '=' )
            # Deo.g:84:9: '='
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

            # Deo.g:86:8: ( LETTER ( LETTER | DIGIT | SPACE )* )
            # Deo.g:86:10: LETTER ( LETTER | DIGIT | SPACE )*
            pass 
            self.mLETTER()
            # Deo.g:86:17: ( LETTER | DIGIT | SPACE )*
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
                    # Deo.g:86:18: LETTER
                    pass 
                    self.mLETTER()


                elif alt1 == 2:
                    # Deo.g:86:27: DIGIT
                    pass 
                    self.mDIGIT()


                elif alt1 == 3:
                    # Deo.g:86:35: SPACE
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

            # Deo.g:87:7: ( LETTER ( LETTER | DIGIT | SPACE )* )
            # Deo.g:87:9: LETTER ( LETTER | DIGIT | SPACE )*
            pass 
            self.mLETTER()
            # Deo.g:87:16: ( LETTER | DIGIT | SPACE )*
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
                    # Deo.g:87:17: LETTER
                    pass 
                    self.mLETTER()


                elif alt2 == 2:
                    # Deo.g:87:26: DIGIT
                    pass 
                    self.mDIGIT()


                elif alt2 == 3:
                    # Deo.g:87:34: SPACE
                    pass 
                    self.mSPACE()


                else:
                    break #loop2





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STATE"



    # $ANTLR start "AGENT"
    def mAGENT(self, ):

        try:
            _type = AGENT
            _channel = DEFAULT_CHANNEL

            # Deo.g:88:8: ( LETTER ( LETTER | DIGIT | SPACE )* )
            # Deo.g:88:10: LETTER ( LETTER | DIGIT | SPACE )*
            pass 
            self.mLETTER()
            # Deo.g:88:17: ( LETTER | DIGIT | SPACE )*
            while True: #loop3
                alt3 = 4
                LA3 = self.input.LA(1)
                if LA3 == 65 or LA3 == 66 or LA3 == 67 or LA3 == 68 or LA3 == 69 or LA3 == 70 or LA3 == 71 or LA3 == 72 or LA3 == 73 or LA3 == 74 or LA3 == 75 or LA3 == 76 or LA3 == 77 or LA3 == 78 or LA3 == 79 or LA3 == 80 or LA3 == 81 or LA3 == 82 or LA3 == 83 or LA3 == 84 or LA3 == 85 or LA3 == 86 or LA3 == 87 or LA3 == 88 or LA3 == 89 or LA3 == 90 or LA3 == 97 or LA3 == 98 or LA3 == 99 or LA3 == 100 or LA3 == 101 or LA3 == 102 or LA3 == 103 or LA3 == 104 or LA3 == 105 or LA3 == 106 or LA3 == 107 or LA3 == 108 or LA3 == 109 or LA3 == 110 or LA3 == 111 or LA3 == 112 or LA3 == 113 or LA3 == 114 or LA3 == 115 or LA3 == 116 or LA3 == 117 or LA3 == 118 or LA3 == 119 or LA3 == 120 or LA3 == 121 or LA3 == 122:
                    alt3 = 1
                elif LA3 == 48 or LA3 == 49 or LA3 == 50 or LA3 == 51 or LA3 == 52 or LA3 == 53 or LA3 == 54 or LA3 == 55 or LA3 == 56 or LA3 == 57:
                    alt3 = 2
                elif LA3 == 9 or LA3 == 32:
                    alt3 = 3

                if alt3 == 1:
                    # Deo.g:88:18: LETTER
                    pass 
                    self.mLETTER()


                elif alt3 == 2:
                    # Deo.g:88:27: DIGIT
                    pass 
                    self.mDIGIT()


                elif alt3 == 3:
                    # Deo.g:88:35: SPACE
                    pass 
                    self.mSPACE()


                else:
                    break #loop3





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AGENT"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # Deo.g:89:4: ( LETTER ( LETTER | DIGIT | '_' )* )
            # Deo.g:89:6: LETTER ( LETTER | DIGIT | '_' )*
            pass 
            self.mLETTER()
            # Deo.g:89:13: ( LETTER | DIGIT | '_' )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57) or (65 <= LA4_0 <= 90) or LA4_0 == 95 or (97 <= LA4_0 <= 122)) :
                    alt4 = 1


                if alt4 == 1:
                    # Deo.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop4





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

            # Deo.g:91:7: ( ( ' ' | '\\t' )+ )
            # Deo.g:91:9: ( ' ' | '\\t' )+
            pass 
            # Deo.g:91:9: ( ' ' | '\\t' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 9 or LA5_0 == 32) :
                    alt5 = 1


                if alt5 == 1:
                    # Deo.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1





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

            # Deo.g:92:5: ( ( '\\r' )? '\\n' )
            # Deo.g:92:7: ( '\\r' )? '\\n'
            pass 
            # Deo.g:92:7: ( '\\r' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 13) :
                alt6 = 1
            if alt6 == 1:
                # Deo.g:92:7: '\\r'
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

            # Deo.g:93:9: ( '#' (~ ( '\\r' | '\\n' ) )* ( '\\r' )? '\\n' )
            # Deo.g:93:11: '#' (~ ( '\\r' | '\\n' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(35)
            # Deo.g:93:15: (~ ( '\\r' | '\\n' ) )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((0 <= LA7_0 <= 9) or (11 <= LA7_0 <= 12) or (14 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # Deo.g:93:15: ~ ( '\\r' | '\\n' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7


            # Deo.g:93:31: ( '\\r' )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 13) :
                alt8 = 1
            if alt8 == 1:
                # Deo.g:93:31: '\\r'
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
            # Deo.g:95:17: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # Deo.g:96:17: ( '0' .. '9' )
            # Deo.g:96:19: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # Deo.g:1:8: ( OB | PRO | PER | IF | IFF | THEN | NOT | AND | OR | LB | RB | ASSN | ACTION | STATE | AGENT | ID | SPACE | EOL | COMMENT )
        alt9 = 19
        alt9 = self.dfa9.predict(self.input)
        if alt9 == 1:
            # Deo.g:1:10: OB
            pass 
            self.mOB()


        elif alt9 == 2:
            # Deo.g:1:13: PRO
            pass 
            self.mPRO()


        elif alt9 == 3:
            # Deo.g:1:17: PER
            pass 
            self.mPER()


        elif alt9 == 4:
            # Deo.g:1:21: IF
            pass 
            self.mIF()


        elif alt9 == 5:
            # Deo.g:1:24: IFF
            pass 
            self.mIFF()


        elif alt9 == 6:
            # Deo.g:1:28: THEN
            pass 
            self.mTHEN()


        elif alt9 == 7:
            # Deo.g:1:33: NOT
            pass 
            self.mNOT()


        elif alt9 == 8:
            # Deo.g:1:37: AND
            pass 
            self.mAND()


        elif alt9 == 9:
            # Deo.g:1:41: OR
            pass 
            self.mOR()


        elif alt9 == 10:
            # Deo.g:1:44: LB
            pass 
            self.mLB()


        elif alt9 == 11:
            # Deo.g:1:47: RB
            pass 
            self.mRB()


        elif alt9 == 12:
            # Deo.g:1:50: ASSN
            pass 
            self.mASSN()


        elif alt9 == 13:
            # Deo.g:1:55: ACTION
            pass 
            self.mACTION()


        elif alt9 == 14:
            # Deo.g:1:62: STATE
            pass 
            self.mSTATE()


        elif alt9 == 15:
            # Deo.g:1:68: AGENT
            pass 
            self.mAGENT()


        elif alt9 == 16:
            # Deo.g:1:74: ID
            pass 
            self.mID()


        elif alt9 == 17:
            # Deo.g:1:77: SPACE
            pass 
            self.mSPACE()


        elif alt9 == 18:
            # Deo.g:1:83: EOL
            pass 
            self.mEOL()


        elif alt9 == 19:
            # Deo.g:1:87: COMMENT
            pass 
            self.mCOMMENT()







    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\1\uffff\5\17\3\uffff\1\17\3\uffff\1\17\1\32\1\uffff\3\17\1\uffff"
        u"\3\17\1\40\2\17\1\uffff\3\17\1\44\1\45\1\uffff\2\17\1\50\2\uffff"
        u"\2\17\1\uffff\31\17\1\106\3\17\1\uffff\2\17\1\114\1\17\1\116\1"
        u"\uffff\1\117\2\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\120\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\6\11\3\uffff\1\11\3\uffff\2\11\1\uffff\3\11\1\uffff\6\11\1\uffff"
        u"\5\11\1\uffff\3\11\2\uffff\2\11\1\uffff\35\11\1\uffff\5\11\1\uffff"
        u"\1\11\2\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\6\172\3\uffff\1\172\3\uffff\2\172\1\uffff\3\172\1\uffff\6\172"
        u"\1\uffff\5\172\1\uffff\3\172\2\uffff\2\172\1\uffff\35\172\1\uffff"
        u"\5\172\1\uffff\1\172\2\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\6\uffff\1\12\1\13\1\14\1\uffff\1\21\1\22\1\23\2\uffff\1\15\3\uffff"
        u"\1\20\6\uffff\1\4\5\uffff\1\11\3\uffff\1\7\1\10\2\uffff\1\6\35"
        u"\uffff\1\1\5\uffff\1\5\1\uffff\1\3\1\2"
        )

    DFA9_special = DFA.unpack(
        u"\120\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\12\1\13\2\uffff\1\13\22\uffff\1\12\2\uffff\1\14\4"
        u"\uffff\1\6\1\7\23\uffff\1\10\3\uffff\32\11\6\uffff\1\4\7\11\1\1"
        u"\4\11\1\3\1\5\4\11\1\2\6\11"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\5\20\1\16\15\20\1\15\6\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\7\20\1\24\22\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\16\20\1\25\13\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\15\20\1\26\14\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\21\20\1\27\10\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\30\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u"\1\22\26\uffff\1\31\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\4\20\1\35\25\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\23\20\1\36\6\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\3\20\1\37\26\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\41\21\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\1\42\31\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\15\20\1\43\14\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\22\33\1\46\7\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\15\33\1\47\14\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\23\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\51\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\3\33\1\52\26\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\16\33\1\53\1\54\12\33"),
        DFA.unpack(u"\1\22\26\uffff\1\55\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\1\33\1\56\30\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\4\33\1\60\14\33\1\57\10\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\16\33\1\61\13\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\13\33\1\62\16\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\16\33\1\63\13\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\21\33\1\64\10\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\15\33\1\65\14\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\66\21\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\7\33\1\67\22\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\14\33\1\70\15\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\13\33\1\71\16\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\6\33\1\72\23\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\73\21\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\74\21\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\30\33\1\75\1\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\4\33\1\76\25\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\1\33\1\77\30\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\23\33\1\100\6\33"),
        DFA.unpack(u"\1\22\26\uffff\1\101\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\3\33\1\102\26\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\103\21\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\23\33\1\104\6\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\10\33\1\105\21\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\23\33\1\107\6\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\4\33\1\110\25\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\5\33\1\111\24\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\4\33\1\112\25\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\3\33\1\113\26\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\3\33\1\115\26\33"),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\22\26\uffff\1\22\17\uffff\12\34\7\uffff\32\33\6"
        u"\uffff\32\33"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    DFA9 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(DeoLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
