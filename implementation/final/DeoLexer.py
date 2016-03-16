# $ANTLR 3.5.2 Deo.g 2016-03-16 15:50:05

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
DECL=7
DIGIT=8
EOL=9
EXPR=10
FACT=11
GOAL=12
ID=13
IF=14
IFF=15
IFTHEN=16
INF=17
LB=18
LETTER=19
NOT=20
OB=21
OR=22
PER=23
PREF=24
PRO=25
PROG=26
RB=27
RULE=28
SPACE=29
TERM=30
THEN=31


class DeoLexer(Lexer):

    grammarFileName = "Deo.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(DeoLexer, self).__init__(input, state)

        self.delegates = []






    # $ANTLR start "OB"
    def mOB(self, ):
        try:
            _type = OB
            _channel = DEFAULT_CHANNEL

            # Deo.g:90:4: ( 'OB' )
            # Deo.g:90:6: 'OB'
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

            # Deo.g:91:5: ( 'PRO' )
            # Deo.g:91:7: 'PRO'
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

            # Deo.g:92:5: ( 'PER' )
            # Deo.g:92:7: 'PER'
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

            # Deo.g:94:4: ( 'if' )
            # Deo.g:94:6: 'if'
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

            # Deo.g:95:5: ( 'iff' )
            # Deo.g:95:7: 'iff'
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

            # Deo.g:96:6: ( 'then' )
            # Deo.g:96:8: 'then'
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

            # Deo.g:97:5: ( 'not' )
            # Deo.g:97:7: 'not'
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

            # Deo.g:98:5: ( 'and' )
            # Deo.g:98:7: 'and'
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

            # Deo.g:99:4: ( 'or' )
            # Deo.g:99:6: 'or'
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

            # Deo.g:101:9: ( 'term' )
            # Deo.g:101:11: 'term'
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

            # Deo.g:102:9: ( 'goal' )
            # Deo.g:102:11: 'goal'
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

            # Deo.g:103:9: ( 'rule' )
            # Deo.g:103:11: 'rule'
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

            # Deo.g:104:9: ( 'fact' )
            # Deo.g:104:11: 'fact'
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

            # Deo.g:106:4: ( '(' )
            # Deo.g:106:6: '('
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

            # Deo.g:107:4: ( ')' )
            # Deo.g:107:6: ')'
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

            # Deo.g:109:6: ( ': ' )
            # Deo.g:109:9: ': '
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

            # Deo.g:111:6: ( '\"' LETTER ( LETTER | DIGIT | ' ' )* '\"' )
            # Deo.g:111:8: '\"' LETTER ( LETTER | DIGIT | ' ' )* '\"'
            pass 
            self.match(34)

            self.mLETTER()


            # Deo.g:111:19: ( LETTER | DIGIT | ' ' )*
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

            # Deo.g:112:4: ( LETTER ( LETTER | DIGIT | '_' )* )
            # Deo.g:112:6: LETTER ( LETTER | DIGIT | '_' )*
            pass 
            self.mLETTER()


            # Deo.g:112:13: ( LETTER | DIGIT | '_' )*
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
            # Deo.g:114:18: ( 'a' .. 'z' | 'A' .. 'Z' )
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
            # Deo.g:115:18: ( '0' .. '9' )
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



    # $ANTLR start "EOL"
    def mEOL(self, ):
        try:
            _type = EOL
            _channel = DEFAULT_CHANNEL

            # Deo.g:117:9: ( ( '\\r' )? '\\n' )
            # Deo.g:117:11: ( '\\r' )? '\\n'
            pass 
            # Deo.g:117:11: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # Deo.g:117:11: '\\r'
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

            # Deo.g:118:9: ( ( '\\t' | ' ' )+ )
            # Deo.g:118:11: ( '\\t' | ' ' )+
            pass 
            # Deo.g:118:11: ( '\\t' | ' ' )+
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
        # Deo.g:1:8: ( OB | PRO | PER | IF | IFF | THEN | NOT | AND | OR | TERM | GOAL | RULE | FACT | LB | RB | ASSN | ATOM | ID | EOL | SPACE )
        alt5 = 20
        LA5 = self.input.LA(1)
        if LA5 == 79:
            LA5_1 = self.input.LA(2)

            if (LA5_1 == 66) :
                LA5_18 = self.input.LA(3)

                if ((48 <= LA5_18 <= 57) or (65 <= LA5_18 <= 90) or LA5_18 == 95 or (97 <= LA5_18 <= 122)) :
                    alt5 = 18
                else:
                    alt5 = 1

            else:
                alt5 = 18

        elif LA5 == 80:
            LA5 = self.input.LA(2)
            if LA5 == 82:
                LA5_19 = self.input.LA(3)

                if (LA5_19 == 79) :
                    LA5_31 = self.input.LA(4)

                    if ((48 <= LA5_31 <= 57) or (65 <= LA5_31 <= 90) or LA5_31 == 95 or (97 <= LA5_31 <= 122)) :
                        alt5 = 18
                    else:
                        alt5 = 2

                else:
                    alt5 = 18

            elif LA5 == 69:
                LA5_20 = self.input.LA(3)

                if (LA5_20 == 82) :
                    LA5_32 = self.input.LA(4)

                    if ((48 <= LA5_32 <= 57) or (65 <= LA5_32 <= 90) or LA5_32 == 95 or (97 <= LA5_32 <= 122)) :
                        alt5 = 18
                    else:
                        alt5 = 3

                else:
                    alt5 = 18

            else:
                alt5 = 18

        elif LA5 == 105:
            LA5_3 = self.input.LA(2)

            if (LA5_3 == 102) :
                LA5 = self.input.LA(3)
                if LA5 == 102:
                    LA5_33 = self.input.LA(4)

                    if ((48 <= LA5_33 <= 57) or (65 <= LA5_33 <= 90) or LA5_33 == 95 or (97 <= LA5_33 <= 122)) :
                        alt5 = 18
                    else:
                        alt5 = 5

                elif LA5 == 48 or LA5 == 49 or LA5 == 50 or LA5 == 51 or LA5 == 52 or LA5 == 53 or LA5 == 54 or LA5 == 55 or LA5 == 56 or LA5 == 57 or LA5 == 65 or LA5 == 66 or LA5 == 67 or LA5 == 68 or LA5 == 69 or LA5 == 70 or LA5 == 71 or LA5 == 72 or LA5 == 73 or LA5 == 74 or LA5 == 75 or LA5 == 76 or LA5 == 77 or LA5 == 78 or LA5 == 79 or LA5 == 80 or LA5 == 81 or LA5 == 82 or LA5 == 83 or LA5 == 84 or LA5 == 85 or LA5 == 86 or LA5 == 87 or LA5 == 88 or LA5 == 89 or LA5 == 90 or LA5 == 95 or LA5 == 97 or LA5 == 98 or LA5 == 99 or LA5 == 100 or LA5 == 101 or LA5 == 103 or LA5 == 104 or LA5 == 105 or LA5 == 106 or LA5 == 107 or LA5 == 108 or LA5 == 109 or LA5 == 110 or LA5 == 111 or LA5 == 112 or LA5 == 113 or LA5 == 114 or LA5 == 115 or LA5 == 116 or LA5 == 117 or LA5 == 118 or LA5 == 119 or LA5 == 120 or LA5 == 121 or LA5 == 122:
                    alt5 = 18
                else:
                    alt5 = 4

            else:
                alt5 = 18

        elif LA5 == 116:
            LA5 = self.input.LA(2)
            if LA5 == 104:
                LA5_22 = self.input.LA(3)

                if (LA5_22 == 101) :
                    LA5_35 = self.input.LA(4)

                    if (LA5_35 == 110) :
                        LA5_46 = self.input.LA(5)

                        if ((48 <= LA5_46 <= 57) or (65 <= LA5_46 <= 90) or LA5_46 == 95 or (97 <= LA5_46 <= 122)) :
                            alt5 = 18
                        else:
                            alt5 = 6

                    else:
                        alt5 = 18

                else:
                    alt5 = 18

            elif LA5 == 101:
                LA5_23 = self.input.LA(3)

                if (LA5_23 == 114) :
                    LA5_36 = self.input.LA(4)

                    if (LA5_36 == 109) :
                        LA5_47 = self.input.LA(5)

                        if ((48 <= LA5_47 <= 57) or (65 <= LA5_47 <= 90) or LA5_47 == 95 or (97 <= LA5_47 <= 122)) :
                            alt5 = 18
                        else:
                            alt5 = 10

                    else:
                        alt5 = 18

                else:
                    alt5 = 18

            else:
                alt5 = 18

        elif LA5 == 110:
            LA5_5 = self.input.LA(2)

            if (LA5_5 == 111) :
                LA5_24 = self.input.LA(3)

                if (LA5_24 == 116) :
                    LA5_37 = self.input.LA(4)

                    if ((48 <= LA5_37 <= 57) or (65 <= LA5_37 <= 90) or LA5_37 == 95 or (97 <= LA5_37 <= 122)) :
                        alt5 = 18
                    else:
                        alt5 = 7

                else:
                    alt5 = 18

            else:
                alt5 = 18

        elif LA5 == 97:
            LA5_6 = self.input.LA(2)

            if (LA5_6 == 110) :
                LA5_25 = self.input.LA(3)

                if (LA5_25 == 100) :
                    LA5_38 = self.input.LA(4)

                    if ((48 <= LA5_38 <= 57) or (65 <= LA5_38 <= 90) or LA5_38 == 95 or (97 <= LA5_38 <= 122)) :
                        alt5 = 18
                    else:
                        alt5 = 8

                else:
                    alt5 = 18

            else:
                alt5 = 18

        elif LA5 == 111:
            LA5_7 = self.input.LA(2)

            if (LA5_7 == 114) :
                LA5_26 = self.input.LA(3)

                if ((48 <= LA5_26 <= 57) or (65 <= LA5_26 <= 90) or LA5_26 == 95 or (97 <= LA5_26 <= 122)) :
                    alt5 = 18
                else:
                    alt5 = 9

            else:
                alt5 = 18

        elif LA5 == 103:
            LA5_8 = self.input.LA(2)

            if (LA5_8 == 111) :
                LA5_27 = self.input.LA(3)

                if (LA5_27 == 97) :
                    LA5_40 = self.input.LA(4)

                    if (LA5_40 == 108) :
                        LA5_50 = self.input.LA(5)

                        if ((48 <= LA5_50 <= 57) or (65 <= LA5_50 <= 90) or LA5_50 == 95 or (97 <= LA5_50 <= 122)) :
                            alt5 = 18
                        else:
                            alt5 = 11

                    else:
                        alt5 = 18

                else:
                    alt5 = 18

            else:
                alt5 = 18

        elif LA5 == 114:
            LA5_9 = self.input.LA(2)

            if (LA5_9 == 117) :
                LA5_28 = self.input.LA(3)

                if (LA5_28 == 108) :
                    LA5_41 = self.input.LA(4)

                    if (LA5_41 == 101) :
                        LA5_51 = self.input.LA(5)

                        if ((48 <= LA5_51 <= 57) or (65 <= LA5_51 <= 90) or LA5_51 == 95 or (97 <= LA5_51 <= 122)) :
                            alt5 = 18
                        else:
                            alt5 = 12

                    else:
                        alt5 = 18

                else:
                    alt5 = 18

            else:
                alt5 = 18

        elif LA5 == 102:
            LA5_10 = self.input.LA(2)

            if (LA5_10 == 97) :
                LA5_29 = self.input.LA(3)

                if (LA5_29 == 99) :
                    LA5_42 = self.input.LA(4)

                    if (LA5_42 == 116) :
                        LA5_52 = self.input.LA(5)

                        if ((48 <= LA5_52 <= 57) or (65 <= LA5_52 <= 90) or LA5_52 == 95 or (97 <= LA5_52 <= 122)) :
                            alt5 = 18
                        else:
                            alt5 = 13

                    else:
                        alt5 = 18

                else:
                    alt5 = 18

            else:
                alt5 = 18

        elif LA5 == 40:
            alt5 = 14
        elif LA5 == 41:
            alt5 = 15
        elif LA5 == 58:
            alt5 = 16
        elif LA5 == 34:
            alt5 = 17
        elif LA5 == 65 or LA5 == 66 or LA5 == 67 or LA5 == 68 or LA5 == 69 or LA5 == 70 or LA5 == 71 or LA5 == 72 or LA5 == 73 or LA5 == 74 or LA5 == 75 or LA5 == 76 or LA5 == 77 or LA5 == 78 or LA5 == 81 or LA5 == 82 or LA5 == 83 or LA5 == 84 or LA5 == 85 or LA5 == 86 or LA5 == 87 or LA5 == 88 or LA5 == 89 or LA5 == 90 or LA5 == 98 or LA5 == 99 or LA5 == 100 or LA5 == 101 or LA5 == 104 or LA5 == 106 or LA5 == 107 or LA5 == 108 or LA5 == 109 or LA5 == 112 or LA5 == 113 or LA5 == 115 or LA5 == 117 or LA5 == 118 or LA5 == 119 or LA5 == 120 or LA5 == 121 or LA5 == 122:
            alt5 = 18
        elif LA5 == 10 or LA5 == 13:
            alt5 = 19
        elif LA5 == 9 or LA5 == 32:
            alt5 = 20
        else:
            nvae = NoViableAltException("", 5, 0, self.input)

            raise nvae


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
            # Deo.g:1:24: IFF
            pass 
            self.mIFF()



        elif alt5 == 6:
            # Deo.g:1:28: THEN
            pass 
            self.mTHEN()



        elif alt5 == 7:
            # Deo.g:1:33: NOT
            pass 
            self.mNOT()



        elif alt5 == 8:
            # Deo.g:1:37: AND
            pass 
            self.mAND()



        elif alt5 == 9:
            # Deo.g:1:41: OR
            pass 
            self.mOR()



        elif alt5 == 10:
            # Deo.g:1:44: TERM
            pass 
            self.mTERM()



        elif alt5 == 11:
            # Deo.g:1:49: GOAL
            pass 
            self.mGOAL()



        elif alt5 == 12:
            # Deo.g:1:54: RULE
            pass 
            self.mRULE()



        elif alt5 == 13:
            # Deo.g:1:59: FACT
            pass 
            self.mFACT()



        elif alt5 == 14:
            # Deo.g:1:64: LB
            pass 
            self.mLB()



        elif alt5 == 15:
            # Deo.g:1:67: RB
            pass 
            self.mRB()



        elif alt5 == 16:
            # Deo.g:1:70: ASSN
            pass 
            self.mASSN()



        elif alt5 == 17:
            # Deo.g:1:75: ATOM
            pass 
            self.mATOM()



        elif alt5 == 18:
            # Deo.g:1:80: ID
            pass 
            self.mID()



        elif alt5 == 19:
            # Deo.g:1:83: EOL
            pass 
            self.mEOL()



        elif alt5 == 20:
            # Deo.g:1:87: SPACE
            pass 
            self.mSPACE()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(DeoLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
