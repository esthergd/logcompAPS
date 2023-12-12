# APS de Lógica da Computação


## Linguagem de Programação relacionada à nutrição


### EBNF


```
PROGRAMA = { DECLARAÇÃO } ;
DECLARAÇÃO = "função", IDENTIFICADOR, "(", { IDENTIFICADOR, ( "inteiro" | "string" ), [ "," ] }, ")", ( "inteiro" | "string" ), BLOCO, "\n" ;
BLOCO = "{", "\n", { DECLARAÇÃO }, "}" ;
DECLARAÇÃO = ( λ | ATRIBUIÇÃO | IMPRIME | SE | PARA | VAR | RETORNA ), "\n" ;
ATRIBUIÇÃO = IDENTIFICADOR, ( ( "=", EXPRESSÃO BOOLEANA ) | ( "(", { EXPRESSÃO BOOLEANA, [ "," ] }, ")" ) ) ;
IMPRIME = "Imprime", "(", EXPRESSÃO BOOLEANA, ")" ;
SE = "se", EXPRESSÃO BOOLEANA, BLOCO, { "senão", BLOCO } ;
PARA = "para", ATRIBUIÇÃO, ";", EXPRESSÃO BOOLEANA, ";", ATRIBUIÇÃO, BLOCO ;
VAR = "var", IDENTIFICADOR, ( "int" | "string" ), ( λ | "=", EXPRESSÃO BOOLEANA ) ;
RETORNA = "retorna", EXPRESSÃO BOOLEANA ;
EXPRESSÃO BOOLEANA = TERMO BOOLEANO, { "||" TERMO BOOLEANO } ;
TERMO BOOLEANO = EXPRESSÃO RELACIONAL, { "&&", EXPRESSÃO RELACIONAL } ;
EXPRESSÃO RELACIONAL = EXPRESSÃO, { ("==" | ">" | "<"), EXPRESSÃO } ;
EXPRESSÃO = TERMO, { ("+" | "-" | "." ), TERMO } ;
TERMO = FATOR, { ("*" | "/"), FATOR } ;
FATOR = NÚMERO | STRING | IDENTIFICADOR ["(", { EXPRESSÃO BOOLEANA, [ "," ] }, ")" ] | (("+" | "-" | "!"), FATOR) | "(", EXPRESSÃO BOOLEANA, ")" | ESCANEAR ;
ESCANEAR = "Escaneia", "(", ")" ;
IDENTIFICADOR = LETRA, { LETRA | DÍGITO | "_" } ;
NÚMERO = DÍGITO, { DÍGITO } ;
STRING = ( " | ' ), { λ | LETRA | DÍGITO }, ( " | ' ) ;
LETRA = ( a | ... | z | A | ... | Z ) ;
DÍGITO = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```
