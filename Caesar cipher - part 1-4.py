# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:15:49 2020

@author: Wenbo Deng
"""

import random #Part 1.6 import random to make the rotation value can choose random value
empty = ""
new = ""
mode = input("Please choose the cipher mode(encrypt or decrypt or auto-decrypt):") #Part 1.1 let user to choose which mode they perfer
wrong1 = (mode != "encrypt") and (mode != "decrypt") and (mode != "auto-decrypt") #Part 1.1 situation if there is a problem with input mode

while wrong1:
    print("Sorry, you may give me a wrong information. Please try agian.")
    mode = input("Please choose the cipher mode(encrypt or decrypt or auto-decrypt):")
    wrong1 = (mode != "encrypt") and (mode != "decrypt") and (mode != "auto-decrypt")

if mode == "encrypt" or mode == "decrypt":
    value = input("please tell me the rotation value(you will choose random value if you leave it blank):") #Part 1.1 let user to input a rotation value
    message_mode = input("please select a message entry mode(manual entry or read from file):") #Part 3.1 let user to select a message entry mode 
    wrong2 = (message_mode == empty) or (message_mode != "manual entry" and message_mode != "read from file") #Part 3.1 situation if there is a problem with input message_mode
    while wrong2:
        print("Sorry, you may give me a wrong information. Please try agian.")
        message_mode = input("please select a message entry mode(manual entry or read from file):")
        wrong2 = (message_mode == empty) or (message_mode != "manual entry" and message_mode != "read from file")

    if message_mode == "manual entry": #Part 3.2 when message mode is manual entry
        message = input("please tell me the message:") #Part 1.1 let user input the message
        wrong3 = message == empty #Part 1.1 situdation if message is empty
        while wrong3:
            print("Sorry, you may give me a wrong information. Please try agian.")
            message = input("please tell me the message:")
            wrong3 = message == empty

    elif message_mode == "read from file": #part 3.2 when message mode is read from file
        file1 = input("please tell me the filename(including file path):") #Part 3.2 let user imput the file name
        while True: #part 3.4 situation that file name not be found
            try:  #Part 3.3 try open a file with the name given
                with open(file1) as file1:
                    message = file1.read()
                break
            except OSError:
                print("Sorry, you may give me a wrong information. Please try agian.")
            file1 = input("please tell me the filename(including file path):")

elif mode == "auto-decrypt":
    message = input("please tell me the message:") #Part 4.3 input the message needs to be auto-decryped
    wrong4 = message == empty #Part 4 situation that message is empty
    while wrong4:
            print("Sorry, you may give me a wrong information. Please try agian.")
            message = input("please tell me the message:")
            wrong4 = message == empty
    with open("auto-decrypt words.txt","w+") as file2: #Part 4.3 attempt to get the first line of the message 
        file2.write(message.casefold())
    file2 = open("auto-decrypt words.txt")
    message_firstline = file2.readline()
    file2.close()
    with open("words.txt") as file3: #Part 4.2 get the common English words
        common_words_list = file3.read()
        common_words_list = common_words_list.replace("\n", " ")
        common_words_list = common_words_list.split()
    len2 = len(message_firstline) 
    value = 1
    while value < 26: #Part 4.3 iterate all possible rotations
        exit_flag = False
        for i in range(len2):
            if "a" <= message_firstline[i] <= "z":
                new1 = ord("a") + (ord(message_firstline[i]) - ord("a") - int(value)) % 26
            else:
                new1 = ord(message_firstline[i])
            new += chr(new1)
        new = new.split()
        for each in new:
            if each in common_words_list:
                print(new)
                temp = input("Is the line has been successfully decrypted(yes or no)?:") #Part 4.3 ask if the line has been successfully decrypted
                if temp == "yes": #Part 4.3 if user answer is yes, break the while loop
                    exit_flag = True
                    break
        if exit_flag == True:
            mode = "decrypt"
            break
        value += 1
        new = ""

len1 = len(message) 
message_lower = message.casefold()
if value == empty:
    value = random.randint(0,26) #Part 1.6 let user to choose a random value

if mode == "encrypt": #Part 1.3 encrypt the message given by user
    for i in range(len1):
        if "a" <= message_lower[i] <= "z":
            new1 = ord("a") + (ord(message_lower[i]) - ord("a") + int(value)) % 26
        else:
            new1 = ord(message_lower[i])
        new = chr(new1)
        print(new.upper(), end = "") #Part 1.5 all message return as upper case
elif mode == "decrypt": #Part 1.4 decrypt the message given by user
    for i in range(len1):
        if "a" <= message_lower[i] <= "z":
            new1 = ord("a") + (ord(message_lower[i]) - ord("a") - int(value)) % 26
        else:
            new1 = ord(message_lower[i])
        new = chr(new1)
        print(new.upper(),end = "")
print("")

if mode != "auto-decrypt": 
    str1 = empty
    for each in message: #Part 2.1 collect the words (definition in Part 2.1)
        if "a" <= each <= "z" or "A" <= each <= "Z" or each == " ":
            str1 += each
            str1 = str1.replace("\n","")
            word_list = str1.split()
    total_words = "the total number of words is: " + str(len(word_list))
    print(total_words)  #Part 2.1(a) print total words
    
    a = 0
    for each in word_list:
        if word_list.count(each) == 1:
            a += 1
    unique_words = "Number of unique words: " + str(a)
    print(unique_words) #Part 2.1(b) print unique words
     
    word_list_set = set(word_list)
    str2 = empty
    len1 = empty
    for each in word_list_set:
        times = str(word_list.count(each))
        str2 += " " + times
        times = str2.split()
        len1 += str(len(each))
        len1 = list(len1)
    dict1 = dict(zip(word_list_set, times))
    dict1 = dict(sorted(dict1.items(),key = lambda x:x[1], reverse = True)) #Part 2.2 make the order in a descending order
    most_common_words = list(dict1.items())
    dict1 = dict(most_common_words[0:10]) #Part 2.1(c) make a dict to collect these metrics
    print("(up to ten) most common words:", dict1) #Part 2.2 collect up to the ten most common words
    minimum_word_lenth = "minimum word lenth: " + str(min(len1))
    print(minimum_word_lenth) #Part 2.1(d) minimum word length
    maximum_word_lenth = "maximum word lenth: " + str(max(len1))
    print(maximum_word_lenth) #Part 2.1(d) maximum word length
    
    import string
    class Solution:
        def getMostWord(self,wordstr):
            wordstr = wordstr.lower()
            return max(string.ascii_lowercase, key=wordstr.count)
    
    Commen_letter = Solution() #Part 2.1(e) collect the most common letter
    print ("most common letter:",Commen_letter.getMostWord(message))
    
    with open("record.txt","w") as f: #Part 2.3 collet the metrics in the record.txt
        f.write(total_words + "\n")
        f.write(unique_words + "\n")
        f.write(minimum_word_lenth + "\n")
        f.write(maximum_word_lenth + "\n")
else:
    print("auto-decrypt failed") #Part 4.3 if there is no auto-decrypt words match with the common word list the auto-decrypt failed






