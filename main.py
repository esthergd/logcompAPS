import sys
from abc import ABC, abstractmethod

#identifier -> nova variavel

class PrePro:
    #atualizar o preprocessamento tendo certeza de que toda linha tem um \n no final
    def filter(code):
        code = code.split("\n")
        for i in range(len(code)):
            if "//" in code[i]:
                code[i] = code[i].split("//")[0]
        code = "\n".join(code)
        return code

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

    @abstractmethod

    def Evaluate(self, st):
        pass

class SymbolTable:
    def __init__(self) -> None:
        self.symbol_table = {}

    #tem 2 metodos (getter e setter)
    #getter manda nome do identifier (checar se existe esse nome no dicio, senao raise error)
    def getter(self, ident):
        if ident in self.symbol_table:
            return self.symbol_table[ident]
        else:
            raise TypeError("Erro")
    
    #setter recebe um identifier e um valor
    #Na SymbolTable, além de guardar nome e valor da variável, agora tem que guardar o tipo.
    
    def setter(self, id, value):
        if value[0] == self.symbol_table[id][0]:
            if id in self.symbol_table:
                self.symbol_table[id] = value
            else:
                raise TypeError("Error: Variable not declared")
        else:
            raise TypeError("Error: Type mismatch") #tipo nao de acordo com o tipo da variavel
    
    def create(self, id, type):
        if id not in self.symbol_table:
            self.symbol_table[id] = (type, None)
        else:
            raise TypeError("Error: Variable already declared")  

class FuncTable():
    func_table = {}

    def getter(id):
        if id in FuncTable.func_table:
            return FuncTable.func_table[id]
        else:
            raise TypeError("Erro")
    
    def setter(id, value):
        if value[0] == FuncTable[id][0]:
            if id in FuncTable.func_table:
                FuncTable.func_table[id] = value
            else:
                raise TypeError("Erro")
        else:
            raise TypeError("Erro")
            
    def create(id, type, node):
        if id in FuncTable.func_table:
            raise TypeError("Erro")
        else:
            FuncTable.func_table[id] = (node, type)

class Block(Node):
    #classe vai ter n filhos (1 filho por statement)
    #sem value
    #Evaluate é um loop que vai rodar o Evaluate de cada filho
    def Evaluate(self, st):
        for child in self.children:
            if isinstance(child, Return):
                return child.Evaluate(st)
            child.Evaluate(st)

class Program(Node):
    #classe vai ter n filhos (1 filho por statement)
    #sem value
    #Evaluate é um loop que vai rodar o Evaluate de cada filho
    def Evaluate(self, st):
        for child in self.children:
            if isinstance(child, Return):
                return child.Evaluate(st)
            child.Evaluate(st)

class Print(Node):
    #só tem 1 filho
    #vc nao sabe o tipo o filho
    #Evaluate nao faz nada, só tem que mandar um print do Evaluate do filho
    def Evaluate(self, st):
        print(self.children[0].Evaluate(st)[1])

class Identifier(Node):
    #nao tem filho
    #tem que buscar o valor dele numa symbol table (tem que dar um get. Symbol Table é a memoria do nosso compilador. Ele que associa uma variavel ao valor dela. É um dicionario)
    def Evaluate(self, st):
        return st.getter(self.value)

class Assignment(Node): #atualiza a symbol table
    #tem 2 filhos (identifier e valor do identifier)
    #nao tem value
    #Evaluate vê o nome do filho da esquerda e dá um set na symbol table com o nome do filho da esquerda e o Evaluate do filho da direita
    def Evaluate(self, st):
        st.setter(self.children[0].value, self.children[1].Evaluate(st))



