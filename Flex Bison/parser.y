%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
extern char *yytext;
void yyerror(const char *s) { fprintf(stderr, "Erro de análise: %s\n", s); }
%}

%token FUNCAO INTEIRO STRING IMPRIME SE SENAO PARA VAR RETORNA LE EPAREN DPAREN EBRACE DBRACE
%token PONTO_VIRGULA VIRGULA IGUAL IGUAL_IGUAL MAIOR MENOR OU E SOMA SUB CONCAT MULT DIV NEG NUMERO ID
%token QUEBRA_LINHA TIPO
%%

programa:
        /* vazio */
        | declaracao programa
        | QUEBRA_LINHA programa
        ;

declaracao:
        FUNCAO ID EPAREN lista_parametros DPAREN TIPO bloco QUEBRA_LINHA
        ;

lista_parametros: 
        /* vazio */
        | ID TIPO
        | ID TIPO VIRGULA lista_parametros
        ;

bloco:
        EBRACE QUEBRA_LINHA lista_afirmacoes DBRACE
        ;

lista_afirmacoes:
        /* vazio */
        | afirmacao lista_afirmacoes

afirmacao:
        opcao_afirmacao QUEBRA_LINHA
        ;

opcao_afirmacao:
        /* vazio */
        | VAR ID TIPO 
        | VAR ID TIPO IGUAL expressao_booleana
        | IMPRIME EPAREN expressao_booleana DPAREN
        | SE expressao_booleana bloco
        | SE expressao_booleana bloco SENAO bloco
        | PARA atribuicao PONTO_VIRGULA expressao_booleana PONTO_VIRGULA atribuicao bloco
        | RETORNA expressao_booleana
        | atribuicao
        ;

atribuicao:
        ID IGUAL expressao_booleana
        | ID EPAREN argumentos_atribuicao DPAREN 
        ;

argumentos_atribuicao:
        /* vazio */
        | expressao_booleana
        | expressao_booleana VIRGULA argumentos_atribuicao
        ;

expressao_booleana:
        termo_booleano
        | termo_booleano OU expressao_booleana
        ;

termo_booleano:
        expressao_relacional
        | expressao_relacional E termo_booleano
        ;

expressao_relacional:
        expressao
        | expressao IGUAL_IGUAL expressao_relacional
        | expressao MAIOR expressao_relacional
        | expressao MENOR expressao_relacional

expressao:
        termo
        | termo SOMA expressao
        | termo SUB expressao
        | termo CONCAT expressao
        ;

termo:
        fator
        | fator MULT termo
        | fator DIV termo
        ;

fator:
        NUMERO
        | ID
        | ID EPAREN argumentos_atribuicao DPAREN
        | SUB fator
        | SOMA fator
        | NEG fator
        | EPAREN expressao_booleana DPAREN
        | LE EPAREN DPAREN
        ;

%%

int main() {
    if (yyparse()) {
        fprintf(stderr, "Análise Falhou\n");
        return 1;
    }
    return 0;
}