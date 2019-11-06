#Written by: Eunsoo Jang
#Date: 12/05/2018


import re
import nltk
from nltk.corpus import brown
from nltk.corpus import inaugural
from nltk.corpus import gutenberg
from nltk.tag import hmm 
import urllib.request


def main (string):
    #taking in the file and storing it into an array of string of sentences
    split_text = re.sub('\r|(\n)+', '', string)
    split_lines = re.sub ('\.|\?|\!|\:', '\n',split_text)
    sent = split_lines.split('\n')

    #taking the array of sentences and tokenizing them into words
    sentences = []
    for i in sent:
        i = i.lower()
        words = nltk.word_tokenize(i)
        sentences.append(words)
    
    #making the grammar
    grammar1 = nltk.CFG.fromstring(
   """
   S -> WH-NP VP
   S -> Aux NP VP
   S -> NP VP
   NP -> Nominal | ProperN | PreDet NP | Det Nominal 
   VP -> V | V ADJ  | V WH-NP | V NP  
   Nominal -> N | Nominal N
   WH-NP -> WH-PRON 
   V -> "does" | "bite" | "flies" | "fly" | "walk" | "walks" | "are" | "is" | "have" | "has" | "bites" | "swims" | "swim"
   PreDet -> "all"
   Det -> "a" | "the" | "an"
   Aux -> "does"
   N -> "animals" | "humans" |"mammals" | "dogs" | "birds" | "hair" | "fish" | "animal" | "bird" | "collies" | "collie" | "beagles" | "beagle" | "canaries" | "parrot" | "parrots" | "feathers" |"gills" | "canary" | "canines"
   ProperN -> "socrates" | "deepak" | "tweety" | "rover" | "snoopy" | "polly" 
   WH-PRON -> "who" | "what"
   ADJ ->  "human" | "biped"
   """)

    #using Earley Chart Parser to make the parse trees
    parser = nltk.parse.EarleyChartParser(grammar1)

    print("Result of the parsed sentences: \n")
    #parsing for each sentence
    for r in sentences:
      for p in parser.parse(r):
        print(p)

    

