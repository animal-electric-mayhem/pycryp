#!/usr/bin/env python
#
# File Name: pycryp.py
#
# Purpose: Command line tool for Caesar & Vigenère ciphers
# Created: 09.12.2015
# Author: Daniel Stemmer 
# eMail: joe.doe.2504(at)gmail.com
# GitHub: joezifer
#

import re
import argparse

# Takes list "text", converts each item into uppercase, then converts into number and subtracts 65
def AlphaToNum(text):
    message = []
    message.append([ord(char) - 65 for char in text.upper()])
    # flattens the list
    clean = message[0]
    return clean

# Takes list "number", adds 65 to each item and converts the result into a letter
def NumToAlpha(number):
    message = []
    message.append([chr(num + 65) for num in number])
    # flattens the list
    clean = message[0]
    return clean

# Takes list "number" and adds "rot" + 26 to each item, then modulo 26. It can be used for both en- and decryption
def rotate(number, rot):
    message = []
    if decode == True:
        rot = -rot
    message.append([(num + 26 + rot) % 26 for num in number])
    # flattens the list
    clean = message [0]
    return clean

# Pretty self-explanatory, isn't it?
def vigenere(number_txt, number_kw):
    i = 0
    message = []
    for num in number_txt:
        temp = [num]
        vgn = number_kw[i]
        message.append([rotate(temp,vgn)])
        i += 1
        if i == len(number_kw):
            i = 0
    # Flatten²: The Flattening
    flatten = [s[0] for s in message]
    clean = [s[0] for s in flatten]
    return clean

# Converts lists of letters into strings
def ListToString(myList):
    myString = ""
    myString = myString.join(myList)
    return myString

# Removes spaces, numbers, and special characters from string
def cleanString(myString):
    clean = re.sub('[^A-Za-z]+', '', myString)
    return clean

def main():
    global decode
    decode = False

    # Setting up the command line parser
    parser = argparse.ArgumentParser(description='Tool for de/encrypting Caesar and Vigenère ciphers')
    parser.add_argument('-d', action='store_true', help='decryption flag')
    parser.add_argument('-c', type=int, help='-c [C] where C is shift value')
    parser.add_argument('-v', help='-v [V] where V is the Vigenère keyword')
    parser.add_argument('-vf', help='-vf [VF] where VF is the Vigenère keyword file')
    parser.add_argument('-i', required=True, help='path to input file')
    parser.add_argument('-o', required=True, help='path to output file')
    args = parser.parse_args()
    # Decode?
    if args.d:
        decode = True
    # Writes contents of input file to mystring, cleans it up and closes input file, the opens output file.
    inF = open(args.i)
    mystring = cleanString(inF.read())
    inF.close()
    opF = open(args.o, 'w')
    # Caesar
    if args.c:
        opF.write(ListToString(NumToAlpha(rotate(AlphaToNum(mystring),args.c))) + '\n')
    # Vigenère without keyword file
    if args.v:
        keyW = cleanString(args.v.upper())
        opF.write(ListToString(NumToAlpha(vigenere(AlphaToNum(mystring),AlphaToNum(keyW)))) + '\n')
    # Vigenère with a keyword file
    if args.vf:
        keyF = open(args.vf)
        keyString = cleanString(keyF.read())
        keyF.close()
        opF.write(ListToString(NumToAlpha(vigenere(AlphaToNum(mystring),AlphaToNum(keyString)))) + '\n')
    opF.close()

main()
