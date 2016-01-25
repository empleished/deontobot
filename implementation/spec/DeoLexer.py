# $ANTLR 3.5.2 Deo.g 2016-01-25 15:39:11

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



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


class DeoLexer(Lexer):

    grammarFileName = "Deo.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(DeoLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa3 = self.DFA3(
            self, 3,
            eot = self.DFA3_eot,
            eof = self.DFA3_eof,
            min = self.DFA3_min,
            max = self.DFA3_max,
            accept = self.DFA3_accept,
            special = self.DFA3_special,
            transition = self.DFA3_transition
            )






    # $ANTLR start "OB"
    def mOB(self, ):
        try:
            _type = OB
            _channel = DEFAULT_CHANNEL

            # Deo.g:82:4: ( 'OB' )
            # Deo.g:82:6: 'OB'
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

            # Deo.g:83:5: ( 'PRO' )
            # Deo.g:83:7: 'PRO'
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

            # Deo.g:84:5: ( 'PER' )
            # Deo.g:84:7: 'PER'
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

            # Deo.g:86:4: ( 'if' )
            # Deo.g:86:6: 'if'
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

            # Deo.g:88:6: ( 'then' )
            # Deo.g:88:8: 'then'
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

            # Deo.g:89:5: ( 'not' )
            # Deo.g:89:7: 'not'
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

            # Deo.g:90:5: ( 'and' )
            # Deo.g:90:7: 'and'
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

            # Deo.g:91:4: ( 'or' )
            # Deo.g:91:6: 'or'
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

            # Deo.g:93:4: ( '(' )
            # Deo.g:93:6: '('
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

            # Deo.g:94:4: ( ')' )
            # Deo.g:94:6: ')'
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

            # Deo.g:96:6: ( ':' )
            # Deo.g:96:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ASSN"



    # $ANTLR start "EOL"
    def mEOL(self, ):
        try:
            _type = EOL
            _channel = DEFAULT_CHANNEL

            # Deo.g:98:6: ( '.' )
            # Deo.g:98:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EOL"



    # $ANTLR start "ATOM"
    def mATOM(self, ):
        try:
            _type = ATOM
            _channel = DEFAULT_CHANNEL

            # Deo.g:100:6: ( LETTER ( LETTER | DIGIT | ' ' )* )
            # Deo.g:100:8: LETTER ( LETTER | DIGIT | ' ' )*
            pass 
            self.mLETTER()


            # Deo.g:100:15: ( LETTER | DIGIT | ' ' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 32 or (48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # Deo.g:
                    pass 
                    if self.input.LA(1) == 32 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1




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

            # Deo.g:101:4: ( LETTER ( LETTER | DIGIT | '_' )* )
            # Deo.g:101:6: LETTER ( LETTER | DIGIT | '_' )*
            pass 
            self.mLETTER()


            # Deo.g:101:13: ( LETTER | DIGIT | '_' )*
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
            # Deo.g:103:18: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # Deo.g:104:18: ( '0' .. '9' )
            # Deo.g:
            pass 
            if (48 <= self.input.LA(1) <= 57):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "DIGIT"



    def mTokens(self):
        # Deo.g:1:8: ( OB | PRO | PER | IF | THEN | NOT | AND | OR | LB | RB | ASSN | EOL | ATOM | ID )
        alt3 = 14
        alt3 = self.dfa3.predict(self.input)
        if alt3 == 1:
            # Deo.g:1:10: OB
            pass 
            self.mOB()



        elif alt3 == 2:
            # Deo.g:1:13: PRO
            pass 
            self.mPRO()



        elif alt3 == 3:
            # Deo.g:1:17: PER
            pass 
            self.mPER()



        elif alt3 == 4:
            # Deo.g:1:21: IF
            pass 
            self.mIF()



        elif alt3 == 5:
            # Deo.g:1:24: THEN
            pass 
            self.mTHEN()



        elif alt3 == 6:
            # Deo.g:1:29: NOT
            pass 
            self.mNOT()



        elif alt3 == 7:
            # Deo.g:1:33: AND
            pass 
            self.mAND()



        elif alt3 == 8:
            # Deo.g:1:37: OR
            pass 
            self.mOR()



        elif alt3 == 9:
            # Deo.g:1:40: LB
            pass 
            self.mLB()



        elif alt3 == 10:
            # Deo.g:1:43: RB
            pass 
            self.mRB()



        elif alt3 == 11:
            # Deo.g:1:46: ASSN
            pass 
            self.mASSN()



        elif alt3 == 12:
            # Deo.g:1:51: EOL
            pass 
            self.mEOL()



        elif alt3 == 13:
            # Deo.g:1:55: ATOM
            pass 
            self.mATOM()



        elif alt3 == 14:
            # Deo.g:1:60: ID
            pass 
            self.mID()








    # lookup tables for DFA #3

    DFA3_eot = DFA.unpack(
        u"\1\uffff\7\16\4\uffff\1\16\1\30\1\uffff\1\16\1\uffff\2\16\1\33"
        u"\3\16\1\37\1\uffff\1\40\1\41\1\uffff\1\16\1\43\1\44\3\uffff\1\45"
        u"\3\uffff"
        )

    DFA3_eof = DFA.unpack(
        u"\46\uffff"
        )

    DFA3_min = DFA.unpack(
        u"\1\50\7\60\4\uffff\1\60\1\40\1\uffff\1\60\1\uffff\2\60\1\40\3\60"
        u"\1\40\1\uffff\2\40\1\uffff\1\60\2\40\3\uffff\1\40\3\uffff"
        )

    DFA3_max = DFA.unpack(
        u"\10\172\4\uffff\2\172\1\uffff\1\172\1\uffff\7\172\1\uffff\2\172"
        u"\1\uffff\3\172\3\uffff\1\172\3\uffff"
        )

    DFA3_accept = DFA.unpack(
        u"\10\uffff\1\11\1\12\1\13\1\14\2\uffff\1\15\1\uffff\1\16\7\uffff"
        u"\1\1\2\uffff\1\4\3\uffff\1\10\1\2\1\3\1\uffff\1\6\1\7\1\5"
        )

    DFA3_special = DFA.unpack(
        u"\46\uffff"
        )


    DFA3_transition = [
        DFA.unpack(u"\1\10\1\11\4\uffff\1\13\13\uffff\1\12\6\uffff\16\14"
        u"\1\1\1\2\12\14\6\uffff\1\6\7\14\1\3\4\14\1\5\1\7\4\14\1\4\6\14"),
        DFA.unpack(u"\12\17\7\uffff\1\17\1\15\30\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u"\12\17\7\uffff\4\17\1\22\14\17\1\21\10\17\4\uffff\1"
        u"\20\1\uffff\32\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\5\17\1\23"
        u"\24\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\7\17\1\24"
        u"\22\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\16\17\1\25"
        u"\13\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\15\17\1\26"
        u"\14\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\21\17\1\27"
        u"\10\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\32\17"),
        DFA.unpack(u"\1\16\17\uffff\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\7\uffff\16\17\1\31\13\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u"\12\17\7\uffff\21\17\1\32\10\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u"\1\16\17\uffff\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\4\17\1\34"
        u"\25\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\23\17\1\35"
        u"\6\17"),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\3\17\1\36"
        u"\26\17"),
        DFA.unpack(u"\1\16\17\uffff\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\16\17\uffff\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u"\1\16\17\uffff\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff\15\17\1\42"
        u"\14\17"),
        DFA.unpack(u"\1\16\17\uffff\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u"\1\16\17\uffff\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\16\17\uffff\12\17\7\uffff\32\17\4\uffff\1\20\1\uffff"
        u"\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #3

    class DFA3(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(DeoLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
