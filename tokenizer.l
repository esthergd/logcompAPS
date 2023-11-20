/* tokenizer.l */

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"
%}

%%

"FOOD"          { printf("Token Identified: FOOD\n"); return FOOD; }
"MEAL"          { printf("Token Identified: MEAL\n"); return MEAL; }
"SEARCH"        { printf("Token Identified: SEARCH\n"); return SEARCH; }
"PRINT"         { printf("Token Identified: PRINT\n"); return PRINT; }
"IF"            { printf("Token Identified: IF\n"); return IF; }
"ELSE"          { printf("Token Identified: ELSE\n"); return ELSE; }
"FOR"           { printf("Token Identified: FOR\n"); return FOR; }
"WHILE"         { printf("Token Identified: WHILE\n"); return WHILE; }
"ATTRIBUTION"   { printf("Token Identified: ATTRIBUTION\n"); return ATTRIBUTION; }
"CARB"          { printf("Token Identified: CARB\n"); return CARB; }
"PROTEIN"       { printf("Token Identified: PROTEIN\n"); return PROTEIN; }
"FAT"           { printf("Token Identified: FAT\n"); return FAT; }
"FIBER"         { printf("Token Identified: FIBER\n"); return FIBER; }
"VITAMIN"       { printf("Token Identified: VITAMIN\n"); return VITAMIN; }
"MINERAL"       { printf("Token Identified: MINERAL\n"); return MINERAL; }
"CALORIES"      { printf("Token Identified: CALORIES\n"); return CALORIES; }
"PROTEINS"      { printf("Token Identified: PROTEINS\n"); return PROTEINS; }
"CARBS"         { printf("Token Identified: CARBS\n"); return CARBS; }
"FATS"          { printf("Token Identified: FATS\n"); return FATS; }
"FIBERS"        { printf("Token Identified: FIBERS\n"); return FIBERS; }
"VITAMINS"      { printf("Token Identified: VITAMINS\n"); return VITAMINS; }
"MINERALS"      { printf("Token Identified: MINERALS\n"); return MINERALS; }

"("             { printf("Token Identified: LPAREN\n"); return LPAREN; }
")"             { printf("Token Identified: RPAREN\n"); return RPAREN; }

"+"             { printf("Token Identified: PLUS\n"); return PLUS; }
"-"             { printf("Token Identified: MINUS\n"); return MINUS; }
"*"             { printf("Token Identified: TIMES\n"); return TIMES; }
"/"             { printf("Token Identified: DIVIDE\n"); return DIVIDE; }
"=="            { printf("Token Identified: EQUAL\n"); return EQUAL; }
"!="            { printf("Token Identified: NOTEQUAL\n"); return NOTEQUAL; }
"<"             { printf("Token Identified: LESS\n"); return LESS; }
"<="            { printf("Token Identified: LESSEQUAL\n"); return LESSEQUAL; }
">"             { printf("Token Identified: GREATER\n"); return GREATER; }
">="            { printf("Token Identified: GREATEREQUAL\n");return GREATEREQUAL; }

[0-9]+                       { printf("Token Identified: NUMBER\n", yytext); return NUMBER; }
[a-zA-Z][a-zA-Z0-9_]*        { printf("Token Identified: IDENTIFIER\n", yytext); return IDENTIFIER; }

[ \t\n]         { /* Ignorar espaços em branco */ }

.               { /* Tratar caracteres não reconhecidos */ }

%%