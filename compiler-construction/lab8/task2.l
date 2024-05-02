%{
    #include <stdio.h>
%}

DIGIT [0-9]

%%
{DIGIT}{5}[- ]{DIGIT}{7}[- ]{DIGIT}      {printf("Valid ID. Number is: %s\n", yytext);}
[^\n]+  {printf("Invalid ID. Number is: %s\n", yytext);}
%%

int main()
{
yylex();

return 0;
}
