// Generated from /Users/bookie/ModScript/ModScript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ModScriptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, TK_ITEM=2, TK_BOSS=3, TK_PHASE=4, TK_LOOT=5, TK_DROP=6, ID=7, 
		NUMBER=8, PERCENTAGE=9, STRING=10, TIME_LITERAL=11, LBRACE=12, RBRACE=13, 
		SEMI=14, COLON=15, OP_REL=16, WS=17;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_itemDecl = 2, RULE_bossDecl = 3, 
		RULE_lootDecl = 4, RULE_dropList = 5, RULE_dropDecl = 6, RULE_attrList = 7, 
		RULE_attr = 8, RULE_value = 9, RULE_condition = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "itemDecl", "bossDecl", "lootDecl", "dropList", 
			"dropDecl", "attrList", "attr", "value", "condition"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'condition'", "'item'", "'boss'", "'phase'", "'loot'", "'drop'", 
			null, null, null, null, null, "'{'", "'}'", "';'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "TK_ITEM", "TK_BOSS", "TK_PHASE", "TK_LOOT", "TK_DROP", "ID", 
			"NUMBER", "PERCENTAGE", "STRING", "TIME_LITERAL", "LBRACE", "RBRACE", 
			"SEMI", "COLON", "OP_REL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ModScript.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ModScriptParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ModScriptParser.EOF, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(22);
				declaration();
				}
				}
				setState(25); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 60L) != 0) );
			setState(27);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public ItemDeclContext itemDecl() {
			return getRuleContext(ItemDeclContext.class,0);
		}
		public BossDeclContext bossDecl() {
			return getRuleContext(BossDeclContext.class,0);
		}
		public LootDeclContext lootDecl() {
			return getRuleContext(LootDeclContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(32);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TK_ITEM:
				enterOuterAlt(_localctx, 1);
				{
				setState(29);
				itemDecl();
				}
				break;
			case TK_BOSS:
			case TK_PHASE:
				enterOuterAlt(_localctx, 2);
				{
				setState(30);
				bossDecl();
				}
				break;
			case TK_LOOT:
				enterOuterAlt(_localctx, 3);
				{
				setState(31);
				lootDecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ItemDeclContext extends ParserRuleContext {
		public TerminalNode TK_ITEM() { return getToken(ModScriptParser.TK_ITEM, 0); }
		public TerminalNode ID() { return getToken(ModScriptParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(ModScriptParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(ModScriptParser.RBRACE, 0); }
		public ItemDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_itemDecl; }
	}

	public final ItemDeclContext itemDecl() throws RecognitionException {
		ItemDeclContext _localctx = new ItemDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_itemDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(TK_ITEM);
			setState(35);
			match(ID);
			setState(36);
			match(LBRACE);
			setState(37);
			attrList();
			setState(38);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BossDeclContext extends ParserRuleContext {
		public TerminalNode TK_BOSS() { return getToken(ModScriptParser.TK_BOSS, 0); }
		public TerminalNode ID() { return getToken(ModScriptParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(ModScriptParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(ModScriptParser.RBRACE, 0); }
		public TerminalNode TK_PHASE() { return getToken(ModScriptParser.TK_PHASE, 0); }
		public BossDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bossDecl; }
	}

	public final BossDeclContext bossDecl() throws RecognitionException {
		BossDeclContext _localctx = new BossDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_bossDecl);
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TK_BOSS:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				match(TK_BOSS);
				setState(41);
				match(ID);
				setState(42);
				match(LBRACE);
				setState(43);
				attrList();
				setState(44);
				match(RBRACE);
				}
				break;
			case TK_PHASE:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				match(TK_PHASE);
				setState(47);
				match(ID);
				setState(48);
				match(LBRACE);
				setState(49);
				attrList();
				setState(50);
				match(RBRACE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LootDeclContext extends ParserRuleContext {
		public TerminalNode TK_LOOT() { return getToken(ModScriptParser.TK_LOOT, 0); }
		public TerminalNode ID() { return getToken(ModScriptParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(ModScriptParser.LBRACE, 0); }
		public DropListContext dropList() {
			return getRuleContext(DropListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(ModScriptParser.RBRACE, 0); }
		public LootDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lootDecl; }
	}

	public final LootDeclContext lootDecl() throws RecognitionException {
		LootDeclContext _localctx = new LootDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_lootDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(TK_LOOT);
			setState(55);
			match(ID);
			setState(56);
			match(LBRACE);
			setState(57);
			dropList();
			setState(58);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DropListContext extends ParserRuleContext {
		public List<DropDeclContext> dropDecl() {
			return getRuleContexts(DropDeclContext.class);
		}
		public DropDeclContext dropDecl(int i) {
			return getRuleContext(DropDeclContext.class,i);
		}
		public DropListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dropList; }
	}

	public final DropListContext dropList() throws RecognitionException {
		DropListContext _localctx = new DropListContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_dropList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(60);
				dropDecl();
				}
				}
				setState(63); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==TK_DROP );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DropDeclContext extends ParserRuleContext {
		public TerminalNode TK_DROP() { return getToken(ModScriptParser.TK_DROP, 0); }
		public TerminalNode ID() { return getToken(ModScriptParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(ModScriptParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(ModScriptParser.RBRACE, 0); }
		public DropDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dropDecl; }
	}

	public final DropDeclContext dropDecl() throws RecognitionException {
		DropDeclContext _localctx = new DropDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_dropDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(TK_DROP);
			setState(66);
			match(ID);
			setState(67);
			match(LBRACE);
			setState(68);
			attrList();
			setState(69);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttrListContext extends ParserRuleContext {
		public List<AttrContext> attr() {
			return getRuleContexts(AttrContext.class);
		}
		public AttrContext attr(int i) {
			return getRuleContext(AttrContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(ModScriptParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(ModScriptParser.SEMI, i);
		}
		public AttrListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attrList; }
	}

	public final AttrListContext attrList() throws RecognitionException {
		AttrListContext _localctx = new AttrListContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_attrList);
		int _la;
		try {
			int _alt;
			setState(89);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(71);
				attr();
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==SEMI) {
					{
					{
					setState(72);
					match(SEMI);
					setState(73);
					attr();
					}
					}
					setState(78);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				attr();
				setState(84);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(80);
						match(SEMI);
						setState(81);
						attr();
						}
						} 
					}
					setState(86);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				}
				setState(87);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttrContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ModScriptParser.ID, 0); }
		public TerminalNode COLON() { return getToken(ModScriptParser.COLON, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public AttrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr; }
	}

	public final AttrContext attr() throws RecognitionException {
		AttrContext _localctx = new AttrContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_attr);
		try {
			setState(97);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(91);
				match(ID);
				setState(92);
				match(COLON);
				setState(93);
				value();
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 2);
				{
				setState(94);
				match(T__0);
				setState(95);
				match(COLON);
				setState(96);
				condition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ModScriptParser.ID, 0); }
		public TerminalNode NUMBER() { return getToken(ModScriptParser.NUMBER, 0); }
		public TerminalNode PERCENTAGE() { return getToken(ModScriptParser.PERCENTAGE, 0); }
		public TerminalNode STRING() { return getToken(ModScriptParser.STRING, 0); }
		public TerminalNode TIME_LITERAL() { return getToken(ModScriptParser.TIME_LITERAL, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3968L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ModScriptParser.ID, 0); }
		public TerminalNode OP_REL() { return getToken(ModScriptParser.OP_REL, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(ID);
			setState(102);
			match(OP_REL);
			setState(103);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0011j\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0004\u0000\u0018"+
		"\b\u0000\u000b\u0000\f\u0000\u0019\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001!\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u00035\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0004\u0005>\b\u0005\u000b\u0005\f\u0005?\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0005\u0007K\b\u0007\n\u0007\f\u0007N\t\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0005\u0007S\b\u0007\n\u0007\f\u0007V\t"+
		"\u0007\u0001\u0007\u0001\u0007\u0003\u0007Z\b\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0003\bb\b\b\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0000\u0000\u000b\u0000\u0002\u0004\u0006\b"+
		"\n\f\u000e\u0010\u0012\u0014\u0000\u0001\u0001\u0000\u0007\u000bg\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0002 \u0001\u0000\u0000\u0000\u0004\""+
		"\u0001\u0000\u0000\u0000\u00064\u0001\u0000\u0000\u0000\b6\u0001\u0000"+
		"\u0000\u0000\n=\u0001\u0000\u0000\u0000\fA\u0001\u0000\u0000\u0000\u000e"+
		"Y\u0001\u0000\u0000\u0000\u0010a\u0001\u0000\u0000\u0000\u0012c\u0001"+
		"\u0000\u0000\u0000\u0014e\u0001\u0000\u0000\u0000\u0016\u0018\u0003\u0002"+
		"\u0001\u0000\u0017\u0016\u0001\u0000\u0000\u0000\u0018\u0019\u0001\u0000"+
		"\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u0019\u001a\u0001\u0000"+
		"\u0000\u0000\u001a\u001b\u0001\u0000\u0000\u0000\u001b\u001c\u0005\u0000"+
		"\u0000\u0001\u001c\u0001\u0001\u0000\u0000\u0000\u001d!\u0003\u0004\u0002"+
		"\u0000\u001e!\u0003\u0006\u0003\u0000\u001f!\u0003\b\u0004\u0000 \u001d"+
		"\u0001\u0000\u0000\u0000 \u001e\u0001\u0000\u0000\u0000 \u001f\u0001\u0000"+
		"\u0000\u0000!\u0003\u0001\u0000\u0000\u0000\"#\u0005\u0002\u0000\u0000"+
		"#$\u0005\u0007\u0000\u0000$%\u0005\f\u0000\u0000%&\u0003\u000e\u0007\u0000"+
		"&\'\u0005\r\u0000\u0000\'\u0005\u0001\u0000\u0000\u0000()\u0005\u0003"+
		"\u0000\u0000)*\u0005\u0007\u0000\u0000*+\u0005\f\u0000\u0000+,\u0003\u000e"+
		"\u0007\u0000,-\u0005\r\u0000\u0000-5\u0001\u0000\u0000\u0000./\u0005\u0004"+
		"\u0000\u0000/0\u0005\u0007\u0000\u000001\u0005\f\u0000\u000012\u0003\u000e"+
		"\u0007\u000023\u0005\r\u0000\u000035\u0001\u0000\u0000\u00004(\u0001\u0000"+
		"\u0000\u00004.\u0001\u0000\u0000\u00005\u0007\u0001\u0000\u0000\u0000"+
		"67\u0005\u0005\u0000\u000078\u0005\u0007\u0000\u000089\u0005\f\u0000\u0000"+
		"9:\u0003\n\u0005\u0000:;\u0005\r\u0000\u0000;\t\u0001\u0000\u0000\u0000"+
		"<>\u0003\f\u0006\u0000=<\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000"+
		"?=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@\u000b\u0001\u0000"+
		"\u0000\u0000AB\u0005\u0006\u0000\u0000BC\u0005\u0007\u0000\u0000CD\u0005"+
		"\f\u0000\u0000DE\u0003\u000e\u0007\u0000EF\u0005\r\u0000\u0000F\r\u0001"+
		"\u0000\u0000\u0000GL\u0003\u0010\b\u0000HI\u0005\u000e\u0000\u0000IK\u0003"+
		"\u0010\b\u0000JH\u0001\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001"+
		"\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MZ\u0001\u0000\u0000\u0000"+
		"NL\u0001\u0000\u0000\u0000OT\u0003\u0010\b\u0000PQ\u0005\u000e\u0000\u0000"+
		"QS\u0003\u0010\b\u0000RP\u0001\u0000\u0000\u0000SV\u0001\u0000\u0000\u0000"+
		"TR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000UW\u0001\u0000\u0000"+
		"\u0000VT\u0001\u0000\u0000\u0000WX\u0005\u000e\u0000\u0000XZ\u0001\u0000"+
		"\u0000\u0000YG\u0001\u0000\u0000\u0000YO\u0001\u0000\u0000\u0000Z\u000f"+
		"\u0001\u0000\u0000\u0000[\\\u0005\u0007\u0000\u0000\\]\u0005\u000f\u0000"+
		"\u0000]b\u0003\u0012\t\u0000^_\u0005\u0001\u0000\u0000_`\u0005\u000f\u0000"+
		"\u0000`b\u0003\u0014\n\u0000a[\u0001\u0000\u0000\u0000a^\u0001\u0000\u0000"+
		"\u0000b\u0011\u0001\u0000\u0000\u0000cd\u0007\u0000\u0000\u0000d\u0013"+
		"\u0001\u0000\u0000\u0000ef\u0005\u0007\u0000\u0000fg\u0005\u0010\u0000"+
		"\u0000gh\u0003\u0012\t\u0000h\u0015\u0001\u0000\u0000\u0000\b\u0019 4"+
		"?LTYa";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}