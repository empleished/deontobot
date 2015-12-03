# $ANTLR 3.5.2 Deo.g 2015-12-02 15:25:37

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


class DeoLexer(Lexer):

    grammarFileName = "Deo.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(DeoLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )






    # $ANTLR start "OB"
    def mOB(self, ):
        try:
            _type = OB
            _channel = DEFAULT_CHANNEL

            # Deo.g:73:4: ( 'OB' )
            # Deo.g:73:6: 'OB'
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

            # Deo.g:74:5: ( 'PRO' )
            # Deo.g:74:7: 'PRO'
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

            # Deo.g:75:5: ( 'PER' )
            # Deo.g:75:7: 'PER'
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

            # Deo.g:77:4: ( 'if' )
            # Deo.g:77:6: 'if'
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

            # Deo.g:78:5: ( 'iff' )
            # Deo.g:78:7: 'iff'
            pass 
            self.match("iff")




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

            # Deo.g:79:6: ( 'then' )
            # Deo.g:79:8: 'then'
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

            # Deo.g:80:5: ( 'not' )
            # Deo.g:80:7: 'not'
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

            # Deo.g:81:5: ( 'and' )
            # Deo.g:81:7: 'and'
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

            # Deo.g:82:4: ( 'or' )
            # Deo.g:82:6: 'or'
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

            # Deo.g:84:4: ( '(' )
            # Deo.g:84:6: '('
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

            # Deo.g:85:4: ( ')' )
            # Deo.g:85:6: ')'
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

            # Deo.g:87:6: ( ':' )
            # Deo.g:87:9: ':'
            pass 
            self.match(58)



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

            # Deo.g:89:6: ( LETTER ( LETTER | DIGIT | SPACE )* )
            # Deo.g:89:8: LETTER ( LETTER | DIGIT | SPACE )*
            pass 
            self.mLETTER()


            # Deo.g:89:15: ( LETTER | DIGIT | SPACE )*
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
                    # Deo.g:89:16: LETTER
                    pass 
                    self.mLETTER()



                elif alt1 == 2:
                    # Deo.g:89:25: DIGIT
                    pass 
                    self.mDIGIT()



                elif alt1 == 3:
                    # Deo.g:89:33: SPACE
                    pass 
                    self.mSPACE()



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

            # Deo.g:90:4: ( LETTER ( LETTER | DIGIT | '_' )* )
            # Deo.g:90:6: LETTER ( LETTER | DIGIT | '_' )*
            pass 
            self.mLETTER()


            # Deo.g:90:13: ( LETTER | DIGIT | '_' )*
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

            # Deo.g:92:7: ( ( ' ' | '\\t' )+ )
            # Deo.g:92:9: ( ' ' | '\\t' )+
            pass 
            # Deo.g:92:9: ( ' ' | '\\t' )+
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



    # $ANTLR start "EOF"
    def mEOF(self, ):
        try:
            _type = EOF
            _channel = DEFAULT_CHANNEL

            # Deo.g:93:5: ( '.' )
            # Deo.g:93:8: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EOF"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # Deo.g:94:10: ( '#' (~ ( '\\r' | '\\n' ) )* ( '\\r' )? '\\n' )
            # Deo.g:94:12: '#' (~ ( '\\r' | '\\n' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(35)

            # Deo.g:94:16: (~ ( '\\r' | '\\n' ) )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((0 <= LA4_0 <= 9) or (11 <= LA4_0 <= 12) or (14 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # Deo.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop4


            # Deo.g:94:32: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # Deo.g:94:32: '\\r'
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
            # Deo.g:96:18: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # Deo.g:97:18: ( '0' .. '9' )
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
        # Deo.g:1:8: ( OB | PRO | PER | IF | IFF | THEN | NOT | AND | OR | LB | RB | ASSN | ATOM | ID | SPACE | EOF | COMMENT )
        alt6 = 17
        alt6 = self.dfa6.predict(self.input)
        if alt6 == 1:
            # Deo.g:1:10: OB
            pass 
            self.mOB()



        elif alt6 == 2:
            # Deo.g:1:13: PRO
            pass 
            self.mPRO()



        elif alt6 == 3:
            # Deo.g:1:17: PER
            pass 
            self.mPER()



        elif alt6 == 4:
            # Deo.g:1:21: IF
            pass 
            self.mIF()



        elif alt6 == 5:
            # Deo.g:1:24: IFF
            pass 
            self.mIFF()



        elif alt6 == 6:
            # Deo.g:1:28: THEN
            pass 
            self.mTHEN()



        elif alt6 == 7:
            # Deo.g:1:33: NOT
            pass 
            self.mNOT()



        elif alt6 == 8:
            # Deo.g:1:37: AND
            pass 
            self.mAND()



        elif alt6 == 9:
            # Deo.g:1:41: OR
            pass 
            self.mOR()



        elif alt6 == 10:
            # Deo.g:1:44: LB
            pass 
            self.mLB()



        elif alt6 == 11:
            # Deo.g:1:47: RB
            pass 
            self.mRB()



        elif alt6 == 12:
            # Deo.g:1:50: ASSN
            pass 
            self.mASSN()



        elif alt6 == 13:
            # Deo.g:1:55: ATOM
            pass 
            self.mATOM()



        elif alt6 == 14:
            # Deo.g:1:60: ID
            pass 
            self.mID()



        elif alt6 == 15:
            # Deo.g:1:63: SPACE
            pass 
            self.mSPACE()



        elif alt6 == 16:
            # Deo.g:1:69: EOF
            pass 
            self.match(EOF)



        elif alt6 == 17:
            # Deo.g:1:73: COMMENT
            pass 
            self.mCOMMENT()








    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\1\uffff\7\20\3\uffff\1\20\3\uffff\1\33\1\uffff\2\20\1\uffff\2"
        u"\20\1\37\3\20\1\43\1\uffff\1\44\1\45\1\46\1\uffff\1\20\1\50\1\51"
        u"\4\uffff\1\52\3\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\53\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\11\7\60\3\uffff\1\60\3\uffff\1\11\1\uffff\2\60\1\uffff\2\60"
        u"\1\11\3\60\1\11\1\uffff\3\11\1\uffff\1\60\2\11\4\uffff\1\11\3\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\10\172\3\uffff\1\172\3\uffff\1\172\1\uffff\2\172\1\uffff\7\172"
        u"\1\uffff\3\172\1\uffff\3\172\4\uffff\1\172\3\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\10\uffff\1\12\1\13\1\14\1\uffff\1\17\1\20\1\21\1\uffff\1\15\2"
        u"\uffff\1\16\7\uffff\1\1\3\uffff\1\4\3\uffff\1\11\1\2\1\3\1\5\1"
        u"\uffff\1\7\1\10\1\6"
        )

    DFA6_special = DFA.unpack(
        u"\53\uffff"
        )


    DFA6_transition = [
        DFA.unpack(u"\1\14\26\uffff\1\14\2\uffff\1\16\4\uffff\1\10\1\11\4"
        u"\uffff\1\15\13\uffff\1\12\6\uffff\16\13\1\1\1\2\12\13\6\uffff\1"
        u"\6\7\13\1\3\4\13\1\5\1\7\4\13\1\4\6\13"),
        DFA.unpack(u"\12\22\7\uffff\1\21\1\17\30\21\4\uffff\1\23\1\uffff"
        u"\32\21"),
        DFA.unpack(u"\12\22\7\uffff\4\21\1\25\14\21\1\24\10\21\4\uffff\1"
        u"\23\1\uffff\32\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\5\21\1\26"
        u"\24\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\7\21\1\27"
        u"\22\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\16\21\1\30"
        u"\13\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\15\21\1\31"
        u"\14\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\21\21\1\32"
        u"\10\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\7\uffff\16\21\1\34\13\21\4\uffff\1\23\1\uffff"
        u"\32\21"),
        DFA.unpack(u"\12\22\7\uffff\21\21\1\35\10\21\4\uffff\1\23\1\uffff"
        u"\32\21"),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\5\21\1\36\24\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\4\21\1\40"
        u"\25\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\23\21\1\41"
        u"\6\21"),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\3\21\1\42"
        u"\26\21"),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\7\uffff\32\21\4\uffff\1\23\1\uffff\15\21\1\47"
        u"\14\21"),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\20\26\uffff\1\20\17\uffff\12\22\7\uffff\32\21\4"
        u"\uffff\1\23\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
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