class BinOp(Node):
    def Evaluate(self, st): #COLOCAR SYMBOL TABLE EM TODOS OS EVALUATES
        child0 = self.children[0].Evaluate(st)
        child1 = self.children[1].Evaluate(st)
        if self.value == "+" and child0[0] == child1[0] and child0[0] == "inteiro":
            return (child0[0], child0[1] + child1[1])
        
        elif self.value == "-" and child0[0] == child1[0] and child0[0] == "inteiro":
            return (child0[0], child0[1] - child1[1])
        
        elif self.value == "*" and child0[0] == child1[0] and child0[0] == "inteiro":
            return (child0[0], child0[1] * child1[1])
        
        elif self.value == "/" and child0[0] == child1[0] and child0[0] == "inteiro":
            return (child0[0], child0[1] // child1[1])
        
        elif self.value == "==" and child0[0] == child1[0]:
            return (child0[0], int(child0[1] == child1[1]))
        
        elif self.value == ">" and child0[0] == child1[0]:
            return (child0[0], int(child0[1] > child1[1]))
        
        elif self.value == "<" and child0[0] == child1[0]:
            return (child0[0], int(child0[1] < child1[1]))
        
        elif self.value == "&&" and child0[0] == child1[0] and child0[0] == "inteiro":
            return (child0[0], int(child0[1] and child1[1]))
        
        elif self.value == "||" and child0[0] == child1[0] and child0[0] == "inteiro":
            return (child0[0], int(child0[1] or child1[1]))
        
        elif self.value == ".":
            return ("string", str(child0[1]) + str(child1[1]))
        else:
            raise TypeError("Erro")

class UnOp(Node):
    def Evaluate(self, st):
        child0 = self.children[0].Evaluate(st)
        if self.value == "+" and child0[0] == "inteiro":
            return ("inteiro", child0[1])
        elif self.value == "-" and child0[0] == "inteiro":
            return ("inteiro", -child0[1])
        elif self.value == "!" and child0[0] == "inteiro":
            return ("inteiro", int(not child0[1]))

class IntVal(Node):
    def Evaluate(self, st):
        return ("inteiro", self.value)

class NoOp(Node):
    def Evaluate(self, st):
        pass

class Scanln(Node):
    def Evaluate(self, st):
        return ("inteiro", int(input()))

class If(Node):
    #children[0] = condição
    #children[1] = bloco caso verdadeiro
    #children[2] = else (bloco caso falso) (opcional)

    def Evaluate(self, st):
        if self.children[0].Evaluate(st):
            self.children[1].Evaluate(st)
        elif len(self.children) == 3:
            self.children[2].Evaluate(st)

class For(Node):
    #children[0] = atribuição
    #children[1] = condição
    #children[2] = incremento
    #children[3] = bloco

    def Evaluate(self, st):
        self.children[0].Evaluate(st)
        while self.children[1].Evaluate(st)[1]:
            self.children[3].Evaluate(st)
            self.children[2].Evaluate(st)

class VarDec(Node):
    def Evaluate(self, st):
        if len(self.children) == 2:
            #Cria a variável
            st.create(self.children[0].value, self.value)
            #Atribui valor à variável
            st.setter(self.children[0].value, self.children[1].Evaluate(st))
        else:
            #Cria a variável
            st.create(self.children[0].value, self.value)

class FuncDec(Node):
    def Evaluate(self, st):
        func_name = self.children[0].children[0].value
        func_type = self.children[0].value
        FuncTable.create(id=func_name, type=func_type, node=self)
    
class FuncCall(Node):
    def Evaluate(self, st):
        func_name = self.value
        func_node, type = FuncTable.getter(func_name)
        func_st = SymbolTable()
        for i in range(len(self.children)):
            func_node.children[i+1].Evaluate(func_st)
            func_st.setter(func_node.children[i+1].children[0].value, self.children[i].Evaluate(st))
        
        ret_block = func_node.children[-1].Evaluate(func_st)
        if ret_block is not None:
            if type == ret_block[0]:
                return ret_block
            else:
                raise TypeError("Erro")

class StrVal(Node):
    def Evaluate(self, st):
        return ("string", self.value)

class Return(Node):
    def Evaluate(self, st):
        return self.children[0].Evaluate(st)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Tokenizer:
    #adicionar \n, igual e print
    #o print no go é Println (criar nova lista pra ir analisando o println)
    #adicionar identifier (variavel), que é igual ao numero de multiplos digitos (identificar se é letra, numero (.isalnum()) ou caracter especial)
    
    palavras_reservadas = ["Imprime", "Le", "se", "senão", "para", "var", "inteiro", "string", "função", "retorna"]

    #pra cada identifier, checar se ele nao ta na lista de palavras reservadas

    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.next = None

    def select_next(self):

        while self.position < len(self.source) and self.source[self.position] == " ":
            self.position += 1
        
        if self.position == len(self.source):
            self.next = Token("EOF", "")
           
        elif self.position != len(self.source):
            if self.source[self.position].isdigit():
                number = ""

                while self.position < len(self.source) and self.source[self.position].isdigit():
                    number += self.source[self.position]
                    self.position += 1
                self.next = Token("INT", int(number))

            elif self.source[self.position] == "*":
                self.next = Token("MULT", "*")
                self.position += 1
            
            elif self.source[self.position] == "/":
                self.next = Token("DIV", "/")
                self.position += 1

            elif self.source[self.position] == "+":
                self.next = Token("SOMA", "+")
                self.position += 1
            
            elif self.source[self.position] == "-":
                self.next = Token("SUB", "-")
                self.position += 1
            
            elif self.source[self.position] == "(":
                self.next = Token("EPAREN", "(")
                self.position += 1
            
            elif self.source[self.position] == ")":
                self.next = Token("DPAREN", ")")
                self.position += 1
            
            elif self.source[self.position] == "\n":
                self.next = Token("QUEBRA_LINHA", "\n")
                self.position += 1
            
            elif self.source[self.position] == "=":
                if self.source[self.position + 1] == "=":
                    self.next = Token("IGUAL_IGUAL", "==")
                    self.position += 2
                else:
                    self.next = Token("IGUAL", "=")
                    self.position += 1
            
            #dnd, or, maior, menor, not, ;, {, }
            
            elif self.source[self.position] == "&":
                if self.source[self.position + 1] == "&":
                    self.next = Token("E", "&")
                    self.position += 2
                else:
                    raise TypeError("Erro")
            
            elif self.source[self.position] == "|":
                if self.source[self.position + 1] == "|":
                    self.next = Token("OU", "|")
                    self.position += 2
                else:
                    raise TypeError("Erro")

            elif self.source[self.position] == ">":
                self.next = Token("MAIOR", ">")
                self.position += 1
            
            elif self.source[self.position] == "<":
                self.next = Token("MENOR", "<")
                self.position += 1
            
            elif self.source[self.position] == "!":
                self.next = Token("NEG", "!")
                self.position += 1
            
            elif self.source[self.position] == ";":
                self.next = Token("PONTO_VIRGULA", ";")
                self.position += 1
            
            elif self.source[self.position] == "{":
                self.next = Token("EBRACE", "{")
                self.position += 1
            
            elif self.source[self.position] == "}":
                self.next = Token("DBRACE", "}")
                self.position += 1
            
            elif self.source[self.position] == ".":
                self.next = Token("CONCAT", ".")
                self.position += 1
            
            elif self.source[self.position] == ",":
                    self.next = Token("VIRGULA", self.source[self.position])
                    self.position += 1
            
            elif self.source[self.position] == '"': #Verifica se é string (se começa com aspas)
                string = ""
                self.position += 1
                #Repete até encontrar outra aspas (final da string)
                while self.position < len(self.source) and self.source[self.position] != '"':
                    string += self.source[self.position]
                    self.position += 1
                if self.source[self.position] == '"':
                    self.position += 1
                    self.next = Token("STRING", string)
                    
                else:
                    raise TypeError("Erro")

            elif self.source[self.position].isalpha():
                id = ""
                while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == "_"):
                    id += self.source[self.position]
                    self.position += 1
                
                if id == "Imprime":
                    self.next = Token("Imprime", id)
                elif id == "Le":
                    self.next = Token("Le", id)
                elif id == "se":
                    self.next = Token("se", id)
                elif id == "senão":
                    self.next = Token("senão", id)
                elif id == "para":
                    self.next = Token("para", id)
                elif id == "var":
                    self.next = Token("var", id)
                elif id == "inteiro":
                    self.next = Token("type", id)
                elif id == "string":
                    self.next = Token("type", id)
                elif id == "função":
                    self.next = Token("função", id)
                elif id == "retorna":
                    self.next = Token("retorna", id)
                else:
                    self.next = Token("ID", id)

            
            elif self.source[self.position].isspace():
                self.position += 1
                self.select_next()
            
            else:
                raise TypeError("Erro")
        else:
            raise ValueError("Erro")

