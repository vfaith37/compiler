# parser.py
import ply.yacc as yacc
from lexer import tokens

# Define the keywords
KEYWORDS = [
    'VAR',
    'AND',
    'OR',
    'NOT',
    'IF',
    'ELIF',
    'ELSE',
    'FOR',
    'TO',
    'STEP',
    'WHILE',
    'FUN',
    'THEN',
    'END',
    'RETURN',
    'CONTINUE',
    'BREAK',
]

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)


# Define the new rule for a function call with arguments and incorporate keywords
def p_expression_function_call(p):
    '''
    expression : ID LPAREN args RPAREN
               | expression PLUS term
               | expression MINUS term
               | term
               | KEYWORD
               | STRING
    '''
    if len(p) == 5:  # Function call
        p[0] = (p[1], p[3])
    elif len(p) == 4:  # Addition or Subtraction
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:  # Just a term, keyword, or ID
        p[0] = p[1]


def p_args_single(p):
    '''
    args : expression
    '''
    p[0] = [p[1]]


def p_args_multiple(p):
    '''
    args : args COMMA expression
    '''
    p[0] = p[1] + [p[3]]


def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]


def p_factor(p):
    '''
    factor : NUMBER
           | LPAREN expression RPAREN
           | STRING
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]


def p_statement_var_declaration(p):
    '''
    statement : VAR ID
    '''
    # Process variable declaration here


def p_statement_assignment(p):
    '''
    statement : ID EQUALS expression
    '''
    # Process variable assignment here


def p_statement_if(p):
    '''
    statement : IF expression THEN statement ELSE statement END
    '''
    # Process IF-THEN-ELSE statement here


def p_statement_for(p):
    '''
    statement : FOR ID EQUALS expression TO expression STEP expression NEXT
    '''
    # Process FOR loop statement here


# Error rule for syntax errors
def p_error(p):
    print(f"PARSER DEBUG: Syntax error")


# Build the parser
parser = yacc.yacc()
data = '''
print(1+1)
'''

parsed_data = parser.parse(data)
