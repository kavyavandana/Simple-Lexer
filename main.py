#!/usr/bin/env python3
import copy 
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize 
file = open("lexar_input.txt")


operators = {'=' : 'Assignment op', '+' : 'Addition op', '-' : 'Subtraction op', '/' : 'Division op', '*' : 'Multiplication op', '<' : 'Lessthan op', '>' : 'Greaterthan op'}
operators_key = operators.keys()


data_type = {'int' : 'integer type', 'float' : 'floating point', 'char' : 'character type', 'long' : 'long int'}
data_type_key = data_type.keys()


punctuation_symbol = {':' : 'colon', ';' : 'semi-colon', '.' : 'dot', ',' : 'comma'}
punctuation_symbol_key = punctuation_symbol.keys()


identifier = {'a' : 'id', 'b' : 'id', 'c' : 'id', 'd' : 'id'}
identifier_key = identifier.keys()


keywords = {'while': 'keyword', 'fahr' : 'keyword', 'upper' : 'keyword'}
keywords_key = keywords.keys()

separators = {'(' : 'separator', ')' : 'separator'}
separators_key = separators.keys()


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
			print(token, " is ", operators[token])
		if token in data_type_key:
			print(token, " is ", data_type[token])
		if token in punctuation_symbol_key:
			print(token, " is ", punctuation_symbol[token])
		if token in identifier_key:
			print(token, " is ", identifier[token])
		if token in keywords_key:
			print(token, " is ", keywords[token])
		if token in separators_key:
			print(token, " is ", separators[token])
			
	dataFlag=False
	print("_________________________________")