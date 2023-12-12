/* tokenizer.l */

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"
%}

%option noyywrap

%%

"função"        { printf("Token Identified: função\n"); return FUNCAO; }
"inteiro"       { printf("Token Identified: inteiro\n"); return INTEIRO; }
"string"        { printf("Token Identified: string\n"); return STRING; }
"Imprime"       { printf("Token Identified: Imprime\n"); return IMPRIME; }
"se"            { printf("Token Identified: se\n"); return SE; }
"senão"         { printf("Token Identified: senão\n"); return SENAO; }
"para"          { printf("Token Identified: para\n"); return PARA; }
"var"           { printf("Token Identified: var\n"); return VAR; }
"retorna"       { printf("Token Identified: retorna\n"); return RETORNA; }
"Le"            { printf("Token Identified: Le\n"); return LE; }
"("             { printf("Token Identified: EPAREN\n"); return EPAREN; }
")"             { printf("Token Identified: DPAREN\n"); return DPAREN; }
"{"             { printf("Token Identified: EBRACE\n"); return EBRACE; }
"}"             { printf("Token Identified: DBRACE\n"); return DBRACE; }
";"             { printf("Token Identified: PONTO_VIRGULA\n"); return PONTO_VIRGULA; }
","             { printf("Token Identified: VIRGULA\n"); return VIRGULA; }
"="             { printf("Token Identified: IGUAL\n"); return IGUAL; }
"=="            { printf("Token Identified: IGUAL_IGUAL\n"); return IGUAL_IGUAL; }
">"             { printf("Token Identified: MAIOR\n"); return MAIOR; }
"<"             { printf("Token Identified: MENOR\n"); return MENOR; }
"||"            { printf("Token Identified: OU\n"); return OU; }
"&&"            { printf("Token Identified: E\n"); return E; }
"+"             { printf("Token Identified: SOMA\n");return SOMA; }
"-"             { printf("Token Identified: SUB\n"); return SUB; }
"."             { printf("Token Identified: CONCAT\n"); return CONCAT; }
"*"             { printf("Token Identified: MULT\n"); return MULT; }
"/"             { printf("Token Identified: DIV\n"); return DIV; }
"!"             { printf("Token Identified: NEG\n"); return NEG; }

[0-9]+                       { printf("Token Identified: NUMERO %s\n", yytext); return NUMERO; }
[a-zA-Z][a-zA-Z0-9_]*        { printf("Token Identified: ID %s\n", yytext); return ID; }

[ \t\n]         { /* Ignorar espaços em branco */ }

.               { /* Tratar caracteres não reconhecidos */ }

%%