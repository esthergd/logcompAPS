
%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
extern char *yytext;
void yyerror(const char *s) { fprintf(stderr, "Erro de análise: %s\n", s); }
%}

%token FUNCAO INTEIRO STRING IMPRIME SE SENAO PARA VAR RETORNA LE EPAREN DPAREN EBRACE DBRACE
%token PONTO_VIRGULA VIRGULA IGUAL IGUAL_IGUAL MAIOR MENOR OU E SOMA SUB CONCAT MULT DIV NEG NUMERO ID

%%

programa:
          /* vazio */
        | declaracao
        ;

declaracao:
          VAR ID tipo IGUAL expressao 
        | FUNCAO ID EPAREN lista_parametros DPAREN tipo EBRACE programa DBRACE
        | RETORNA ID
        | IMPRIME expressao
        | SE EPAREN expressao DPAREN EBRACE programa DBRACE
        | SE EPAREN expressao DPAREN EBRACE programa DBRACE SENAO EBRACE programa DBRACE
        | PARA expressao PONTO_VIRGULA expressao PONTO_VIRGULA expressao EBRACE programa DBRACE
        | expressao
        ;

expressao:
          expressao SOMA expressao
        | expressao SUB expressao
        | expressao MULT expressao
        | expressao DIV expressao
        | expressao MAIOR expressao
        | expressao MENOR expressao
        | VAR ID tipo IGUAL NUMERO
        | ID IGUAL ID SOMA NUMERO EBRACE
        | ID IGUAL ID MULT NUMERO 
        | ID
        | NUMERO
        | STRING
        | EPAREN expressao DPAREN
        ;


lista_parametros: /* vazio */
            | lista_parametros VIRGULA parametro
            | parametro
            ;

parametro: ID tipo
     ;

tipo:
    |INTEIRO
    |STRING
    ;

%%

int main() {
    if (yyparse()) {
        fprintf(stderr, "Análise Falhou\n");
        return 1;
    }
    return 0;
}