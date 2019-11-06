#Written by: Eunsoo Jang
#Date: 12/05/2018

import re
import nltk
from nltk.corpus import brown
from nltk.corpus import inaugural
from nltk.corpus import gutenberg
from nltk.tag import hmm 
import urllib.request


def main (file):
    #taking in the file and storing it into an array of string of sentences
    url= file
    open_url = urllib.request.urlopen(url).read().decode('utf-8')
    split_text = re.sub('(\n)+', '', open_url)
    split_lines = re.sub ('\.|\?|\!|\:', '\n',split_text)
    sent = split_lines.split('\n')
    #tagging words in each sentence
    tagged = tagging(split_lines)
    tagging2(tagged)


#tagging: tags all the words in the given input.
def tagging(input_text):
    words = nltk.word_tokenize(input_text)
    tagged_text= nltk.pos_tag(words, tagset="universal")
    return tagged_text

#tagging2: takes in the tagged input and prints out each of the taggers and words were tagged as what.
def tagging2(tagged):
    ttable = nltk.FreqDist()

    #printing out all the tags
    for (wrd, tag) in tagged:
        ttable[tag] += 1
    print("frequent tags: ", ttable.most_common()[:6])
    print("\n")

    #Printing out all nouns
    ntable = nltk.FreqDist()
    for (word, tag) in tagged:
        if tag == 'NOUN':
            ntable[word+"/"+tag] += 1
    print("Nouns: ", ntable.most_common()[:63])
    print("\n")

    #Printing all verbs
    vtable = nltk.FreqDist()
    for (word, tag) in tagged:
       if tag == 'VERB':
           vtable[word+"/"+tag] += 1
    print("Verbs: ", vtable.most_common()[:39])
    print("\n")

    #Printing out all adjectives
    adjtable = nltk.FreqDist()
    for (word, tag) in tagged:
       if tag == 'ADJ':
           adjtable[word+"/"+tag] += 1
    print("Adjectives: ", adjtable.most_common()[:7])
    print("\n")

    #Printing out all pronouns
    prontable = nltk.FreqDist()
    for (word, tag) in tagged:
       if tag == 'PRON':
           prontable[word+"/"+tag] += 1
    print("Pronouns: ", prontable.most_common()[:9])
    print("\n")

    #printing out all determiners
    dettable = nltk.FreqDist()
    for (word, tag) in tagged:
       if tag == 'DET':
            dettable[word+"/"+tag] += 1
    print("Determiners: ", dettable.most_common()[:17])
    print("\n")
