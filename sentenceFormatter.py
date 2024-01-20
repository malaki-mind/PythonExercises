# -*- coding: utf-8 -*-
"""
Started on 7:58 PM :: Wed Jan 17 2024
Ended on 9:40 PM :: Fri Jan 19 2024 

@author: Max McMahon

inspired by Ardit Sulce's Python Mega Course on Udemy. the prompt is to create 
a program that analyzes user input and adds punctuation automatically. He sugg-
ested learners to have a go on their own first before seeing his solution.

this is the result of me making this program without any tutorial.

"""

greet = "                   :::: SENTENCE FORMATTER ::::                      "
welcome = """

Type any sentence you please and I will build a pargraph from your sentences. 
I'll know when you're asking (some) questions and when you're making statements. 
No punctuation or case-sensitivity necessary! I got you! Don't expect 
me to save your spelling or grammar this time, though <.< """
info = """

Click enter when you're done typing your sentence

Best results when only a sentence at a time

Don't worry about case-sensitivity or punctuation

type "r" to repeat last sentence you typed
type "h" for help

type "done" to see the final creation

"""

print(greet + welcome + info)
pronouns = ["i", "you", "me", "they", "he", "she", "anybody", "we", "it"]

modal_verbs = [
    "do ", "did ", "does ", 
    "may ", "can ", "will ", 
    "should ", "could ", "would ",
    "have ", "shall ", "doth "
    ]

modal_Qs = []
maxMod = 2
verbCount = 0
nounCount = 0

while verbCount < len(modal_verbs):
    for pronoun in pronouns:
        if pronoun == "it":
            if modal_verbs[verbCount] == "have ":           
                continue
            elif modal_verbs[verbCount] == "shall ":
                continue
            else: 
                modal_Qs.append(modal_verbs[verbCount] + pronoun)
        else:
            modal_Qs.append(modal_verbs[verbCount] + pronoun)
    verbCount+=1


interrogatives = ["who", "what", "where", "when", "why", "how", "is", "are"]

conjugations = ["'s", "'re", "'ve", "s", "re", "ve", "v", "r", "er", "ev"]  

interog = 0
conjug = 0
interog_base = len(interrogatives)

while interog < interog_base:
    for conj in conjugations:
        interrogatives.append(interrogatives[interog] + conj)
    interog+=1    

questions = [[interrogatives],[modal_Qs]]

punctuations = [".", "!", "?"]

def sentenceStripCase(sentence):
    countPunc = 0
    for punc in punctuations:
        countPunc += sentence.count(punc)
    if countPunc == 0:
        return sentence
    else:
        for punc in punctuations:
            sentence = sentence.strip(punc)
    if sentence == "":
        sentence = "nice"
    sentence = sentence.casefold()
    return sentence
    

def sentenceBreaker(sentence):
    i = 0    
    broken_sent = []
    curr_sent = ""
    word_count = 0    
    last_letter = len(sentence)-1
    while i <= len(sentence)-1:
        if sentence[i] == " ":
            broken_sent.append(sentence[:i])
            curr_sent = broken_sent[len(broken_sent)-1]
            word_count+=1
            i+=1
        elif i == len(sentence)-1:
            if sentence != "":
                broken_sent.append(sentence[:i] + sentence[last_letter])
                curr_sent = broken_sent[len(broken_sent)-1]
                word_count+=1
                i+=1
        else:
            i+=1
            continue    
    return [broken_sent, curr_sent, word_count]

def questionAnalyzer(sentence):    
    broke = c = 0
    wrds = 0
    qSet = 0
    wrd_cnt = 2
    while qSet < len(questions):
        for isQ in questions[qSet][c]:
            if isQ == sentence[broke][wrds]:
                return True        
        if sentence[wrd_cnt] > 1:
            wrds+=1
            qSet+=1
        else:
            return False
    return False

commands = ["done", "r", "h"]
done = commands[0]
repeat = commands[1]
h = commands[2]
        
def checkDone(sentence):    
    sentence = sentence.casefold()    
    if sentence == done:
        return True    
    return False

def checkRepeat(sentence):    
    sentence = sentence.casefold()
    if sentence == repeat:
        return True    
    return False

def checkHelp(sentence):
    sentence = sentence.casefold()
    if sentence == h:
        return True
    return False

end = False

paragraph = ""
current_sentence = ""

while end == False:
    user_input = input("Type a sentence: ")
    if checkDone(user_input) == True:
        end = True
        print(paragraph)
    elif checkHelp(user_input) == True:
        print(info)
    else:
        if checkRepeat(user_input) == True:
            if current_sentence == "":
                current_sentence = repeat
            else:                
                user_input = current_sentence
                
        user_input = sentenceBreaker(user_input)
        current_sentence = user_input[1]
        current_sentence = sentenceStripCase(current_sentence)
        questionAnalyzer(user_input)
        
        if questionAnalyzer(user_input) == True:
            current_sentence = "?".join([current_sentence, ""])            
        else:
            current_sentence = ".".join([current_sentence, ""])
            
        if paragraph == "":
                paragraph += current_sentence.capitalize()                
        else:
                paragraph += " " + current_sentence.capitalize()