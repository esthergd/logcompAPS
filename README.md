# APS de Lógica da Computação


## Linguagem de Programação - Go em português


### EBNF


```
PROGRAM = { DECLARATION } ;
DECLARATION = "função", IDENTIFIER, "(", { IDENTIFIER, ( "inteiro" | "string" ), [ "," ] }, ")", ( "inteiro" | "string" ), BLOCK, "\n" ;
BLOCK = "{", "\n", { STATEMENT }, "}" ;
STATEMENT = ( λ | ASSIGN | PRINT | IF | FOR | VAR | RETURN ), "\n" ;
ASSIGN = IDENTIFIER, ( ( "=", BOOLEAN EXPRESSION ) | ( "(", { BOOLEAN EXPRESSION, [ "," ] }, ")" ) ) ;
PRINT = "Imprime", "(", BOOLEAN EXPRESSION, ")" ;
IF = "se", BOOLEAN EXPRESSION, BLOCK, { "senão", BLOCK } ;
FOR = "para", ASSIGN, ";", BOOLEAN EXPRESSION, ";", ASSIGN, BLOCK ;
VAR = "var", IDENTIFIER, ( "int" | "string" ), ( λ | "=", BOOLEAN EXPRESSION ) ;
RETURN = "retorna", BOOLEAN EXPRESSION ;
BOOLEAN EXPRESSION = BOOLEAN TERM, { "||" BOOLEAN TERM } ;
BOOLEAN TERM = RELATIONAL EXPRESSION, { "&&", RELATIONAL EXPRESSION } ;
RELATIONAL EXPRESSION = EXPRESSION, { ("==" | ">" | "<"), EXPRESSION } ;
EXPRESSION = TERM, { ("+" | "-" | "." ), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = NUMBER | STRING | IDENTIFIER ["(", { BOOLEAN EXPRESSION, [ "," ] }, ")" ] | (("+" | "-" | "!"), FACTOR) | "(", BOOLEAN EXPRESSION, ")" | SCAN ;
SCAN = "Escaneia", "(", ")" ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
STRING = ( " | ' ), { λ | LETTER | DIGIT }, ( " | ' ) ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```
