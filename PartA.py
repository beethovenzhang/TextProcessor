# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Thu Jan 17 20:25:49 2019

@author: beethovenzhang
"""

# Part A of project 1 Text Processing.
# Time complexity O(max(m, nlog(n)) where m is the total number of 
# characters in the file and n is the number of valid tokens

import sys
import re
import operator



def tokenize_and_count(n):
    '''
    Read the file given line by line. 
    Tokenize the text into words and count number of occurrences of each word
    '''
    counter = dict()
    with open(sys.argv[n]) as file:
        for line in file:
            text = line.lower()
            l1 = re.split('[^a-zA-Z0-9]',text)
            for word in l1:
                if word.isalnum():
                    counter[word] = counter.get(word, 0) + 1

    return counter

def print_word_frequencies(counter):
    '''Print out the word frequencies in given order'''
    l2 = list(counter.items())
    l2.sort(key = operator.itemgetter(0))
    l2.sort(key = operator.itemgetter(1), reverse = True)
    for pair in l2:
        print(pair[0] + '\t' + str(pair[1]))
    
    

if __name__ == '__main__':
    counter = tokenize_and_count(1)
    print_word_frequencies(counter)
