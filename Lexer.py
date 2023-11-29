# coding: utf-8

from sly import Lexer
import os
import re
import sys





class CoolLexer(Lexer):
    tokens = {OBJECTID, INT_CONST, BOOL_CONST, TYPEID,
              ELSE, IF, FI, THEN, NOT, IN, CASE, ESAC, CLASS,
              INHERITS, ISVOID, LET, LOOP, NEW, OF,
              POOL, THEN, WHILE, NUMBER, STR_CONST, LE, DARROW, ASSIGN, 
              COMMENTMULTI, COMMENTSINGLE}
    #ignore = '\t '
    literals = {'-': '-', '':'(*.**)'}

    @_(r'(\*.*\*)')
    def COMMENTMULTI(self, t):
        self.lineno += 1

    @_(r'--.*')
    def COMMENTSINGLE(self, t):
        self.lineno += 1
    
    # Ejemplo
    ELSE = r'\b[eE][lL][sS][eE]\b'
    CARACTERES_CONTROL = [bytes.fromhex(i+hex(j)[-1]).decode('ascii')
                          for i in ['0', '1']
                          for j in range(16)] + [bytes.fromhex(hex(127)[-2:]).decode("ascii")]

    @_(r'\t| |\v|\r|\f')
    def spaces(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    @_(r'\b[0-9][0-9]*')
    def INT_CONST(self, t):
        return t

    @_(r't[rR][uU][eE]')
    def BOOL_CONST(self, t):
        t.value = 'true'
        return t
    
    @_(r'T[rR][uU][eE]')
    def TYPEID(self, t):
        return t

    @_(r'\"[.]*\"')
    def STR_CONST(self, t):
        return t

    @_(r'[A-Za-z]+')
    def OBJECTID(self, t):
        return t
    
    @_(r'[(][*][\d]*[*][)]')

    def error(self, t):
        self.index += 1
    #Fin Ejemplo
    def salida(self, texto):
        lexer = CoolLexer()
        list_strings = []
        for token in lexer.tokenize(texto):
            result = f'#{token.lineno} {token.type} '
            if token.type == 'OBJECTID':
                result += f"{token.value}"
            elif token.type == 'BOOL_CONST':
                result += "true" if token.value else "false"
            elif token.type == 'TYPEID':
                result += f"{str(token.value)}"
            elif token.type in self.literals:
                result = f'#{token.lineno} \'{token.type}\' '
            elif token.type == 'STR_CONST':
                result += token.value
            elif token.type == 'INT_CONST':
                result += str(token.value)
            elif token.type == 'ERROR':
                result = f'#{token.lineno} {token.type} {token.value}'
            else:
                result = f'#{token.lineno} {token.type}'
            list_strings.append(result)
        return list_strings
