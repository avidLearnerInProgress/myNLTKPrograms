# -*- coding: utf-8 -*-

#Chinking is a top-down approach to chunking. Instead of adding words together to form a chunk, superfluous words (‘chinks’) are removed from existing phrases to form useful chunks.
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

trainText=state_union.raw("2005-GWBush.txt")
sampleText=state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer=PunktSentenceTokenizer(trainText)
tokenized=custom_sent_tokenizer.tokenize(sampleText)

def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            namedEnt=nltk.ne_chunk(tagged,binary=True)
            namedEnt.draw()
            
    except Exception as e:
        print(str(e))

process_content()