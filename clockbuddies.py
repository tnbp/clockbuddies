#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import math

students = ["Alice", 
            "Bob",
            "Carol",
            "Dave",
            "Erin",
            "Frank",
            "Grace",
            "Heidi",
            "Judy",
            "Mallory",
            "Olivia",
            "Pat",
            "Sybil",
            "Ted",
            "Victor",
            "Walter",
            "Xaver"]
result = []

while len(result) < 12:
    i = len(result)
    counter = 0                         # counter to prevent deadlock
    temp_students = list(students)
    temp_result = []
    while len(temp_students) > 1:
        if counter > 20:                # tried too many times--give up, start over
            i -= 1
            break
        dont_add = 0
        rand_entry1 = randint(0,len(temp_students)-1)
        first = temp_students[rand_entry1]
        rand_entry2 = randint(0,len(temp_students)-1)
        second = temp_students[rand_entry2]
        if not rand_entry1 == rand_entry2:  # don't pair a student with themselves
            for j in range(i):
                # don't add pairs that already exist
                if (((first,second) in result[j]) or ((second,first) in result[j])):
                    dont_add = 1
                    counter += 1
            if dont_add != 1: # add the pairing to the result list
                temp_result.append((first,second))
                del temp_students[max(rand_entry1,rand_entry2)]
                del temp_students[min(rand_entry1,rand_entry2)]
    if len(temp_students) == 1:
        temp_result.append((temp_students[0],"** NOBODY **"))
    if len(temp_result) == math.ceil(len(students)/2):          
        # if pairing fails on the last pair, the resulting list
        # is one item short; don't add it in that case
        result.append(temp_result)
        
    
for i in range(len(result)):    # output
    print("Pairings for", (i+1), "o'clock:")
    for j in range(len(result[i])):
        print("\t", result[i][j][0], "and", result[i][j][1])
    print("\n************************\n")
