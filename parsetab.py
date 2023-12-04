
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDECOMMA DIVIDE ELSE END EQUALS FOR ID IF KEYWORD LPAREN MINUS NEXT NUMBER PLUS RPAREN STEP STRING THEN TIMES TO VAR\n    expression : ID LPAREN args RPAREN\n               | expression PLUS term\n               | expression MINUS term\n               | term\n               | KEYWORD\n               | STRING\n    \n    args : expression\n    \n    args : args COMMA expression\n    \n    term : term TIMES factor\n         | term DIVIDE factor\n         | factor\n    \n    factor : NUMBER\n           | LPAREN expression RPAREN\n           | STRING\n    \n    statement : VAR ID\n    \n    statement : ID EQUALS expression\n    \n    statement : IF expression THEN statement ELSE statement END\n    \n    statement : FOR ID EQUALS expression TO expression STEP expression NEXT\n    '
    
_lr_action_items = {'ID':([0,3,11,24,],[2,2,2,2,]),'KEYWORD':([0,3,11,24,],[5,5,5,5,]),'STRING':([0,3,9,10,11,13,14,24,],[6,6,16,16,6,16,16,6,]),'NUMBER':([0,3,9,10,11,13,14,24,],[8,8,8,8,8,8,8,8,]),'LPAREN':([0,2,3,9,10,11,13,14,24,],[3,11,3,3,3,3,3,3,3,]),'$end':([1,4,5,6,7,8,15,16,17,20,21,22,23,],[0,-4,-5,-6,-11,-12,-2,-14,-3,-13,-9,-10,-1,]),'PLUS':([1,4,5,6,7,8,12,15,16,17,19,20,21,22,23,25,],[9,-4,-5,-6,-11,-12,9,-2,-14,-3,9,-13,-9,-10,-1,9,]),'MINUS':([1,4,5,6,7,8,12,15,16,17,19,20,21,22,23,25,],[10,-4,-5,-6,-11,-12,10,-2,-14,-3,10,-13,-9,-10,-1,10,]),'RPAREN':([4,5,6,7,8,12,15,16,17,18,19,20,21,22,23,25,],[-4,-5,-6,-11,-12,20,-2,-14,-3,23,-7,-13,-9,-10,-1,-8,]),'COMMA':([4,5,6,7,8,15,16,17,18,19,20,21,22,23,25,],[-4,-5,-6,-11,-12,-2,-14,-3,24,-7,-13,-9,-10,-1,-8,]),'TIMES':([4,6,7,8,15,16,17,20,21,22,],[13,-14,-11,-12,13,-14,13,-13,-9,-10,]),'DIVIDE':([4,6,7,8,15,16,17,20,21,22,],[14,-14,-11,-12,14,-14,14,-13,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,11,24,],[1,12,19,25,]),'term':([0,3,9,10,11,24,],[4,4,15,17,4,4,]),'factor':([0,3,9,10,11,13,14,24,],[7,7,7,7,7,21,22,7,]),'args':([11,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> ID LPAREN args RPAREN','expression',4,'p_expression_function_call','parser.py',35),
  ('expression -> expression PLUS term','expression',3,'p_expression_function_call','parser.py',36),
  ('expression -> expression MINUS term','expression',3,'p_expression_function_call','parser.py',37),
  ('expression -> term','expression',1,'p_expression_function_call','parser.py',38),
  ('expression -> KEYWORD','expression',1,'p_expression_function_call','parser.py',39),
  ('expression -> STRING','expression',1,'p_expression_function_call','parser.py',40),
  ('args -> expression','args',1,'p_args_single','parser.py',55),
  ('args -> args COMMA expression','args',3,'p_args_multiple','parser.py',62),
  ('term -> term TIMES factor','term',3,'p_term','parser.py',69),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',70),
  ('term -> factor','term',1,'p_term','parser.py',71),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',84),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser.py',85),
  ('factor -> STRING','factor',1,'p_factor','parser.py',86),
  ('statement -> VAR ID','statement',2,'p_statement_var_declaration','parser.py',96),
  ('statement -> ID EQUALS expression','statement',3,'p_statement_assignment','parser.py',103),
  ('statement -> IF expression THEN statement ELSE statement END','statement',7,'p_statement_if','parser.py',110),
  ('statement -> FOR ID EQUALS expression TO expression STEP expression NEXT','statement',9,'p_statement_for','parser.py',117),
]