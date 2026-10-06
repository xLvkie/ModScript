grammar ModScript;

// --- REGLAS SINTÁCTICAS (Parser) ---
program     : declaration+ EOF ;
declaration : itemDecl | bossDecl | lootDecl ;

itemDecl    : KW_ITEM ID LBRACE attrList RBRACE ;
bossDecl    : KW_BOSS ID LBRACE attrList RBRACE 
            | KW_PHASE ID LBRACE attrList RBRACE ;
lootDecl    : KW_LOOT ID LBRACE dropList RBRACE ;

dropList    : dropDecl+ ;
dropDecl    : KW_DROP ID LBRACE attrList RBRACE ;

attrList    : attr (SEMI attr)* SEMI? ;
attr        : ID COLON value 
            | 'condition' COLON condition ;

value       : ID | NUMBER | PERCENTAGE | STRING | TIME_LITERAL ;
condition   : ID OP_REL value ;

// --- REGLAS LÉXICAS (Lexer) ---
KW_ITEM     : 'item' ;
KW_BOSS     : 'boss' ;
KW_PHASE    : 'phase' ;
KW_LOOT     : 'loot' ;
KW_DROP     : 'drop' ;

ID          : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER      : [0-9]+ ('.' [0-9]+)? ;
PERCENTAGE  : [0-9]+ '%' ;
STRING      : '"' .*? '"' ;
TIME_LITERAL: [0-9]+ ':' [0-9]+ ;

LBRACE      : '{' ;
RBRACE      : '}' ;
SEMI        : ';' ;
COLON       : ':' ;
OP_REL      : '<' | '>' | '<=' | '>=' | '==' ;

WS          : [ \t\r\n]+ -> skip ; // Ignorar espacios en blanco y saltos de línea