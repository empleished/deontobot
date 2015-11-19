# $ANTLR 3.1.2 Deo.g 2015-11-19 08:56:20

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
IFF=5
ASSN=14
RULE=9
RB=23
PER=17
LETTER=24
NOT=21
AND=19
ID=13
EOF=-1
SPACE=26
PRO=16
ACTION=18
OB=15
IF=4
AXIOM=10
PROG=11
EXPR=7
EOL=27
THEN=6
OR=20
LB=22
VAR=12
DIGIT=25
COMMENT=28
FACT=8


class DeoLexer(Lexer):

    grammarFileName = "Deo.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )






    # $ANTLR start "OB"
    def mOB(self, ):

        try:
            _type = OB
            _channel = DEFAULT_CHANNEL

            # Deo.g:65:4: ( 'it is obliged' )
            # Deo.g:65:6: 'it is obliged'
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

            # Deo.g:66:5: ( 'it is prohibited' )
            # Deo.g:66:7: 'it is prohibited'
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

            # Deo.g:67:5: ( 'it is permitted' )
            # Deo.g:67:7: 'it is permitted'
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

            # Deo.g:69:4: ( 'if' )
            # Deo.g:69:6: 'if'
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

            # Deo.g:70:5: ( 'if and only if' )
            # Deo.g:70:7: 'if and only if'
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

            # Deo.g:71:6: ( 'then' )
            # Deo.g:71:8: 'then'
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

            # Deo.g:72:5: ( 'not' )
            # Deo.g:72:7: 'not'
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

            # Deo.g:73:5: ( 'and' )
            # Deo.g:73:7: 'and'
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

            # Deo.g:74:4: ( 'or' )
            # Deo.g:74:6: 'or'
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

            # Deo.g:76:4: ( '(' )
            # Deo.g:76:6: '('
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

            # Deo.g:77:4: ( ')' )
            # Deo.g:77:6: ')'
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

            # Deo.g:79:6: ( '=' )
            # Deo.g:79:9: '='
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

            # Deo.g:81:8: ( LETTER ( LETTER | DIGIT | SPACE )* )
            # Deo.g:81:10: LETTER ( LETTER | DIGIT | SPACE )*
            pass 
            self.mLETTER()
            # Deo.g:81:17: ( LETTER | DIGIT | SPACE )*
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
                    # Deo.g:81:18: LETTER
                    pass 
                    self.mLETTER()


                elif alt1 == 2:
                    # Deo.g:81:27: DIGIT
                    pass 
                    self.mDIGIT()


                elif alt1 == 3:
                    # Deo.g:81:35: SPACE
                    pass 
                    self.mSPACE()


                else:
                    break #loop1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ACTION"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # Deo.g:82:4: ( LETTER ( LETTER | DIGIT | '_' )* )
            # Deo.g:82:6: LETTER ( LETTER | DIGIT | '_' )*
            pass 
            self.mLETTER()
            # Deo.g:82:13: ( LETTER | DIGIT | '_' )*
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



    # $ANTLR start "SPACE"
    def mSPACE(self, ):

        try:
            _type = SPACE
            _channel = DEFAULT_CHANNEL

            # Deo.g:84:7: ( ( ' ' | '\\t' )+ )
            # Deo.g:84:9: ( ' ' | '\\t' )+
            pass 
            # Deo.g:84:9: ( ' ' | '\\t' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 9 or LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # Deo.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1





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

            # Deo.g:85:5: ( ( '\\r' )? '\\n' )
            # Deo.g:85:7: ( '\\r' )? '\\n'
            pass 
            # Deo.g:85:7: ( '\\r' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 13) :
                alt4 = 1
            if alt4 == 1:
                # Deo.g:85:7: '\\r'
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

            # Deo.g:86:9: ( '#' (~ ( '\\r' | '\\n' ) )* ( '\\r' )? '\\n' )
            # Deo.g:86:11: '#' (~ ( '\\r' | '\\n' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(35)
            # Deo.g:86:15: (~ ( '\\r' | '\\n' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 9) or (11 <= LA5_0 <= 12) or (14 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # Deo.g:86:15: ~ ( '\\r' | '\\n' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5


            # Deo.g:86:31: ( '\\r' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 13) :
                alt6 = 1
            if alt6 == 1:
                # Deo.g:86:31: '\\r'
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
            # Deo.g:88:17: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # Deo.g:89:17: ( '0' .. '9' )
            # Deo.g:89:19: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # Deo.g:1:8: ( OB | PRO | PER | IF | IFF | THEN | NOT | AND | OR | LB | RB | ASSN | ACTION | ID | SPACE | EOL | COMMENT )
        alt7 = 17
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # Deo.g:1:10: OB
            pass 
            self.mOB()


        elif alt7 == 2:
            # Deo.g:1:13: PRO
            pass 
            self.mPRO()


        elif alt7 == 3:
            # Deo.g:1:17: PER
            pass 
            self.mPER()


        elif alt7 == 4:
            # Deo.g:1:21: IF
            pass 
            self.mIF()


        elif alt7 == 5:
            # Deo.g:1:24: IFF
            pass 
            self.mIFF()


        elif alt7 == 6:
            # Deo.g:1:28: THEN
            pass 
            self.mTHEN()


        elif alt7 == 7:
            # Deo.g:1:33: NOT
            pass 
            self.mNOT()


        elif alt7 == 8:
            # Deo.g:1:37: AND
            pass 
            self.mAND()


        elif alt7 == 9:
            # Deo.g:1:41: OR
            pass 
            self.mOR()


        elif alt7 == 10:
            # Deo.g:1:44: LB
            pass 
            self.mLB()


        elif alt7 == 11:
            # Deo.g:1:47: RB
            pass 
            self.mRB()


        elif alt7 == 12:
            # Deo.g:1:50: ASSN
            pass 
            self.mASSN()


        elif alt7 == 13:
            # Deo.g:1:55: ACTION
            pass 
            self.mACTION()


        elif alt7 == 14:
            # Deo.g:1:62: ID
            pass 
            self.mID()


        elif alt7 == 15:
            # Deo.g:1:65: SPACE
            pass 
            self.mSPACE()


        elif alt7 == 16:
            # Deo.g:1:71: EOL
            pass 
            self.mEOL()


        elif alt7 == 17:
            # Deo.g:1:75: COMMENT
            pass 
            self.mCOMMENT()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\1\uffff\5\17\3\uffff\1\17\3\uffff\1\17\1\31\1\uffff\2\17\1\uffff"
        u"\3\17\1\35\2\17\1\uffff\1\17\1\41\1\42\1\uffff\2\17\1\45\2\uffff"
        u"\2\17\1\uffff\31\17\1\103\3\17\1\uffff\2\17\1\111\1\17\1\113\1"
        u"\uffff\1\114\2\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\115\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\5\60\3\uffff\1\60\3\uffff\1\40\1\11\1\uffff\2\60\1\uffff"
        u"\3\60\1\11\1\151\1\141\1\uffff\1\60\2\11\1\uffff\1\163\1\156\1"
        u"\11\2\uffff\1\40\1\144\1\uffff\1\157\1\40\1\142\1\145\1\157\1\154"
        u"\1\157\1\162\1\156\1\151\1\150\1\155\1\154\1\147\2\151\1\171\1"
        u"\145\1\142\1\164\1\40\1\144\1\151\1\164\1\151\1\11\1\164\1\145"
        u"\1\146\1\uffff\1\145\1\144\1\11\1\144\1\11\1\uffff\1\11\2\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\6\172\3\uffff\1\172\3\uffff\2\172\1\uffff\2\172\1\uffff\4\172"
        u"\1\151\1\141\1\uffff\3\172\1\uffff\1\163\1\156\1\172\2\uffff\1"
        u"\40\1\144\1\uffff\1\160\1\40\1\142\1\162\1\157\1\154\1\157\1\162"
        u"\1\156\1\151\1\150\1\155\1\154\1\147\2\151\1\171\1\145\1\142\1"
        u"\164\1\40\1\144\1\151\1\164\1\151\1\172\1\164\1\145\1\146\1\uffff"
        u"\1\145\1\144\1\172\1\144\1\172\1\uffff\1\172\2\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\6\uffff\1\12\1\13\1\14\1\uffff\1\17\1\20\1\21\2\uffff\1\15\2\uffff"
        u"\1\16\6\uffff\1\4\3\uffff\1\11\3\uffff\1\7\1\10\2\uffff\1\6\35"
        u"\uffff\1\1\5\uffff\1\5\1\uffff\1\3\1\2"
        )

    DFA7_special = DFA.unpack(
        u"\115\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\12\1\13\2\uffff\1\13\22\uffff\1\12\2\uffff\1\14\4"
        u"\uffff\1\6\1\7\23\uffff\1\10\3\uffff\32\11\6\uffff\1\4\7\11\1\1"
        u"\4\11\1\3\1\5\4\11\1\2\6\11"),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\5\20\1\16"
        u"\15\20\1\15\6\20"),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\7\20\1\23"
        u"\22\20"),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\16\20\1\24"
        u"\13\20"),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\15\20\1\25"
        u"\14\20"),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\21\20\1\26"
        u"\10\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\27\17\uffff\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff"
        u"\32\20"),
        DFA.unpack(u"\1\17\26\uffff\1\30\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\4\20\1\32"
        u"\25\20"),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\23\20\1\33"
        u"\6\20"),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\3\20\1\34"
        u"\26\20"),
        DFA.unpack(u"\1\17\26\uffff\1\17\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\21\7\uffff\32\20\4\uffff\1\22\1\uffff\15\20\1\40"
        u"\14\20"),
        DFA.unpack(u"\1\17\26\uffff\1\17\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u"\1\17\26\uffff\1\17\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\17\26\uffff\1\17\17\uffff\12\21\7\uffff\32\20\4"
        u"\uffff\1\22\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\50\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\55\14\uffff\1\54"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\17\26\uffff\1\17\17\uffff\12\17\7\uffff\32\17\6"
        u"\uffff\32\17"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\17\26\uffff\1\17\17\uffff\12\17\7\uffff\32\17\6"
        u"\uffff\32\17"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\17\26\uffff\1\17\17\uffff\12\17\7\uffff\32\17\6"
        u"\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\17\26\uffff\1\17\17\uffff\12\17\7\uffff\32\17\6"
        u"\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    DFA7 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(DeoLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
