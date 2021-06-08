#!/usr/bin/env python3
import copy 
import re
from nltk.tokenize import word_tokenize 
file = open("lexar_input.txt")


operators = {'=' : 'Assignment op', '+' : 'Addition op', '-' : 'Subtraction op', '/' : 'Division op', '*' : 'Multiplication op', '<' : 'Lessthan op', '>' : 'Greaterthan op'}
operators_key = operators.keys()


data_type = {'int' : 'integer type', 'float' : 'floating point', 'char' : 'character type', 'long' : 'long int'}
data_type_key = data_type.keys()


punctuation_symbol = {':' : 'colon', ';' : 'semi-colon', '.' : 'dot', ',' : 'comma'}
punctuation_symbol_key = punctuation_symbol.keys()


indentifier = {'a' : 'id', 'b' : 'id', 'c' : 'id', 'd' : 'id'}
indentifier_key = indentifier.keys()

keywords = {'while': 'keyword', 'fahr' : 'keyword'}
keywords_key = keywords.keys()

dataFlag = False

a=file.read()

count = 0

program = a.split("\n")



for line in program:
	count = count + 1
	print("line#" , count, "\n", line)
	tokens = word_tokenize(line)
	print("Tokens are ", tokens)
	print("Line#", count, "properties \n")
	for token in tokens:
		if token in operators_key:
			print(token, "operator is ", operators[token])
		if token in data_type_key:
			print(token, "datatype is", data_type[token])
		if token in punctuation_symbol_key:
			print(token, "Punctuation symbol is", punctuation_symbol[token])
		if token in indentifier_key:
			print(token, "Identifier is", indentifier[token])
    if token in keywords_key:
      print(token, "Keyword is ", keywords[token])
			
	dataFlag=False
	print("_________________________________")
	

