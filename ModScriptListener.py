# Generated from ModScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ModScriptParser import ModScriptParser
else:
    from ModScriptParser import ModScriptParser

# This class defines a complete listener for a parse tree produced by ModScriptParser.
class ModScriptListener(ParseTreeListener):

    # Enter a parse tree produced by ModScriptParser#program.
    def enterProgram(self, ctx:ModScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by ModScriptParser#program.
    def exitProgram(self, ctx:ModScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by ModScriptParser#declaration.
    def enterDeclaration(self, ctx:ModScriptParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ModScriptParser#declaration.
    def exitDeclaration(self, ctx:ModScriptParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ModScriptParser#itemDecl.
    def enterItemDecl(self, ctx:ModScriptParser.ItemDeclContext):
        pass

    # Exit a parse tree produced by ModScriptParser#itemDecl.
    def exitItemDecl(self, ctx:ModScriptParser.ItemDeclContext):
        pass


    # Enter a parse tree produced by ModScriptParser#bossDecl.
    def enterBossDecl(self, ctx:ModScriptParser.BossDeclContext):
        pass

    # Exit a parse tree produced by ModScriptParser#bossDecl.
    def exitBossDecl(self, ctx:ModScriptParser.BossDeclContext):
        pass


    # Enter a parse tree produced by ModScriptParser#lootDecl.
    def enterLootDecl(self, ctx:ModScriptParser.LootDeclContext):
        pass

    # Exit a parse tree produced by ModScriptParser#lootDecl.
    def exitLootDecl(self, ctx:ModScriptParser.LootDeclContext):
        pass


    # Enter a parse tree produced by ModScriptParser#dropList.
    def enterDropList(self, ctx:ModScriptParser.DropListContext):
        pass

    # Exit a parse tree produced by ModScriptParser#dropList.
    def exitDropList(self, ctx:ModScriptParser.DropListContext):
        pass


    # Enter a parse tree produced by ModScriptParser#dropDecl.
    def enterDropDecl(self, ctx:ModScriptParser.DropDeclContext):
        pass

    # Exit a parse tree produced by ModScriptParser#dropDecl.
    def exitDropDecl(self, ctx:ModScriptParser.DropDeclContext):
        pass


    # Enter a parse tree produced by ModScriptParser#attrList.
    def enterAttrList(self, ctx:ModScriptParser.AttrListContext):
        pass

    # Exit a parse tree produced by ModScriptParser#attrList.
    def exitAttrList(self, ctx:ModScriptParser.AttrListContext):
        pass


    # Enter a parse tree produced by ModScriptParser#attr.
    def enterAttr(self, ctx:ModScriptParser.AttrContext):
        pass

    # Exit a parse tree produced by ModScriptParser#attr.
    def exitAttr(self, ctx:ModScriptParser.AttrContext):
        pass


    # Enter a parse tree produced by ModScriptParser#value.
    def enterValue(self, ctx:ModScriptParser.ValueContext):
        pass

    # Exit a parse tree produced by ModScriptParser#value.
    def exitValue(self, ctx:ModScriptParser.ValueContext):
        pass


    # Enter a parse tree produced by ModScriptParser#condition.
    def enterCondition(self, ctx:ModScriptParser.ConditionContext):
        pass

    # Exit a parse tree produced by ModScriptParser#condition.
    def exitCondition(self, ctx:ModScriptParser.ConditionContext):
        pass



del ModScriptParser