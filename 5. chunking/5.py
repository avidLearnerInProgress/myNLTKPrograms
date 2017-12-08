import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


#Chunking is the process of finding natural word groups (‘chunks’) such as noun phrases and verb phrases. The rules for finding these phrases are simpler, but by limiting the problem it becomes practical to use a classifier to chunk sentences.

trainText=state_union.raw("2005-GWBush.txt")
sampleText=state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer=PunktSentenceTokenizer(trainText)
tokenized=custom_sent_tokenizer.tokenize(sampleText)

def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkGram=r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)
            chunked.draw(),   
    except Exception as e:
        print(str(e))

process_content()