class Parser:

    tokenizer = None

    #criar um parse_block e um parse_statement
    #parse_block vai ser um loop que vai rodar o parse_statement até encontrar "EOF"
    #parse_statement sao varios ifs e no final tem que checar o \n

    def parse_program():
        result = Program("", [])
        while Parser.tokenizer.next.type != "EOF":
            while Parser.tokenizer.next.type == "QUEBRA_LINHA":
                Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != "EOF":
                result.children.append(Parser.parse_declaration())
        result.children.append(FuncCall("main", []))
        return result
    
    def parse_declaration():
        parameters = []
        
        if Parser.tokenizer.next.type == "função":
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "ID":
                func_name = Parser.tokenizer.next.value
                Parser.tokenizer.select_next()
                if Parser.tokenizer.next.type == "EPAREN":
                    Parser.tokenizer.select_next()
                    while Parser.tokenizer.next.type == "ID":
                        variable_name = Parser.tokenizer.next.value
                        Parser.tokenizer.select_next()
                        variable_type = Parser.tokenizer.next.value
                        Parser.tokenizer.select_next()
                        parameters.append((variable_type, variable_name))
                        if Parser.tokenizer.next.type == "VIRGULA":
                            Parser.tokenizer.select_next()
                        else:
                            break

                    if Parser.tokenizer.next.type == "DPAREN":
                        Parser.tokenizer.select_next()
                        if Parser.tokenizer.next.type == "type":
                            func_type = Parser.tokenizer.next.value
                            Parser.tokenizer.select_next()
                            result = FuncDec(None, [VarDec(func_type, [Identifier(func_name, [])])])
                            if len(parameters) > 0:
                                for i in range(len(parameters)):
                                    result.children.append(VarDec(parameters[i][0], [Identifier(parameters[i][1], [])]))
                            result.children.append(Parser.parse_block())

                            if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                                Parser.tokenizer.select_next()
                            else:
                                raise TypeError("Erro")
                            return result
                        else:
                            raise TypeError("Erro")
                    else:
                        raise TypeError("Erro")
                else:
                    raise TypeError("Erro")
            else:
                raise TypeError("Erro")
        else:
            raise TypeError("Erro")


    def parse_block():
        if Parser.tokenizer.next.type == "EBRACE":
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                Parser.tokenizer.select_next()
                result = Block("", [])
                while Parser.tokenizer.next.type != "DBRACE":
                    result.children.append(Parser.parse_statement())
                if Parser.tokenizer.next.type == "DBRACE":
                    Parser.tokenizer.select_next()
                    return result
                else:
                    raise TypeError("Erro")

    def rel_expression():
        result = Parser.parse_expression()

        while Parser.tokenizer.next.type == "IGUAL_IGUAL" or Parser.tokenizer.next.type == "MAIOR" or Parser.tokenizer.next.type == "MENOR":
            if Parser.tokenizer.next.type == "IGUAL_IGUAL":
                Parser.tokenizer.select_next()
                result = BinOp("==", [result, Parser.parse_expression()])
            elif Parser.tokenizer.next.type == "MAIOR":
                Parser.tokenizer.select_next()
                result = BinOp(">", [result, Parser.parse_expression()])
            elif Parser.tokenizer.next.type == "MENOR":
                Parser.tokenizer.select_next()
                result = BinOp("<", [result, Parser.parse_expression()])
        
        return result

    def bool_term():
        result = Parser.rel_expression()

        while Parser.tokenizer.next.type == "E":
            Parser.tokenizer.select_next()
            result = BinOp("&&", [result, Parser.rel_expression()])
        
        return result
    
    def bool_expression():
        result = Parser.bool_term()

        while Parser.tokenizer.next.type == "OU":
            Parser.tokenizer.select_next()
            result = BinOp("||", [result, Parser.bool_term()])
        
        return result
    
    def assign():
        if Parser.tokenizer.next.type == "ID":
            id = Parser.tokenizer.next.value
            id_node = Identifier(id, [])
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "IGUAL":
                Parser.tokenizer.select_next()
                bool_expression = Parser.bool_expression()
                return Assignment("=",[id_node, bool_expression])
            if Parser.tokenizer.next.type == "EPAREN":
                Parser.tokenizer.select_next()
                result = FuncCall(id_node, [])
                while Parser.tokenizer.next.type != "DPAREN":
                    result.children.append(Parser.bool_expression())
                    if Parser.tokenizer.next.type == "VIRGULA":
                        Parser.tokenizer.select_next()
                    else:
                        break
                if Parser.tokenizer.next.type == "DPAREN":
                    Parser.tokenizer.select_next()
                    if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                        Parser.tokenizer.select_next()
                        return result
                    else:
                        raise TypeError("Erro")
                else:
                    raise TypeError("Erro")       
            else:
                raise TypeError("Erro")
        else:
            raise TypeError("Erro")

    def parse_expression():

        result = Parser.parse_term()

        while Parser.tokenizer.next.type == "SOMA" or Parser.tokenizer.next.type == "SUB" or Parser.tokenizer.next.type == "CONCAT":
            if Parser.tokenizer.next.type == "SOMA":
                Parser.tokenizer.select_next()
                result = BinOp("+", [result, Parser.parse_term()])
            elif Parser.tokenizer.next.type == "SUB":
                Parser.tokenizer.select_next()
                result = BinOp("-", [result, Parser.parse_term()])
            elif Parser.tokenizer.next.type == "CONCAT":
                Parser.tokenizer.select_next()
                result = BinOp(".", [result, Parser.parse_term()])
            
        return result

    def parse_term():
        
        result = Parser.parse_factor()

        while Parser.tokenizer.next.type == "MULT" or Parser.tokenizer.next.type == "DIV":
            if Parser.tokenizer.next.type == "MULT":
                Parser.tokenizer.select_next()
                result = BinOp("*", [result, Parser.parse_factor()])
            elif Parser.tokenizer.next.type == "DIV":
                Parser.tokenizer.select_next()
                result = BinOp("/", [result, Parser.parse_factor()])

        return result

    def parse_factor():
        #começa a receber o identifier

        result = None
        
        if Parser.tokenizer.next.type == "INT":
            result = IntVal(Parser.tokenizer.next.value, [])
            Parser.tokenizer.select_next()
            return result
        
        elif Parser.tokenizer.next.type == "STRING":
            result = StrVal(Parser.tokenizer.next.value, [])
            Parser.tokenizer.select_next()
            return result
        
        elif Parser.tokenizer.next.type == "SOMA":
            Parser.tokenizer.select_next()
            result = UnOp("+", [Parser.parse_factor()])
            return result
        
        elif Parser.tokenizer.next.type == "SUB":
            Parser.tokenizer.select_next()
            result = UnOp("-", [Parser.parse_factor()])
            return result
        
        elif Parser.tokenizer.next.type == "NEG":
            Parser.tokenizer.select_next()
            result = UnOp("!", [Parser.parse_factor()])
            return result
        
        elif Parser.tokenizer.next.type == "EPAREN":
            Parser.tokenizer.select_next()
            result = Parser.bool_expression()
            if Parser.tokenizer.next.type == "DPAREN":
                Parser.tokenizer.select_next()
                return result
        
        elif Parser.tokenizer.next.type == "ID":
            id = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "EPAREN":
                Parser.tokenizer.select_next()
                result = FuncCall(id, [])
                while Parser.tokenizer.next.type != "DPAREN":
                    result.children.append(Parser.bool_expression())
                    if Parser.tokenizer.next.type == "VIRGULA":
                        Parser.tokenizer.select_next()
                    else:
                        break
                if Parser.tokenizer.next.type == "DPAREN":
                    Parser.tokenizer.select_next()
                    return result
                else:
                    raise TypeError("Erro")
            else:
                result = Identifier(id, [])
                return result
        
        elif Parser.tokenizer.next.type == "Le":
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "EPAREN":
                Parser.tokenizer.select_next()
                result = Scanln("Le", [])
                if Parser.tokenizer.next.type == "DPAREN":
                    Parser.tokenizer.select_next()
                    return result
                else:
                    raise TypeError("Erro")
            else:
                raise TypeError("Erro")
        else:
            raise TypeError("Erro")
    
    def parse_statement():
        result = None
        if Parser.tokenizer.next.type == "QUEBRA_LINHA":
            Parser.tokenizer.select_next()
            return NoOp("NoOp", [])
        
        elif Parser.tokenizer.next.type == "ID":
            ident = Identifier(Parser.tokenizer.next.value, [])
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "IGUAL":
                Parser.tokenizer.select_next()
                result = Assignment("=", [ident, Parser.bool_expression()])
                if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                    Parser.tokenizer.select_next()
                    return result
                else:
                    raise TypeError("Erro")
                
            elif Parser.tokenizer.next.type == "EPAREN":
                Parser.tokenizer.select_next()
                result = FuncCall(ident.value, [])
                while Parser.tokenizer.next.type != "DPAREN":
                    result.children.append(Parser.bool_expression())
                    if Parser.tokenizer.next.type == "VIRGULA":
                        Parser.tokenizer.select_next()
                    else:
                        break
                if Parser.tokenizer.next.type == "DPAREN":
                    Parser.tokenizer.select_next()
                    if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                        Parser.tokenizer.select_next()
                        return result
                    else:
                        raise TypeError("Erro")
                else:
                    raise TypeError("Erro")
            else:
                raise TypeError("Erro")
        
        elif Parser.tokenizer.next.type == "se":
            Parser.tokenizer.select_next()
            condition = Parser.bool_expression()
            if_block = Parser.parse_block()
            if Parser.tokenizer.next.type == "senão":
                Parser.tokenizer.select_next()
                else_block = Parser.parse_block()
                result = If("se", [condition, if_block, else_block])
            else:
                result = If("se", [condition, if_block])
            if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                Parser.tokenizer.select_next()
                return result
        
        elif Parser.tokenizer.next.type == "para":
            Parser.tokenizer.select_next()
            atribution = Parser.assign()
            if Parser.tokenizer.next.type == "PONTO_VIRGULA":
                Parser.tokenizer.select_next()
                condition = Parser.bool_expression()
                if Parser.tokenizer.next.type == "PONTO_VIRGULA":
                    Parser.tokenizer.select_next()
                    increment = Parser.assign()
                    block = Parser.parse_block()
                    result = For("para", [atribution, condition, increment, block])
            if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                Parser.tokenizer.select_next()
                return result
            else:
                raise TypeError("Erro")
        
        elif Parser.tokenizer.next.type == "var":
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "ID":
                ident = Identifier(Parser.tokenizer.next.value, [])
                Parser.tokenizer.select_next()
                if Parser.tokenizer.next.type == "type":
                    type = Parser.tokenizer.next.value
                    result = VarDec(type, [ident])
                    Parser.tokenizer.select_next()
                    if Parser.tokenizer.next.type == "IGUAL":
                        Parser.tokenizer.select_next()
                        result.children.append(Parser.bool_expression())
                    if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                        Parser.tokenizer.select_next()
                        return result
                    else:
                        raise TypeError("Erro")
                else:
                    raise TypeError("Erro")
        
        elif Parser.tokenizer.next.type == "Imprime":
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "EPAREN":
                Parser.tokenizer.select_next()
                result = Print("Imprime", [Parser.bool_expression()])
                if Parser.tokenizer.next.type == "DPAREN":
                    Parser.tokenizer.select_next()
                    if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                        Parser.tokenizer.select_next()
                        return result
                    else:
                        raise TypeError("Erro")
                else:
                    raise TypeError("Erro")
            else:
                raise TypeError("Erro")
            
        elif Parser.tokenizer.next.type == "retorna":
            Parser.tokenizer.select_next()
            resultado = Return("retorna", [Parser.bool_expression()])
            if Parser.tokenizer.next.type == "QUEBRA_LINHA":
                Parser.tokenizer.select_next()
                return resultado
            else:
                raise TypeError("Erro")
        else:
            raise TypeError("Erro")


        
    def run(code):
        #recebe o código fonte como argumento, inicializa um objeto Tokenizer,
        #posiciona no primeiro token e retorna o resultado do parse_term(). 
        #Ao final, verificar se terminou de consumir toda a cadeia (o token deve ser EOF).

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        result = Parser.parse_program()
        if Parser.tokenizer.next.type == "EOF":
            return result
        else:
            raise TypeError("Erro")

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        codigo = file.read()
        codigo = PrePro.filter(codigo) + "\n"

    run = Parser.run(codigo)
    symbol_table = SymbolTable()
    run.Evaluate(symbol_table)