# Generated from ModScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,97,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,53,8,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,4,5,62,8,5,11,5,12,5,63,1,6,1,6,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,5,7,75,8,7,10,7,12,7,78,9,7,1,7,3,7,81,8,7,1,8,1,8,1,8,1,
        8,1,8,1,8,3,8,89,8,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,0,0,11,0,2,
        4,6,8,10,12,14,16,18,20,0,1,1,0,7,11,93,0,23,1,0,0,0,2,32,1,0,0,
        0,4,34,1,0,0,0,6,52,1,0,0,0,8,54,1,0,0,0,10,61,1,0,0,0,12,65,1,0,
        0,0,14,71,1,0,0,0,16,88,1,0,0,0,18,90,1,0,0,0,20,92,1,0,0,0,22,24,
        3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,
        26,27,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,33,3,4,2,0,30,33,3,6,
        3,0,31,33,3,8,4,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,
        1,0,0,0,34,35,5,2,0,0,35,36,5,7,0,0,36,37,5,12,0,0,37,38,3,14,7,
        0,38,39,5,13,0,0,39,5,1,0,0,0,40,41,5,3,0,0,41,42,5,7,0,0,42,43,
        5,12,0,0,43,44,3,14,7,0,44,45,5,13,0,0,45,53,1,0,0,0,46,47,5,4,0,
        0,47,48,5,7,0,0,48,49,5,12,0,0,49,50,3,14,7,0,50,51,5,13,0,0,51,
        53,1,0,0,0,52,40,1,0,0,0,52,46,1,0,0,0,53,7,1,0,0,0,54,55,5,5,0,
        0,55,56,5,7,0,0,56,57,5,12,0,0,57,58,3,10,5,0,58,59,5,13,0,0,59,
        9,1,0,0,0,60,62,3,12,6,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,
        0,63,64,1,0,0,0,64,11,1,0,0,0,65,66,5,6,0,0,66,67,5,7,0,0,67,68,
        5,12,0,0,68,69,3,14,7,0,69,70,5,13,0,0,70,13,1,0,0,0,71,76,3,16,
        8,0,72,73,5,14,0,0,73,75,3,16,8,0,74,72,1,0,0,0,75,78,1,0,0,0,76,
        74,1,0,0,0,76,77,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,79,81,5,14,
        0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,15,1,0,0,0,82,83,5,7,0,0,83,84,
        5,15,0,0,84,89,3,18,9,0,85,86,5,1,0,0,86,87,5,15,0,0,87,89,3,20,
        10,0,88,82,1,0,0,0,88,85,1,0,0,0,89,17,1,0,0,0,90,91,7,0,0,0,91,
        19,1,0,0,0,92,93,5,7,0,0,93,94,5,16,0,0,94,95,3,18,9,0,95,21,1,0,
        0,0,7,25,32,52,63,76,80,88
    ]

