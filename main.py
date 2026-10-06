import sys
from antlr4 import * # type: ignore
from ModScriptLexer import ModScriptLexer
from ModScriptParser import ModScriptParser
from ModScriptVisitor import ModScriptVisitor

# Analizador Semántico
class SemanticAnalyzer(ModScriptVisitor):
    def __init__(self):
        self.errores = []

    # Error Semántico 1: Validación de Tipos 
    def visitAttr(self, ctx: ModScriptParser.AttrContext):
        id_node = ctx.ID() 
        atributo_nombre = getattr(id_node, "getText", lambda: "condition")() if id_node is not None else "condition"
        valor_ctx = ctx.value()

        if atributo_nombre == "damage":
            if valor_ctx is not None and not valor_ctx.NUMBER():
                start = getattr(ctx, "getStart", lambda: None)()  
                linea = getattr(start, "line", 0) if start is not None else 0
                self.errores.append(f"Error Semántico [Línea {linea}]: 'damage' requiere un NUMBER.")

        return self.visitChildren(ctx)

    # Error Semántico 2: Inconsistencia Matemática (Semana 6 - Recorrido de AST)
    def visitLootDecl(self, ctx: ModScriptParser.LootDeclContext):
        # Obtención de los nombres de los drops
        id_node = getattr(ctx, "ID", lambda: None)()
        loot_name = getattr(id_node, "getText", lambda: "Desconocido")() if id_node is not None else "Desconocido"
        
        suma_probabilidades = 0
        
        # Obtención de la lista de drops
        drop_list = getattr(ctx, "dropList", lambda: None)()
        if drop_list is not None:
            drops = getattr(drop_list, "dropDecl", lambda: [])()
            if not isinstance(drops, list):
                drops = [drops]
                
            for drop in drops:
                if drop is None: continue
                
                attr_list = getattr(drop, "attrList", lambda: None)()
                if attr_list is not None:
                    attrs = getattr(attr_list, "attr", lambda: [])()
                    if not isinstance(attrs, list):
                        attrs = [attrs]
                        
                    for attr in attrs:
                        if attr is None: continue
                        
                        attr_id = getattr(attr, "ID", lambda: None)()
                        if attr_id is not None:
                            attr_name = getattr(attr_id, "getText", lambda: "")()
                            
                            if attr_name == "chance":
                                valor_ctx = getattr(attr, "value", lambda: None)()
                                if valor_ctx is not None:
                                    pct_node = getattr(valor_ctx, "PERCENTAGE", lambda: None)()
                                    if pct_node is not None:
                                        val_str = getattr(pct_node, "getText", lambda: "0")().replace("%", "")
                                        suma_probabilidades += float(val_str)
        
        # Validación del limite logico (errores semanticos)
        if suma_probabilidades > 100.0:
            start = getattr(ctx, "getStart", lambda: None)()
            linea = getattr(start, "line", 0) if start is not None else 0
            self.errores.append(f"Error Semántico [Línea {linea}]: El loot '{loot_name}' tiene probabilidades que suman más del 100% ({suma_probabilidades}%).")
            
        return self.visitChildren(ctx)

# Driver Principal
def main(argv):
    if len(argv) < 2:
        print("Uso: python main.py <archivo_codigo.mod>")
        return

    # Leer el archivo de entrada
    input_stream = FileStream(argv[1], encoding='utf-8')
    
    # Análisis Léxico
    lexer = ModScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Análisis Sintáctico
    parser = ModScriptParser(stream)
    tree = parser.program()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Errores sintácticos encontrados. Abortando análisis semántico.")
        return

    # Análisis Semántico
    print("Análisis sintáctico exitoso. Iniciando análisis semántico...")
    analyzer = SemanticAnalyzer()
    analyzer.visit(tree)

    if len(analyzer.errores) > 0:
        print("\nSe encontraron errores semánticos:")
        for error in analyzer.errores:
            print(error)
    else:
        print("\nCompilación completada sin errores semánticos.")

if __name__ == '__main__':
    main(sys.argv)