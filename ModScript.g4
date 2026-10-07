grammar ModScript;

// --- REGLAS SINTÁCTICAS ---
program     : declaration+ EOF ; //ITERATIVA
declaration : itemDecl | bossDecl | lootDecl ;

itemDecl    : TK_ITEM ID LBRACE attrList RBRACE ;
bossDecl    : TK_BOSS ID LBRACE attrList RBRACE 
            | TK_PHASE ID LBRACE attrList RBRACE ;
lootDecl    : TK_LOOT ID LBRACE dropList RBRACE ;

dropList    : dropDecl+ ;
dropDecl    : TK_DROP ID LBRACE attrList RBRACE ;

attrList    : attr (SEMI attr)* 
            | attr (SEMI attr)* SEMI ;
attr        : ID COLON value 
            | 'condition' COLON condition ;

value       : ID | NUMBER | PERCENTAGE | STRING | TIME_LITERAL ;
condition   : ID OP_REL value ;

// --- REGLAS LÉXICAS, lexer ---
TK_ITEM     : 'item' ;
TK_BOSS     : 'boss' ;
TK_PHASE    : 'phase' ;
TK_LOOT     : 'loot' ;
TK_DROP     : 'drop' ;

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

WS          : [ \t\r\n]+ -> skip ; 