class ModScriptParser ( Parser ):

    grammarFileName = "ModScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'condition'", "'item'", "'boss'", "'phase'", 
                     "'loot'", "'drop'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "KW_ITEM", "KW_BOSS", "KW_PHASE", 
                      "KW_LOOT", "KW_DROP", "ID", "NUMBER", "PERCENTAGE", 
                      "STRING", "TIME_LITERAL", "LBRACE", "RBRACE", "SEMI", 
                      "COLON", "OP_REL", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_itemDecl = 2
    RULE_bossDecl = 3
    RULE_lootDecl = 4
    RULE_dropList = 5
    RULE_dropDecl = 6
    RULE_attrList = 7
    RULE_attr = 8
    RULE_value = 9
    RULE_condition = 10

    ruleNames =  [ "program", "declaration", "itemDecl", "bossDecl", "lootDecl", 
                   "dropList", "dropDecl", "attrList", "attr", "value", 
                   "condition" ]

    EOF = Token.EOF
    T__0=1
    KW_ITEM=2
    KW_BOSS=3
    KW_PHASE=4
    KW_LOOT=5
    KW_DROP=6
    ID=7
    NUMBER=8
    PERCENTAGE=9
    STRING=10
    TIME_LITERAL=11
    LBRACE=12
    RBRACE=13
    SEMI=14
    COLON=15
    OP_REL=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ModScriptParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ModScriptParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ModScriptParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ModScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ModScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.declaration()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                    break

            self.state = 27
            self.match(ModScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def itemDecl(self):
            return self.getTypedRuleContext(ModScriptParser.ItemDeclContext,0)


        def bossDecl(self):
            return self.getTypedRuleContext(ModScriptParser.BossDeclContext,0)


        def lootDecl(self):
            return self.getTypedRuleContext(ModScriptParser.LootDeclContext,0)


        def getRuleIndex(self):
            return ModScriptParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ModScriptParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.itemDecl()
                pass
            elif token in [3, 4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.bossDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.lootDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ITEM(self):
            return self.getToken(ModScriptParser.KW_ITEM, 0)

        def ID(self):
            return self.getToken(ModScriptParser.ID, 0)

        def LBRACE(self):
            return self.getToken(ModScriptParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(ModScriptParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(ModScriptParser.RBRACE, 0)

        def getRuleIndex(self):
            return ModScriptParser.RULE_itemDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemDecl" ):
                listener.enterItemDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemDecl" ):
                listener.exitItemDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemDecl" ):
                return visitor.visitItemDecl(self)
            else:
                return visitor.visitChildren(self)




    def itemDecl(self):

        localctx = ModScriptParser.ItemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_itemDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ModScriptParser.KW_ITEM)
            self.state = 35
            self.match(ModScriptParser.ID)
            self.state = 36
            self.match(ModScriptParser.LBRACE)
            self.state = 37
            self.attrList()
            self.state = 38
            self.match(ModScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BossDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BOSS(self):
            return self.getToken(ModScriptParser.KW_BOSS, 0)

        def ID(self):
            return self.getToken(ModScriptParser.ID, 0)

        def LBRACE(self):
            return self.getToken(ModScriptParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(ModScriptParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(ModScriptParser.RBRACE, 0)

        def KW_PHASE(self):
            return self.getToken(ModScriptParser.KW_PHASE, 0)

        def getRuleIndex(self):
            return ModScriptParser.RULE_bossDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBossDecl" ):
                listener.enterBossDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBossDecl" ):
                listener.exitBossDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBossDecl" ):
                return visitor.visitBossDecl(self)
            else:
                return visitor.visitChildren(self)




    def bossDecl(self):

        localctx = ModScriptParser.BossDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bossDecl)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(ModScriptParser.KW_BOSS)
                self.state = 41
                self.match(ModScriptParser.ID)
                self.state = 42
                self.match(ModScriptParser.LBRACE)
                self.state = 43
                self.attrList()
                self.state = 44
                self.match(ModScriptParser.RBRACE)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(ModScriptParser.KW_PHASE)
                self.state = 47
                self.match(ModScriptParser.ID)
                self.state = 48
                self.match(ModScriptParser.LBRACE)
                self.state = 49
                self.attrList()
                self.state = 50
                self.match(ModScriptParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LootDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LOOT(self):
            return self.getToken(ModScriptParser.KW_LOOT, 0)

        def ID(self):
            return self.getToken(ModScriptParser.ID, 0)

        def LBRACE(self):
            return self.getToken(ModScriptParser.LBRACE, 0)

        def dropList(self):
            return self.getTypedRuleContext(ModScriptParser.DropListContext,0)


        def RBRACE(self):
            return self.getToken(ModScriptParser.RBRACE, 0)

        def getRuleIndex(self):
            return ModScriptParser.RULE_lootDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLootDecl" ):
                listener.enterLootDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLootDecl" ):
                listener.exitLootDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLootDecl" ):
                return visitor.visitLootDecl(self)
            else:
                return visitor.visitChildren(self)




    def lootDecl(self):

        localctx = ModScriptParser.LootDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lootDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ModScriptParser.KW_LOOT)
            self.state = 55
            self.match(ModScriptParser.ID)
            self.state = 56
            self.match(ModScriptParser.LBRACE)
            self.state = 57
            self.dropList()
            self.state = 58
            self.match(ModScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dropDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ModScriptParser.DropDeclContext)
            else:
                return self.getTypedRuleContext(ModScriptParser.DropDeclContext,i)


        def getRuleIndex(self):
            return ModScriptParser.RULE_dropList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropList" ):
                listener.enterDropList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropList" ):
                listener.exitDropList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropList" ):
                return visitor.visitDropList(self)
            else:
                return visitor.visitChildren(self)




    def dropList(self):

        localctx = ModScriptParser.DropListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dropList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.dropDecl()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DROP(self):
            return self.getToken(ModScriptParser.KW_DROP, 0)

        def ID(self):
            return self.getToken(ModScriptParser.ID, 0)

        def LBRACE(self):
            return self.getToken(ModScriptParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(ModScriptParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(ModScriptParser.RBRACE, 0)

        def getRuleIndex(self):
            return ModScriptParser.RULE_dropDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropDecl" ):
                listener.enterDropDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropDecl" ):
                listener.exitDropDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropDecl" ):
                return visitor.visitDropDecl(self)
            else:
                return visitor.visitChildren(self)




    def dropDecl(self):

        localctx = ModScriptParser.DropDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dropDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ModScriptParser.KW_DROP)
            self.state = 66
            self.match(ModScriptParser.ID)
            self.state = 67
            self.match(ModScriptParser.LBRACE)
            self.state = 68
            self.attrList()
            self.state = 69
            self.match(ModScriptParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ModScriptParser.AttrContext)
            else:
                return self.getTypedRuleContext(ModScriptParser.AttrContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ModScriptParser.SEMI)
            else:
                return self.getToken(ModScriptParser.SEMI, i)

        def getRuleIndex(self):
            return ModScriptParser.RULE_attrList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrList" ):
                listener.enterAttrList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrList" ):
                listener.exitAttrList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrList" ):
                return visitor.visitAttrList(self)
            else:
                return visitor.visitChildren(self)




    def attrList(self):

        localctx = ModScriptParser.AttrListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.attr()
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72
                    self.match(ModScriptParser.SEMI)
                    self.state = 73
                    self.attr() 
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 79
                self.match(ModScriptParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ModScriptParser.ID, 0)

        def COLON(self):
            return self.getToken(ModScriptParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(ModScriptParser.ValueContext,0)


        def condition(self):
            return self.getTypedRuleContext(ModScriptParser.ConditionContext,0)


        def getRuleIndex(self):
            return ModScriptParser.RULE_attr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr" ):
                listener.enterAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr" ):
                listener.exitAttr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)




    def attr(self):

        localctx = ModScriptParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(ModScriptParser.ID)
                self.state = 83
                self.match(ModScriptParser.COLON)
                self.state = 84
                self.value()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(ModScriptParser.T__0)
                self.state = 86
                self.match(ModScriptParser.COLON)
                self.state = 87
                self.condition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ModScriptParser.ID, 0)

        def NUMBER(self):
            return self.getToken(ModScriptParser.NUMBER, 0)

        def PERCENTAGE(self):
            return self.getToken(ModScriptParser.PERCENTAGE, 0)

        def STRING(self):
            return self.getToken(ModScriptParser.STRING, 0)

        def TIME_LITERAL(self):
            return self.getToken(ModScriptParser.TIME_LITERAL, 0)

        def getRuleIndex(self):
            return ModScriptParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ModScriptParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3968) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ModScriptParser.ID, 0)

        def OP_REL(self):
            return self.getToken(ModScriptParser.OP_REL, 0)

        def value(self):
            return self.getTypedRuleContext(ModScriptParser.ValueContext,0)


        def getRuleIndex(self):
            return ModScriptParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = ModScriptParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(ModScriptParser.ID)
            self.state = 93
            self.match(ModScriptParser.OP_REL)
            self.state = 94
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





