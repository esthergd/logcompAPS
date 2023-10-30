# APS de Lógica da Computação


## LINGUAGEM DE PROGRAMAÇÃO RELACIONADA À NUTRIÇÃO


### EBNF


```
PROGRAM= { COMMAND } .
COMMAN= FOOD | MEAL | SEARCH | PRINT | IF | FOR | WHILE | ATTRIBUTION
FOOD = 'FOOD' IDENTIFIER '=' AMOUNT 'g' 'de' FOOD';' .
MEAL = 'MEAL' IDENTIFIER'=' { IDEENTIFIER } ';' .
SEARCH = 'SEARCH' SEARCHTYPE'(' [ IDENTIFIER] ')' ';' .
PRINT = 'PRINT' '('')' ';' .
IF= 'IF' '(' EXPRESSION ')' '{' PROGRAM'}' [ 'ELSE' '{' PROGRAM'}' ]
FOR = 'FOR' '(' EXPRESSION ')' '{' PROGRAM '}'
WHILE= 'WHILE' '(' EXPRESSION')' '{' PROGRAM'}' .
ATTRIBUTION = IDENTIFIER '=' EXPRESSION';' .

EXPRESSION = TERM{ OPERATOR } .
TERM = IDENTIFIER | NUMBER | SEARCH | '(' EXPRESSION')' .
Operador = '+' | '-' | '*' | '/' | '==' | '!=' | '<' | '<=' | '>' | '>=' .

AMOUNT = NUMBER
NUMBER = [0-9] { [0-9] | '.' } .
INDENTIFIER = LETTER { LETTER | DIGIT | '_' } .
LETTER = 'A' | 'B' | ... | 'Z' | 'a' | 'b' | ... | 'z' .
DIGIT = '0' | '1' | ... | '9' .

FOOD = 'CARB' | 'PROTEIN' | 'FAT' | 'FIBER' | 'VITAMIN' | 'MINERAL' .
SEARCHTYPE = 'CALORIES' | 'PROTEINS' | 'CARBS' | 'FATS' | 'FIBERS' | 'VITAMINS' | 'MINERALS' .

```
