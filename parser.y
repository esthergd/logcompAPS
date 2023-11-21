%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();

void yyerror(const char *s) {
    fprintf(stderr, "Parser error: %s\n", s);
}

%}

%token FOOD MEAL SEARCH PRINT IF ELSE FOR WHILE ATTRIBUTION
%token CARB PROTEIN FAT FIBER VITAMIN MINERAL
%token CALORIES PROTEINS CARBS FATS FIBERS VITAMINS MINERALS
%token NUMBER IDENTIFIER
%token PLUS MINUS TIMES DIVIDE EQUAL NOTEQUAL LESS LESSEQUAL GREATER GREATEREQUAL
%token LPAREN RPAREN

%start program

%%

program:
    | program command
    ;

command:
      FOOD IDENTIFIER '=' NUMBER FOOD ';'
    | MEAL IDENTIFIER '=' identifier_list ';'
    | SEARCH '(' identifier_opt ')' ';'
    | PRINT '(' ')' ';'
    | IF '(' expression ')' '{' program '}' ELSE
    | FOR '(' expression ')' '{' program '}'
    | WHILE '(' expression ')' '{' program '}'
    | ATTRIBUTION IDENTIFIER '=' expression ';'
    ;

identifier_list:
      IDENTIFIER
    | identifier_list IDENTIFIER
    ;

identifier_opt:
    | IDENTIFIER
    ;

expression:
      term
    | expression operator term
    ;

term:
      IDENTIFIER
    | NUMBER
    | SEARCH
    | LPAREN expression RPAREN
    ;

operator:
      PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | EQUAL
    | NOTEQUAL
    | LESS
    | LESSEQUAL
    | GREATER

%%

/* Implement any necessary additional functions or actions */

int main() {
    yyparse();
    return 0;
}