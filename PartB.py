# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Tue Jan 22 19:29:39 2019

@author: beethovenzhang
"""

# Part B of project 1 Text Processing.
# Main time complexity: O(m) where m = max(m1, m2) and m1 and m2 are number of 
# characters in the first and second file

from PartA import tokenize_and_count

def count_common_tokens(counter1, counter2):
    '''
    Count the number of tokens the two counter have in common.
    Time complexity: O(n) where n = max(n1, n2) and n1 and n2 are number of 
    tokens in counter1 and counter2.
    '''
    num_of_common_tokens = 0
    for token in counter1:
        if token in counter2:
            num_of_common_tokens+=1
    
    return num_of_common_tokens

if __name__ == '__main__':
    # Get tokens from two files given 
    counter1 = tokenize_and_count(1)
    counter2 = tokenize_and_count(2)
    print(count_common_tokens(counter1, counter2))