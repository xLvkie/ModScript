// Generated from /Users/bookie/ModScript/ModScript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ModScriptParser}.
 */
public interface ModScriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ModScriptParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ModScriptParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(ModScriptParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(ModScriptParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#itemDecl}.
	 * @param ctx the parse tree
	 */
	void enterItemDecl(ModScriptParser.ItemDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#itemDecl}.
	 * @param ctx the parse tree
	 */
	void exitItemDecl(ModScriptParser.ItemDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#bossDecl}.
	 * @param ctx the parse tree
	 */
	void enterBossDecl(ModScriptParser.BossDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#bossDecl}.
	 * @param ctx the parse tree
	 */
	void exitBossDecl(ModScriptParser.BossDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#lootDecl}.
	 * @param ctx the parse tree
	 */
	void enterLootDecl(ModScriptParser.LootDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#lootDecl}.
	 * @param ctx the parse tree
	 */
	void exitLootDecl(ModScriptParser.LootDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#dropList}.
	 * @param ctx the parse tree
	 */
	void enterDropList(ModScriptParser.DropListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#dropList}.
	 * @param ctx the parse tree
	 */
	void exitDropList(ModScriptParser.DropListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#dropDecl}.
	 * @param ctx the parse tree
	 */
	void enterDropDecl(ModScriptParser.DropDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#dropDecl}.
	 * @param ctx the parse tree
	 */
	void exitDropDecl(ModScriptParser.DropDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#attrList}.
	 * @param ctx the parse tree
	 */
	void enterAttrList(ModScriptParser.AttrListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#attrList}.
	 * @param ctx the parse tree
	 */
	void exitAttrList(ModScriptParser.AttrListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#attr}.
	 * @param ctx the parse tree
	 */
	void enterAttr(ModScriptParser.AttrContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#attr}.
	 * @param ctx the parse tree
	 */
	void exitAttr(ModScriptParser.AttrContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(ModScriptParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(ModScriptParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModScriptParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(ModScriptParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModScriptParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(ModScriptParser.ConditionContext ctx);
}