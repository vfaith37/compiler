# lexer.py
import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'COMMA',
    'KEYWORD',
    'STRING',
    'VAR',
    'IF',
    'THEN',
    'ELSE',
    'END',
    'FOR',
    'NEXT',
    'TO',
    'STEP',
    "EQUALS"
)

# Define the keywords
keywords = {
    'VAR': 'VAR',
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT',
    'IF': 'IF',
    'ELIF': 'ELIF',
    'ELSE': 'ELSE',
    'FOR': 'FOR',
    'TO': 'TO',
    'STEP': 'STEP',
    'WHILE': 'WHILE',
    'FUN': 'FUN',
    'THEN': 'THEN',
    'END': 'END',
    'RETURN': 'RETURN',
    'CONTINUE': 'CONTINUE',
    'BREAK': 'BREAK',
    'NEXT': 'NEXT',
}

# Token definitions
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_VAR = r'VAR'
t_IF = r'IF'
t_COMMA = r','
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_END = r'END'
t_FOR = r'FOR'
t_NEXT = r'NEXT'
t_TO = r'TO'
t_EQUALS = r'EQUALS'
t_STEP = r'STEP'


# Ignore comments (lines starting with #)
def t_COMMENT(t):
    r'\#.*'
    t.lexer.skip(1)


# Tokenize string literals
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'  # Match double-quoted strings
    t.value = t.value[1:-1]  # Remove quotes
    return t


# Tokenize numbers
def t_NUMBER(t):
    r'\d+(\.\d+)?'  # Match integers or floating-point numbers
    t.value = float(t.value)
    return t


# Tokenize function and variable names (ID token or KEYWORD)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # Match function and variable names
    t.type = keywords.get(t.value.upper(), 'ID')  # Check if it's a keyword (use upper() for case-insensitivity)
    return t


# Ignore whitespace
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print(f"LEXER DEBUG: Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
