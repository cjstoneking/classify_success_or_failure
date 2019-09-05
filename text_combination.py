# MIT License
#
# Copyright (c) 2019 Colin James Stoneking

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#-------------------------------------------------------------------------------

#This file contains functions for expanding strings that contain multiple options
#where the options are enclosed in curly braces {} and separated by forward slash /
#an example of such a string is:
#  "we crossed the {stream/river} {by boat/by raft/via the bridge}"
#this has two sections with options, which lead to 2 x 3 = 6 different possible expansions
# "we crossed the stream by boat"
# "we crossed the river via the bridge"
# etc.

# note that an option can include an empty string

# "hard work paid off {in the end/}"
# has two expansions: "hard work paid off in the end" and "hard work paid off"

#(but "hard work paid off {in the end}" has only one expansion: "hard work paid off in the end"  )

#nested options aren't allowed


# main functions:
#
#  expand_random returns a single expansion, sampled randomly
#  expand_all returns a list containing all possible expansions
#

#-------------------------------------------------------------------------------

import re
import numpy as np
import itertools


#this function takes as input a string that contains multiple options
#where the options are written as {option a/option b/option c}
#returns a list containing all possible combinations of the options (as strings)
def get_all(s):
    flat_list = to_flat_list(to_nested_list(s))
    #flat list is a list that contains only strings or lists of strings
    #the strings are sections of non-optional text
    #the lists of strings correspond to options {a/b/c}
    #flat list is flat because its lists cannot themselves contain lists
    index_sets = [list(range(len(x))) for x in flat_list if not isinstance(x, str)]
    all_combinations = itertools.product(*index_sets)
    output = []
    for comb in all_combinations:
        pos = 0
        s = ""
        for x in flat_list:
            if(isinstance(x, str)): s = s + x
            else:
                s = s + x[comb[pos]]
                pos = pos + 1
        output.append(s)
    return output

#this function takes as input a string that contains multiple options
#where the options are written as {option a/option b/option c}
#this return a single randomly selected combination of the options (as a string)
def get_random(s):
    while(True):
        search_result = re.search("\{.*?\}", s)
        if(not search_result): break
        m = search_result.span() #tuple giving start and end indices of match
        t = s[m[0]:m[1]] #actual text that matched
        options = t[1:-1].split("/")
        s = s[:m[0]] + options[np.random.randint(len(options))] + s[m[1]:]
    return s

#turn string with options {a/b/c} into nested list
#use regex to find all options {a/b/c}
#and replace them with list of options as separate strings
#apply recursively to text following a match -> final output is nested list
def to_nested_list(s):
    search_result = re.search("\{.*?\}", s)
    if(not search_result): return s
    m = search_result.span() #tuple giving start and end indices of match
    t = s[m[0]:m[1]] #actual text that matched
    options = t[1:-1].split("/")
    return [to_nested_list(s[:m[0]]),\
            options,\
            to_nested_list(s[m[1]:])]

#recursively flatten the output of to_nested_list()
def to_flat_list(ls):
    flat_list = []
    for x in ls:
        if isinstance(x, str):
            flat_list.append(x)
        else:
            if(all([isinstance(y, str) for y in x])):
                #list containing only strings
                #this corresponds to a set of options
                flat_list.append(x)
            else:
                #list with some sublists
                #flatten it recursively
                flat_list = flat_list + to_flat_list(x)
    return flat_list
