# Generated from ModScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ModScriptParser import ModScriptParser
else:
    from ModScriptParser import ModScriptParser

# This class defines a complete generic visitor for a parse tree produced by ModScriptParser.

class ModScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ModScriptParser#program.
    def visitProgram(self, ctx:ModScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#declaration.
    def visitDeclaration(self, ctx:ModScriptParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#itemDecl.
    def visitItemDecl(self, ctx:ModScriptParser.ItemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#bossDecl.
    def visitBossDecl(self, ctx:ModScriptParser.BossDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#lootDecl.
    def visitLootDecl(self, ctx:ModScriptParser.LootDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#dropList.
    def visitDropList(self, ctx:ModScriptParser.DropListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#dropDecl.
    def visitDropDecl(self, ctx:ModScriptParser.DropDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#attrList.
    def visitAttrList(self, ctx:ModScriptParser.AttrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#attr.
    def visitAttr(self, ctx:ModScriptParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#value.
    def visitValue(self, ctx:ModScriptParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModScriptParser#condition.
    def visitCondition(self, ctx:ModScriptParser.ConditionContext):
        return self.visitChildren(ctx)



del ModScriptParser